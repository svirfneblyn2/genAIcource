---
name: course-deck-design
description: >-
  Design system and build/QA procedure for GenAI course HTML slide decks (v2 standard, as in
  L04 v2 and L05 v2). Use whenever creating, redesigning, reviewing or exporting a lesson deck
  (presentation_LXX_*.html / PDF), or when the user asks for "нормальный дизайн", fewer text
  cards, more images/diagrams, readable fonts, or a deck review.
---

# Course Deck Design (v2 standard)

Reference implementation: `GenAI Basics — Course Production/L05/deck_v2/` (`build.py`, `style.css`, `deck.js`, `make_media.py`).
Start a new lesson by copying that folder, not by hand-writing HTML. Content rules (tone, instructor phrasing, case studies) stay in `GEMINI.md` and `.agents/skills/course-deck-producer/SKILL.md`.

## 1. Generator, not hand-edited HTML
- One `build.py` per lesson renders RU and EN from the same source: every string is `t("ru", "en")`, so the two decks always have the same slide count, media and layout.
- Output: `presentation_LXX_<Topic>_v2.html` and `_EN_v2.html` (self-contained: inline CSS/JS, media by relative path) plus PDFs with the same basenames.
- Fix problems in the generator, then rebuild. Never patch the built HTML.

## 2. Canvas, type and colour
- Fixed 1600×900 stage, scaled to the window (`--s`). Slide padding 50/76/62 px.
- Fonts: **Onest** (display and body, Cyrillic-friendly) and **JetBrains Mono** (kickers, code, prompts, timecodes), loaded from Google Fonts with `Segoe UI` / `Consolas` fallbacks.
- Minimum sizes on the 1600×900 canvas (they must survive Teams screen share):
  - title 50px, lead 23px, body/bullets 21–22px, captions ≥17px, footnotes/sources ≥14px;
  - key numbers 48–56px, coloured by meaning;
  - code ≥16px mono.
- Palette (`style.css :root`): bg `#0b0f17`, surface `#121a28`, cyan `#38bdf8` (primary), green `#34d399` (good / I2V), amber `#fbbf24` (warning, money), red `#f87171` (failure), violet `#c084fc`. A colour always means the same thing across the deck.

## 3. Composition rules
- **One slide = one idea = one main visual.** The title states the takeaway as a sentence, not a topic label.
- At most 3–4 bullets per slide, one line each when possible. If a slide needs more text, it needs to be split or turned into a diagram.
- Prefer, in this order: real media from the lesson case (clips, frames, screenshots) → annotated image (callouts on the picture) → diagram/flow (inline SVG) → chart (bar/scale) → short table → bullets.
- Comparisons are charts or position maps, not tables. Tables only when nothing else works, ≤6 rows.
- No "card walls": never more than 4 bordered boxes of text on a slide.
- No decorative AI art and no stock wallpaper. Every image must carry information.
- No CSS animations or moving elements. Camera moves and processes are static diagrams with arrows.
- Fill the canvas: content should use the vertical space; avoid a dense top half with an empty bottom third.
- Every slide has speaker notes (`.notes`) that match the 90-minute instructor script.

## 4. Media
- Videos: re-encode (`make_media.py`: 960×540, H.264, CRF ~27, no audio unless the slide is about audio), `preload="metadata"`, click-to-play, muted, poster frame. In the PDF the poster shows with the label "▶ video in the HTML version".
- Images: JPG ≤ 300 KB for photos, PNG only for UI screenshots and diagrams. Keep sources in `assets/`, built copies in `assets/v2/`.
- New raster images: `python tools/image_generator.py --prompt "..." --output ... --aspect-ratio 16:9` (Vertex; runs on the instructor's machine). English text inside diagrams.

## 5. Interaction (deck.js)
`←/→/Space` navigate, `N` speaker notes, `G` slide grid, `F` fullscreen, `#n` deep links, a 5-minute break timer on the break slide. Clicks on media do not flip slides.

## 6. Build and verify
1. `python deck_v2/build.py --no-pdf`.
2. Screenshot every slide at 1600×900, RU and EN. In the cloud container use Playwright with `/opt/pw-browsers/chromium`, opening `file://…html#N` per slide. Locally use `msedge --headless`.
3. Look at every screenshot. Reject the slide if text is clipped or overlaps, anything is below the minimum sizes, there are more than 4 text boxes, a big area is empty, or RU and EN differ in layout.
4. Grep the built HTML for banned leftovers listed in the lesson's fix plan (invented percentages, "100%", outdated model names).
5. PDF: `python deck_v2/build.py` (headless Edge, zero margins) locally; check the page count matches the slide count.
6. Update the lesson `README.md` slide map and `COURSE_STATUS.md`.
