---
name: course-deck-producer
description: >-
  Standardized procedure and templates for creating, refining, and translating
  enterprise-grade slide decks, instructor scripts, and cheatsheets for the GenAI course.
---

# Course Deck Producer Skill

Use this skill whenever creating or updating slide decks, instructor scripts, or course materials in the GenAI Course Production repository.

---

## Step 1: Slide Deck Structure (21-Slide Template)

When generating or auditing an HTML presentation deck:
- Ensure the 21-slide structure defined in `GEMINI.md` is strictly observed.
- Keep the dark C4 architectural theme:
  - Background: `#0b0f17`
  - Cards: `#101622` with border `#1e293b`
  - Accent Primary: `#38bdf8` (Cyan)
  - Accent Success: `#10b981` (Emerald)
  - Accent Warning: `#f59e0b` (Amber)
  - Accent Danger: `#ef4444` (Red)
- Embed interactive features:
  - Slide navigation (`←`/`→`, `Space`)
  - Speaker notes drawer (`N`)
  - Grid view modal (`G`)
  - Fullscreen toggle (`F`)
  - Midpoint countdown timer on Slide 15 (`▶ Start 5 Min`, `⏸ Pause`, `↺ Reset`)

---

## Step 2: Content Rules

* **Tone:** Senior engineering peer-to-peer. Zero fluff.
* **Instructor Credentials:**
  - Igor Rubanovich / Ihar Rubanovich (`ihar_rubanovich@epam.com`).
  - Engineering Manager II & AI Ambassador @ EPAM.
  - Creator Tools description: "Architect & Developer of Creator Tools — AI platform for video translation and localization across 140+ languages (Hands-on AI R&D pet-project)".
* **Case Studies:**
  - Production win: EPAM CodeMie @ Dawn Foods (35% SDLC acceleration).
  - Homework benchmark: Glovo Food Delivery Courier (routing = graph/ML, messaging = GenAI, tap-to-send, taboo on refunds/cancellations).

---

## Step 3: Visual Asset Generation

For any diagram:
1. Formulate a prompt requesting a clean C4 diagram or infographic with dark background (`#0b0f17`) and English typography.
2. Run Vertex AI generator:
   ```bash
   python tools/image_generator.py --prompt "<PROMPT>" --output "<ASSET_PATH>" --aspect-ratio 16:9
   ```
3. Use the generated asset in the slide with `.slide-page.visual-slide`.

---

## Step 4: Verification & Export Workflow

1. Capture high-resolution screenshots at `1540x866`:
   ```bash
   msedge --headless --disable-gpu --window-size=1540,866 --screenshot=slide_preview.png deck.html
   ```
2. Visually verify with `view_file` to confirm zero clipping and balanced margins.
3. Export multi-page vector PDF:
   ```bash
   msedge --headless --disable-gpu --no-margins --print-to-pdf=deck.pdf deck.html
   ```
4. Generate the corresponding 90-minute script (`LXX_02_Instructor_Script_90MIN.md`) and 1-page cheatsheet (`LXX_00_Lecture_Cheatsheet.md`).
5. Repeat for English deck (`*_EN.html`, `*_EN.pdf`, `*_EN.md`).
