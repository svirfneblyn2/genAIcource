# Instructor Script • Lesson 08: AI for Data Analysis (90 minutes)

**Course:** GenAI Basics • Lesson 08 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners — people in different roles, not data analysts. We explain in plain words; code is one short example for reference.
**Format:** 18 slides (`presentation_L08_AI_for_Data_Analysis_EN.html` / PDF) • session in **Microsoft Teams** • break timer on slide 9
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Materials:** `demo_assets/northstar_sales_messy.csv` (73 rows, 4 planted problems), `northstar_sales_truth.csv` (ground truth), `reference_analysis.py` (fallback), `no_code_experiment_2026-10-13.md` (the experiment for slide 2), live demo runbook `L08_04_Live_Demo_Runbook_READY_EN.md`, homework `L08_05_Homework_EN.md`, cheatsheet `L08_00_Lecture_Cheatsheet_EN.md`.
**Facts as of October 2026:** `L08_08_Source_Notes_Research_2026-10.md`.

**Lesson goal:** the student understands that in a "chat with data" the model writes code and the sandbox does the calculating; knows to start with a data profile, tells a mechanical fix from a meaning fix, asks the AI for evidence (code, reconciliation, a log), checks the numbers another way, and does not draw "what will happen if…" conclusions from descriptive data.

> **Before you start (Teams):** share the browser window with the deck (not the whole screen). For the demo, have a second browser window with a chat assistant in your work account, zoom 125–150%. The file `northstar_sales_messy.csv` is on the desktop. Run `python reference_analysis.py` once.

---

## Session map (18 slides • 90 minutes, including a 5-minute break)

| Slide | Block | Time | Min | On screen | Key idea |
|---|---|---|---|---|---|
| **01** | Cover | 00:00 — 02:00 | 2 | A table turns into a chart | The model writes code, the sandbox calculates, you check. |
| **02** | Hook: experiment | 02:00 — 07:00 | 5 | Haiku's answer without code + 4 takeaways | It got the sum right, but "fixed" 66 → 6 (it was 4) and "checked" without code. |
| **03** | How it works | 07:00 — 13:00 | 6 | Diagram: you → model ⇄ sandbox → files | The model is not a calculator. Open the code. |
| **04** | Where to find it | 13:00 — 19:00 | 6 | 4 places on a "easier ↔ more control" axis | Chat, spreadsheet, notebook, API — same mechanics. |
| **05** | Data passport | 19:00 — 24:00 | 5 | First rows with colored column notes | A row is not an order and not a customer. |
| **06** | Profile | 24:00 — 29:00 | 5 | 73 / 72 / 4 + 5 rows with problems highlighted | First "describe", then "calculate". |
| **07** | Cleaning | 29:00 — 35:00 | 6 | Two lanes: mechanics / meaning + log | Found it ≠ allowed to fix it. |
| **08** | Analyst prompt | 35:00 — 41:00 | 6 | A prompt in 6 colored parts | We set which evidence we want to see. |
| **09** | **Break** | **41:00 — 46:00** | **5** | **Timer** | **Rest. Get the chat window ready.** |
| **10** | Live demo | 46:00 — 56:00 | 10 | 4 steps with prompts + audience task | Profile → fixes → calculation → trap. |
| **11** | Result | 56:00 — 61:00 | 5 | Line by month + channel slope | One chart — one claim; "top channel" is two questions. |
| **12** | Chart types | 61:00 — 65:00 | 4 | 5 mini charts with questions | The question picks the chart type. |
| **13** | Checking | 65:00 — 71:00 | 6 | Three paths to $256,045 + a 5-item checklist | Checking = the same number another way. |
| **14** | Limit of a claim | 71:00 — 77:00 | 6 | ROAS Search/Social + hidden-factors diagram | "What happened" ≠ "what will happen if…"; you need a test. |
| **15** | Code for reference | 77:00 — 80:00 | 3 | ~12 lines of pandas | Recognize decisions in code, don't write it. |
| **16** | Privacy | 80:00 — 84:00 | 4 | Data traffic light | Practice data — OK; internal — work account; personal — not without approval. |
| **17** | Practice and homework | 84:00 — 88:00 | 4 | Tree of 5 files | An evidence pack instead of an answer from the chat. |
| **18** | Summary + L09 teaser | 88:00 — 90:00 | 2 | 5 rules | Next: Claude and artifacts. |

