# Lesson 08 • Live demo runbook (v2): Northstar 2025 in ChatGPT and Excel

**Slides and time (from `deck/build_v2.py`, 31 slides):** P1 — send on slide 11 (26:00) • P2 — on slide 13 (33:00) • demo 1 — slide 15, 5 minutes (39:00–44:00) • break — slide 18 (51:00–56:00) • demo 2, P3 and P4 — slide 19, 5 minutes (56:00–61:00) • P5 — slide 21 (64:00–67:00) • the 60-second check — slide 22 (67:00–71:00) • P6 — send at the start of slide 27 (81:00), show on slide 28 (83:00–86:00).
**File:** `demo_v2/northstar_2025_EN.xlsx` (Russian group: `demo_v2/northstar_2025.xlsx`). Sheets `Sales` (1261 rows) and `Reviews` (357 rows). Fictional data.
**Next month’s file:** `demo_v2/northstar_sales_2026-01.csv` (100 rows, January 2026, sales only, no reviews).
**Service:** ChatGPT (it shows the code and lets you download files). Any chat with file upload works for demo 1.
**Reference numbers:** `demo_v2/answers.md`. Reference workbook with formulas: `demo_v2/excel_demo/northstar_2025_formulas_EN.xlsx` (RU: `northstar_2025_formulas.xlsx`).
**Ready frames:** `assets/v2/chat/` — live prompts P1–P6; `assets/v2/chat_badgood/` — the pairs on slides 9, 12, 16, 23. Slide crops are in `assets/v2/shots/` (`p*.jpg`, `b*.jpg`), cut by `deck/make_shots.py`. All runs were in Russian, so with the EN group describe the frames in English as you show them.

---

## Fallback rule

If a prompt thinks longer than 90 seconds, show the ready frame and move on. Let the answer finish in the background. The lesson has no buffer: 85 minutes of slides and a 5-minute break.
The exception is prompt 6 (the report). In our run it took 3 min 34 s. Send it no later than the start of slide 27 (81:00). You can send it earlier, on slide 24 (74:00): slides 24–26 run on ready frames, so the chat is free.

| Prompt | When to send | Where to show | Ready frame (`assets/v2/chat/`) |
|---|---|---|---|
| P1 describe the file | slide 11 | slide 12 (frames on the right), slide 15 | `gpt_p1_problems.jpg`, `gpt_p1_questions.jpg` |
| P2 “Ad return” sheet | slide 13 | slide 15 (fallback — slide 14) | `gpt_p2_roas_table.jpg`, `gpt_p2_roas_chart_sheet.jpg` |
| P3 return-rate heatmap | slide 19 | slide 19 | `gpt_p3_heatmap.jpg` |
| P4 review themes | slide 19, after P3 | slide 19 | `gpt_p3_themes_before.jpg`, `gpt_p3_examples_caveat.jpg` |
| P5 chart makeover | slide 21 | slides 21–22 | `gpt_p4_themes_after.jpg`, `gpt_p4_what_changed.jpg` |
| P6 report and script | slide 27 (or 24) | slide 28 | `gpt_p5_fake_report_preview.jpg`, `gpt_p5_report_answer_small.jpg`, `gpt_p5_report_top_script.jpg`, `gpt_p5_report_bottom.jpg` |

## 15 minutes before the session

1. Open ChatGPT in a work or training account. Start **one** new chat for the whole lesson: P6 builds on the charts from P2–P5. Check that file upload works.
2. Put `northstar_2025_EN.xlsx` and `northstar_sales_2026-01.csv` on the desktop.
3. Start Excel (desktop or Excel for the web): in demo 1 you open the downloaded file in it. Empty the Downloads folder so the new `.xlsx` is easy to find.
4. Open `assets/v2/chat/` in an image viewer. Keep `answers.md` and this runbook on a second monitor.
5. **Teams:** share the whole screen or practise switching windows: Excel opens in a separate window. Browser zoom 125–150 %.
6. If you have time in the morning, run P1–P6 in a separate chat, plus the pairs from slides 12, 16, 23 (texts below). That shows you how the model answers today.

