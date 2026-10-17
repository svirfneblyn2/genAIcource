# Lesson 08: AI for Data Analysis — spreadsheet → answer → chart → one-page report

## Status: deck v2 built for review (31 slides, 85 min + 5 min break), 2026-10-17

v2 files carry a `_v2` suffix; the unsuffixed v1 files (73-row CSV, data-hygiene arc) stay the delivered version until v2 is accepted, then v1 is removed (git history keeps it). Why and how: `L08_11_Method_Review_2026-10-17.md`
(Opus + Fable methodologist review) and `L08_09_Deck_Plan_v2.md` (plan of 2026-10-13).

## Source of truth
- **Slide decks (RU/EN):** `presentation_L08_AI_for_Data_Analysis_v2.html` / `_EN_v2.html` + PDFs with the same basenames. `←/→` navigate, `N` speaker notes, `G` grid, `F` fullscreen, break timer on slide 8.
- **Generator:** `deck/build_v2.py` (RU/EN side by side, `t("ru", "en")`) + `deck/style.css` + `deck/deck.js`. `python deck/build_v2.py` (HTML + PDF via headless Edge) or `--no-pdf`. Edit the generator, not the HTML.
- **Numbers and charts are computed at build time** from `demo_v2/northstar_sales_2025.csv`; `build_v2.py` asserts the key numbers against `demo_v2/answers.md` (1,261 → 1,260 rows, $2,520,078, Dec vs Jan +161.7 %, Dec vs Nov +15.1 %, North × Electronics returns 24.8 %).
- **Real screenshots:** `assets/v2/chat/` (ChatGPT run on `northstar_2025.xlsx`, Oct 2026); slide crops in `assets/v2/shots/` made by `deck/make_shots.py`. The EN deck reuses the Russian-language screens.
- **Channel database sample (slide 13):** `demo_v2/channels/` (raw sample files are git-ignored: the repo is public) — frozen, anonymised sample of the author's cooking-YouTube database (1,943 channels, 46,132 videos; full DB 26,544 / 416,809 / 668,665). DuckDB + CSV, `queries.sql`, `results/`. Show charts only; do not hand out the files.
- **Instructor materials:** 90-min script `L08_02_*_v2`, cheatsheet `L08_00_*_v2`, live-demo runbook `L08_04_*_v2` (prompts P1–P6 with fallback screens), homework `L08_05_*_v2` — RU + EN. Student kit: `demo_v2/student_starter/`.
- **Facts:** `L08_08_Source_Notes_Research_2026-10.md`. **No-code experiment** (now a speaker note on slide 12): `demo_assets/no_code_experiment_2026-10-13.md`.

## Slide map (31 slides, 85 min + 5 min break)
Story and reasoning: `L08_12_Lesson_Story_v2.md`. Weak/strong pairs are real ChatGPT runs from 2026-10-17 (`assets/v2/chat_badgood/`).
| # | Min | Slide |
|---|---|---|
| 01 | 1 | Cover |
| 02 | 2 | Five skills + Anna's e-mail (the task) |
| 03 | 3 | Part 1 · where data lives (6 types) |
| 04 | 3 | Table vs text (real Sales rows, real reviews) |
| 05 | 3 | Anatomy of one row |
| 06 | 3 | Size ladder: 73 / 1,261 / 46,132 / 416,809 |
| 07 | 3 | Key diagram: data stays in the file, AI writes instructions, a program counts |
| 08 | 3 | Four traps in real data |
| 09 | 3 | Experiment: 73 rows pasted, no tools (real run) |
| 10 | 2 | Part 2 · three questions → three parts + the file |
| 11 | 3 | Prompt 1 line by line |
| 12 | 4 | Quick / under control #1: "find insights" vs prompt 1 (real runs, ✓/✗ marks) |
| 13 | 3 | Prompt 2 line by line |
| 14 | 3 | Quick / under control #2: numbers vs formulas (ChatGPT sheet vs real Excel fx frame) |
| 15 | 5 | Demo 1 live — instructor checklist |
| 16 | 4 | Weak / good: "one number for the slide" → +161.7 % vs three bases (real runs) |
| 17 | 3 | Five questions, five charts (from the data) |
| 18 | 5 | Break |
| 19 | 5 | Part 3 · demo 2: prompts 3 and 4 line by line + real heatmap and themes |
| 20 | 3 | What we found: Social, N2 |
| 21 | 3 | Makeover (prompt 5) |
| 22 | 4 | 60-second check: 49 / 46 / 44 % vs 61 % |
| 23 | 3 | Quick / under control #3: "cut Social?" — first line vs paragraphs below (real run) |
| 24 | 2 | Part 4 · channel DB: three linked tables |
| 25 | 3 | SQL line by line |
| 26 | 2 | Result and trap: 12× vs within-channel ≈1.0 |
| 27 | 2 | Where data comes from |
| 28 | 3 | Part 5 · report file vs chat preview + recipe |
| 29 | 1 | Privacy |
| 30 | 2 | Homework |
| 31 | 1 | Summary: the five skills, ticked |

## Not done yet
- **Claude for Excel side panel** on slide 5 is not captured yet (the Excel frame shows the reference workbook `demo_v2/excel_demo/northstar_2025_formulas.xlsx`, built by `make_formulas_workbook.py`; the panel's WebView window was not granted for capture).
- **Real frames for slide 4** (Gemini side panel in Google Sheets, a SQL client) — currently icons.
- No Colab notebook for L08.