---

## Detailed script

### Part 1: how AI analysis works and how to prepare for it (00:00 — 41:00)

---

### Slide 01 (00:00 — 02:00) • Cover
**On screen:** illustration: a table grid turns into a growing chart, a magnifying glass over one cell. Title "AI for Data Analysis", subtitle "Chat with a spreadsheet: the model writes code, a sandbox calculates, you check".

> "Hi everyone! Today is data analysis with AI. Almost all of us have a spreadsheet we'd like to ask about: what changed, where it grew, where it dropped. Now you can do that right in a chat: upload the file, ask in plain language.
>
> The whole lesson uses one file: sales of the Northstar online shop for January through June. It's a fictional project, the same one from L07. The file has 73 rows and a few errors that we hid on purpose.
>
> The main idea is right in the subtitle: the model writes code, the sandbox calculates, you check. By the end of the lesson it'll be clear why it works that way."

---

### Slide 02 (02:00 — 07:00) • Hook: the model did the maths without code — and got it right
**On screen:** left — the question and the answer from Claude Haiku 5.5 with no tools, highlighted: green for the correct total 256,045, red for "probably a typo, should be 6" and "I checked the work". Right — four takeaways: ✓ the total is right (Sonnet 5.5 gave the same total); ✗ "probably 6" — the source said 4; ✗ "I checked" — with what?; ! 100,000 rows will not fit in a message.

> "Let's start with an experiment. While preparing the lesson, we pasted our whole file — 73 rows — straight into a message and didn't allow the model to use any tools. We asked: what's the total revenue, and are there any problems in the data?
>
> And here's the surprise: the model got it right — 256,045 dollars. A second model, Sonnet, gave the same total, and honestly added a caveat: "computed by hand, please double-check". So the old argument "models can't do maths" no longer holds for small tables.
>
> So why do we need this lesson? Look at the red. In one row there are 66 returns and 62 orders — that's impossible. The model decided on its own: "probably a typo, should be 6". We checked the source system — it was 4. A guess sounded like a fact.
>
> Next: "I checked the work, the totals match." Checked with what? There was no code. You can't repeat the steps of the calculation.
>
> And last: 73 rows fit in a message. A real export with 100 thousand rows doesn't. There you can't do without a file and code."

**Question for the chat:** "What would you do with a row that has more returns than orders?" Collect 2–3 answers.
*If you repeat the experiment live, the answer may differ. Show whatever you get.*

---

### Slide 03 (07:00 — 13:00) • The model is not the calculator. The sandbox is
**On screen:** a diagram. "You" (question + file) → "Language model" (understands the question, writes code, explains) → down: "code" → "Python sandbox" (reads the file, calculates, draws) → up: "result or error", a loop "fixes and reruns" → "Result files". From the model to you — "answer + code". Three captions at the bottom: the model decides what to calculate; the sandbox calculates; you check.

> "Here's how a chat with data works in ChatGPT, Claude and Gemini. You upload a file and ask a question. The model doesn't do the maths in its head — it writes a small Python program.
>
> The program runs in a sandbox. A sandbox is an isolated computer at the provider where your file has been placed. The code runs there, and the result goes back to the model. If the code fails with an error, the model fixes it and runs it again. Sometimes you'll see this happen two or three times in a row.
>
> At the end you get an answer, the code and files: a table, a chart, cleaned data.
>
> Why this matters: the numbers are calculated by a program. That means they can be rechecked, repeated and shared with a colleague. In ChatGPT the code opens with a button next to the answer, in Claude it's in the analysis block, in Gemini it's "show code". Habit number one for today: always open the code, even just to glance at it."

---

### Slide 04 (13:00 — 19:00) • Four places where AI analyses data
**On screen:** four columns with icons on an axis "easier to start → more control and repeatability". Chat with a file: ChatGPT (data analysis in Python, sheets up to ~50 MB), Claude (code execution and files, all plans, up to 30 MB), Gemini (files up to 100 MB). Inside the spreadsheet: Copilot in Excel ("Edit with Copilot", runs Python), ChatGPT and Claude for Excel (Claude — paid plans), Gemini in Google Sheets (side panel: analysis and charts; =AI() is text only). Notebook: Colab + Gemini, Jupyter. API: OpenAI Code Interpreter (code in an isolated container), Gemini API (up to 30 s per run), Claude API. Footer: the mechanics are the same everywhere; button names and limits change, so check the docs on the day of class.

