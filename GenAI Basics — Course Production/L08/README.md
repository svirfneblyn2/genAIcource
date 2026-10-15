# Lesson 08: AI for Data Analysis — chat with a spreadsheet

## Status: deck v1 (18 slides, facts as of October 2026), 2026-10-13

## Source of truth
- **Slide decks (RU/EN):** `presentation_L08_AI_for_Data_Analysis.html` / `_EN.html` + PDFs with the same basenames. Self-contained HTML (inline CSS/JS, fonts from Google Fonts): `←/→` navigate, `N` speaker notes, `G` slide grid, `F` fullscreen, break timer on slide 9. No video, no animation.
- **Generator:** `deck/build.py` (RU/EN strings side by side, `t("ru", "en")`) + `deck/style.css` + `deck/deck.js` (same engine as L05 `deck_v2`). Run `python deck/build.py` (HTML + PDF via headless Edge) or `--no-pdf`. Edit the generator, not the HTML.
- **All numbers and charts on the slides are computed at build time** from `demo_assets/northstar_sales_messy.csv` (and `northstar_sales_truth.csv` for the “what the source really said” values). Change the data → rebuild → slides stay consistent with `reference_analysis.py`.
- **Cover image:** `assets/l08_cover_hero.png` (genai-assets, subscription provider, no paid spend).
- **Facts:** `L08_08_Source_Notes_Research_2026-10.md` (primary sources checked 2026-10-13; `[UNCERTAIN]` items are not on slides).
- **Hook experiment:** `demo_assets/no_code_experiment_2026-10-13.md` — Claude Haiku 5.5 and Sonnet 5.5 with no tools on the 73-row CSV: totals correct, but both “repaired” returns 66 as “6” / “6 or 2” (truth: 4).
- **Instructor materials:** 90-min script `L08_02_*` (RU/EN), one-page cheatsheet `L08_00_*` (RU/EN), live-demo runbook `L08_04_*` (RU/EN), homework `L08_05_*` (RU/EN).
- **Demo assets:** `demo_assets/` — messy + truth CSV, dependency-free `reference_analysis.py`, `local_outputs/`, `fallback_outputs/` (charts), `student_starter/` (templates).
- **Previous package** (Sept 2026, 22-slide English .pptx + .docx set) stays on Google Drive `GenAI Basics — Course Production/08 — AI for Data Analysis — DONE/`; this folder replaces it (same dataset and teaching arc, rebuilt to the v2 deck standard: beginner language, graphics instead of box walls, RU + EN).
- **Audit:** student-mode Opus audit 2026-10-13 → REVISE (14 fixes: privacy wording for Claude, slide-7 date caption, RU number format, small type, label overlaps) → all applied.

## Slide map (18 slides, 90 minutes incl. 5-minute break)
| # | Min | Slide | Main visual |
|---|---|---|---|
| 01 | 2 | Cover | Spreadsheet grid → rising chart illustration |
| 02 | 5 | Hook: the model did the maths without code | Real no-tool answer with highlights + 4 verdicts (✓ total, ✗ “probably 6” vs 4, ✗ “I checked”, ! 100k rows) |
| 03 | 6 | The model is not the calculator | Schematic: you → model ⇄ Python sandbox → output files |
| 04 | 6 | Four places where AI analyses data | Chat / spreadsheet / notebook / API on an “easier → more control” axis |
| 05 | 5 | Data passport | First rows with colour-coded column roles; “row ≠ order ≠ customer” |
| 06 | 5 | Profile first | 73 / 72 / 4 + the five problem rows with highlighted cells |
| 07 | 6 | Finding ≠ permission to fix | Two lanes: mechanics (fix + log) vs meaning (flag + ask the source) |
| 08 | 6 | Analyst prompt | 6-part colour-coded prompt |
| 09 | 5 | Break | Timer |
| 10 | 10 | Live demo | 4 steps with prompts + audience task |
| 11 | 5 | One chart — one claim | Real line chart by month + slope chart Jan → Jun by channel |
| 12 | 4 | The question picks the chart | 5 mini chart schematics |
| 13 | 6 | Check the numbers | Three paths converge on $256,045 + 5-item checklist |
| 14 | 6 | “What happened” ≠ “what will happen if…” | ROAS bars + hidden-factor schematic |
| 15 | 3 | Code for reference | ~13 lines of pandas (verified) |
| 16 | 4 | What you may upload | Data traffic light |
| 17 | 4 | Homework | `verified_analysis_pack/` tree |
| 18 | 2 | Summary + L09 teaser | 5 rules |

## Not done yet
- No Colab notebook for L08 (L03–L06 have one). The pandas snippet on slide 15 and `reference_analysis.py` cover the code path.
