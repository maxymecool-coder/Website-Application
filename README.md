# What Helping Means

My personal site: the story, awards and service, my Substack writing, and my zettelkasten.

- `index.html`, `writing.html`, `styles.css`, `images/`: the main site
- `notes/`: the zettelkasten, built by Quartz from my Obsidian vault
- `notes-builder/`: Quartz itself, used only to build `notes/`
- `tools/`: scripts that refresh the site

## Updating

New Substack post:

```bash
python3 tools/update_writing.py
```

New or edited notes (only `6 - Full Notes`, `4 - Indexes` and `3 - Tags` are published; add `draft: true` to a note's properties to keep it off the site):

```bash
python3 tools/update_notes.py
```

Then publish:

```bash
git add -A && git commit -m "Update site" && git push
```

GitHub Pages republishes within a minute or two.

## Previewing on this computer

```bash
python3 tools/serve.py
```

Then open http://localhost:8123.

## On a new computer

Quartz's packages aren't stored in the repository. Install them once before building notes:

```bash
cd notes-builder && npm ci
```
