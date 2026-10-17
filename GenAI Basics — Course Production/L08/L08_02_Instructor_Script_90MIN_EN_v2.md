# Instructor Script • Lesson 08: AI for Data Analysis (90 minutes, v2)

**Course:** GenAI Basics • Lesson 08 of 16 • Module 3: AI assistants at work
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners — people in different roles, not data analysts. Keep it plain. We show code and SQL for reference; we don't teach how to write them.
**Format:** 19 slides (`presentation_L08_AI_for_Data_Analysis_EN_v2.html` / PDF, generator `deck/build_v2.py`) • session in **Microsoft Teams** • break timer on slide 8
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Materials:** `demo_v2/northstar_2025_EN.xlsx` (sheets `Sales`, 1,261 rows, and `Reviews`, 357 reviews; the Russian group uses `northstar_2025.xlsx`), `demo_v2/northstar_sales_2026-01.csv` (next month's file), reference numbers `demo_v2/answers.md`, the channel database `demo_v2/channels/` (answers in `results/answers.md`), ready frames from the run in `assets/v2/chat/`, runbook `L08_04_Live_Demo_Runbook_READY_EN_v2.md`, homework `L08_05_Homework_EN_v2.md`, cheatsheet `L08_00_Lecture_Cheatsheet_EN_v2.md`.
**Time:** the slides take 83 minutes; the other 7 are buffer. The demos usually eat it.

**Lesson goal:** students take their own spreadsheet through the whole path: describe the file → ask for a formula and a chart in words → find the slice where a problem hides → build a one-page report as a file → check the numbers in 60 seconds. And they can say what the data does not show.

> **Before you start (Teams):** share the whole screen, or practise switching windows beforehand: the browser with the deck, ChatGPT, Excel. Browser zoom 125–150%. In ChatGPT open **one** new chat for the whole lesson: prompt 6 builds on the charts from prompts 2–5. On the desktop: `northstar_2025_EN.xlsx` and `northstar_sales_2026-01.csv`. Excel is running, the Downloads folder is empty. The `assets/v2/chat/` folder is open in an image viewer. The ready frames come from the Russian-language run; the English file gives the same numbers.

---

## Session map (19 slides • 83 minutes + 7 minutes of buffer)

| Slide | Block | Time | Min | On screen | In one line |
|---|---|---|---|---|---|
| **01** | Cover | 00:00 — 02:00 | 2 | Spreadsheet → answer → chart → one-page report | The whole lesson uses one file, Northstar 2025. |
| **02** | Anna's e-mail | 02:00 — 05:00 | 3 | The director's e-mail + a 1,261-row file | The manager's question comes first, then the file. |
| **03** | First prompt | 05:00 — 09:00 | 4 | The describe prompt + two frames of ChatGPT's answer | "Describe the file, suggest 5 questions, change nothing." |
| **04** | Four doors | 09:00 — 13:00 | 4 | Excel, Google Sheets, chat with a file, database | Pick the tool by where the data lives. |
| **05** | Demo 1: Excel | 13:00 — 25:00 | 12 | Prompt 2, ChatGPT frames: the chart and the workbook sheet | Ask for a formula and a chart in words; see the formula in the cell. |
| **06** | Seasonality | 25:00 — 28:00 | 3 | Revenue by month: +161.7% and +15.1% | A percentage depends on its base. |
| **07** | Five charts | 28:00 — 32:00 | 4 | Five mini charts from our file | Name the question; the model picks the chart type. |
| **08** | **Break** | **32:00 — 37:00** | **5** | **Timer** | **Same chat: check the file is still there.** |
| **09** | Demo 2: chat with a file | 37:00 — 49:00 | 12 | Prompts 3–5: heatmap, review themes, makeover | Breaking data down finds what the total hides. |
| **10** | What we found | 49:00 — 53:00 | 4 | Social: spend and revenue; warehouse N2: returns | The number shows where; the text explains why. |
| **11** | A slide-ready chart | 53:00 — 57:00 | 4 | Before / after one prompt | You edit a chart with words. |
| **12** | 60-second check | 57:00 — 60:00 | 3 | 49% / 46% / 44% vs 61% + three steps | After every redo, compare a couple of numbers. |
| **13** | Channel database | 60:00 — 65:00 | 5 | An SQL query + views by video length | The model writes a query; the database counts. |
| **14** | Where data comes from | 65:00 — 68:00 | 3 | Export → API → scraping | Look for the Export button first. **Send prompt 6.** |
| **15** | Report and recipe | 68:00 — 73:00 | 5 | Fake preview, the downloaded .docx, the script | The manager gets the opened file. |
| **16** | After the finding: test | 73:00 — 75:00 | 2 | Hidden-factors diagram | Only a test shows what a budget cut will do. |
| **17** | Privacy | 75:00 — 77:00 | 2 | Data traffic light | Practice data anywhere, work data in the work account, personal data only with approval. |
| **18** | Homework | 77:00 — 81:00 | 4 | The `analysis_pack/` folder, five parts | A pack you can send to a manager. |
| **19** | Summary + L09 | 81:00 — 83:00 | 2 | Five moves + teaser | Try them on Monday on your own spreadsheet. |
| — | Buffer | 83:00 — 90:00 | 7 | — | Questions, or catching up after the demos. |

---

## Detailed script

### Part 1: from the e-mail to the first charts (00:00 — 32:00)

---

### Slide 01 (00:00 — 02:00) • Cover
**On screen:** a full-slide illustration. Title "AI for Data Analysis", subtitle "Spreadsheet → answer → chart → one-page report". Below: formulas, pivots and charts on request in plain words — in Excel, Google Sheets or a chat with a file.

> "Hi everyone! Today we work with spreadsheets. We take an ordinary sales export, and in an hour and a half we turn it into formulas, a pivot, three charts and a one-page report for a manager. We do it with tools you already have.
>
> The whole lesson uses one file. It's the sales of a made-up online shop, Northstar, for 2025: 1,261 rows plus a separate sheet of customer reviews. Near the end I'll show one more example — a large database of YouTube channels. That one no longer fits in Excel."

**What to do:** show the slide and name the file. Details come on the next slide.

---

### Slide 02 (02:00 — 05:00) • The manager's question comes first, then the file
**On screen:** left, an e-mail. From: Anna, Commercial Director. Subject: 2025 sales. "Hi! How did sales go this year? Why did advertising pay off worse in the second half? And why so many returns in the autumn? I need one page by Friday." Under it: "Three questions — three charts." Right, a frame of `northstar_2025.xlsx`, 1,261 rows.

> "This is what analysis looks like at work. An e-mail arrives with questions, and an export comes with it.
>
> Let me read it. Anna asks three things. How the year went. Why advertising paid off worse in the second half. And why there were so many returns in the autumn. She wants one page by Friday.
>
> Each question will become one chart. If you tell a model 'find insights', it gives you ten general observations. They won't help Anna. We spend the whole lesson answering her.
>
> On the right is the real lesson file, opened in ChatGPT. One row is the sales of one channel for one category, region and warehouse on one day. So one row is not one order. The second sheet holds 357 customer reviews."

**Ask the Teams chat:** "Which question from the e-mail would you check first, and why?" Collect 2–3 answers and read them out.

---

### Slide 03 (05:00 — 09:00) • First prompt: describe the file and suggest 5 questions
**On screen:** the prompt in large type. Below and to the right, two frames of ChatGPT's answer. Two notes: "The model found the duplicate and the period and said: 'I did not change the file'. But it took zero ad spend for missing values — that is the first question for the data owner" and "We take question 1, channels including ad spend — it matches the e-mail. That is what the demo computes."

The prompt (P1 in the runbook):
```
Describe this file: what one row is, how many rows, what period, what data problems. Suggest 5 questions a manager would ask. Don’t change anything yet.
```

> "I start every file with this prompt. It does two things. The model describes what's in the table. And it suggests questions worth asking.
>
> Look at the last sentence: 'don't change anything yet'. Without it, the model may quietly drop duplicates or fill in empty cells. You get an answer and never find out what it changed in your data.
>
> On the left is the real answer. 1,261 rows, 1 January to 31 December 2025, one row repeated in full. The model says it didn't touch the file.
>
> But the model got something wrong. It says '632 ad_spend values are missing'. Let's see what's really there. They're zeros; there are no blank cells. Email and Organic don't buy ads, so zero is normal for them. The model can't know that. Whoever exported the data knows. So questions like this go to the data owner.
>
> It also missed something: one date is stored as text, 10/05/2025. Ask back: 'Are these missing or zeros? Any dates in another format?'
>
> On the right are five questions a manager might ask. The first is about channels including ad spend. It matches Anna's e-mail, and demo 1 computes it. The third, about returns, is for demo 2. The rest can wait."

**Ask the Teams chat (optional):** "Which of the five questions would your manager ask?"

**If time is short:** don't read all five questions. Name only the first and the third.

---

### Slide 04 (09:00 — 13:00) • Pick the tool by where the data lives
**On screen:** four door cards. Excel: AI writes formulas and pivots (Claude / Copilot in Excel, or a file from a chat). Google Sheets: Gemini in the side panel builds pivots and charts. Chat with a file: the model writes Python code (ChatGPT, Claude, Gemini). Database: the model writes an SQL query and the database does the counting. At the bottom, a chain: your question → the model writes a formula, code or SQL → a program counts → you open and check.

> "There are four places where AI helps with data. The choice is simple: where does the file live, and what do you need at the end?
>
> Excel — when the data is already in a workbook that colleagues will open. AI writes formulas, and you see them in the formula bar. Claude has an Excel panel on paid plans. Copilot needs a Microsoft 365 Copilot licence. There's also ChatGPT for Excel. No panel? There's a workaround, and I'll show it in the demo: upload the file to a chat and download a workbook with formulas back.
>
> Google Sheets — if your company runs Google Workspace with Gemini. Gemini in the side panel builds pivots, charts and formulas.
>
> Chat with a file — the fastest start. Upload a CSV or Excel file and ask. The model writes Python code, a program runs it, and you can open the code.
>
> Database — when there are millions of rows and they won't fit in a chat. I'll show an example on slide 13.
>
> Look at the bottom row. Inside, it's always the same. The model writes a formula, code or a query. A program does the counting. That's why you can open the working and check it."

**If someone asks whether they have Copilot in Excel:** look for the Copilot button on the right of the Home tab. Button names and plans change, so check on the day.

---

### Slide 05 (13:00 — 25:00) • Demo 1: you can ask for a formula and a chart in words
**On screen:** prompt 2. Real ChatGPT frames: the ad-return line chart and a sheet from the downloaded workbook. The sheet is called `Ad ROAS 2025` and its cells hold numbers. Notes: "Open the workbook and click an ad-return cell. The fx bar should show a formula. If it shows a number, write: 'replace the numbers with formulas'" and "Have Claude or Copilot in Excel? Type the same text in the side panel; nothing to download."

Runbook plan: P1 — 4 minutes • P2, downloading the workbook and opening it in Excel — 8 minutes. The Copilot / Claude for Excel side panel — 90 seconds, only if time allows. Gemini in Google Sheets — one spoken sentence; there is no frame.

> "I'm switching to ChatGPT. I upload the same file and send the first prompt you just saw."

**What to do — P1 (4 min).** Upload `northstar_2025_EN.xlsx` and send P1. While the model answers, talk over slide 3. Read out question 1 from the answer; in our run it was "Which sales channels are the most profitable once ad spend is taken into account?"

> "That's the question we'll calculate with the next prompt."

**What to do — P2 (8 min including the workbook in Excel).** Send:
```
Add a sheet “Ad return” to the workbook: by month, revenue, ad spend and revenue per $1 of ads for Search and Social. Use Excel formulas, not pasted numbers. Build a line chart and let me download the .xlsx.
```

> "While it works, look at the part about Excel formulas. Without it, the model often types finished values into the cells. You can't check a number like that in the workbook: there's no way to see where it came from.
>
> Now I'll download the workbook and open it in Excel."

Download the `.xlsx`, open it in Excel, go to the new sheet (in our run, `Ad ROAS 2025`) and click an ad-return cell.

> "Open the workbook and click an ad-return cell. The fx bar should show a formula. If it shows a number, write: 'replace the numbers with formulas'. In our run, by the way, there were numbers. That's on the slide: a sheet from the workbook ChatGPT returned.
>
> When fx shows a formula, say =B2/C2, Excel is doing the counting. The model only wrote the formula. Change the spend and the number recalculates."

If there's no formula, send "replace the numbers with formulas", download the workbook again and click the same cell. If that doesn't help, be specific: "The revenue-per-$1 column contains numbers. Rewrite it as a formula: revenue / spend." Revenue and spend should be formulas too (`SUMIFS` over the `Sales` sheet).

> "Now the chart. For Search, every ad dollar brings about 5.4 dollars of revenue, all year long. For Social, about 4 until June. In July the line halves, down to 2. That's the second question in Anna's e-mail. We'll come back to it after the break."

**What to look for (from `answers.md`):** Search 5.15–5.39 all year (January 5.39, December 5.35). Social 3.91–4.05 until June, 1.97–2.02 from July. The duplicate is gone: March Social revenue 50,378, spend 12,514. If the March numbers are higher, the model kept the duplicate.

**Optional, 90 seconds, if time allows.** If you have Claude for Excel or Copilot in Excel, open `northstar_2025_EN.xlsx` and type the same request in the side panel.

> "That's what it looks like with a licence. Without one, you do the same thing through a chat and a downloaded workbook."

**If something goes wrong:**
* **Takes longer than 90 seconds.** Show the ready frames (`gpt_p1_problems.jpg`, `gpt_p1_questions.jpg`, `gpt_p2_roas_table.jpg`, `gpt_p2_roas_chart_sheet.jpg`) and move on.
* **The model calls the zeros missing values** (in our run: "632 ad_spend values missing"). Ask: "Is a zero in ad_spend a missing value or a real zero? Check by channel."
* **It misses the text date.** It missed it in our run too. Prompt it: "Check whether every date in order_date has the same format." The answer is the row `10/05/2025`.
* **The sheet has a different name** (in our run, `Ad ROAS 2025`). Doesn't matter, move on.
* **The chart is in the chat but missing from the workbook.** Ask: "Put this chart into the workbook on the ad-return sheet."
* **Numbers differ from the reference by more than 0.05.** Ask whether the duplicate was removed and what the model did with the `10/05/2025` row.
* **Download fails or Excel won't open.** Show the frames. There's no frame of the `fx` bar. Open `northstar_2025_EN.xlsx`, type `=` on an empty sheet and click two cells. That takes 30 seconds.

---

### Slide 06 (25:00 — 28:00) • Growth this year: +161.7% or +15.1%? It depends on the base
**On screen:** a line of revenue by month for 2025: January $142k, December $373k. On the right, three numbers: +161.7% — December vs January; +15.1% — December vs November; 27.7% of annual revenue came in November and December. Note: "A percentage of which month, over what period?"

> "The file's first story is seasonality.
>
> Compare December with January and you get 161.7 percent growth. Compare it with November and you get 15.1 percent. Both numbers are right. They sound very different.
>
> A model will happily write '160 percent growth'. Your job is to ask: from what base? January, after the holidays, is the weakest month of the year. November and December are sales season; they bring in 27.7 percent of the year's revenue.
>
> You only see this on a monthly chart. The annual total won't show it."

**Ask the Teams chat:** "Which of the two numbers would you put in Anna's report?" A good answer is either one, as long as it says which month it's compared with.

---

### Slide 07 (28:00 — 32:00) • Five questions, five charts — all from our file
**On screen:** five mini charts. Line — "How did it change over time?" (peak in Nov–Dec). Sorted bars — "Which is bigger?" (Electronics leads revenue). Histogram — "How are values spread?" (red tail — rows with 14%+ returns). Scatter — "Are two numbers related?" (amber — Social from July: spend up, revenue not). 100% bars — "What makes up the whole?" (channel shares by quarter). At the bottom, how to ask.

> "Five everyday questions and a chart for each. All five are built from the Northstar file.
>
> How did it change over time — a line. You can see the peak at the end of the year.
>
> Which is bigger — bars sorted from largest, with the axis starting at zero. Otherwise a small difference looks huge. Electronics leads revenue.
>
> How are values spread — a histogram. Most rows have 2 to 8 percent returns. But there's a red tail on the right, 14 percent and up. That's warehouse N2; we'll get to it.
>
> Are two numbers related — a scatter. Each dot is one month of one channel. The amber dots are Social in the second half. They moved right: spend went up. They didn't move up: revenue stayed about the same.
>
> What makes up the whole — 100 percent bars. Keep it to 4 or 5 parts.
>
> How to ask: 'Build one chart that answers this question, label the axes and units.' Name the question, and the model will pick the chart type. AI loves making six-chart dashboards. Ask for one chart per question: it's easier to check and easier to present."

---

### Slide 08 (32:00 — 37:00) • Break
**On screen:** a 05:00 timer, "Start" and "Reset" buttons. Caption: next, a demo in a chat with a file, then a large database, a report and homework.

> "Five-minute break. Then back to the chat: returns, reviews and a slide-ready chart."

**What to do:** press "Start". During the break check that the chat from demo 1 is open and the file is uploaded there. Stay in that chat: prompt 6 needs the charts from demo 1. Open a new chat only if the old one breaks, and upload the file again.

---

### Part 2: slicing, the report and checking (37:00 — 83:00)

---

### Slide 09 (37:00 — 49:00) • Demo 2: breaking data down finds what the total hides
**On screen:** three prompts with frames: a return-rate heatmap, review themes, a chart makeover (→ slide 11). Note: "Teams chat task: which number on the heatmap would you check first?"

Runbook plan: P3 — 3 minutes • P4 — 4 minutes • P5 — 4 minutes • 1 minute spare.

> "Back to the chat. A task for you while I work: write in the Teams chat which number on the heatmap you would check first."

The demo answers question 3 from the P1 answer and the third question in Anna's e-mail: why so many returns in the autumn.

After every answer, open the code: in ChatGPT it's the "Analysis complete" block or the code button above the chart. Labels change, so look above the chart.

> "I open the code every time. A program the model wrote does the counting. You can open it and read it."

**P3 — the heatmap (3 min).**
```
Compute the return rate by region and category for September–December and show it as a heatmap.
```

> "The overall return rate is about 6 percent. But one cell lights up: North and Electronics, 24.8 percent. The other fifteen cells are between 4.5 and 5.4. The annual total hides this."

**P4 — review themes (4 min).**
```
For the warehouse with the highest return rate, sort the reviews into themes and compare it with the other warehouses. Show 5 example reviews.
```

> "The model picked warehouse N2 by itself. That's the cell that lit up: warehouse N2 = the North × Electronics cell. Look at how it explains the choice: N2 is first by return rate, while S1 is first only by the number of returns. A rate and a count are different questions.
>
> Now the themes. At N2, 'packaging and damage' is 49 percent of reviews. At the other warehouses it's 12. The text explains the number: parcels arrive damaged."

Read out the model's caveat: the theme also includes praise of packaging ("Neatly packed, everything intact"). You'll need it two slides from now.

**P5 — a slide-ready chart (4 min, live).** Show P5 live; on slide 11 you will show the same pair large.
```
Rework this chart for a slide: the title states the finding, bars sorted, value labels on the bars, no legend and no gridlines, one accent colour for N2, everything else grey. Explain in 3 points what you changed.
```

> "We'll go through this chart on slide 11. For now, just remember the numbers: 49 percent against 12."

**What to look for (from the runbook):** a 4 × 4 grid; North × Electronics 24.8%; the rate is computed from orders. N2 has 87 reviews in September–December, the other warehouses 116. In P5, a title with a number; in our run, "almost 9 times more: 46% vs 5%", answered in 36 seconds.

**If something goes wrong:**
* **Takes longer than 90 seconds.** Ready frames: `gpt_p3_heatmap.jpg`; `gpt_p3_themes_before.jpg` and `gpt_p3_examples_caveat.jpg`; `gpt_p4_themes_after.jpg` and `gpt_p4_what_changed.jpg`.
* **It used the whole year.** The cell will look paler. Ask: "September–December only."
* **It divides returns by revenue.** Ask: "Return rate means returns divided by orders."
* **One cell is off by 0.1** (in our run North × Sports came out 5.3% instead of 5.4%). That's rounding; move on.
* **It picked the wrong warehouse.** Ask: "Did you choose by return rate or by number of returns?"
* **The theme percentages differ.** The model splits themes its own way every time. What matters: at N2 the damage theme is several times higher.
* **Running out of time.** Send P5 and move to slide 10 without waiting for the answer. Look at the answer on slide 11, where the pair is also shown large.

---

### Slide 10 (49:00 — 53:00) • Two problems the annual total doesn't show
**On screen:** left, Social: bars of spend and revenue by month, second half highlighted. Note: second half vs first — spend +184%, revenue +43%, revenue per $1 of ads 4 → 2. Right, warehouse N2: return rate by month, a red N2 line against a grey line for the other warehouses. Note: from September N2 returns are about 26%, others about 5%. At the bottom: "The number shows where; the text explains why. Reviews are data too."

> "Two findings from the demo. I redrew them straight from the data.
>
> On the left, Social. From July, ad spend nearly tripled: 69 thousand dollars in the first half, 197 thousand in the second. Revenue grew 43 percent over the same period. Each ad dollar now brings half as much. And the annual total looks fine: revenue is growing. That's why Anna can't see where the money leaks.
>
> On the right, warehouse N2. It's the same North × Electronics cell from the heatmap. Until August its returns match everyone else, about 5 percent. From September, about a quarter of orders come back: the cell shows 24.8 percent for September–December, the line about 26 in some months. The reviews explain why: crushed boxes, broken screens.
>
> The numbers show where the problem is. The review text explains why. Reviews are data like any other; you can count them too."

**Ask the Teams chat:** "What would you suggest to Anna for each finding?" If someone writes "cut Social", say: "Let's hold that until slide 16."

---

### Slide 11 (53:00 — 57:00) • You edit a chart with words, like text
**On screen:** left, "Before: the default chart" and prompt 5. Right, "After: 36 seconds later". Three notes: title = finding ("Almost 9× more" instead of "Review themes"); one colour (N2 blue, the rest grey); values on the bars, no legend or grid.

> "This is prompt 5 from the demo.
>
> On the left is the chart the model builds by default. The title names a topic. There's a legend, two bright colours, small labels. Nothing for the eye to hold on to.
>
> On the right is the same chart after one prompt, 36 seconds later. The title states the finding: almost 9 times more. N2 is blue, the rest are grey, and your eye finds the point in a second. The values sit right on the bars.
>
> The prompt has five rules, and they work for any chart. The title is the finding. Sort the bars. Put labels on the bars. Nothing extra — no legend, no grid. One accent colour. Save this prompt; it's in the cheatsheet.
>
> Now look at the numbers. It was 49 percent. Now it's 46. That's the next slide."

**Ask the Teams chat:** "What changed on the chart besides the colours?" Wait until someone notices the numbers.

---

### Slide 12 (57:00 — 60:00) • Three versions of a chart, three different numbers
**On screen:** share of N2 reviews about damage, September–December: 49% — first chart; 46% — after restyling; 44% — in the Word report; 61% — by the labels the file was built from. A frame: the model explains what it changed. On the right, three check steps: rows before and after (1,261 → 1,260); one point: against the source and the previous version; percent of what (+161% and +15% are both right). Note: check review themes by reading.

> "We only asked for a new look. The model also re-sorted the themes. It moved praise of packaging, 'neatly packed', from 'damage' to 'product OK'. The share became 46 percent. In the final report, which we'll build later, it's 44.
>
> By the labels we used to build the practice file, 53 of the 87 N2 reviews are about damage. That's 61 percent. The model searches by keywords and misses complaints written in other words.
>
> The conclusion about the warehouse doesn't change: there are many times more damage complaints there than at the others. What changes is the number that goes to the manager.
>
> So after every redo we do the 60-second check. Three steps.
>
> One — rows. How many before, how many after. The file has 1,261 rows; after removing the duplicate, 1,260. Ask the model how many it dropped and why.
>
> Two — one point: against the source and the previous version. Take one number from the chart and find it in the source file. For example, filter December and select the revenue column: Excel shows the sum at the bottom, 373,435 dollars. The same point as on the chart. Then compare it with the previous answer: it was 49, now it's 46.
>
> Three — percent of what. Of which month, over what period. 46 percent is a share of 87 N2 reviews for September–December. Out of all 357 reviews you'd get a different number.
>
> Check review themes by reading: open ten reviews and count them yourself."

**What to do:** if you have a minute, show step 2 live in Excel: filter December, read the sum in the status bar.

**If someone asks "do models count correctly at all?":** while preparing the lesson, models with no code got the sum of a small table right. But they "fixed" a row with 66 returns on 62 orders to 6. The source said 4. Tell the model's guess apart from the data. Details: `demo_assets/no_code_experiment_2026-10-13.md`.

---

### Slide 13 (60:00 — 65:00) • The database updates daily: don't export a file, ask the database
**On screen:** three numbers for the full database: 26,544 channels, 416,809 videos, 668,665 daily view measurements. Caption: for the lesson, an anonymised sample — 1,943 channels, 46,132 videos, no e-mails, links or ids. The sample was frozen on 2026-10-17 from the author's working database; views were measured in August–October 2026. Left, the prompt and an SQL query with comments. Right, bars: typical views per video by length. Note: "20–40 minutes gets 12× more than short videos? Compared with ordinary videos of the same channel, the gap is almost zero (1.03)."

**What to do:** don't run it live; talk over the ready frames.

> "This is my working database: cooking YouTube channels collected through the official API. Twenty-six and a half thousand channels, over 400 thousand videos and 668 thousand view measurements. The data sits in three linked tables and updates every day. Exporting a file for every question is a pain, and it wouldn't fit in a chat anyway.
>
> The move is the same as with Excel. You describe the table and ask your question in words. The model writes a query in SQL. The database does the counting, in about a second.
>
> SQL reads almost like English. Select the length. Count the videos. Take typical views. From the videos table. Group by length.
>
> MEDIAN is the typical value: half the videos are above it, half below. Rare viral hits spoil the average, so we use the median.
>
> Now the answer. Videos of 20 to 40 minutes get 13 thousand views; short ones get 1,100. Twelve times more. You want to say: make long videos.
>
> But big channels, which already have lots of viewers, make long videos more often. A second query compares each video with ordinary videos from its own channel. And the gap nearly disappears: 1.03, so plus three percent.
>
> So this data does not prove 'make long videos'. Big channels simply make long videos more often. Social ads are the same story; we'll come back to it in two slides."

**If someone asks about the sample:** the author found and picked the channels himself, by his own interests — lots of German baking. It's not all of cooking YouTube. Views are a snapshot on the measurement dates, and 63% of videos have no publish date. Details: `demo_v2/channels/results/answers.md`. We don't hand out the files, only show the charts.

**If time is short:** skip the line-by-line SQL. Keep the video-length trap — 12 times versus 1.03.

---

### Slide 14 (65:00 — 68:00) • Look for an Export button first, then an API. Scraping is the last option
**On screen:** three cards. Export: an "Export to Excel / CSV" button exists almost everywhere — CRM, accounting, ad accounts, YouTube Studio, Google Analytics. Official API: a sample JSON answer, "this is how the slide 13 channel database was collected". Scraping: three checks — the site's terms allow it, no personal data, you don't overload the site. Note: a question for the AI about an official export or API.

**What to do — in the first seconds of the slide:** switch to ChatGPT and send P6. In our run the answer took 3 min 34 s. Talk over the slide while the model works.
```
Build a one-page report for a manager in Word: the question, 3 charts (revenue by month, ad return, N2 complaints), 3 findings and one point on “what this data does not prove”. And give me a short Python script that builds the same 3 charts from next month’s file.
```

> "I've sent the report prompt; it takes a few minutes. Meanwhile, let's talk about where to get data for your own spreadsheet.
>
> The data almost always sits somewhere already. First, look for an export button. CRMs, accounting software, ad accounts and YouTube Studio all have one. It's the fastest and safest route.
>
> Second, an official API. That's the way into a service for programs. The answer comes back like the middle of this slide; the example is simplified. You don't write the code yourself: AI writes a script that turns the answer into a table. The channel database we just saw was collected this way, through the YouTube Data API.
>
> Third, scraping: a program reads a site's pages the way a person would. That's the last resort. Three checks first. The site's terms allow it. There's no personal data. You're not putting load on someone else's server.
>
> For most work tasks, export is enough. If you don't know where it is, ask the AI: 'What official export or API does system X have to download a year of sales?'"

**Ask the Teams chat (optional):** "Which system would you export data from for your job?" It's also the bonus question in the homework.

---

### Slide 15 (68:00 — 73:00) • Send the manager the report file. The chat preview can lie
**On screen:** left, "✗ preview in the chat" — a placeholder picture with "Series A" and invented numbers. Centre, "✓ the downloaded .docx": the question, three charts, three findings, "what the data does not prove". Right, prompt 6 and a frame titled "recipe for next month".

> "Back to the chat. The result of an analysis is a file you can forward. A chat screenshot won't do. Prompt 6 asks for two things: a report page and a recipe script.
>
> Look at what ChatGPT showed in the chat as a report preview. A stock picture: 'Series A–E', January to June, millions of dollars. None of our analysis is there. Is this our report? No.
>
> Now I download the same file and open it. Everything's there. The title, 'How did sales go in 2025?'. Annual revenue 2,520,078 dollars, December 373,435. Three charts and three findings. And the point on what the data doesn't prove: the cause of the damage and the profit from advertising.
>
> I check two numbers against the reference: 2,520,078 and 373,435. They match. The rule is simple: don't judge the preview. Check the opened file, and send only that.
>
> On the right is the recipe: a script that builds the same charts from next month's file. In January you don't repeat the whole conversation. You drop in the new file and run the script — in Colab, or right in the chat: 'Run this script on the new file.'
>
> One caveat. The script from our run expects an .xlsx workbook with two sheets, sales and reviews. Our January file is a CSV with one month of sales only. So the reviews chart won't rebuild, and the monthly chart will have a single point. That's fine: a recipe has to be checked on the real next file."

**What to do:** show the preview, download and open the .docx, check the two numbers. If you have a minute, upload `northstar_sales_2026-01.csv` and ask: "Run the script on this file. If something is missing, tell me what." Expect this: the script wants a two-sheet .xlsx, so the model first fixes how it reads the CSV. The reviews chart won't rebuild: the January file has no reviews. The monthly revenue chart has one point — January. No minute? Say it in words.

**If something goes wrong:**
* **The report isn't ready.** Show the frames in order: the preview (`gpt_p5_fake_report_preview.jpg`), the report top with the script (`gpt_p5_report_top_script.jpg`), the report bottom (`gpt_p5_report_bottom.jpg`).
* **The preview is correct right away.** Good. Show the frame from our run: "This is what we got."
* **The report runs to two pages.** Ask: "Fit it on one A4 page."
* **No "what the data does not prove" point.** Ask for it.
* **The script expects a two-sheet .xlsx, and the file is CSV.** That's expected: let the model say what to change. The reviews chart still won't build, and the monthly chart has one point.

---

### Slide 16 (73:00 — 75:00) • The table says what happened. Only a test shows what a budget cut will do
**On screen:** the question "cut Social ads in half?". Left: the data shows — since July Social spends twice as much per dollar of revenue; the data doesn't show — how much revenue disappears if ads are cut. How to find out: cut the budget in one region for 2–4 weeks and compare with the others. Right, a diagram: sales season, who saw the ads, new ad creatives and which channel got credit for a sale affect both the Social budget and revenue; between them a red arrow, "cause? not proven".

> "After the Social finding, it's tempting to cut the budget in half right away. Models often advise exactly that.
>
> But the table describes the past. It shows that since July Social spends twice as much per dollar of revenue. It doesn't show how much revenue you'd lose if you cut the ads.
>
> Look at the diagram. The season, who saw the ads, new creatives and which channel got credit for a sale all affect budget and revenue at once. Maybe some buyers would have come without the ads. Maybe not. The table can't tell you.
>
> A test can. Cut the budget in one region for 2 to 4 weeks and compare it with the other regions.
>
> A good AI answer sounds like this: 'This data can't say how much revenue would be lost. I suggest a test.' If the model didn't say that, ask it: 'What assumption are you making?'"

---

### Slide 17 (75:00 — 77:00) • What you may upload to a chat
**On screen:** a traffic light. Green — practice, public, anonymised data, like Northstar: any service. Amber — internal company data: only in the work account (ChatGPT Business/Enterprise, Claude Team/Enterprise, Google Workspace), where data is not used for training. Red — customers, staff, finance, health: only in an approved environment with the data owner's consent. On the right: delete unneeded columns before uploading; in personal accounts training depends on settings.

> "A traffic light. Green is practice and public data, like our file. Any service is fine.
>
> Amber is internal company data. Work account only. On the business plans of ChatGPT, Claude and Google Workspace, your data isn't used for training by default.
>
> Red is personal data about customers and staff, finance, health. Only in an environment your company has approved, and with the data owner's consent.
>
> In personal accounts it depends on your settings. In ChatGPT it's 'Improve the model for everyone', in Gemini 'Keep Activity'. Claude trains on your chats only if you've allowed it.
>
> And one simple rule: before uploading, delete the columns your question doesn't need. A sales analysis needs no names, phone numbers or e-mails."

---

### Slide 18 (77:00 — 81:00) • A pack you can send to a manager
**On screen:** file `northstar_2025.xlsx`; the task — answer Anna: how did sales go this year, and what should we check next? A tree of the `analysis_pack/` folder: `analysis.xlsx` (AI formula + pivot + chart), `charts/` (3 charts, one as before / after), `report.docx` (1 page: question, 3 findings), `recipe.md` (prompt + script for January), `checks.md` (60 seconds + "does not prove"). Notes: no paid AI in Excel needed; required — one statement the data does not prove.

> "The homework is a five-part pack. Someone else should be able to open it and understand it in five minutes.
>
> An Excel workbook: a formula the AI wrote, a month-by-channel pivot and a chart. The formula must show in the fx bar.
>
> Three charts, one per question. Keep one of them in two versions: before the makeover and after.
>
> A one-page report. Every finding has a number, a period and a base.
>
> A recipe: the full prompt and a script that builds the charts from the January file. If the script didn't rebuild something, write what and why.
>
> And a checks file: the three 60-second steps. Plus one statement that sounds plausible but the data doesn't support. For example: 'If we cut the Social budget, revenue won't drop.' And write how you'd test it.
>
> You don't need a paid licence: the chat-and-download route works for everyone. You can use your own work data if it's anonymised and you're allowed to. Check the traffic light. Templates are in student_starter; the full text and the rubric are in the homework file. Maximum 12 points, pass from 8."

---

### Slide 19 (81:00 — 83:00) • What to take away
**On screen:** five moves. 1 — the describe prompt first: "describe the file, suggest 5 questions, change nothing". 2 — formulas in words: "Excel formulas, not pasted numbers". 3 — one chart per question: title = finding, one accent colour. 4 — the report as a file: open the downloaded file, attach the recipe. 5 — 60 seconds of checks: rows, one point, percent of what. Note: next lesson L09 — the Claude ecosystem and artifacts.

> "Five moves you can try on Monday on your own spreadsheet. Start with the describe prompt. Ask for formulas in words. Build one chart per question. Send the report as a file, with the recipe attached. And spend 60 seconds checking.
>
> Next time — Claude and artifacts. An analysis like this can become an interactive page with charts that your colleagues open from a link.
>
> Any questions?"

**What to do:** use whatever buffer is left for questions. If the demos ate the buffer, finish on slide 19 and ask people to post questions in the course chat.
