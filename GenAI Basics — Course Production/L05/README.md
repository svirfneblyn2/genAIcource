# Lesson 05: Video Generation — from a key frame to a finished clip

## Status: deck v2 (19 slides, facts as of October 2026), 2026-10-12

Review 2026-10-12 (Fable): facts verified against primary sources; fixes applied — Kling 4.0 Flash vs full 4.0, LTX-2 capabilities, Veo Lite limits, free-credit wording, EU AI Act 50(2)/50(4), notebook 6 slots aligned with slide 8, larger type for Teams. Lesson graph: `L05_10_Lesson_Graph.md`. **PDFs need a rebuild on a machine with Edge** (`python deck_v2/build.py`).

## Source of truth
- **Slide decks (RU/EN):** `presentation_L05_Video_Generation_v2.html` / `presentation_L05_Video_Generation_EN_v2.html` + PDFs with the same basenames. Self-contained HTML (inline CSS/JS): `←/→` navigate, `N` speaker notes, `G` slide grid, `F` fullscreen, break timer on slide 12. Videos are click-to-play and muted; in the PDF each video shows its poster with the label “▶ video in the HTML version”.
- **Generator:** `deck_v2/build.py` (RU/EN strings side by side, `t("ru", "en")`) + `deck_v2/style.css` + `deck_v2/deck.js`. Run `python deck_v2/build.py` (HTML + PDF via headless Edge) or `--no-pdf`. Edit the generator, not the HTML.
- **Media:** `deck_v2/make_media.py` → `assets/v2/video/*.mp4` (re-encoded copies of `demo_veo_showcase/` clips: 960×540, H.264 CRF 27, no audio, ~6 MB total) and `assets/v2/img/*.jpg` (posters, failure-gallery frames, QA frames, noise schematic, stills).
- **Plan / facts:** `L05_09_Deck_Fix_Plan_v2.md` (author decisions at the top take priority), `L05_08_Source_Notes_Research_2026-10.md`.
- **Case clips:** `demo_veo_showcase/` — Veo 3.1 (`veo-3.1-generate-001`), 1280×720, 8 s each, with audio; `courier_delivery_final.mp4` = 8 + 8 + 8 s with two 0.5 s transitions = 23 s; `trainwreck_naive_t2v.mp4` = naive one-prompt T2V.
- The v1 decks (`presentation_L05_Video_Generation.html` / `_EN.html`, 17 slides) and the legacy `*.py` generators in this folder are kept for reference only (outdated models and pseudo-science).
- **Aligned with v2 (2026-10-12):** instructor scripts (`L05_02_*`), cheatsheets (`L05_00_*`), homework (`L05_05_*`), live-demo runbook (`L05_04_*`). The notebook `L05_Video_Generation_API_Pipeline.ipynb` (copy in `/notebooks`) uses the real Veo 3.1 API via `google-genai`; paid calls are off by default (`RUN_PAID = False`). `L05_01_Lecture_Text_READY.md` is outdated (marked at the top).

## Slide map (19 slides, 90 minutes incl. 5-minute break)
| # | Min | Slide | Main visual |
|---|---|---|---|
| 01 | 2 | Cover | Shot 2 frame |
| 02 | 4 | Hook: the finished clip | `final.mp4` (23 s) + 3 key numbers (3 shots, 8+8+8 → 23 s, ≈ $10 list price) |
| 03 | 5 | How a model makes video | Noise → step-by-step cleanup (patches × time) → frames; “no physics engine” plaque |
| 04 | 6 | Failure gallery (T2V in one prompt) | Trainwreck video + 4 frames with timecodes: action skipped, details drift after cut, broken space, pseudo-text |
| 05 | 6 | T2V vs I2V | Two videos side by side + two flow diagrams |
| 06 | 4 | Character sheet / references | Sheet with anchor callouts; Veo 3.1 ≤3 refs, Kling 3.0 Elements |
| 07 | 4 | Key frame in chat | Sprite → draft → approved with edit prompts; “seconds · cents” vs “minutes · $0.40/s” |
| 08 | 6 | Director’s prompt | Real shot-2 prompt with 6 colour-coded slots + shot 2 video |
| 09 | 5 | Camera language | 8 static SVG diagrams (Static, Pan, Tilt, Dolly, Tracking, Orbit, Crane, Handheld) |
| 10 | 4 | Local control | Motion Brush illustration with callouts; first/last frame, extend, references |
| 11 | 5 | Editing | SVG timeline 8+8+8 s with 0.5 s transitions = 23 s + final video |
| 12 | 5 | Break | Timer |
| 13 | 7 | Market, October 2026 | Bar chart of max clip length + capability chips; Sora 2 marked shut down |
| 14 | 3 | Code (for reference) | ~15-line `google-genai` Veo example + $/s bars (Veo 3.1 / Fast / Lite) |
| 15 | 5 | Economics | Bar chart: T2V trial and error $96 vs frame + I2V $28.80 vs Fast $7.20 |
| 16 | 5 | Quality check | Real defects from our shots 2–3 + 6-item checklist (= homework rubric) |
| 17 | 6 | Risks & provenance | Traffic light + SynthID vs C2PA survival flow; EU AI Act Art. 50 |
| 18 | 5 | Homework | Track A (product) / Track B (courier), deliverables |
| 19 | 3 | Summary + L06 teaser | 4 rules; sound covered in L06 |
