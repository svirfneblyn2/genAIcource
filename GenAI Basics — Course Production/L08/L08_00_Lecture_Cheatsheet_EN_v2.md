# One-page speaker cheatsheet • Lesson 08 v2 (19 slides • 90 minutes)
*Speaker: Igor Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*
*Topic: AI for data analysis — from a spreadsheet to a formula, charts and a one-page report • facts as of 2026-10-17*
*Deck: `deck/build_v2.py` • script: `L08_02_Instructor_Script_90MIN_EN_v2.md` • demos: `L08_04_Live_Demo_Runbook_READY_EN_v2.md` • reference: `demo_v2/answers.md`*
*Homework: `L08_05_Homework_EN_v2.md` • starter kit: `demo_v2/student_starter/` • repository: `genai-homeworks/L08/`*

---

### Before you start
* Teams: share the whole screen or practise switching windows (browser with the deck, ChatGPT, Excel). Browser zoom 125–150 %.
* ChatGPT: **one** chat for the whole lesson; keep it through the break. On the desktop: `northstar_2025_EN.xlsx` and `northstar_sales_2026-01.csv`. Excel is running, Downloads is empty.
* The `assets/v2/chat/` folder is open in an image viewer: a ready frame for every live prompt.
* Rule: if a prompt takes longer than 90 seconds, show the frame and move on.

### Part 1 (00:00 — 32:00)
* **01 Cover (2):** spreadsheet → answer → chart → one-page report. In Excel, Google Sheets or a chat with a file.
* **02 Anna’s e-mail (3):** “Hi! How did sales go this year? Why did advertising pay off worse in the second half? And why so many returns in the autumn? I need one page by Friday.” Three questions — three charts. File: `Sales` 1261 rows, `Reviews` 357 reviews.
* **03 First prompt (4):** P1 “describe the file and suggest 5 questions”. The model found the duplicate and the period and did not change the file. Mistakes: it called the zeros in `ad_spend` missing (“632 values are missing”) and missed the text date `10/05/2025`. Question 1 (channels including ad spend) is demo 1; question 3 (returns) is demo 2.
* **04 Four doors (4):** Excel (Claude / Copilot in Excel, or a file from a chat), Google Sheets (Gemini in the side panel), chat with a file (Python code), database (SQL). Pick by where the data lives. AI panels in Excel come with paid plans; without one, use a chat.
* **05 Demo 1, Excel (12):** P1 — 4 min; P2 “Ad return” sheet, download the .xlsx and open it in Excel — 8 min. The slide shows the real sheet from ChatGPT’s workbook: `Ad ROAS 2025`, numbers in the cells. “Open the workbook and click an ad-return cell. The fx bar should show a formula. If it shows a number, write: ‘replace the numbers with formulas’.” Gemini in Sheets — one spoken sentence. Optional 90 s: the same request in the Copilot / Claude for Excel side panel.
* **06 Seasonality (3):** December is **+161.7 %** vs January but **+15.1 %** vs November. November and December make **27.7 %** of annual revenue. Ask: “Percent of which month?”
* **07 Five questions, five charts (4):** time — line; comparison — sorted bars from zero; distribution — histogram of the return rate per row (the red tail from 14 % is N2); relationship — scatter (Social from July: spend moves right, revenue doesn’t move up); composition — 100 % bars.

### Break (32:00 — 37:00) • slide 08
Press “Start”. Check that the demo 1 chat is open and the file is in it.

