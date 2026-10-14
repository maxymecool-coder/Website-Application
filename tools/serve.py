"""Preview the whole site locally, Notes included: python3 tools/serve.py [port]

Quartz links notes without ".html" (most web hosts resolve that themselves);
this server does the same so links work on your own computer too.
"""
import http.server
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def translate_path(self, path):
        local = super().translate_path(path)
        if not os.path.exists(local) and os.path.exists(local + ".html"):
            return local + ".html"
        return local


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8123
    print(f"Serving {ROOT} at http://localhost:{port}")
    http.server.ThreadingHTTPServer(("", port), Handler).serve_forever()
