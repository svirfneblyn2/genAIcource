# Lesson 10: Open Models. LM Studio, local inference and Runpod

## Status: deck v2 (21 slides, 90 min), facts as of 2026-10-16, student-mode, visual and fact audits applied, final audit fixes 2026-10-16

Rebuilt from the September 2026 Drive package (`10 — Open Models, LM Studio, Local Inference and Runpod — DONE`: 28-slide pptx with an engineering focus — five-layer stack, GGUF, KV cache, Inference Decision Record). The v2 deck is a beginner tour: what an open model is (a file plus a licence), whether it fits your computer and how fast it runs, LM Studio and the local server, a coding agent that installs Ollama, security, the open model market, then Runpod (Pod vs Serverless), price, how to choose, homework.

Deck structure: one app and three places to run a model; Hugging Face page of Granite 4.2 8B; why your own model (Artificial Analysis index); five parts (file, engine, hardware, server, app); quantisation (real Granite 4.2 8B file sizes); will it fit (Q4 sizes + 25% margin against 6/16/24 GB); speed (llama.cpp tokens per second); LM Studio tour; demo; local server code; agent prompt; local ≠ private; market by size; break; laptop limits; Runpod pricing and a Pod vs Serverless day; GPU price per hour and the utilisation effect; 2×2 choice; homework; summary.

## Source of truth
- **Generator:** `deck_v2/build.py` (RU/EN strings side by side, `t("ru", "en")`; slide order in `SLIDES`; minutes per slide in `min=`) + `deck_v2/style.css` + `deck_v2/deck.js` (copied from the L06 v2 deck). Run `python deck_v2/build.py` (HTML + PDF via headless Edge) or `--no-pdf`. Edit the generator, not the HTML.
- **Instructor scripts** `L10_02_*` are generated from the deck: `python deck_v2/make_docs.py`.
- **Slide decks (RU/EN):** `presentation_L10_Open_Models_Local_and_RunPod_v2.html` / `presentation_L10_Open_Models_Local_and_RunPod_EN_v2.html` + PDFs with the same basenames. `←/→` navigate, `N` speaker notes, `G` grid, `F` fullscreen, break timer on slide 15.
- **Facts:** `L10_08_Source_Notes_Research_2026-10.md` (primary sources checked 2026-10-16, image credits, volatile list).
- **Companion documents:** cheatsheets (`L10_00_*`, with the 24-hour recheck list), instructor scripts (`L10_02_*`), homework (`L10_05_*`).

## Images
- Own captures (2026-10-16): Hugging Face `ibm-granite/granite-4.2-8b-GGUF` (`hf_granite_header.png`, `hf_granite_files.png`), Runpod pricing in Community Cloud mode (`runpod_pricing_community.png`).
- Official image with credit: LM Studio app screen from the 0.4.0 release blog (`lmstudio_app.png`, “LM Studio / Element Labs”).
- Schematics (cover, slide 2 “three places”, slide 5 “five parts”) are drawn in HTML/SVG in `build.py` (`places_cover()`, `places_diagram()`, `parts_diagram()`), so RU and EN decks have labels in their own language. The earlier genai-assets PNGs with English labels were removed.
- LM Studio was not installed for this rebuild (owner decision), so slide 9 uses the official image. To replace it with an own capture, install LM Studio 0.4.x, take a Discover or Developer tab screenshot on synthetic data and update `s_lmstudio`.

## Slide map (21 slides, 90 minutes incl. 5-minute break)
| # | Min | Time | Slide | Main visual |
|---|---|---|---|---|
| 01 | 2 | 00:00–02:00 | Cover | Three HTML cards: cloud / laptop / rented GPU with addresses |
| 02 | 4 | 02:00–06:00 | One app, three places where the model runs | HTML schematic: one app → three addresses + legend |
| 03 | 5 | 06:00–11:00 | An open model is a file plus a licence | Hugging Face screenshots with 3 callouts |
| 04 | 4 | 11:00–15:00 | Your own model: data stays home, quality trails | Pros/cons + Artificial Analysis bars |
| 05 | 4 | 15:00–19:00 | Five parts: file, engine, hardware, server, app | HTML schematic with icons + LM Studio/Ollama bracket |
| 06 | 5 | 19:00–24:00 | Quantisation: 2–5× smaller | Bars of Granite 4.2 8B file sizes |
| 07 | 5 | 24:00–29:00 | File + margin must fit GPU memory | Q4 bars + hatched 25% vs 6/16/24 GB VRAM lines, bars coloured by the smallest GPU they fit |
| 08 | 4 | 29:00–33:00 | A GPU answers 2–25× faster than a CPU | Tokens/s bars (Apple M5 / M5 Max, RTX, H100) |
| 09 | 5 | 33:00–38:00 | LM Studio | Official app screenshot with 4 callouts |
| 10 | 5 | 38:00–43:00 | Demo: download a small model, ask a work question | 5-step timeline + ticket prompt + sample JSON answer |
| 11 | 5 | 43:00–48:00 | Local server answers like a cloud API | L03 Python code + 3 address settings |
| 12 | 4 | 48:00–52:00 | A coding agent installs the model | Agent prompt (Ollama, granite4.2:3b) |
| 13 | 4 | 52:00–56:00 | Local ≠ private | Data-path traffic light + class rule |
| 14 | 4 | 56:00–60:00 | Open models by size | Three plain lists by GPU memory (up to 8 GB, 16–24 GB, server) under coloured headers |
| 15 | 5 | 60:00–65:00 | Break | Timer |
| 16 | 3 | 65:00–68:00 | When a laptop is not enough | Four signs |
| 17 | 5 | 68:00–73:00 | Runpod: per-second rental, two modes | Community pricing screenshot + Pod vs Serverless day |
| 18 | 5 | 73:00–78:00 | Renting pays off only when busy | GPU $/hour bars + $0.73 → $7.30 per 1M tokens |
| 19 | 4 | 78:00–82:00 | Choose by two questions | 2×2 with axes |
| 20 | 5 | 82:00–87:00 | Homework | 5 steps + `genai-homeworks/L10/` folder tree |
| 21 | 3 | 87:00–90:00 | Your own model is a file and memory; only the address and model name change | 4 rules + L11 preview |

## Before class
Install LM Studio (classic, not Bionic) and download `granite-4.2-3b` Q4_K_M (2.2 GB) for the slide 10 demo. Recheck the volatile facts (end of the cheatsheet). Runpod is shown on screenshots; a live launch is paid and optional (Terminate afterwards).
