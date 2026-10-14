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

## The look

Every page is one framed sheet floating on a painted sky. A cloud band runs across the top (name, tabs, light/dark switch) and the bottom (footer), and Miku and Cinnamoroll sit on the frame's edges. Inside, chapters are divided by a dotted line.

- **Skies:** `images/sky/sky-day.webp` (Sera) and `images/sky/sky-night.webp` (Minatsuki Ren) sit behind the sheet and cross-fade when the theme changes. To swap one, replace the file, or change its `url()` in `styles.css` (search for `body::before`).
- **Cloud bands:** a soft base colour (`--band`) with `images/sky/clouds-bank.webp` (clouds lifted out of Sera's sky) laid over it, cut to a puffy edge. At night the same clouds are dimmed by `--cloud-filter`.
- **Light and dark:** the switch in the top band saves the choice as `theme` in the browser, the same key the Notes pages use, so it carries over to the vault. With nothing saved, the site follows the device setting. Both palettes are the variables at the top of `styles.css`.
- **Tab icon:** `images/icon-32.png`, `icon-180.png` (phones) and `icon-512.png`, cut from nacchan's Cinnamoroll in headphones. Notes has its own copy in `notes-builder/quartz/static/icon.png` (200px).

## Mascots (Miku and Cinnamoroll)

All the art is fan art or free material, credited on `credits.html`. Whenever you add someone else's art, add a row for it there (the comment has the pattern) with the artist and a link to where you found it.

### On the frame

These are cut-outs with transparent backgrounds, positioned in `styles.css` so each sits on an edge:

| Class | Where | Art |
|---|---|---|
| `perch--top` | every page, standing on the top edge | Cinnamoroll in headphones (nacchan) |
| `perch--ledge` | every page, peeking over the bottom cloud | Miku and a tiny Miku (tina_muchimu) |
| `perch--cheer` | every page, on the bottom cloud | Cinnamoroll with a "!" (nacchan) |
| `peek` | Story, beside "The turn" (wide screens only) | Miku peeking round the left edge (tina_muchimu) |
| `perch--leek` | Story, over the Awards board | Miku dangling a leek (tina_muchimu) |
| `perch--lean` | Research, on the abstract | Miku leaning on the edge (tina_muchimu) |

Several of these line up a cut edge in the picture with an edge on the page (the `translateY` percentages in their rules). If you swap one for different art, adjust those numbers.

### Pointing at things

The rest stand beside what's worth clicking:

| `data-spot` | Page | Now | Points at |
|---|---|---|---|
| `story-chapters` | Story | Miku on a robot vacuum, pointing (nukotun) | the chapter row |
| `story-research` | Story, end of "The turn" | Miku peeking out of a mug (tina_muchimu) | the link to Research |
| `story-awards` | Story | Miku cheering (meruko-san) | the award covers |
| `story-notes` | Story, bottom | Cinnamoroll flying with airplanes (biskyfresh) | "Explore the vault" |
| `writing-latest` | Writing | Miku waving "Hi!" (tina_muchimu) | the latest essay |
| `writing-notes` | Writing, bottom | Cinnamoroll saying "Hello" (nacchan) | "Explore the vault" |
| `footer` | every page | Miku in a leek costume (lulalang) | "Back to top" |

To change one, save the picture as `images/mascots/<data-spot>.webp` (transparent background, about 480px) and point its `<img>` at it. A spot waiting for art can show a dashed "draw me" frame instead:

```html
<span class="mascot is-empty" data-character="miku" data-spot="story-chapters" aria-hidden="true"><span class="sketch"><b>Miku</b>pointing<em>draw me</em></span></span>
```

The tabs at the top carry small round crops of the same art (`images/mascots/tab-*.webp`). Clicking any of the friends makes them hop and throw out notes and sparkles (Miku) or hearts (Cinnamoroll); that's in `site.js`.

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
