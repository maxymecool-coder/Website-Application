# What Helping Means

My personal site: the story, awards and service, my Substack writing, and my zettelkasten.

- `index.html` (Story), `research.html`, `writing.html`, `credits.html`, `styles.css`, `images/`: the main site
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

## Editing the Research page

Each section of `research.html` sits between markers like `<!-- research:abstract -->` and `<!-- /research:abstract -->`. Paste your edited text between them. To add the full paper, put the PDF in a `papers/` folder and swap the dashed box under "Full paper" for the link shown in the comment there.

## Mascots (Miku and Cinnamoroll)

Every spot starts as a dashed "draw me" frame:

```html
<span class="mascot is-empty" data-character="miku" data-spot="story-chapters" aria-hidden="true">…</span>
```

To fill one, save the picture as `images/mascots/<data-spot>.png` (transparent background, about 500px tall), then replace the whole `<span>…</span>` with:

```html
<span class="mascot" data-character="miku" data-spot="story-chapters" aria-hidden="true"><img src="images/mascots/story-chapters.png" alt=""></span>
```

| `data-spot` | Page | Character and pose | Points at |
|---|---|---|---|
| `story-chapters` | Story | Miku, pointing down | the chapter row |
| `story-research` | Story, end of "The turn" | Cinnamoroll, peeking, pointing left | the link to Research |
| `story-awards` | Story | Cinnamoroll, cheering, pointing down-left | the award covers |
| `story-notes` | Story, bottom | Cinnamoroll, floating, pointing right | "Explore the vault" |
| `research-abstract` | Research | Miku, holding a clipboard, pointing down | the abstract |
| `writing-latest` | Writing | Miku, waving, pointing down | the latest essay |
| `writing-notes` | Writing, bottom | Cinnamoroll, floating, pointing right | "Explore the vault" |
| `footer` | every page | Miku, small round face | "Back to top" |

Whenever you add someone else's art, add a row for it in `credits.html` (the comment there has the pattern) with the artist and a link to where you found it.

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