> "Where can you find this? Left to right, from "easier to start" to "more control".
>
> Chat with a file is the fastest start: drag in a CSV or Excel file and ask. ChatGPT has it, Claude has it — even on the free plan — and so does Gemini.
>
> Inside the spreadsheet is for when your data already lives in Excel or Google Sheets. Copilot in Excel is now called "Edit with Copilot" and can run Python. ChatGPT and Claude both have add-ins for Excel. In Google Sheets the analysis is done by the Gemini side panel, with charts. The =AI function works with text only and handles at most 350 cells at a time, so it's not an analysis of the whole table.
>
> Notebook means Colab or Jupyter. The code stays with you, and you can rerun it a month from now on new data.
>
> API is for when the analysis has to repeat automatically, say every week. That's already developer territory.
>
> The mechanics are the same everywhere: the model writes code, it runs, you check. In today's demo we use a chat with a file."

*If asked: the =COPILOT() function in Excel was retired on 14 Sep 2026 — old formulas show #NAME?. ChatGPT for Excel/Google Sheets has been on all plans since 5 May 2026. Claude for Google Workspace has been in beta since 6 Oct 2026.*

---

### Slide 05 (19:00 — 24:00) • First the data passport, then the questions
**On screen:** the first 5 rows of the file. Above the columns — four colored notes: key (order_id must be unique), time (one date format, January–June), dimensions (channel, category, region), numbers and units ($ and counts; returns ≤ orders). A banner at the bottom: one row is the sales of one channel in one category on one date; not an order and not a customer.

> "Before asking "what are the insights?", we find out what's actually in the file. I call this the data passport. Five questions: what is one row, which field must be unique, what period does the data cover, what units are the numbers in, and which values are impossible.
>
> Let's go through the colors. Amber is the key, order_id, which must be unique. Blue is the date. Violet is the dimensions: we group by them. Green is numbers: revenue and ad spend in dollars, orders and returns as counts. A common-sense rule: returns can't be higher than orders.
>
> And here's a trap: despite the name order_id, one row is not one order. Look at the orders column: 36, 41, 46 orders. One row is the sales of a channel in a category on a date. If you mix this up, every "average per customer" will be wrong. Ask the model first to say what one row is — that catches half the mistakes."

---

### Slide 06 (24:00 — 29:00) • Profile the data before any conclusions
**On screen:** big numbers: 73 rows in the file; 72 unique order_ids; 4 problems hidden among 73 rows. The profile prompt. A table of five rows with red highlights: 1010 — empty region; 1028 ×2 — duplicate; 1041 — date with slashes; 1055 — 66 returns on 62 orders.

> "The first prompt for any file is a profile. Not "find insights" but "describe what's here". And a separate phrase: "Do not fix anything yet." Otherwise the model starts cleaning silently, and you won't know what it changed.
>
> Our file has four problems. A row with no region. A row recorded twice. A date in a different format. And a row with impossible returns.
>
> See what one duplicate costs: the extra row adds 3,312 dollars to revenue. The total "as in the file" is 259,357; the correct one is 256,045. The difference looks small, but this is exactly the kind of error that comes up later in a meeting."

---

### Slide 07 (29:00 — 35:00) • Finding a problem ≠ permission to fix it
**On screen:** two lanes. Green "Mechanics — OK to fix": 1028 ×2 → keep one row; region (empty) → UNKNOWN, don't drop the row; 2026/04/22 → 2026-04-22 (format fixed, but the source has a different day — 2026-04-13 → log it). Red "Meaning — do not fix": returns 66 on 62 orders → keep + flag, ask the data owner; models guessed "6", "6 or 2"; the source had 4. At the bottom — a banner about the cleaning log.

> "The key fork of the lesson. On the left are mechanical fixes. Remove an exact duplicate. Label an empty region as UNKNOWN — label it, don't throw the row out: it has revenue in it. Bring the date to one format. The meaning of the data doesn't change.
>
> But even a "safe" fix is an assumption. We replaced the slashes with dashes and got 22 April. And in the source system the date was 13 April. It doesn't affect revenue by month, but that's exactly why we need a log: what changed, in which rows, why, and how it moved the total.
>
> On the right is a meaning error: 66 returns on 62 orders. The models in our experiment suggested 6 or 2. Only the source knew the right answer — it was 4. The rule: don't edit or delete such a row. Flag it and ask the data owner.
>
> The model can sort fixes into these two groups — if you ask it to."

