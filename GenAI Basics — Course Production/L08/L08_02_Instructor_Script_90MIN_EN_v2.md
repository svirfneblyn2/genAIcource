# Instructor Script • Lesson 08: AI for Data Analysis (90 minutes, v2)

**Course:** GenAI Basics • Lesson 08 of 16 • Module 3: AI assistants at work
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners — people in different roles, not data analysts. Keep it plain. We show code and SQL for reference; we don't teach how to write them.
**Format:** 31 slides (`presentation_L08_AI_for_Data_Analysis_EN_v2.html` / PDF, generator `deck/build_v2.py`) • session in **Microsoft Teams** • break timer on slide 18
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Materials:** `demo_v2/northstar_2025_EN.xlsx` (sheets `Sales`, 1,261 rows, and `Reviews`, 357 reviews; the Russian group uses `northstar_2025.xlsx`), `demo_v2/northstar_sales_2026-01.csv` (next month's file), reference numbers `demo_v2/answers.md`, reference workbook with formulas `demo_v2/excel_demo/northstar_2025_formulas_EN.xlsx`, the channel database `demo_v2/channels/` (answers in `results/answers.md`), live-prompt frames `assets/v2/chat/`, frames for the pairs on slides 12, 14, 16, 23 — `assets/v2/chat_badgood/`, runbook `L08_04_Live_Demo_Runbook_READY_EN_v2.md`, homework `L08_05_Homework_EN_v2.md`, cheatsheet `L08_00_Lecture_Cheatsheet_EN_v2.md`.
**Time:** 85 minutes of slides and a 5-minute break. No buffer. If a demo runs long, cut where the script says "If time is short".

**Lesson goal:** students understand where data lives and what AI does with it. They take their own spreadsheet through the whole path: describe the file → ask for a formula and a chart in words → find the slice where a problem hides → build a one-page report as a file → check the numbers in 60 seconds. And they can say what the data does not show.

> **Before you start (Teams):** share the whole screen, or practise switching windows beforehand: the browser with the deck, ChatGPT, Excel. Browser zoom 125–150%. In ChatGPT open **one** new chat for the whole lesson: prompt 6 builds on the charts from prompts 2–5. On the desktop: `northstar_2025_EN.xlsx` and `northstar_sales_2026-01.csv`. Excel is running, the Downloads folder is empty. The `assets/v2/chat/` folder is open in an image viewer. The ready frames come from the Russian-language run; the English file gives the same numbers.

---

## Session map (31 slides • 85 minutes + 5-minute break)

**Live prompts.** P1 and P2 are demo 1 on slide 15. To fit into 5 minutes, send P1 early, on slide 11, and P2 on slide 13. On slide 15 you only download the workbook and click a cell. P3 and P4 — slide 19. P5 — slide 21. P6 — at the start of slide 27, shown on slide 28.
**Ready frames, not run live:** the experiment on slide 9, the pairs on slides 12, 14, 16, 23, the channel database on slides 24–26.

| Slide | Block | Time | Min | On screen | In one line |
|---|---|---|---|---|---|
| **01** | Cover | 00:00 — 01:00 | 1 | Spreadsheet → answer → chart → one-page report | The whole lesson on one file, Northstar 2025. |
| **02** | Five skills | 01:00 — 03:00 | 2 | Five skills + Anna's e-mail | We answer the e-mail all lesson. |
| | **Part 1. Data** | | | | |
| **03** | Where data lives | 03:00 — 06:00 | 3 | Six tiles: spreadsheets, exports, databases, text, documents, logs | Most often you have a spreadsheet or an export. |
| **04** | Table and text | 06:00 — 09:00 | 3 | Sales sheet rows and Reviews | AI counts a table with a program; it reads text itself. |
| **05** | One row | 09:00 — 12:00 | 3 | One row of the file, colour-coded | First question for any file: what is one row? |
| **06** | How much data | 12:00 — 15:00 | 3 | Ladder: 73 / 1,261 / 46,132 / 416,809 | Size decides where the data goes. |
| **07** | Key diagram | 15:00 — 18:00 | 3 | Two lanes: data and AI | Data stays in the file; AI writes instructions; a program counts. |
| **08** | Four traps | 18:00 — 21:00 | 3 | Duplicate, text date, zero or missing, mixed units | The data owner knows what oddities mean. |
| **09** | Experiment: 73 rows | 21:00 — 24:00 | 3 | Pasted CSV and the ChatGPT answer, 17 Oct 2026 | Got it right, but no visible working. |
| | **Part 2. Excel** | | | | |
| **10** | The file and three questions | 24:00 — 26:00 | 2 | Three e-mail questions → three lesson parts + file frame | Each question gets its own part. |
| **11** | Prompt 1 line by line | 26:00 — 29:00 | 3 | Five prompt lines with notes | **Upload the file, send P1.** |
| **12** | Quick / under control #1 | 29:00 — 33:00 | 4 | "Find insights" vs the prompt 1 answer with ✓ / ✗ marks | Works, but the model picks the questions. We take question 1. |
| **13** | Prompt 2 line by line | 33:00 — 36:00 | 3 | Six prompt lines | **Send P2.** |
| **14** | Quick / under control #2 | 36:00 — 39:00 | 3 | Numbers in cells vs a SUMIFS formula | Numbers can't be checked; formulas can. |
| **15** | Demo 1 live | 39:00 — 44:00 | 5 | Six-step checklist | **Download the workbook, open in Excel, click a cell.** |
| **16** | Weak / good: seasonality | 44:00 — 48:00 | 4 | "One number for the slide" vs three ways | A percentage without a base misleads. |
| **17** | Five charts | 48:00 — 51:00 | 3 | Five mini-charts from the file | Name the question; the model picks the chart type. |
| **18** | **Break** | **51:00 — 56:00** | **5** | **Timer** | **Keep the chat open.** |
| | **Part 3. Chat with a file** | | | | |
| **19** | Demo 2: prompts 3 and 4 | 56:00 — 61:00 | 5 | Two prompt breakdowns + heatmap and review themes | **Send P3, then P4.** One cell shows 24.8%. |
| **20** | What we found | 61:00 — 64:00 | 3 | Social: spend and revenue; warehouse N2 | The number shows where; the text explains why. |
| **21** | A slide-ready chart | 64:00 — 67:00 | 3 | Before / after P5 | **Send P5.** You edit a chart with words. |
| **22** | 60-second check | 67:00 — 71:00 | 4 | 49 / 46 / 44% vs 61% + three steps | After every redo, compare a couple of numbers. |
| **23** | Quick / under control #3: Social | 71:00 — 74:00 | 3 | The first line of the answer and the paragraphs below | The first line is a scenario. Look for assumptions. |
| | **Part 4. Database** | | | | |
| **24** | Channel database | 74:00 — 76:00 | 2 | Three linked tables | Linked tables, updated daily. |
| **25** | SQL line by line | 76:00 — 79:00 | 3 | Prompt and query with each line translated | SQL reads almost like a sentence. |
| **26** | Result and trap | 79:00 — 81:00 | 2 | 12× vs ≈1.0 within a channel | Big channels make long videos. |
| **27** | Where data comes from | 81:00 — 83:00 | 2 | Export → API → scraping | **Send P6.** Look for the Export button first. |
| | **Part 5. Wrap-up** | | | | |
| **28** | Report and recipe | 83:00 — 86:00 | 3 | Fake preview, downloaded .docx, script | The manager gets the opened file. |
| **29** | Privacy | 86:00 — 87:00 | 1 | Data traffic light | Practice data anywhere; work data in the work account. |
| **30** | Homework | 87:00 — 89:00 | 2 | `analysis_pack/` folder | A pack you can send to a manager. |
| **31** | Summary + L09 | 89:00 — 90:00 | 1 | Five moves + teaser | On Monday — on your own spreadsheet. |

---

## Detailed script

### Opening (00:00 — 03:00)

---

### Slide 01 (00:00 — 01:00) • Cover
**On screen:** a full-slide illustration. "AI for Data Analysis". Subtitle "Spreadsheet → answer → chart → one-page report". Below: formulas, pivots and charts on request in plain words — in Excel, Google Sheets or a chat with a file. Case study: Northstar online shop sales for 2025.

> "Hi everyone! Today we work with spreadsheets. We take an ordinary sales export and, during the lesson, turn it into formulas, charts and a one-page report for a manager. Using tools you already have.
>
> The whole lesson uses one file: sales of a made-up shop, Northstar, for 2025. Near the end I'll show a large YouTube channel database that no longer fits in Excel."

**What to do:** one minute. Move on.

---

### Slide 02 (01:00 — 03:00) • Five skills you take away today
**On screen:** left, five skills: describe a file, a formula in words, a slide-ready chart, a one-page report, a one-minute check. Right, the commercial director's e-mail: "How did sales go this year? Why did advertising pay off worse in the second half? And why so many returns in the autumn? I need one page by Friday." Below: "We spend the lesson answering this e-mail."

> "What you'll leave with. Five skills. You'll describe any file in a minute. Ask for a formula and a pivot in Excel in plain words. Make a chart you can put on a slide. Build a one-page report. And check the numbers in a minute.
>
> I'll show each skill on a live example. Several come with a pair of real ChatGPT answers: how to get an answer quickly, and how to keep it under control.
>
> On the right is the task. Anna, commercial director of the Northstar shop, wants one page by Friday. We answer this e-mail all lesson. The shop and the data are made up, so the file can go into any chat."

---

### Part 1: what data is (03:00 — 24:00)

---

### Slide 03 (03:00 — 06:00) • Where data lives at work
**On screen:** six tiles. Spreadsheets (Excel, Google Sheets) — AI writes formulas and pivots. Exports (CSV from a CRM, accounting, ad accounts, YouTube Studio) — file into a chat, AI writes code. Databases (millions of rows, updated daily) — AI writes an SQL query. Text (reviews, e-mails, support chats) — AI reads and sorts into themes. Documents (PDF invoices, contracts) — AI pulls the numbers into a table. Events and logs — usually via a database and an analyst. Bottom: "Most often you have a spreadsheet or an export. Sometimes text. Less often a database. Today we cover all three."

> "Before we upload files to a chat, let's agree what data is. Any records you can count or read something from.
>
> Look at the bottom line of each tile. It says how AI works with it. With a table it writes a formula or code. With text it reads. With a database it writes a query. That's the main point of this slide.
>
> At work you most often have a spreadsheet or an export. Sometimes text. Less often a database. Today we'll look at all three."

**Teams chat question:** "Which of these do you have at work?" Read 2–3 answers aloud.

---

### Slide 04 (06:00 — 09:00) • Table and text: AI handles them differently
**On screen:** left, the first six rows of the Sales sheet (date, channel, category, region, orders, revenue). Caption: "AI counts: it writes a formula or code, a program adds and divides. The typical error is a wrong formula." Right, four real reviews from the Reviews sheet, two of them bad autumn reviews for warehouse N2. Caption: "AI reads: it assigns each review to a theme and counts themes. The typical error is the wrong theme."

> "Left: real rows from the sales sheet. Right: real reviews from the same file. Two different worlds.
>
> With a table, AI doesn't add anything in its head. It writes a formula or code, and a program counts. Errors are usually in the formula: wrong column, wrong period.
>
> With text it's the other way round. AI reads each review itself and decides what it is about. The error here is a wrong theme. In half an hour we'll see exactly that error on these reviews."

---

### Slide 05 (09:00 — 12:00) • One row: what the record is and what it measures
**On screen:** one row of the file, enlarged: `2025-01-05 · Email · Electronics · North · N2 · 11 · 980.0 · 0 · 1`. Under each cell, its type: date (blue), categories (violet), numbers with units (green — pieces, amber — dollars). Three notes: what a row is, categories, numbers. Bottom: "First question for any file: what is one row?"

> "One real row of our file. Blue is the date. Violet are categories: channel, product category, region, warehouse. We slice the data by them. Green and amber are numbers. Each number has its unit: orders in pieces, revenue and ad spend in dollars.
>
> A question for you."

**Teams chat question:** "What is one row in this file?" Wait for answers.

> "A common answer is 'an order'. Look at the orders column: this row holds 11 orders. So a row is the sales of one channel for one category, region and warehouse on one day.
>
> Get this wrong and every 'average per customer' comes out wrong. The model can get it wrong too. That's why the lesson's first prompt asks it to describe a row."

---

### Slide 06 (12:00 — 15:00) • Size decides where the data goes
**On screen:** four bars on a log scale. 73 rows — can be pasted into a message. 1,261 — our Northstar file, upload as a file. 46,132 — channel database sample, a file still works. 416,809 — the whole video database, ask it with a query.

> "Four steps. Dozens of rows can be pasted as text into a message. Thousands, like our file, go in as a file. Tens of thousands, like the channel database sample, a file still handles.
>
> Hundreds of thousands and millions of rows, updated every day, aren't exported to a file. You ask the database with a query. I'll show that in part four.
>
> The scale is logarithmic: each step is roughly ten times the previous one. Otherwise the first three bars would be invisible."

---

### Slide 07 (15:00 — 18:00) • Data stays in the file. AI writes instructions, a program counts
**On screen:** a two-lane diagram. Top, "Data": file or database (1,261 rows stay there) → a program counts (Excel, Python, database) → result (table, chart, file). Bottom, "AI": your question → the model writes a formula, code or SQL → the model explains in words. Arrows: "code goes to the data", "the answer comes back". Notes: "You stand at two points: asking the question and checking the result" and "Rule: when AI states a number, ask which program computed it."

> "This is the key diagram of the lesson. We'll come back to it.
>
> The top lane is the data. The file stays where it was. A program counts. You get a result.
>
> The bottom lane is AI. It reads your question and the column names. It writes a formula, code or a query. That instruction goes to the data, and the program runs it. Then the model retells the result in words.
>
> Hence the rule. A program should compute any number in an AI answer. If the model 'just knows' a number, it's a guess.
>
> And you stand at two points. At the start you ask the question. At the end you check the result."

---

### Slide 08 (18:00 — 21:00) • Four traps in real data, three of them in our file
**On screen:** four cards. A duplicated row: `2025-03-19 · Social · Home · 3,890.5 ×2`, revenue inflated by this amount. A date as text: `10/05/2025 ← 2025-05-10?` — 10 May or 5 October. Zero or missing: `Email · ad_spend = 0` — Email has no ads, the model called these zeros "missing". Mixed units: roubles and dollars in one column, a real-life example. Bottom: "The model often finds these, but doesn't always understand them."

> "We deliberately put a few typical problems into the practice file.
>
> A duplicate: one sales row written twice. Revenue is inflated by 3,890 dollars.
>
> A text date: 10/05/2025. Is it 10 May or 5 October? It depends on the country the export came from.
>
> Zeros in ad spend for Email and Organic. These channels have no ads, so zero is normal for them.
>
> The fourth is mixed units in one column. Our file doesn't have that; it's a real-life example.
>
> In our run ChatGPT found the duplicate itself. But it called the zeros missing and didn't notice the text date. The model sees oddities. The data owner knows what they mean."

---

### Slide 09 (21:00 — 24:00) • 73 rows pasted into a message: the model got it right. Why we still don't do it
**On screen:** left, the prompt frame: 73 CSV rows pasted into a message, "no tools or code". Right, the ChatGPT answer from 17 Oct 2026: 259,357 across all rows, 256,045 without the duplicate, a table of four problems. Three notes: the total is right, duplicate and blank region found; no visible working; 1,261 rows won't paste like this.

> "A small experiment. We took a small 73-row table, pasted it straight into a message and asked the model not to use any tools. Let it count in its head.
>
> The result on 17 October: ChatGPT got revenue right, 256,045 without the duplicate. It found all four problems. For the row with 66 returns on 62 orders it said 'needs checking'.
>
> For comparison: on 13 October other models 'fixed' that row on the same table. They wrote 'probably 6'. The source said 4. Models have become more careful.
>
> So why don't we work this way? The working is invisible; there's nothing to repeat or check. And a real file of thousands of rows won't fit in a message. So from here on we work with the file and look at the code the model wrote."

**If asked about the table:** it's the small practice file from the previous lesson version, `demo_assets/northstar_sales_messy.csv`. The 13 October experiment is in `demo_assets/no_code_experiment_2026-10-13.md`.

---

### Part 2: Excel and Anna's first question (24:00 — 51:00)

---

### Slide 10 (24:00 — 26:00) • Three questions in the e-mail — three parts of the lesson
**On screen:** left, the e-mail's three questions, each with its part of the lesson. 1 — "How did sales go this year?" (part 2: Excel, formulas, seasonality). 2 — "Why does advertising pay off worse?" (parts 2–3: Search and Social return). 3 — "Why the autumn returns?" (part 3: the table + review text). Right, a frame of `northstar_2025.xlsx`: 1,261 rows, Reviews sheet — 357 reviews.

> "You've already seen Anna's e-mail. It has three questions, and each becomes its own part of the lesson.
>
> The first, how sales went this year, we do now in Excel. The second, about advertising, we start in Excel and finish after the break. The third, about returns, comes after the break; there we need both numbers and review text.
>
> On the right is the real lesson file, opened in ChatGPT. 1,261 sales rows and a second sheet with reviews."

**Teams chat question:** "Which question from the e-mail would you check first, and why?" Collect 2–3 answers.

---

### Slide 11 (26:00 — 29:00) • Prompt 1 line by line
**On screen:** the prompt split into five lines, each with a number, a colour and a note on the right:
1. "Describe this file: what one row is," — understand the data first;
2. "how many rows, what period," — numbers you'll check later;
3. "what data problems." — duplicates and oddities before any maths;
4. "Suggest 5 questions a manager would ask." — a work plan;
5. "Don't change anything yet." — or the model quietly "cleans" the file.

**What to do — in the first seconds of the slide:** switch to ChatGPT, upload `northstar_2025_EN.xlsx`, send P1. Come back to the slide and talk while the model thinks. These are the first two steps of demo 1 on slide 15; doing them now saves time.
```
Describe this file: what one row is, how many rows, what period, what data problems. Suggest 5 questions a manager would ask. Don’t change anything yet.
```

> "I've sent the first prompt. While the model thinks, let's go through it line by line.
>
> Line one makes the model understand what's in the file first. Let it describe one row.
>
> Line two gives numbers to check: how many rows and what period. We know the answer: 1,261 rows, 2025. If the model says something else, you see it at once.
>
> Line three asks for problems before any maths. Duplicates, odd dates.
>
> Line four turns the answer into a plan: five manager questions. We'll pick the one that matches the e-mail.
>
> Line five is the shortest and the most useful: 'don't change anything yet'. Without it the model may quietly drop duplicates or fill blanks. You get an answer and never learn what it changed.
>
> The full prompt is in the cheatsheet. Use it for any file of your own."

---

### Slide 12 (29:00 — 33:00) • Quick / under control #1: "Find insights" works too. But the model picks the questions
**On screen:** left, "Quick" — "Here is the file. Find interesting insights." and frames of the answer. Note: "The model found Social and N2. But it chose the comparisons itself (quarters) and kept the duplicate in the maths." Right, "Under control" — prompt 1 and two frames of its answer. Note with marks: "✓ 1,261 rows, period, duplicate · ✗ called 632 zero ad-spend values 'missing' · ✗ missed the text date. We take question 1."

> "You've probably written 'find insights' to a model. We tried it too, on 17 October.
>
> The result is good. In a minute and a half ChatGPT found both main stories in the file: Social's falling ad return and the returns at warehouse N2. Models have become strong, and this prompt often works.
>
> But look closer. The model chose the comparisons itself: quarters, half-years. It found the duplicate but wrote that the calculations keep the original rows. So the duplicate stayed in the numbers. And Anna's question, 'how did sales go this year', gets no direct answer.
>
> On the right is the answer to prompt 1. Let's check it by the marks. 1,261 rows — right. The period, all of 2025 — right. Duplicate found — right. And the model says it didn't change the file.
>
> Now the mistakes. The model says '632 ad_spend values are missing'. Those are zeros. Email and Organic have no ads; we saw that on slide 8. And it missed the text date. Ask back: 'Are these missing or zeros? Any dates in another format?'
>
> Of the five manager questions we take the first: which channels pay off best including ad spend. It matches Anna's second question. That's what the next prompt computes."

**What to do:** glance at the chat. If the live P1 answer is in, show it alongside and check the same three things: 1,261 rows, 2025, the duplicate. If its question 1 is also about channels or ads, take it. If not, say: "We'll take the question from our run."

---

### Slide 13 (33:00 — 36:00) • Prompt 2 line by line
**On screen:** the prompt split into six lines:
1. "Add a sheet 'Ad return' to the workbook:" — where the result appears;
2. "by month … for Search and Social." — the breakdown: time and channels;
3. "revenue, ad spend and revenue per $1 of ads." — the metric: revenue ÷ spend;
4. "Use Excel formulas, not pasted numbers." — so you can check and recalculate;
5. "Build a line chart" — the type for "how did it change";
6. "and let me download the .xlsx." — the result as a file.

**What to do — in the first seconds of the slide:** send P2 to the same chat.
```
Add a sheet “Ad return” to the workbook: by month, revenue, ad spend and revenue per $1 of ads for Search and Social. Use Excel formulas, not pasted numbers. Build a line chart and let me download the .xlsx.
```

> "I've sent the second prompt. Let's go through it while the model works.
>
> Where the result goes — a new sheet in the workbook. The breakdown — months and two ad channels. The metric — revenue per ad dollar. That's revenue divided by spend.
>
> Then the key line: Excel formulas. Without it the model often pastes already computed values into the cells. You can't check such a number in the workbook.
>
> A line chart, because the question is 'how did it change over time'. And a file at the end that you can open and forward."

---

### Slide 14 (36:00 — 39:00) • Quick / under control #2: numbers in cells can't be checked. Formulas can
**On screen:** top, "Quick" — a sheet from ChatGPT with plain numbers in the cells. Note: "Where 5.39 comes from is invisible. Change the file — numbers don't update." Bottom, "✓ Under control" — the same table in Excel with a `SUMIFS` formula in the fx bar. Note: "The fix is one phrase: 'replace the numbers with formulas'."

> "Top: the real sheet ChatGPT returned in our run. We asked for formulas. The cells held numbers. Where 5.39 came from, you can't see. Change the data and the number stays the same.
>
> Bottom: the same table in Excel. Revenue is a SUMIFS over the Sales sheet; the return is =B2/C2. The numbers match. But only the bottom table can be checked.
>
> The rule: click any result cell. See a number? Write to the model: 'replace the numbers with formulas'. We'll do it live now."

**What to do:** at the end of the slide, check whether the workbook has arrived. These frames are the fallback for demo 1.

---

### Slide 15 (39:00 — 44:00) • Demo 1 live: from the file to a formula in a cell
**On screen:** a six-step checklist: upload `northstar_2025.xlsx` to ChatGPT; prompt 1 (slide 11); prompt 2 (slide 13); download the workbook and open it in Excel; click an ad-return cell — a number → "replace the numbers with formulas"; out of time — the ready frames from slide 14. Right: "What you should get: Search earns about $5 per ad dollar all year; Social drops to about $2 from July." Notes: the same prompt 2 works in the Claude or Copilot side panel in Excel; an answer over 90 seconds — show the frame.

**What to do (per the runbook):**
1. If you didn't send P1 and P2 on slides 11 and 13, do it now. Then you'll most likely finish on the slide 14 frames.
2. Download the `.xlsx` from the chat, open it in Excel, go to the new sheet.
3. Click an ad-return cell. Show the fx bar.
4. If it shows a number, send "replace the numbers with formulas", download the workbook again, click the same cell.

> "I'm opening the workbook the model returned. I click an ad-return cell and look at the formula bar."

If there's a formula:

> "The formula is there. Excel does the counting here; the model only wrote the formula. Change the spend and the number recalculates."

If there's a number:

> "A number. I write 'replace the numbers with formulas' and download again."

Then the chart:

> "Now the chart. For Search each ad dollar brings about 5.4 dollars of revenue, all year. For Social it's about 4 until June. From July the line halves, down to 2. That's the second question in Anna's e-mail. We'll come back to it after the break."

**What to look for (from `answers.md`):** Search 5.15–5.39 all year. Social 3.91–4.05 until June, 1.97–2.02 from July. Social in March: revenue 50,378, spend 12,514. If the March numbers are higher, the model kept the duplicate.

**If something goes wrong:**
* **The workbook hasn't arrived within 90 seconds.** Go back to slide 14, or open the reference `demo_v2/excel_demo/northstar_2025_formulas_EN.xlsx` and click the cell there.
* **"Replace the numbers with formulas" didn't help.** Be specific: "The revenue-per-$1 column holds numbers. Rewrite it as a formula: revenue / spend." Still nothing — open the reference workbook.
* **The chart is only in the chat.** Ask: "Insert this chart into the workbook on the ad-return sheet." No time — move on.
* **Claude for Excel or Copilot side panel.** Only if you're ahead of time. Otherwise one sentence: "With a licence you type the same text in the side panel."

---

### Slide 16 (44:00 — 48:00) • Weak / good: "One number for the slide" — and the model picked the loudest
**On screen:** left, "✗ Weak" — "How much did sales grow this year? One number for the slide." The answer: "+161.7% — December revenue vs January." Below it, the revenue-by-month chart: January $142.7k, December $373.4k, a dashed line from the January level, a green segment +15.1% vs November. Right, "✓ Good" — "Compute growth three ways, give the base and period for each. Which number goes on the slide and why?" and the answer table. Note: "on the slide — 'the second half is about 40% above the first'."

> "In the earlier pairs the quick prompt also gave a useful answer. Here it gave a misleading one.
>
> A real run from 17 October. We asked for one number for the slide. The model said: plus 161.7 percent, December revenue versus January.
>
> The number is right. But January after the holidays is the weakest month. December is sales season. A manager will read this as the business growing two and a half times. It's the season. The chart on the left shows it: December versus November is only 15 percent.
>
> On the right is the good prompt. Compute it three ways: December versus January, December versus November, second half versus first. Give the base and period for each. And say which number goes on the slide.
>
> The model gave three numbers: 161.7, 15.1 and 39.4 percent. And it proposed the second half versus the first for the slide, about 40 percent. It also noted there's no 2024 data, so 'year over year' can't be claimed.
>
> The rule is simple. See a percentage — ask: from which month, over what period?"

**Teams chat question (optional):** "Which number would you put in Anna's report?" A good answer: any, as long as the base is written next to it.

---

### Slide 17 (48:00 — 51:00) • Five questions, five charts — all from our file
**On screen:** five mini-charts. Line — "How did it change over time?" (peak in Nov–Dec). Sorted bars — "Which is bigger?" (Electronics leads revenue). Histogram — "How are values spread?" (red tail: 22 rows with 14%+ returns). Scatter — "Are two numbers related?" (Social from July: spend up, revenue not). 100% bars — "What makes up the whole?" (channel shares by quarter). Bottom — how to ask.

> "Five ordinary questions and a chart for each. All five are built from our file.
>
> How did it change over time — a line. You see the year-end peak.
>
> Which is bigger — sorted bars, axis from zero. Electronics leads revenue.
>
> How are values spread — a histogram. Most rows have 2–8 percent returns. On the right is a red tail from 14 percent. That's warehouse N2; we'll get there.
>
> Are two numbers related — a scatter. Each dot is one channel-month. Social's amber dots in the second half moved right: spend went up. They didn't move up: revenue stayed about the same.
>
> What makes up the whole — 100 percent bars. No more than 4–5 parts.
>
> How to ask: 'Build one chart that answers such-and-such question, label the axes and units.' Name the question; the model picks the chart type. One chart per question: it's easier to check and to present."

**If time is short:** name only the line, the bars and the scatter.

---

### Slide 18 (51:00 — 56:00) • Break
**On screen:** a 05:00 timer, "Start" and "Reset" buttons. Caption: next, a demo in a chat with a file, then a large database, the report and homework.

> "Five-minute break. Then we go back to the same chat: returns, reviews and a slide-ready chart."

**What to do:** press "Start". Don't close the demo 1 chat: prompt 6 needs the charts from demos 1 and 2. Check the file is still in the chat. Open a new chat only if the old one broke. Then upload the file again.

---

### Part 3: chat with a file, returns and reviews (56:00 — 74:00)

---

### Slide 19 (56:00 — 61:00) • Demo 2: 6% returns for the year. One cell shows 24.8%
**On screen:** two columns. Prompt 3 — the table: "Compute the return rate" (metric: returns ÷ orders) · "by region and category" (breakdown: two axes) · "for September–December" (the period Anna asked about) · "and show it as a heatmap" (the outlier shows as colour). Under it, the heatmap frame: "result: 24.8% in one cell". Prompt 4 — the text: "For the warehouse with the highest return rate" (the model finds the slice) · "sort the reviews into themes" (text → categories) · "and compare with the other warehouses" (the base for comparison) · "Show 5 example reviews" (a check by eye). Under it, the review-themes frame: "prompt 5 → slide 21".

**What to do — in the first seconds of the slide:** send P3. When the answer arrives (usually within a minute), send P4 straight away.
```
Compute the return rate by region and category for September–December and show it as a heatmap.
```
```
For the warehouse with the highest return rate, sort the reviews into themes and compare it with the other warehouses. Show 5 example reviews.
```

> "Anna's third question is the autumn returns. I've sent prompt 3.
>
> It works with the table. The metric is the return rate: returns divided by orders. The breakdown is regions and categories, two axes. The period is September to December, the one Anna asked about. The type is a heatmap: an unusual value shows up as colour at once.
>
> Prompt 4 works with text. The model finds the warehouse with the worst return rate itself. It sorts that warehouse's reviews into themes. It compares them with the other warehouses. And the five examples let you check the themes by eye."

When the P3 answer arrives, show it. Open the code: in ChatGPT it's the "Analysis complete" block or the code button above the chart. Names change; look above the chart.

> "I'm opening the code. A program the model wrote does the counting. You can open and read it.
>
> The heatmap. The overall return rate is about 6 percent. But one cell lights up: North and Electronics, 24.8 percent. The rest are about 5. The annual total hides it.
>
> Now the reviews. The model picked warehouse N2 by itself. That's the cell that lights up. The 'packaging and damage' theme is 49 percent of N2 reviews. At the other warehouses it's 12. The text explains the number: parcels arrive damaged."

Read the model's caveat aloud if it gives one: the theme also caught praise of packaging ("Neatly packed, everything intact"). You'll need it on slide 22.

**Teams chat question:** "Which number on the heatmap would you check first?"

**What to look for:** a 4 × 4 grid; North × Electronics 24.8%; the rest 4.5–5.4%; the rate is per order. N2 — 87 reviews for September–December.

**If something goes wrong:**
* **Thinks longer than 90 seconds.** Talk over the frames under the breakdowns and move on.
* **Computed the whole year.** The cell will be paler. Ask: "Only September–December."
* **Divides returns by revenue.** Ask: "The return rate is returns divided by orders."
* **Picked the wrong warehouse.** Ask: "Did you choose by rate or by number of returns?"
* **Theme percentages differ.** The model splits themes its own way each time. One thing matters: the damage theme is several times higher at N2.

---

### Slide 20 (61:00 — 64:00) • Two problems the annual total doesn't show
**On screen:** left, Social — spend and revenue bars by month, second half highlighted. Note: second half vs first — spend +184%, revenue +43%, revenue per $1 of ads 4 → 2. Right, warehouse N2 — return rate by month: the red N2 line against the grey line for other warehouses. Note: from September N2 returns are about 26%, others about 5%. Bottom: "The number shows where; the text explains why. Reviews are data too."

> "Two findings. I redrew them straight from the data.
>
> Left, Social. From July ad spend nearly tripled: 69 thousand dollars in the first half, 197 thousand in the second. Revenue grew 43 percent. Each ad dollar now brings half as much. And the annual total looks fine; revenue grows. That's why Anna can't see where the hole is.
>
> Right, warehouse N2. Until August returns are like everyone else's, about 5 percent. From September, about a quarter of orders. The heatmap showed 24.8 percent for the whole September–December period; the monthly line shows about 26. Reviews explain why: crushed boxes, broken screens.
>
> The numbers show where the problem is. The text explains why."

**Teams chat question:** "What would you suggest to Anna for each finding?" If someone writes "cut Social", say: "We'll discuss that on slide 23."

---

### Slide 21 (64:00 — 67:00) • You edit a chart with words, like text
**On screen:** left, "Before: the default chart" and prompt 5. Right, "After: 36 seconds later". Three notes: title = finding ("Almost 9× more" instead of "Review themes"); one colour (N2 blue, the rest grey); values on the bars, no legend or grid.

**What to do — in the first seconds of the slide:** send P5. In our run the answer came in 36 seconds.
```
Rework this chart for a slide: the title states the finding, bars sorted, value labels on the bars, no legend and no gridlines, one accent colour for N2, everything else grey. Explain in 3 points what you changed.
```

> "I've sent prompt 5. While it works, look left. That's how the model draws a chart by default. The title names a topic. A legend, two bright colours, small labels. Nothing for the eye to catch.
>
> The prompt has five rules, and they work for any chart. Title = finding. Bars in order. Labels right on the bars. Nothing extra: no legend, no grid. One accent colour."

Show the live answer or the frame on the right.

> "Here's the result. The title states the finding at once. N2 is blue, the rest grey; the eye finds the point in a second. This version goes on a manager's slide. The prompt is in the cheatsheet.
>
> Now look at the numbers. It was 49 percent. Now it's 46. That's the next slide."

**Teams chat question (optional):** "What changed on the chart besides the colour?" Wait until someone spots the numbers.

**If the answer hasn't come within 90 seconds:** talk over the frame on the right.

---

### Slide 22 (67:00 — 71:00) • Three versions of a chart, three different numbers. Compare after every redo
**On screen:** share of N2 reviews about damage, September–December: 49% — first chart; 46% — after restyling; 44% — in the Word report; 61% — by the labels the file was built from. A frame: the model explains what it changed. Right, three steps: rows before and after (1,261 → 1,260); one point against the source and the previous version; percent of what (+161% and +15% are both right). Note: check review themes by reading.

> "We only asked for a new look. The model also re-counted the themes. It moved praise of packaging, 'neatly packed', from 'damage' to 'product OK'. The share became 46 percent. In the final report of our run — 44.
>
> By the labels we used to build the practice file, 53 of 87 N2 reviews are about damage. That's 61 percent. The model searches by words and misses complaints written in other words.
>
> The conclusion about the warehouse doesn't change: there are many times more damage complaints there. What changes is the number that goes to the manager.
>
> So after every redo — a 60-second check. Three steps.
>
> One — rows. The file has 1,261 rows; after the duplicate is removed, 1,260. Ask the model how many it dropped and why.
>
> Two — one point. Take one number from the chart and find it in the source file. For example, filter December and select revenue: Excel shows 373,435 dollars at the bottom. And compare with the previous answer: it was 49, now it's 46.
>
> Three — percent of what. From which month and over what period. 46 percent is a share of 87 N2 reviews for September–December. Out of all 357 reviews you'd get a different number.
>
> Check review themes by reading. Open a dozen reviews and count yourself."

**If asked about "the other warehouses":** 12% on the first chart, 5% after restyling. The model re-counted both groups.

**If your live run gives different numbers:** say so aloud. Compare your two versions the same way: it was this, now it's that.

**What to do if you have a minute:** show step two in Excel: filter December, sum in the status bar.

---

### Slide 23 (71:00 — 74:00) • Quick / under control #3: the first line of the answer is a scenario
**On screen:** left, "Quick" — the first line of the answer to "If we cut the Social budget in half from January, how much do we save and how much revenue do we lose per quarter?". Note: "'Revenue loss — 122.5k' in the first line. That assumes revenue falls together with the budget." Right, "Under control" — the same answer, paragraphs below. Note: "The model itself says: the file can't show the real loss; you need a test with a control group."

> "After the Social finding it's tempting to cut the budget at once. We asked the model directly: if we cut Social in half from January, how much do we save and how much do we lose?
>
> The first line of the answer: savings of 61 thousand, revenue loss of 122.5 thousand. It sounds like a ready number for a decision. But next to it: 'assuming it falls proportionally'. So the model assumed revenue falls exactly in step with the budget. That's a scenario.
>
> Read to the end. Further down the model itself says this file can't show the actual loss. And it suggests a test: cut the budget for a test group and compare with a control group.
>
> The answer is good. But a manager reads the first line. So before you pass a number on, look for the words 'assuming', 'if', 'assumption' in the answer. The table says what happened. Only a test shows what will happen."

**If the model in your run didn't name the assumption:** ask it: "What assumption are you making? Can this data tell us that?"

---

### Part 4: when the data is bigger than a file (74:00 — 83:00)

---

### Slide 24 (74:00 — 76:00) • The channel database: three linked tables, updated daily
**On screen:** three cards. `channels` — 26,544 rows, row = one channel (title, subscribers, country, language). `videos` — 416,809 rows, row = one video (channel id, date, length, tags). `video_stat_observations` — 668,665 rows, row = one view measurement (video id, measurement date, views). Chain `channels → videos → video_stat_observations`. Caption: for the lesson, an anonymised sample of 1,943 channels and 46,132 videos.

> "My working database: cooking YouTube channels collected via the official API. Three tables. Channels — twenty-six and a half thousand. Videos — over 400 thousand. Daily view measurements — 668 thousand.
>
> The tables are linked. Each video holds its channel id. Each measurement holds its video id.
>
> Why not a file? There are three tables; they're linked and updated every day. Exporting them for every question is impractical. It's simpler to ask the database with a query."

**What to do:** if you want time in hand for P6, send it here already (text on slide 27). Slides 24–26 run on ready frames, so the chat is free.

---

### Slide 25 (76:00 — 79:00) • SQL reads almost like a plain sentence
**On screen:** the prompt: "The database has a videos table: length and views of every video. Write an SQL query: which video length gets the most views? Explain every line." Below, the query line by line: `SELECT duration_bucket,` — what to show; `COUNT(*) AS videos,` — how many videos in the group; `MEDIAN(views) AS typical` — typical views; `FROM videos` — from which table; `GROUP BY duration_bucket;` — what to group by. Note: "Describe the tables in the prompt. Without it the model guesses column names and the query fails."

> "Same move as with Excel. You describe the table and ask in words. The model writes an SQL query. The database counts by itself, in a second.
>
> Read the query as a sentence. Select the length. Count the videos. Take typical views. From the videos table. Group by length.
>
> MEDIAN is the typical value: half the videos above, half below. Rare viral hits spoil the average here.
>
> You don't need to write SQL. You need to read what the database computed.
>
> And the line at the bottom. Describe the tables to the model: their names and columns. You don't need to give it the data. Without the description the model invents column names, and the query fails."

**If asked why there's no frame of the model's answer:** in our run ChatGPT pulled the real schema of the author's database from connected sources. We don't show that frame. If you repeat it, use a temporary chat with no connected sources (see the runbook).

**If time is short:** don't read the query line by line. Say one sentence about MEDIAN and one about describing tables.

---

### Slide 26 (79:00 — 81:00) • Long videos 12× more popular? No: big channels make them
**On screen:** left, bars: typical views by length; 20–40 minutes — 13,000, short videos — 1,100. Note: "20–40 minutes gets 12× more than short videos? Compared with ordinary videos of the same channel, they are only 3% above usual." Right, the second query: a video vs its own channel's usual video. Every bar is about 1.0.

> "The first answer is tempting. 20–40-minute videos get 13 thousand views; short ones get 1,100. Twelve times more. You want to say: make long videos.
>
> But big channels, which already have many viewers, make long videos more often. The second query compares each video with ordinary videos of its own channel. And the gap nearly disappears: every length is about one. For 20–40 minutes it's 1.03, plus three percent.
>
> This data doesn't support 'make long videos'. Same story as with Social: the table shows what went together. It doesn't show what caused what."

**If asked about the sample:** the author picked the channels himself, by his own topics. It isn't all of cooking YouTube. The sample is anonymised: descriptions, links, phone numbers and ids removed. We don't hand the files to students, only show the charts. Details: `demo_v2/channels/results/answers.md`.

---

### Slide 27 (81:00 — 83:00) • Look for an Export button first, then an API. Scraping is the last option
**On screen:** three cards. Export: an "Export to Excel / CSV" button exists almost everywhere — CRM, accounting, ad accounts, YouTube Studio, Google Analytics. Official API: a simplified JSON answer, "this is how the slide 24 channel database was collected". Scraping: check that the site's terms allow it, there's no personal data, and you don't overload the site. Note: a question for AI about an official export or API.

**What to do — in the first seconds of the slide (if you haven't sent it earlier):** switch to ChatGPT and send P6. In our run the answer took 3 min 34 s; it will arrive during slide 28.
```
Build a one-page report for a manager in Word: the question, 3 charts (revenue by month, ad return, N2 complaints), 3 findings and one point on “what this data does not prove”. And give me a short Python script that builds the same 3 charts from next month’s file.
```

> "I've sent the prompt for the final report. It takes a few minutes. Meanwhile, where do you get data for your own table? It almost always already sits somewhere.
>
> First look for an export button. CRM, accounting software, ad accounts and YouTube Studio all have one. It's the fastest and safest route.
>
> Second, an official API, a way into the service for programs. The answer comes in a form like the middle of the slide. You don't write the code yourself: AI writes a script that turns the answer into a table. That's how the channel database we just saw was collected.
>
> Third, scraping: a program reads a site's pages. It comes last, and only after three checks.
>
> Don't know where the export is? Ask AI: 'What official export or API does system such-and-such have to download a year of sales?'"

---

### Part 5: the answer to Anna and homework (83:00 — 90:00)

---

### Slide 28 (83:00 — 86:00) • Send the manager the report file. The chat preview can lie
**On screen:** left, "✗ preview in the chat" — a placeholder picture with "Series A", invented numbers. Centre, "✓ the downloaded .docx": the question, three charts, three findings, "what the data does not prove". Right, prompt 6 and the "recipe for next month" frame.

**What to do:** go back to the chat. Show the preview, download the .docx, open it, check two numbers: $2,520,078 for the year and $373,435 for December.

> "Back to the chat. The result of an analysis is a file you can forward.
>
> Look at what ChatGPT showed in the chat as the report preview in our run. A stock picture: 'Series A–E', someone else's millions. None of our analysis is there.
>
> I download the same file and open it. Everything is there: the question, three charts, three findings. Revenue for the year 2,520,078 dollars, December 373,435. Matches the reference. The rule: don't judge the preview. Check the opened file and send only that.
>
> On the right is the recipe: a script that builds the same charts from next month's file. In January you drop in the new file and run the script. In Colab or right in the chat: 'Run this script on the new file.'
>
> One caveat. The script expects a workbook with sales and reviews sheets. Our January file is a practice file: sales only, one month. The reviews chart won't build, and the monthly chart will have one point. That's fine."

**If the report isn't ready:** show the frames on the slide in order: preview, downloaded file, script. If the preview in your run is right straight away, say: "Good. Ours looked like this" — and show the left frame.

---

### Slide 29 (86:00 — 87:00) • What you may upload to a chat
**On screen:** a traffic light. Green — practice, public, anonymised data, like Northstar: any service. Amber — internal company data: only in the work account (ChatGPT Business/Enterprise, Claude Team/Enterprise, Google Workspace). Red — customers, staff, finance, health: only in an approved environment with the data owner's consent. Right: delete unneeded columns before uploading; in personal accounts, training depends on settings.

> "A traffic light. Green — practice and public data, like our file. Any service is fine. Amber — internal company data, only in the work account. Red — personal data of customers and staff, finance, health. Only in an environment the company approved.
>
> In personal accounts, check the settings; their names are on the slide. And before uploading, delete the columns the question doesn't need: names, phone numbers, e-mails."

---

### Slide 30 (87:00 — 89:00) • A pack you can send to a manager
**On screen:** file `northstar_2025.xlsx`; the task — answer Anna: how did sales go this year, and what should we check next? Folder `analysis_pack/`: `analysis.xlsx` (AI formula + pivot + chart), `charts/` (3 charts, one as before / after), `report.docx` (1 page), `recipe.md` (prompt + script for January), `checks.md` (60 seconds + "does not prove"). Notes: no paid AI in Excel needed; required — one statement the data doesn't support.

> "The homework is a five-part pack. Another person should open it and understand it in five minutes.
>
> An Excel workbook with a formula the AI wrote, a pivot and a chart. Three charts, one of them in two versions: before and after. A one-page report. A recipe: the prompt and a script for the January file. And a checks file.
>
> One required item: a statement that sounds plausible but the data doesn't support. For example: 'If we cut the Social budget, revenue won't drop.' And how to test it.
>
> No paid licence needed; the chat route works for everyone. Templates are in student_starter; the full text and rubric are in the homework file. Maximum 12 points, pass from 8."

---

### Slide 31 (89:00 — 90:00) • What to take away
**On screen:** five moves. 1 — the describe prompt first. 2 — formulas in words. 3 — one chart per question. 4 — the report as a file with a recipe. 5 — 60 seconds of checks. Note: next lesson L09 — the Claude ecosystem and artifacts.

> "Five moves for Monday. Start with the describe prompt. Ask for formulas in words. One chart per question. The report as a file with a recipe. And 60 seconds of checks.
>
> Next time — Claude and artifacts. The same analysis becomes an interactive page that colleagues open by link.
>
> Please post questions in the course chat."

**What to do:** there's no buffer. Questions go to the course chat or after the session.