## What you should get (from answers.md)

| What | Number |
|---|---|
| Rows in `Sales` / after cleaning | 1261 / 1260 (1 exact duplicate: 2025-03-19, Social, Home, South, $3,890.50; 1 text date `10/05/2025`) |
| Reviews | 357 |
| Revenue for the year | $2,520,078 without the duplicate; $2,523,968.50 as in the file |
| Revenue: January / November / December | $142,712 / $324,344 / $373,435 |
| December vs January / vs November | +161.7 % / +15.1 %; November + December = 27.7 % of annual revenue |
| Second half vs first | $1,054,310.50 → $1,469,658 = +39.4 % |
| Revenue per $1 of ads, Search | all year 5.15–5.39 (January 5.39, December 5.35) |
| Revenue per $1 of ads, Social | January–June 3.91–4.05; from July 1.97–2.02 |
| Social, spend H1 → H2 | $69,402 → $197,009 (+184 %); revenue $275,928 → $393,514 (+43 %) |
| Return rate, September–December | North × Electronics 24.8 %; the other 15 cells 4.5–5.4 % |
| N2 reviews, September–December | 87; 53 about damage (61 %) by the generator’s labels |
| Damage reviews outside N2 | 8 of 270 for the year |

The model sorts reviews into themes by keywords; it doesn’t see our labels. So its N2 “damage” share will be below 61 %. In the run it was 49 %, then 46 %, and 44 % in the report. These four numbers sit side by side on slide 22.

Warehouse N2 is the North × Electronics cell on the heatmap: 24.8 % for September–December, about 26 % in individual months.

---

## Demo 1 — “Excel without a licence” (slides 11–15)

Slide 15 shows a six-step checklist: upload the file → P1 → P2 → download the workbook → click a cell → out of time — the slide 14 frames. You have 5 minutes on slide 15 itself. So do the first three steps early: the file and P1 on slide 11, P2 on slide 13. On slide 15 only the workbook in Excel is left.
Mention Gemini in Google Sheets in one sentence: “If the file lives in Google Drive, you type the same request in the Gemini side panel.” The lesson has no Gemini frame.

### P1 — describe the file (send at the start of slide 11, 26:00)

Upload `northstar_2025_EN.xlsx` and send:

```
Describe this file: what one row is, how many rows, what period, what data problems. Suggest 5 questions a manager would ask. Don’t change anything yet.
```

Russian group:

```
Опиши этот файл: что такое одна строка, сколько строк, какой период, какие проблемы в данных. Предложи 5 вопросов, которые задал бы руководитель. Ничего пока не меняй.
```

You discuss the answer on slide 12 (on the right it shows frames from our run with ✓ / ✗ marks).

**What to look for:**
* `Sales` — 1261 rows, 9 columns; `Reviews` — 357 rows, 7 columns;
* period 01.01.2025–31.12.2025;
* one row = one day’s sales by channel, category, region and warehouse;
* the exact duplicate found;
* the text date `10/05/2025`. In the run the model missed it; slide 12 marks it ✗;
* zeros in `ad_spend`. In the run the model called them missing: “632 values are missing”. Also ✗ on slide 12;
* five manager questions and the line “I did not change the file”.

Read question 1 from the run aloud: “Which sales channels are most profitable once ad spend is included?” Say: “That’s what the next prompt computes.” Question 3, about returns, is demo 2.

**If the answer differs:**
* **Zeros called missing.** In the run the model wrote “632 `ad_spend` values are missing” and “32 `returns` values”. In the file these are zeros. Email and Organic buy no ads, so zero is normal for them. Zeros in `returns` are days without returns. Ask: “Is zero in ad_spend missing or a real zero? Check by channel.”
* **Missed the text date.** Prompt: “Check whether all dates in order_date use one format.” Answer: the row `10/05/2025` (Email, Sports, West).
* **The model already cleaned or computed something.** Ask it to restore the file and only describe it first.
* **Thinks longer than 90 seconds.** Talk over the frames on slide 12.

