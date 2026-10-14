"""Refresh the post list on writing.html from the Substack feed.

Run from the site folder:  python3 tools/update_writing.py
It rewrites only what sits between the posts:start and posts:end markers.
"""
import html
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED = "https://maxymien.substack.com/feed"
PAGE = Path(__file__).resolve().parent.parent / "writing.html"
START, END = "<!-- posts:start -->", "<!-- posts:end -->"
NS = {"content": "http://purl.org/rss/1.0/modules/content/"}
WORDS_PER_MINUTE = 230


def text_of(fragment):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", fragment))).strip()


def opening(body):
    """The post's first paragraph: an epigraph (quote + who said it) or its first sentence."""
    first = re.search(r"<p>(.*?)</p>", body, re.S)
    para = text_of(first.group(1)) if first else ""
    if para[:1] in "“\"'‘":
        close = max(para.rfind("”"), para.rfind('"'))
        if close > 0:
            who = para[close + 1:].strip(" -—–")
            if who:
                return {"quote": para[: close + 1], "who": who}
    sentence = re.match(r"(.+?[.!?])(\s|$)", para)
    return {"line": sentence.group(1) if sentence else para}


def post_html(item, latest):
    title = item.findtext("title").strip()
    link = item.findtext("link").strip()
    when = parsedate_to_datetime(item.findtext("pubDate"))
    body = item.findtext("content:encoded", default="", namespaces=NS)
    minutes = max(1, round(len(text_of(body).split()) / WORDS_PER_MINUTE))
    lead = opening(body)
    e = html.escape
    if "quote" in lead:
        dek = (f'<blockquote class="post-epigraph"><p>{e(lead["quote"])}</p>'
               f'<footer>{e(lead["who"])}</footer></blockquote>')
    else:
        dek = f'<p class="post-dek">{e(lead["line"])}</p>'
    flag = '<span class="post-flag">Latest</span>' if latest else ""
    return f"""      <li class="post{' post--latest' if latest else ''}">
        <time class="post-date" datetime="{when:%Y-%m-%d}">{when.day} {when:%b %Y}</time>
        <div class="post-body">
          {flag}<h2><a href="{e(link)}">{e(title)}</a></h2>
          {dek}
          <p class="post-meta">{minutes} min read</p>
        </div>
      </li>"""


def main():
    # curl uses the system's certificates, which python.org builds of Python on macOS often lack
    feed = subprocess.run(["curl", "-sSfL", "-m", "30", "-A", "Mozilla/5.0", FEED],
                          capture_output=True, check=False)
    if feed.returncode != 0:
        sys.exit(f"Couldn't download the feed: {feed.stderr.decode().strip()}")
    root = ET.fromstring(feed.stdout)
    items = root.findall("./channel/item")
    if not items:
        sys.exit("The feed came back with no posts; writing.html was left as it was.")
    block = "\n".join(post_html(it, i == 0) for i, it in enumerate(items))
    page = PAGE.read_text(encoding="utf-8")
    a, b = page.index(START) + len(START), page.index(END)
    PAGE.write_text(page[:a] + "\n" + block + "\n      " + page[b:], encoding="utf-8")
    print(f"writing.html now lists {len(items)} posts.")


if __name__ == "__main__":
    main()