### Part 2 (37:00 — 83:00, then 7 minutes of buffer)
* **09 Demo 2, ChatGPT (12):** P3 return-rate heatmap → P4 N2 review themes → P5 chart makeover, live. Open the code after every answer (“Analysis complete” / the code button above the chart).
* **10 What we found (4):** Social from July: revenue per $1 of ads **~4 → ~2**; spend H1 → H2 **+184 %**, revenue **+43 %**. Warehouse N2 = the North × Electronics cell: **24.8 %** for September–December, about 26 % in individual months, others ~5 %. N2 reviews are about crushed boxes and broken screens.
* **11 A slide-ready chart (4):** the P5 pair, large: `gpt_p3_themes_before.jpg` → `gpt_p4_themes_after.jpg`. Finding as the title, sorted, labels on the bars, no legend or grid, one accent colour. At the end: “49 % became 46 %”.
* **12 The 60-second check (3):** share of N2 reviews about damage — **49 % / 46 % / 44 %** (three model versions) vs **61 %** by the labels the file was built from (53 of 87). Steps: rows **1261 → 1260**; one point: against the source and the previous version (December **$373,435** in Excel’s status bar); percent of what.
* **13 The database updates daily: don’t export a file, ask the database (5):** the author’s working database — 26,544 channels, 416,809 videos, 668,665 view measurements. For the lesson, a frozen anonymised sample from 2026-10-17: 1,943 channels, 46,132 videos, views measured August–October 2026. The model writes SQL; the database counts. Story: 20–40-minute videos get **12×** the median views of 1–5-minute ones. Against ordinary videos of the same channel, only **+3 %**: big channels simply make long videos more often. Shown as ready frames, not live.
* **14 Where data comes from (3):** **send P6 at the start of this slide (≈65:00)** — the report takes 3–4 minutes. Export → official API → scraping as the last resort. Three checks for scraping: the site’s terms, personal data, load on the site.
* **15 Report and recipe (5):** the chat preview is a stock picture with “Series A–E” (`gpt_p5_fake_report_preview.jpg`). The downloaded .docx is correct: $2,520,078 for the year, December $373,435. Send the opened file. The recipe expects a two-sheet .xlsx; on `northstar_sales_2026-01.csv` the reviews chart won’t rebuild and the monthly chart has one point.
* **16 After the finding: test (2):** the table says what happened. What happens if we cut Social only a test shows: cut the budget in one region for 2–4 weeks. Season, audience, creatives and which channel got credit for a sale affect both budget and revenue.
* **17 What you may upload (2):** green — practice data, any service; amber — work data, work account only; red — personal data, only with approval and in a company-approved environment.
* **18 Homework (4):** `analysis_pack/` folder: `analysis.xlsx` (formula + pivot + chart), `charts/` (3 PNGs, one before/after pair), a one-page report, a recipe, `checks.md`. All doable without an AI licence in Excel. 12 points, pass from 8.
* **19 Summary + L09 (2):** the describe prompt first, formulas in words, one chart per question, the report as a file with a recipe, 60 seconds of checks. Next: Claude and artifacts — an analysis as an interactive page opened by a link.

### Six prompts (copy)
```
P1  Describe this file: what one row is, how many rows, what period, what data problems. Suggest 5 questions a manager would ask. Don’t change anything yet.
P2  Add a sheet “Ad return” to the workbook: by month, revenue, ad spend and revenue per $1 of ads for Search and Social. Use Excel formulas, not pasted numbers. Build a line chart and let me download the .xlsx.
P3  Compute the return rate by region and category for September–December and show it as a heatmap.
P4  For the warehouse with the highest return rate, sort the reviews into themes and compare it with the other warehouses. Show 5 example reviews.
P5  Rework this chart for a slide: the title states the finding, bars sorted, value labels on the bars, no legend and no gridlines, one accent colour for N2, everything else grey. Explain in 3 points what you changed.
P6  Build a one-page report for a manager in Word: the question, 3 charts (revenue by month, ad return, N2 complaints), 3 findings and one point on “what this data does not prove”. And give me a short Python script that builds the same 3 charts from next month’s file.
```

### Numbers at hand (answers.md)
* Revenue for the year **$2,520,078** (as in the file, with the duplicate, $2,523,968.50). January $142,712 • November $324,344 • December $373,435.
* Revenue per $1 of ads: Search **5.15–5.39** all year; Social **~4** until June, **~2** from July (July 1.97).
* Returns September–December: North × Electronics (warehouse N2) **24.8 %**, other cells 4.5–5.4 %.
* N2 reviews September–December: 87, 53 about damage (61 %) by the labels. In the ChatGPT run: **49 % → 46 % → 44 %**.