### P2 — the “Ad return” sheet (send at the start of slide 13, 33:00)

```
Add a sheet “Ad return” to the workbook: by month, revenue, ad spend and revenue per $1 of ads for Search and Social. Use Excel formulas, not pasted numbers. Build a line chart and let me download the .xlsx.
```

Russian group:

```
Добавь в книгу лист «Отдача рекламы»: по месяцам выручка, рекламный расход и выручка на $1 рекламы для Search и Social. Считай формулами Excel, а не готовыми числами. Построй линейный график и дай скачать .xlsx.
```

### Slide 15 — the workbook in Excel (39:00–44:00)

1. Download the `.xlsx` and open it in Excel. In the run the new sheet was called `Ad ROAS 2025`.
2. Click an ad-return cell. The `fx` bar should show a formula.
3. If it shows a number, write in the chat: “replace the numbers with formulas”. That is what happened in our run: the cells held ready numbers (the frame is on slide 14).
4. Download again and click the cell again. Now `fx` shows a formula like `=B2/C2`. Say: “Excel does the counting; the model only wrote the formula. Change the spend and the number recalculates.”

**What to look for:**
* Search 5.15–5.39 all year (January 5.39, December 5.35);
* Social about 4 until June (January 4.05), about 2 from July (July 1.97, December 2.00);
* on the chart the Social line halves in July. That is the lesson’s second story; we return to it on slide 20;
* the duplicate removed: in the run Social in March — revenue 50,378.00, spend 12,514.00. Higher March numbers mean the model kept the duplicate.

**If the answer differs:**
* **Formulas straight away.** Good. Say our run had numbers and show slide 14.
* **“Replace the numbers with formulas” didn’t help.** Be specific: “The revenue-per-$1 column holds numbers. Rewrite it as a formula: revenue / spend.”
* **The sheet has a different name.** Doesn’t matter; move on.
* **The chart is only in the chat, not in the file.** Ask: “Insert this chart into the workbook on the ad-return sheet.” No time — move on.
* **Numbers differ from the reference by more than 0.05.** Ask whether the duplicate was removed and what the model did with the `10/05/2025` row.
* **Download failed or Excel didn’t open.** Go back to slide 14, or open the reference `demo_v2/excel_demo/northstar_2025_formulas_EN.xlsx` and click the ad-return cell there.

**Optional, only if you’re ahead of time.** If you have Claude for Excel or Copilot in Excel, open `northstar_2025_EN.xlsx` and type P2 in the side panel. Say: “This is how it looks with a licence. Without one you do the same through a chat.”

---

## Demo 2 — chat with a file (slide 19, 5 minutes, 56:00–61:00)

Same chat; the file is already uploaded. The slide shows the P3 and P4 breakdowns, each with a result frame from our run underneath. Send P3 at the start of the slide and P4 as soon as the P3 answer arrives.
The demo answers question 3 from the P1 answer and the third question in Anna’s e-mail: why so many returns in the autumn.
After each answer open the code: in ChatGPT it is the “Analysis complete” block or the code button above the result. Say: “A program the model wrote does the counting. You can open it.”

### P3 — return-rate heatmap

```
Compute the return rate by region and category for September–December and show it as a heatmap.
```

Russian group:

```
Посчитай долю возвратов по регионам и категориям за сентябрь–декабрь и покажи тепловой картой.
```

**What to look for:**
* a 4 × 4 grid: regions × categories;
* one dark cell: North × Electronics — 24.8 %. That is warehouse N2; in P4 the model finds it by itself;
* the other cells 4.5–5.4 %;
* the rate is per order (`returns / orders`).