---

### Slide 08 (35:00 — 41:00) • The analyst's prompt
**On screen:** a prompt in six colored parts: 1 question; 2 profile first; 3 cleaning rules; 4 calculation with code; 5 reconciliation; 6 what to return (a table, one chart, the log, one thing the data does not prove).

> "Compare this with the prompt "find interesting insights". Here there are six parts.
>
> The question is specific and has a period. Then the profile. Then the cleaning rules: what the model can do on its own and where it must stop and ask. The calculation comes with code, so it can be opened. Reconciliation: the model totals things two ways itself. And what to return, including an honest "what this data does not prove".
>
> Notice that we don't tell the model how to write the code. We tell it what evidence we want to see. The prompt is in the cheatsheet — after the break I'll use it."

---

### Slide 09 (41:00 — 46:00) • Break
**On screen:** a 05:00 timer, a "Start" button.

> "Five-minute break. After it — the live demo."

*During the break: open the chat window, start a new chat, check that the file uploads.*

---

### Part 2: demo, checking and the limits of a claim (46:00 — 90:00)

---

### Slide 10 (46:00 — 56:00) • Live demo: from a messy CSV to a checked answer
**On screen:** four steps with short prompts and a "Look for" hint: profile; fixes; calculation and chart; the trap "Which channel should get more budget in July?". At the bottom — the audience task. The fallback is in the speaker notes only.

> "I'm switching to the chat. A task for you while I work: write in the Teams chat one fix the model made, one problem it left alone, and one check of the totals."

Follow the runbook `L08_04_Live_Demo_Runbook_READY_EN.md`. After every answer, open the code. Key moments:
* **Step 2.** If the model "fixes" 1055 — don't hide it. Ask: "How do you know the right value?" and show the ground-truth file.
* **Step 3.** Find row 1063 (Search, June, $5,425) out loud — that's the manual check.
* **Step 4.** If the model confidently recommends Search — ask: "What assumption are you making?" We'll unpack it on slide 14.
* If the service thinks for more than 90 seconds — fallback: `python reference_analysis.py`.

---

### Slide 11 (56:00 — 61:00) • One chart — one claim
**On screen:** left — revenue by month (32.7 → 53.9 $k), claim "+64.7%". Right — channel revenue in January and June: Search highlighted (6.7 → 13.4, +99%), claim "Search grew fastest — but from the lowest base; Organic brought the most — $67,580".

> "Here's what we got — these are real numbers from the file after cleaning. On the left is the trend by month: a line, because order in time matters. Revenue grew by 64.7 percent.
>
> On the right is the start and end of the half-year for each channel. And here's the interesting part: which channel is the "main" one? That's two different questions. Organic brought the most over six months. But Search grew fastest — almost doubled, but it started from the lowest base: in June it's still below Email. The model answers the question you asked, so we phrase it precisely.
>
> Each chart carries one claim, and the claim can be checked on the chart itself."

Read out 2–3 audience answers from the chat.

---

### Slide 12 (61:00 — 65:00) • The question picks the chart type
**On screen:** five mini charts: line — "how did it change over time?"; bars — "who is bigger?"; histogram — "how are values spread?"; scatter — "are two numbers related?"; 100% bars — "what makes up the whole?". At the bottom — how to ask.

> "Five questions, five chart types. A trend is a line. A comparison is bars: sorted and with the axis starting at zero, otherwise a small difference looks huge. A distribution is a histogram, and it shows outliers. A relationship between two numbers is a scatter plot, and remember: related doesn't mean cause. Shares are 100% bars, no more than 4–5 parts.
>
> AI will happily build a dashboard of six charts. Ask for one chart per question — it's easier to check."

---

### Slide 13 (65:00 — 71:00) • We check the numbers, not the wording of the answer
**On screen:** three paths — sum by month, by channel, by row — meet at $256,045. Checklist: rows 73 → 72; totals three ways; manual spot check — row 1063; base of a %; chart = table. A banner: rereading the answer is not a check.

