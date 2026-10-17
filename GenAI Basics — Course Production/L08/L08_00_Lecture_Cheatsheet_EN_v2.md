# One-page speaker cheatsheet • Lesson 08 v2 (31 slides • 90 minutes)
*Speaker: Igor Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*
*Topic: AI for data analysis — what data is, formulas in words, charts and a one-page report • facts as of 2026-10-17*
*Deck: `deck/build_v2.py` • script: `L08_02_Instructor_Script_90MIN_EN_v2.md` • demos: `L08_04_Live_Demo_Runbook_READY_EN_v2.md` • reference: `demo_v2/answers.md`*
*Homework: `L08_05_Homework_EN_v2.md` • starter kit: `demo_v2/student_starter/` • repository: `genai-homeworks/L08/`*

---

### Before you start
* Teams: share the whole screen or practise switching windows (browser with the deck, ChatGPT, Excel). Browser zoom 125–150 %.
* ChatGPT: **one** chat for the whole lesson; keep it through the break. On the desktop: `northstar_2025_EN.xlsx` and `northstar_sales_2026-01.csv`. Excel is running, Downloads is empty.
* The `assets/v2/chat/` folder is open in an image viewer: a ready frame for every live prompt.
* Rule: if a prompt takes longer than 90 seconds, show the frame and move on. No buffer: 85 minutes of slides + a 5-minute break.
* When to send: **P1 — slide 11 • P2 — slide 13 • P3, P4 — slide 19 • P5 — slide 21 • P6 — slide 27 (or as early as 24)**.

### Opening and Part 1 “Data” (00:00 — 24:00)
* **01 Cover (1):** spreadsheet → answer → chart → one-page report. One file: Northstar 2025.
* **02 Five skills (2):** describe a file, a formula in words, a slide-ready chart, a one-page report, a one-minute check. Anna’s e-mail: “How did sales go this year? Why did advertising pay off worse in the second half? And why so many returns in the autumn? I need one page by Friday.”
* **03 Where data lives (3):** spreadsheets, exports, databases, text, documents, logs. The bottom line of each tile says how AI works: a formula, code, a query or reading. Chat question: “Which do you have?”
* **04 Table and text (3):** AI counts a table with a program (error — wrong formula); it reads text itself (error — wrong theme).
* **05 One row (3):** `2025-01-05 · Email · Electronics · North · N2 · 11 · 980 · 0 · 1`. A row = sales of a channel × category × region × warehouse for one day. It holds 11 orders. Chat question: “What is one row?”
* **06 How much data (3):** 73 — into a message • 1,261 — as a file • 46,132 — a file still works • 416,809 — a query to the database.
* **07 Key diagram (3):** data stays in the file; AI writes instructions; a program counts. You stand at two points: the question and the check. A number from AI — ask which program computed it.
* **08 Four traps (3):** duplicate (2025-03-19, Social, Home, $3,890.50 ×2) • text date `10/05/2025` • zeros in `ad_spend` for Email and Organic, which the model called missing • mixed units (real-life example).
* **09 Experiment (3):** 73 rows, no code, ChatGPT 17 Oct 2026: total right (256,045), four problems found, row 1055 — “needs checking”. On 13 Oct other models wrote “probably 6”; the source said 4. No visible working, and 1,261 rows won’t paste.

### Part 2 “Excel” (24:00 — 51:00)
* **10 The file and three questions (2):** the year → part 2; advertising → parts 2–3; returns → part 3. File: `Sales` 1,261 rows, `Reviews` 357 reviews.
* **11 Prompt 1 line by line (3):** **upload the file, send P1.** Describe a row → rows and period → problems → 5 questions → change nothing.
* **12 Quick / under control #1 (4):** “Find insights” found Social and N2 but chose quarters itself and kept the duplicate in the maths. The P1 answer: ✓ 1,261 rows, period, duplicate • ✗ “632 missing” (they are zeros) • ✗ text date. We take question 1 — channels including ad spend.
* **13 Prompt 2 line by line (3):** **send P2.** Where the result goes → breakdown → metric (revenue ÷ spend) → Excel formulas → line chart → .xlsx.
* **14 Quick / under control #2 (3):** ChatGPT sheet with numbers (where 5.39 comes from is invisible) vs Excel with `SUMIFS` in fx. The phrase: “replace the numbers with formulas”. These frames are the slide 15 fallback.
* **15 Demo 1 (5):** download the workbook → open in Excel → click an ad-return cell → a number? “replace the numbers with formulas”. Search ≈ 5.4 all year, Social 4 → 2 from July. Reference: `demo_v2/excel_demo/northstar_2025_formulas_EN.xlsx`.
* **16 Weak / good: seasonality (4):** “one number for the slide” → “+161.7% — December revenue vs January”. Three ways with a base: **+161.7% / +15.1% / +39.4%**; for the slide — “the second half is about 40% above the first”; no 2024 data. The quick prompt’s only clean failure.
* **17 Five charts (3):** time — line; comparison — sorted bars (Electronics leads); distribution — histogram (22 rows at 14%+ — N2); relationship — scatter (Social: spend right, revenue not up); composition — 100% bars.