**If the answer differs:**
* **Computed the whole year.** The dark cell will be paler. Ask: “Only September–December.”
* **Divides returns by revenue.** Ask: “The return rate is returns divided by orders.”
* **One cell is off by 0.1.** In the run North × Sports came out at 5.3 %, the reference says 5.4 %. That’s rounding.
* **Thinks longer than 90 seconds.** Talk over the frame under the P3 breakdown (`gpt_p3_heatmap.jpg`).

### P4 — review themes

```
For the warehouse with the highest return rate, sort the reviews into themes and compare it with the other warehouses. Show 5 example reviews.
```

Russian group:

```
Для склада с самой высокой долей возвратов разложи отзывы на темы и сравни с остальными складами. Покажи 5 примеров отзывов.
```

**What to look for:**
* the model picked N2. In the run it explained: it takes N2 by return rate, while S1 leads only by number of returns. Say it aloud: “Rate and count are different questions”;
* N2 — 87 reviews for September–December (matches the reference), other warehouses — 116;
* the packaging and damage theme ranks first at N2: in the run 49 % vs 12 %;
* five example reviews. In the run the model showed examples from other warehouses (C1, S1, N1). If you need N2 examples, ask separately;
* the model’s caveat: the theme also caught praise of packaging (“Neatly packed, everything intact”). Read it aloud; you’ll need it on slide 22.

**If the answer differs:**
* **Different percentages.** The model splits themes its own way each time. What matters is that the damage theme is several times higher at N2. For reference: by the generator’s labels, 53 of 87 N2 reviews are about damage (61 %); outside N2, 8 of 270 for the year.
* **Wrong warehouse.** Ask: “Did you choose by rate or by number of returns?”
* **Thinks longer than 90 seconds.** Talk over the frame under the P4 breakdown (`gpt_p3_themes_before.jpg`; full answer — `gpt_p3_examples_caveat.jpg`).

## P5 — chart makeover for a slide (slide 21, 64:00–67:00)

Send it at the start of the slide. In the run the answer took 36 seconds. While you wait, talk over the left half of the slide.

```
Rework this chart for a slide: the title states the finding, bars sorted, value labels on the bars, no legend and no gridlines, one accent colour for N2, everything else grey. Explain in 3 points what you changed.
```

Russian group:

```
Переделай этот график для слайда: заголовок — вывод, столбцы отсортированы, подписи значений на столбцах, без легенды и сетки, один акцентный цвет для N2, остальное серым. Объясни в 3 пунктах, что поменял.
```

**What to look for:**
* a finding as the title, with numbers. In the run: “N2 has almost 9× more damage complaints: 46 % vs 5 %”;
* bars sorted, labels on the bars, N2 in blue, the rest grey, no legend or grid;
* three points on “what I changed”.

**What to say.** Ask the audience: “What changed besides the colour?” Answer: the numbers. It was 49 % vs 12 %; now 46 % vs 5 %. The model re-counted the theme: it moved praise of packaging into “Product OK”. We only asked for a restyle. In the final report (P6) the same theme becomes 44 % vs 4 %. Details on slide 22.

**If the answer differs:**
* **The numbers didn’t change.** Good. Say they shifted in our run and show `gpt_p4_what_changed.jpg` (it is also on slide 22).
* **Title without a number.** Ask: “The title needs a finding with a number.”
* **Thinks longer than 90 seconds.** Talk over the frame on the right of the slide.

---

## Slide 22 — the 60-second check (4 minutes, 67:00–71:00)

The slide shows four numbers — the share of N2 reviews about damage for September–December: **49 %** (first chart), **46 %** (after restyling), **44 %** (in the Word report from our run) and **61 %** by the labels the file was built from (53 of 87 N2 reviews). The model searches by keywords and misses complaints written in other words. The N2 conclusion doesn’t change; the number for the manager does.

Show three actions on the file and on the demo results:

