"""Rebuild the Notes section (the zettelkasten) from the Obsidian vault.

Run from the site folder:  python3 tools/update_notes.py
Use a different vault:     python3 tools/update_notes.py "/path/to/Obsidian Vault"

Only the folders in PUBLISH are copied, plus the images those notes embed.
Everything else in the vault stays off the site. To keep a single note out,
add `draft: true` to its properties in Obsidian.
The Notes home page text lives in notes-builder/home.md; edit it there.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
BUILDER = SITE / "notes-builder"
CONTENT = BUILDER / "content"
OUTPUT = SITE / "notes"
VAULT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Downloads" / "Obsidian Vault"
PUBLISH = ["6 - Full Notes", "4 - Indexes", "3 - Tags"]
INDEXES = "4 - Indexes"
EMBED = re.compile(r"!\[\[([^\]|#]+)|!\[[^\]]*\]\(([^)]+)\)")


def main():
    if not (BUILDER / "node_modules").is_dir():
        sys.exit("Quartz isn't installed here yet. Run `npm ci` inside notes-builder first.")
    missing = [f for f in PUBLISH if not (VAULT / f).is_dir()]
    if missing:
        sys.exit(f"Couldn't find {', '.join(missing)} in {VAULT}. Nothing was changed.")

    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    CONTENT.mkdir()
    for folder in PUBLISH:
        shutil.copytree(VAULT / folder, CONTENT / folder, ignore=shutil.ignore_patterns(".DS_Store"))

    notes = list(CONTENT.rglob("*.md"))

    # Copy only the images and files the published notes embed, wherever they sit in the vault
    wanted = set()
    for note in notes:
        for a, b in EMBED.findall(note.read_text(encoding="utf-8", errors="ignore")):
            target = Path((a or b).strip()).name
            if target and not target.endswith(".md") and "://" not in (a or b):
                wanted.add(target)
    found = {p.name: p for p in VAULT.rglob("*")
             if p.name in wanted and p.is_file() and ".obsidian" not in p.parts and ".trash" not in p.parts}
    if found:
        (CONTENT / "attachments").mkdir()
        for name, path in found.items():
            shutil.copy2(path, CONTENT / "attachments" / name)

    indexes = sorted(p.stem for p in (VAULT / INDEXES).glob("*.md"))
    home = (BUILDER / "home.md").read_text(encoding="utf-8")
    home = home.replace("{count}", f"{len(notes):,}").replace("{indexes}", "\n".join(f"- [[{n}]]" for n in indexes))
    (CONTENT / "index.md").write_text(home, encoding="utf-8")

    print(f"Copied {len(notes)} notes and {len(found)} embedded files. Building…", flush=True)
    build = subprocess.run(["npx", "quartz", "build", "-o", str(OUTPUT)], cwd=BUILDER)
    if build.returncode != 0:
        sys.exit("Quartz couldn't build the notes; the message above says why.")
    print(f"Done. The Notes section is in {OUTPUT.relative_to(SITE)}/")


if __name__ == "__main__":
    main()