### Break (51:00 — 56:00) • slide 18
Press “Start”. Keep the chat open with the file in it.

### Part 3 “Chat with a file” (56:00 — 74:00)
* **19 Demo 2: prompts 3 and 4 (5):** **send P3, then P4.** Heatmap: North × Electronics **24.8%**, others ~5%. N2 picked by the model; “packaging / damage” **49% vs 12%**. Open the code.
* **20 What we found (3):** Social H1 → H2: spend **+184%** ($69,402 → $197,009), revenue **+43%**, per $1 of ads 4 → 2. N2 = the North × Electronics cell, ~26% by month from September, others ~5%.
* **21 A slide-ready chart (3):** **send P5** (36 s). Finding as the title, sorted, labels on the bars, no legend or grid, one accent colour. “49% became 46%.”
* **22 60-second check (4):** **49% / 46% / 44%** vs **61%** (53 of 87). Rows **1,261 → 1,260**; one point (December **$373,435** in the Excel status bar) and the previous version; percent of what.
* **23 Quick / under control #3 (3):** “If we cut the Social budget in half from January…” → first line “loss 122.5k, assuming a proportional fall”; below — “the file can’t show the actual loss; test with a control group”. Look for “assuming”, “if”, “assumption”.

### Part 4 “Database” (74:00 — 83:00)
* **24 Channel database (2):** `channels` 26,544 → `videos` 416,809 → `video_stat_observations` 668,665. Lesson sample: 1,943 channels, 46,132 videos. Ready frames.
* **25 SQL line by line (3):** SELECT — what to show, COUNT — how many, MEDIAN — typical, FROM — where from, GROUP BY — by what. Describe the tables in the prompt. Re-run only in a temporary chat without connectors.
* **26 Result and trap (2):** 20–40 min — 13,000 vs 1,100, **12×**; vs the channel’s usual video — **1.03**. Big channels make long videos.
* **27 Where data comes from (2):** **send P6 at the start of the slide** (3 min 34 s). Export → API → scraping with three checks.

### Part 5 “Wrap-up” (83:00 — 90:00)
* **28 Report and recipe (3):** preview — stock “Series A–E”; the downloaded .docx is right: **$2,520,078**, December **$373,435**. The recipe expects an .xlsx with two sheets; the January CSV has no reviews and the monthly chart has one point.
* **29 Privacy (1):** green — practice data, any service; amber — work data, work account; red — personal data, only with approval.
* **30 Homework (2):** `analysis_pack/`: `analysis.xlsx`, `charts/` (one before/after pair), `report.docx`, `recipe.md`, `checks.md`. No AI licence in Excel needed. 12 points, pass from 8.
* **31 Summary (1):** describe first, formulas in words, one chart per question, the report as a file with a recipe, 60 seconds of checks. Next: L09 — Claude and artifacts.

### Six live prompts (copy)
```
P1  Describe this file: what one row is, how many rows, what period, what data problems. Suggest 5 questions a manager would ask. Don’t change anything yet.
P2  Add a sheet “Ad return” to the workbook: by month, revenue, ad spend and revenue per $1 of ads for Search and Social. Use Excel formulas, not pasted numbers. Build a line chart and let me download the .xlsx.
P3  Compute the return rate by region and category for September–December and show it as a heatmap.
P4  For the warehouse with the highest return rate, sort the reviews into themes and compare it with the other warehouses. Show 5 example reviews.
P5  Rework this chart for a slide: the title states the finding, bars sorted, value labels on the bars, no legend and no gridlines, one accent colour for N2, everything else grey. Explain in 3 points what you changed.
P6  Build a one-page report for a manager in Word: the question, 3 charts (revenue by month, ad return, N2 complaints), 3 findings and one point on “what this data does not prove”. And give me a short Python script that builds the same 3 charts from next month’s file.
```

### Pairs on ready frames (re-run in the morning in a new chat)
```
12  Here is the file. Find interesting insights.
16✗ How much did sales grow this year? Answer briefly, with one number for the slide.
16✓ Compute growth three ways: December vs January, December vs November, second half vs first half. For each number give the base and the period. Which number should go on the manager’s slide, and why?
23  If we cut the Social budget in half from January, how much do we save and how much revenue do we lose per quarter? Give numbers for a decision.
25  The database has a videos table: length and views of every video. Write an SQL query: which video length gets the most views? Explain every line.
```

### Numbers at hand (answers.md)
* Revenue for the year **$2,520,078** (with the duplicate $2,523,968.50). January $142,712 • November $324,344 • December $373,435. H1 $1,054,310.50 → H2 $1,469,658 (+39.4%).
* Revenue per $1 of ads: Search **5.15–5.39** all year; Social **~4** until June, **~2** from July (July 1.97).
* Returns September–December: North × Electronics (warehouse N2) **24.8%**, other cells 4.5–5.4%.
* N2 reviews September–December: 87, 53 about damage (61%) by the labels. In the ChatGPT run: **49% → 46% → 44%**.