1. **Compare rows before and after.** `Sales` has 1261 rows. After the duplicate is removed — 1260. The `10/05/2025` date is fixed by format; the row stays. Ask the model: “How many rows were there, and how many now?”
2. **One point: against the source and the previous version.** Open `northstar_2025_EN.xlsx`, filter December, select the `revenue` column. The Excel status bar shows $373,435 — the same point as on the revenue-by-month chart. Compare with the previous version the same way: 49 % on the first chart, 46 % after the rework.
3. **Ask: percent of what?** December is +161.7 % vs January and +15.1 % vs November — the same December number. 46 % is a share of 87 N2 reviews for September–December. Out of all 357 reviews you’d get a different number.

---

## Slide 28 — report and recipe (3 minutes, 83:00–86:00)

**When to send.** At the start of slide 27 (81:00), or earlier — on slide 24 (74:00). In the run the answer took 3 min 34 s. Sent on slide 27, it arrives around the middle of slide 28. Not ready — show the frames.

```
Build a one-page report for a manager in Word: the question, 3 charts (revenue by month, ad return, N2 complaints), 3 findings and one point on “what this data does not prove”. And give me a short Python script that builds the same 3 charts from next month’s file.
```

Russian group:

```
Собери одностраничный отчёт для руководителя в Word: вопрос, 3 графика (выручка по месяцам, отдача рекламы, жалобы N2), 3 вывода и один пункт «чего эти данные не доказывают». И дай короткий Python-скрипт, который построит те же 3 графика по файлу следующего месяца.
```

**Step 1. Show the preview in the chat.** In the run ChatGPT showed a thumbnail of a stock picture: “Business Report”, “Series A–E”, months January–June, “million USD” (`gpt_p5_report_answer_small.jpg`, large — `gpt_p5_fake_report_preview.jpg`). None of our data is there. Ask: “Is this our report?”

**Step 2. Download and open the file.** In the run the downloaded .docx was correct (`gpt_p5_report_top_script.jpg`, `gpt_p5_report_bottom.jpg`):
* title “What happened to sales in 2025?”;
* annual revenue $2,520,078, December $373,435, orders 47,989;
* three charts: revenue by month, Search vs Social, N2 complaints;
* three findings: December $373,435 vs January $142,712; Search ≈ 5.2, Social dropped from about 4.0 to 2.0 in July; 44 % of N2 reviews about damage vs 4 % elsewhere, N2 returns 24.8 % in September–December;
* a “what this data does not prove” point: the cause of the damage and ad profitability.

Check two numbers against the reference: $2,520,078 and $373,435. Say: “The preview is a picture. We send the file, and only after we’ve opened it.”

**Step 3. The recipe.** Show the script in the chat (`gpt_p5_report_top_script.jpg`): `pip install pandas openpyxl matplotlib`, then `python rebuild_northstar_charts.py next_month.xlsx`. The result is a `charts` folder with `01_revenue.png`, `02_roas.png`, `03_reviews_N2.png`.
Our next-month file is `northstar_sales_2026-01.csv`: CSV, sales only, no reviews. The script from the run expects an `.xlsx` with two sheets. There’s no time to run it on slide 28, so say it in words: the model will fix the CSV reading; the reviews chart won’t rebuild; the revenue-by-month chart will have one point — January.

**If the answer differs:**
* **The preview is right straight away.** Good. Show `gpt_p5_fake_report_preview.jpg`: “In our run it looked like this.”
* **The report runs to two pages.** Ask: “Fit it on one A4 page.”
* **No “what this data does not prove” point.** Ask to add it.
* **Not ready by slide 28.** Talk over the frames on the slide: preview, top of the report, script.

---

## The pairs and the experiment: texts to re-run before class

Slides 9, 12, 16 and 23 are shown as ready frames, not run live. Below are the exact texts so you can repeat them in the morning and know how the model answers today. Run each in a **new** chat with `northstar_2025.xlsx` uploaded (except slide 9). The runs were in Russian; English versions are given for the EN group.

With today’s models the quick prompts often give a good answer. That happened on slides 12 and 23, so those pairs are labelled “Quick / Under control”. There is only one clean failure — seasonality on slide 16. If the model answers differently today, show what you got and say so aloud.