> "Checking is part of the analysis, not politeness. Five checks, and each catches its own type of error.
>
> Row counts before and after catch duplicates and lost rows. A total calculated three ways catches grouping errors. A spot check is one row that you find by eye in the source file. The base of a percentage: "64 percent growth" — from which number, and over which period? And the chart has to match the table.
>
> It's handy to ask the model to run these checks in code itself. But do one of them — the manual one — yourself.
>
> And this isn't paranoia. On the 2025 DABstep benchmark, the best AI agent solved only 14.5 percent of hard multi-step data-analysis tasks. On simple tasks the models are good; on hard ones they are often wrong, and confidently so."

---

### Slide 14 (71:00 — 77:00) • "What happened" ≠ "what will happen if…"
**On screen:** revenue per $1 of ads: Search 5.52, Social 3.84; Email and Organic — no ads. A diagram: season, who saw the ads, brand awareness and attribution rules affect both budget and revenue; between budget and revenue — a red dashed arrow "cause? not proven". A banner: the honest answer is a test.

> "The trap question from the demo: move budget from Social to Search? Let's look at return on ad spend, ROAS: revenue per dollar of advertising. Search has 5.52, Social has 3.84. The temptation is obvious. By the way, models often advise exactly that.
>
> But this describes the past. On the right is why we can't draw a conclusion about cause. Season, who was shown the ads, brand awareness and attribution rules — meaning the rules for crediting a sale to a channel — all affect budget and revenue at the same time. Maybe Search simply catches people who were going to buy anyway.
>
> The honest answer: the data describes what happened. To learn what will happen, you need a test — for example, move part of the budget in one region for 2–4 weeks and compare with the rest.
>
> A good AI answers like that. If it doesn't, ask it: "What assumption are you making?""

---

### Slide 15 (77:00 — 80:00) • What the model writes "under the hood"
**On screen:** subtitle "pandas is a Python library for working with tables"; ~13 lines of pandas: read the file, check rows and keys, find impossible returns, drop duplicates, fill the region, fix the date, group by month and channel, reconcile.

> "A reference slide; we won't go line by line. pandas is a Python library for working with tables, and almost every AI analyser uses it. This is roughly what you'll see when you open the code. You can see it reads almost like text: read the file, count the rows, find impossible returns, drop duplicates, fill the gap, fix the date, group, reconcile.
>
> The skill you need is not writing this code but recognizing the decisions in it: "aha, here the model dropped rows — how many, and why?""

---

### Slide 16 (80:00 — 84:00) • What you may upload to a chat
**On screen:** a traffic light. Green — practice, public, anonymised data. Amber — internal company data: only the work account (ChatGPT Business/Enterprise, Claude Team/Enterprise, Google Workspace), where data is not used for training by default. Red — customers, staff, finance, health: only in an approved environment and with the data owner's consent. On the right — in personal accounts, training depends on settings; remove unneeded columns before uploading.

> "A traffic light. Green is practice and public data, like our file: any service is fine. Amber is internal company data: only in the work account, where by default the data isn't used for training. Red is personal data of customers and staff, finance, health: only in an environment approved by the company.
>
> In personal accounts it all depends on the settings. In ChatGPT it's "Improve the model for everyone", in Gemini it's "Keep Activity", and Claude uses chats for training only if you allowed it yourself.
>
> A simple rule: before uploading, delete the columns you don't need for the question. For a sales-by-channel analysis you need neither names nor phone numbers."

---

### Slide 17 (84:00 — 88:00) • Practice and homework
**On screen:** the `verified_analysis_pack/` tree of five files (the last one — "3+ checks + 1 "the data does not prove this""), pair work.

> "The homework is not "an answer from the chat" but a pack of five files that another person can check in five minutes. A cleaning log, a short brief with claims, one chart, cleaned data or a script, and a checks file.
>
> Work in pairs: one drives the chat, the other checks, and you swap halfway.
>
> The most important item is the refusal. Write one statement that suggests itself but isn't supported by the data. For example: "If we double the Search budget, revenue will grow." And write what you'd need to test it. Templates are in the student_starter folder, the full text is in L08_05_Homework."

---

### Slide 18 (88:00 — 90:00) • Five rules for analysis with AI
**On screen:** 1 profile first; 2 fix mechanics, not meaning; 3 code does the numbers; 4 a check = the same number another way; 5 "what happened" ≠ "what will happen if…". L09 teaser.

> "The five rules are the lesson. AI makes analysis conversational, but it doesn't remove discipline: a question, a profile, code, checking and an honest limit to the claim.
>
> Next time: the Claude ecosystem and artifacts — how to turn an analysis like this into an interactive page that you can open by link. Questions?"
