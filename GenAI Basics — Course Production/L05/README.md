# Lesson 05: Video Generation. From a key frame to a video of several shots

## Status: deck v2 (21 slides, 90 min, facts as of October 2026), companion documents aligned 2026-10-12

Deck structure: example video, three access layers (chat, web studio, API), how diffusion generates frames, the text-to-video anti-pattern, then a 6-step pipeline (1 storyboard, 2 references, 3 key frame, 4 prompt + camera, 5 controls, 6 editing), market, break, code, cost per clip / minute / hour, acceptance checklist, risks, homework (three-shot mini story), summary. Lesson graph: `L05_10_Lesson_Graph.md`. **PDFs need a rebuild on a machine with Edge** (`python deck_v2/build.py`).

## Source of truth
- **Generator:** `deck_v2/build.py` (RU/EN strings side by side, `t("ru", "en")`; slide order in the `SLIDES` list; minutes per slide in `min=`) + `deck_v2/style.css` + `deck_v2/deck.js`. Run `python deck_v2/build.py` (HTML + PDF via headless Edge) or `--no-pdf`. Edit the generator, not the HTML. If a companion document disagrees with `build.py`, `build.py` wins.
- **Slide decks (RU/EN):** `presentation_L05_Video_Generation_v2.html` / `presentation_L05_Video_Generation_EN_v2.html` + PDFs with the same basenames. Self-contained HTML (inline CSS/JS): `←/→` navigate, `N` speaker notes, `G` slide grid, `F` fullscreen, break timer on slide 15. Videos are click-to-play and muted; in the PDF each video shows its poster with the label “▶ video in the HTML version”.
- **Media:** `deck_v2/make_media.py` → `assets/v2/video/*.mp4` (re-encoded copies of `demo_veo_showcase/` clips: 960×540, H.264 CRF 27, no audio, ~6 MB total) and `assets/v2/img/*.jpg` (posters, failure frames, QA frames, noise schematic, stills).
- **Plan / facts:** `L05_09_Deck_Fix_Plan_v2.md` (author decisions at the top take priority), `L05_08_Source_Notes_Research_2026-10.md`.
- **Case clips:** `demo_veo_showcase/`: Veo 3.1 (`veo-3.1-generate-001`), 1280×720, 8 s each, with audio; `courier_delivery_final.mp4` = 8 + 8 + 8 s with two 0.5 s transitions = 23 s; `trainwreck_naive_t2v.mp4` = naive one-prompt text-to-video.
- The v1 decks (`presentation_L05_Video_Generation.html` / `_EN.html`, 17 slides) and the legacy `*.py` generators in this folder are kept for reference only (outdated models).
- **Aligned with the 21-slide deck (2026-10-12):** instructor scripts (`L05_02_*`), cheatsheets (`L05_00_*`), homework (`L05_05_*`), live-demo runbooks (`L05_04_*`, slide references only), lesson graph (`L05_10_*`). The notebook `L05_Video_Generation_API_Pipeline.ipynb` (copy in `/notebooks`) uses the real Veo 3.1 API via `google-genai`; paid calls are off by default (`RUN_PAID = False`); its prompt-slot reference still points to old slide 8 (now slide 10). `L05_01_Lecture_Text_READY.md` is outdated (marked at the top).

## Slide map (21 slides, 90 minutes incl. 5-minute break)
| # | Min | Time | Slide | Main visual |
|---|---|---|---|---|
| 01 | 2 | 00:00–02:00 | Cover | Shot 2 frame, lesson scope |
| 02 | 3 | 02:00–05:00 | Example: 23 s video from three 8 s shots | `final.mp4` + 3 numbers (3 shots, 8+8+8 → 23 s, ≈ $10 list price) |
| 03 | 4 | 05:00–09:00 | Where to generate: chat, web studio, API | Three columns with tools, control, billing, use, starting point |
| 04 | 4 | 09:00–13:00 | How diffusion generates frames | Noise → denoising (patches × time) → frames; “no physics engine” plaque |
| 05 | 5 | 13:00–18:00 | Anti-pattern: text-to-video, whole story in one prompt | `trainwreck` video + 4 frames with timecodes |
| 06 | 3 | 18:00–21:00 | Text-to-video vs image-to-video | Two videos side by side + two flow diagrams |
| 07 | 7 | 21:00–28:00 | Step 1: storyboard | 3-row storyboard table with previews + 7-column Creator Tools template |
| 08 | 3 | 28:00–31:00 | Step 2: references | Character sheet with 4 callouts + frames of shots 1 and 2 |
| 09 | 4 | 31:00–35:00 | Step 3: key frame | Sprite → draft → approved; “seconds, cents” vs “minutes, $0.40/s” |
| 10 | 6 | 35:00–41:00 | Step 4: prompt (6 slots) | Real shot 2 prompt, colour-coded + `shot2` video |
| 11 | 4 | 41:00–45:00 | Step 4: camera | 8 SVG camera-move diagrams with prompt phrases |
| 12 | 3 | 45:00–48:00 | Step 5: controls | Motion Brush illustration + first/last frame, extension, references tiles |
| 13 | 7 | 48:00–55:00 | Step 6: editing | SVG timeline 8+8+8 − 0.5 − 0.5 = 23 s, ffmpeg command, `final` video |
| 14 | 3 | 55:00–58:00 | Market, October 2026 | Max clip length bars + capability chips; Sora 2 shut down |
| 15 | 5 | 58:00–63:00 | Break | Timer |
| 16 | 3 | 63:00–66:00 | Code (reference) | ~15-line `google-genai` Veo image-to-video example |
| 17 | 5 | 66:00–71:00 | Cost: clip, minute, hour | Table for 6 models: $/s, 8 s, 1 min, 1 h, 1 h with 3 attempts; our video = $28.80 / $7.20 |
| 18 | 5 | 71:00–76:00 | Acceptance checklist | Real defects from shots 2–3 + 6-item checklist (= homework rubric) |
| 19 | 4 | 76:00–80:00 | Risks | Traffic light + SynthID vs C2PA; EU AI Act Art. 50 |
| 20 | 7 | 80:00–87:00 | Homework: three-shot mini story | Track A (product) / Track B (courier), 5 deliverables, repo tree |
| 21 | 3 | 87:00–90:00 | Summary | 5 rules + final frame; L06 note on audio |