### Slide 9 — the “73 rows, no code” experiment

* **Data:** the whole `demo_assets/northstar_sales_messy.csv` (73 rows, the small file from the previous lesson version) pasted as text into a message. Model in the run: ChatGPT Pro, 17 Oct 2026.
* **Prompt text:** only the pasted data made it into the frame; the wording itself wasn’t saved. To repeat, use:
  ```
  Below are 73 CSV rows. Don’t use tools or code; count yourself. 1) What is the total revenue? 2) What problems are there in the data? Briefly, exact numbers.
  ```
  RU: `Ниже 73 строки CSV. Не используй инструменты и код, считай сам. 1) Какая общая выручка? 2) Какие проблемы есть в данных? Кратко, точные числа.`
* **What we got:** 259,357.00 across all 73 rows; 256,045.00 without the duplicate (72 rows). Four problems: duplicate 1028 (+3,312), blank region in 1010, date `2026/04/22` in 1041, 1055 with 66 returns on 62 orders — “needs checking”.
* **For comparison, 13 Oct 2026:** Claude Haiku 5.5 and Sonnet 5.5 got the sum right but “fixed” row 1055: “probably 6” (`northstar_sales_truth.csv` says 4). Details: `demo_assets/no_code_experiment_2026-10-13.md`.
* **Frames:** `chat_badgood/b0_nocode_paste.jpg`, `b0_nocode_answer.jpg` → crops `shots/b0_paste.jpg`, `b0_answer.jpg`.

### Slide 12 — “Find insights” vs prompt 1

* **Quick:**
  ```
  Here is the file. Find interesting insights.
  ```
  RU (as run): `Вот файл. Найди интересные инсайты.` Model in the run: GPT-6.1 Sol, “Light”, answer in 1 min 30 s. It found Social (“from July about half as effective”, 3.94 → 1.98 by quarter) and N2. It chose the comparisons itself: quarters and half-years; Q4 — 36.4 % of annual revenue. It found the duplicate (3,890.5) but wrote that the calculations keep the original rows: the duplicate stayed in the numbers.
* **Under control:** prompt 1 (text above). The frames on the right come from the P1 run.
* **Frames:** `chat_badgood/b1_insights_top.jpg`, `b1_insights_mid.jpg`, `b1_insights_dup.jpg`, `b1_insights_chart.jpg` → on the slide, crops `shots/b1_top.jpg`, `b1_dup.jpg`; on the right `shots/p1_problems.jpg`, `p1_questions.jpg`.

### Slide 14 — numbers vs formulas

* **Quick:** the output of P2 itself in our run — the `Ad ROAS 2025` sheet with ready numbers, although the prompt asked for formulas (`shots/p2_roas_sheet.jpg`).
* **Under control:** the fix phrase `replace the numbers with formulas` (RU: `замени числа формулами`). The Excel frame with the fx bar (`shots/xl_fx_sumifs.jpg`) comes from the reference workbook `demo_v2/excel_demo/northstar_2025_formulas.xlsx` (built by `make_formulas_workbook.py`).

### Slide 16 — seasonality (the only “✗ Weak / ✓ Good” pair)

* **Weak** (model in the run: ChatGPT Pro, 1 min 19 s):
  ```
  How much did sales grow this year? Answer briefly, with one number for the slide.
  ```
  RU (as run): `Насколько выросли продажи за год? Ответь коротко, одним числом для слайда.` Answer: “+161.7 % — December revenue vs January”. In the chat window the text got duplicated while typing, so the slide shows it retyped and shorter. The answer doesn’t depend on it.
* **Good** (same chat, 1 min 35 s):
  ```
  Compute growth three ways: December vs January, December vs November, second half vs first half. For each number give the base and the period. Which number should go on the manager’s slide, and why?
  ```
  RU (as run): `Посчитай рост тремя способами: декабрь к январю, декабрь к ноябрю, второе полугодие к первому. Для каждого числа укажи базу и период. Какое число поставить на слайд руководителю и почему?`
  Answer: a table with base and period — January 142,712.00 → December 373,435.00 = +161.7 %; November 324,344.50 → December = +15.1 %; January–June 1,054,310.50 → July–December 1,469,658.00 = +39.4 %. Recommendation: “Second-half revenue is about 40 % above the first half.” Plus a note that there is no 2024 data.
