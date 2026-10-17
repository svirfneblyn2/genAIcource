# Lesson 08: AI for Data Analysis — spreadsheet → answer → chart → one-page report

## Status: deck v2 built for review (19 slides, 83 min + 7 min buffer), 2026-10-17

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

## Slide map (19 slides)
| # | Min | Slide | Main visual |
|---|---|---|---|
| 01 | 2 | Cover | Spreadsheet → chart illustration |
| 02 | 3 | The manager’s question comes first | Anna’s e-mail + real screen of the 1,261-row file |
| 03 | 4 | First prompt: describe the file, suggest 5 questions | Prompt + two real ChatGPT answer frames |
| 04 | 4 | Pick the tool by where the data lives | Four doors (Excel · Sheets · chat · database) + “model writes, program counts, you check” flow |
| 05 | 12 | Demo 1 — Excel | Prompt 2 + real ChatGPT sheet (values) + real Excel frame: SUMIFS in the fx bar and a chart on those cells |
| 06 | 3 | Growth: +161.7 % or +15.1 %? | 12-month line from the data with both bases |
| 07 | 4 | Five questions, five charts | Five mini charts built from Northstar |
| 08 | 5 | Break | Timer |
| 09 | 12 | Demo 2 — chat with a file | Prompts 3–5 + real heatmap and review-theme frames |
| 10 | 4 | Two problems the total hides | Social spend vs revenue bars; N2 vs others return-rate line |
| 11 | 4 | You edit a chart with words | Real before/after makeover frames + 3 changes |
| 12 | 3 | Three versions, three numbers | 49 / 46 / 44 % (model) vs 61 % (all 87 reviews read) + 60-second check |
| 13 | 5 | Large database: model writes SQL, database counts | DB counts, SQL with comments, duration chart + within-channel trap |
| 14 | 3 | Where data comes from | Export → official API (JSON) → scraping with 3 checks |
| 15 | 5 | Send the report file; the preview can lie | Fake chat preview vs real downloaded .docx + recipe script |
| 16 | 2 | The table says what happened | Hidden-factor schematic for “cut Social?” |
| 17 | 2 | What you may upload | Data traffic light |
| 18 | 4 | Homework | `analysis_pack/` tree |
| 19 | 2 | What to take away + L09 teaser | 5 moves |

## Not done yet
- **Claude for Excel side panel** on slide 5 is not captured yet (the Excel frame shows the reference workbook `demo_v2/excel_demo/northstar_2025_formulas.xlsx`, built by `make_formulas_workbook.py`; the panel's WebView window was not granted for capture).
- **Real frames for slide 4** (Gemini side panel in Google Sheets, a SQL client) — currently icons.
- No Colab notebook for L08.