* **Frames:** `chat_badgood/b3_growth_bad_raw.jpg`, `b3_growth_both.jpg`, `b3_growth_good_table.jpg` → on the slide `shots/b3_bad.jpg`, `b3_table.jpg`.

### Slide 23 — “Cut Social in half?”

* **Prompt text** (model in the run: ChatGPT Pro, 2 min 54 s):
  ```
  If we cut the Social budget in half from January, how much do we save and how much revenue do we lose per quarter? Give numbers for a decision.
  ```
  RU (as run): `Если с января урезать бюджет Social вдвое, сколько мы сэкономим и сколько потеряем выручки за квартал? Дай цифры для решения.`
* **Quick — the first line of the answer:** savings of 61.1k for January–March (with the budget at the Q4 2025 level); “revenue loss, assuming it falls proportionally — 122.5k”.
* **Under control — the paragraphs below:** these are scenarios without estimated probabilities; Social’s return fell from 3.98 to 2.00, but the average return doesn’t show how many sales the half of the budget being cut actually brings; recommendation — test the cut on a test group with a control group.
* **If the model gives a forecast with no caveats,** ask a second question: `What assumption are you making? Can this data tell us that?`
* **Frames:** `chat_badgood/b5_social_top.jpg`, `b5_social_reco.jpg` → `shots/b5_top.jpg`, `b5_reco.jpg`.

## SQL for slides 25–26 (not run live)

The prompt from slide 25:

```
The database has a videos table: length and views of every video. Write an SQL query: which video length gets the most views? Explain every line.
```

Russian group:

```
В базе таблица videos: длительность и просмотры каждого видео. Напиши SQL-запрос: видео какой длины набирают больше всего просмотров? Объясни каждую строку.
```

**How to repeat it.** Only in a **temporary chat** or with connected sources (connectors) switched off. In our run ChatGPT pulled the real schema of the author’s database from connected sources, which is why we don’t show that frame. Expect a query like `SELECT duration_bucket, COUNT(*), MEDIAN(views) … FROM videos GROUP BY duration_bucket`. If the model invents other column names, that is exactly the point of the slide note: “Describe the tables in the prompt.”

**Where the slide 26 numbers come from.** Not from a chat: the queries in `demo_v2/channels/queries.sql` were run locally in DuckDB (`python run_queries.py`) on the anonymised sample `channels_sample.duckdb`. Results: `results/q2_views_by_duration.csv` (20–40 minutes — 13,000 typical views, 1–5 minutes — 1,100, 12× more) and `results/q4_duration_vs_own_channel.csv` (vs the channel’s usual video: 0.99–1.10, 1.03 for 20–40 minutes). We don’t hand the sample files to students.

---

## If something goes wrong

| Problem | What to do |
|---|---|
| A prompt thinks longer than 90 seconds | The ready frame from the table at the top; move on |
| Out of time on slide 15 | The slide 14 frames or the reference workbook `northstar_2025_formulas_EN.xlsx` |
| The code or download button looks different | Don’t search aloud. “The interface changes; the steps stay the same” |
| Upload limit or sign-in error | Run every demo on the ready frames, in the order of the table at the top |
| The model’s numbers differ from the reference | Ask about the duplicate and the `10/05/2025` date. If that doesn’t help, show the frame and say we compare two numbers |
| Someone wants to upload their own data | The practice file only. Traffic light — slide 29 |
| The downloaded .xlsx won’t open | Excel for the web or Google Sheets. If that fails — `gpt_p2_roas_table.jpg` |
| P6 not ready by slide 28 | The frames on the slide; next time send P6 on slide 24 |
