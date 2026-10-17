# Lesson 08 • Live demo runbook (v2): Northstar 2025 in ChatGPT and Excel

**Slides and time (from `deck/build_v2.py`):** demo 1 — slide 5, 12 minutes (13:00–25:00) • break — slide 8 (32:00–37:00) • demo 2 — slide 9, 12 minutes (37:00–49:00) • the 60-second check — slide 12, 3 minutes • report and recipe — slide 15, 5 minutes (68:00–73:00)
**File:** `demo_v2/northstar_2025_EN.xlsx` (Russian group: `demo_v2/northstar_2025.xlsx`). Sheets `Sales` (1261 rows) and `Reviews` (357 rows). Fictional data.
**Next month’s file:** `demo_v2/northstar_sales_2026-01.csv` (100 rows, January 2026, sales only, no reviews).
**Service:** ChatGPT (it shows the code and lets you download files). Any chat with file upload works for demo 1.
**Reference numbers:** `demo_v2/answers.md`.
**Ready frames:** `assets/v2/chat/` — a real run of all six prompts on this file. The run was in Russian, so with the EN group describe the frames in English as you show them.

---

## Fallback rule

If a prompt takes longer than 90 seconds, show the ready frame from the table below and move on. Let the answer keep running. Come back to it if time allows.
The exception is prompt 6 (the report). In our run it took 3 min 34 s. Send it early, at the start of slide 14, around 65:00 (see below).
The slide map leaves about 7 minutes of buffer for the whole session. Each fallback saves another minute or two.

| Prompt | Slide | Ready frame |
|---|---|---|
| P1 describe the file | 5 | `gpt_p1_problems.jpg`, `gpt_p1_questions.jpg` |
| P2 “Ad return” sheet | 5 | `gpt_p2_roas_table.jpg`, `gpt_p2_roas_chart_sheet.jpg` |
| P3 return-rate heatmap | 9 | `gpt_p3_heatmap.jpg` |
| P4 review themes | 9 | `gpt_p3_themes_before.jpg`, `gpt_p3_examples_caveat.jpg` |
| P5 chart rework | 9 (large on slide 11) | `gpt_p4_themes_after.jpg`, `gpt_p4_what_changed.jpg` |
| P6 report and script | 15 | `gpt_p5_fake_report_preview.jpg`, `gpt_p5_report_answer_small.jpg`, `gpt_p5_report_top_script.jpg`, `gpt_p5_report_bottom.jpg` |

## 15 minutes before class

1. Open ChatGPT in your work or practice account. Start **one** new chat for the whole lesson: P6 relies on the charts from P2–P5. Check that file upload works.
2. Put `northstar_2025_EN.xlsx` and `northstar_sales_2026-01.csv` on the desktop.
3. Start Excel (desktop or Excel for the web): in demo 1 you will open the downloaded file in it. Empty your Downloads folder so the new `.xlsx` is easy to find.
4. Open the `assets/v2/chat/` folder in an image viewer. Keep `answers.md` and this runbook on the second monitor.
5. **Teams:** share the whole screen, or practise switching windows: Excel opens in its own window. Browser zoom 125–150 %.
6. If you have time in the morning, run P1–P6 in a separate chat. You will see how the model answers today.

## Expected result (from answers.md)

| What | Number |
|---|---|
| Rows in `Sales` / after cleaning | 1261 / 1260 (1 exact duplicate; 1 date stored as text `10/05/2025`) |
| Reviews | 357 |
| Revenue for the year | $2,520,078 without the duplicate; $2,523,968.50 as in the file |
| Revenue: January / November / December | $142,712 / $324,344 / $373,435 |
| December vs January / vs November | +161.7 % / +15.1 %; November + December = 27.7 % of annual revenue |
| Revenue per $1 of ads, Search | 5.15–5.39 all year (January 5.39, December 5.35) |
| Revenue per $1 of ads, Social | January–June 3.91–4.05; from July 1.97–2.02 |
| Social, spend H1 → H2 | $69,402 → $197,009 (+184 %); revenue $275,928 → $393,514 (+43 %) |
| Return rate, September–December | North × Electronics 24.8 %; the other 15 cells 4.5–5.4 % |
| N2 reviews, September–December | 87; 53 about damage (61 %) by the generator’s labels |
| Damage reviews outside N2 | 8 of 270 for the year |

The model sorts reviews into themes by wording; it does not see our labels. So its “damage” share for N2 comes out below 61 %. In the run it was 49 %, then 46 %, then 44 % in the report. These four numbers sit side by side on slide 12.

Warehouse N2 is the North × Electronics cell on the heatmap: 24.8 % for September–December, about 26 % in individual months.

---

## Demo 1 — “Excel without a licence” (slide 5, 12 minutes)

Plan: P1 — 4 minutes • P2, downloading the workbook and opening it in Excel — 8 minutes.
Mention Gemini in Google Sheets in one sentence: “If the file lives in Google Drive, you type the same request into the Gemini side panel.” The lesson has no Gemini frame.

### P1 — describe the file (4 min)

Upload `northstar_2025_EN.xlsx` and send:

```
Describe this file: what one row is, how many rows, what period, what data problems. Suggest 5 questions a manager would ask. Don’t change anything yet.
```

Russian group:

```
Опиши этот файл: что такое одна строка, сколько строк, какой период, какие проблемы в данных. Предложи 5 вопросов, которые задал бы руководитель. Ничего пока не меняй.
```

**Look for:**
* `Sales` — 1261 rows, 9 columns; `Reviews` — 357 rows, 7 columns;
* period 01.01.2025–31.12.2025;
* one row is one day of sales by channel, category, region and warehouse (in the run the model called it “aggregated sales”);
* the exact duplicate is found;
* the text date `10/05/2025`. In the run the model missed it; slide 3 says so;
* zeros in `ad_spend`. In the run the model called them missing: “632 values are missing”. Slide 3 says this too;
* five manager questions and a line saying the file was not changed.

Read question 1 from the run aloud: “Which sales channels are most profitable once ad spend is taken into account?” Say: “That is what the next prompt calculates.” Question 3, about returns, is for demo 2.

**If the answer differs:**
* **Zeros are called missing values.** In the run the model wrote “632 `ad_spend` values are missing” and “32 `returns` values are missing”. In the file these are zeros. Email and Organic buy no advertising, so zero is normal for them. Zeros in `returns` are days with no returns. Ask: “Is a zero in ad_spend missing or a real zero? Check by channel.”
* **The text date is not found.** It was missing in the run too. Prompt: “Check that every date in order_date has the same format.” Answer: the row `10/05/2025` (Email, Sports, West).
* **The model already cleaned or calculated something.** Ask it to put the file back as it was and only describe it first.
* **It takes longer than 90 seconds.** Show `gpt_p1_problems.jpg`, then `gpt_p1_questions.jpg`.

### P2 — the “Ad return” sheet (8 min including the workbook in Excel)

```
Add a sheet “Ad return” to the workbook: by month, revenue, ad spend and revenue per $1 of ads for Search and Social. Use Excel formulas, not pasted numbers. Build a line chart and let me download the .xlsx.
```

Russian group:

```
Добавь в книгу лист «Отдача рекламы»: по месяцам выручка, рекламный расход и выручка на $1 рекламы для Search и Social. Считай формулами Excel, а не готовыми числами. Построй линейный график и дай скачать .xlsx.
```

**Then** (slide 5 says the same):
1. Download the `.xlsx` and open it in Excel. In the run the new sheet was called `Ad ROAS 2025`; its screenshot is on slide 5.
2. Open the workbook and click an ad-return cell. The `fx` bar should show a formula.
3. If it shows a number, write in the chat: “replace the numbers with formulas”. That is what happened in our run: the cells held ready numbers.
4. Download the workbook again and click the cell again. Now `fx` shows a formula like `=B2/C2`. Say: “Excel does the maths; the model only wrote the formula. Change the spend and the number recalculates.”

**Look for:**
* Search is flat at 5.15–5.39 all year (January 5.39, December 5.35);
* Social is about 4 until June (January 4.05) and about 2 from July (July 1.97, December 2.00);
* on the chart the Social line halves in July. This is the lesson’s second story; we come back to it on slide 10;
* the duplicate is gone: in the run, Social in March shows revenue 50,378.00 and spend 12,514.00. If the March numbers are higher, the model kept the duplicate.

**If the answer differs:**
* **Formulas came straight away.** Good. Say that our run had numbers and show the `Ad ROAS 2025` sheet on slide 5.
* **“Replace the numbers with formulas” didn’t help.** Be specific: “The revenue-per-$1 column has typed numbers. Rewrite it as a formula: revenue / spend.”
* **The sheet has a different name.** In the run it was called `Ad ROAS 2025`. That is fine; move on.
* **The chart is only in the chat, not in the file.** In the run the chart was drawn in the chat next to the table (`gpt_p2_roas_chart_sheet.jpg`). Ask: “Put this chart into the workbook on the ad-return sheet.”
* **Numbers differ from the reference by more than 0.05.** Ask whether the duplicate was removed and what the model did with the `10/05/2025` row.
* **The download failed or Excel won’t open.** Show `gpt_p2_roas_table.jpg` (the monthly table) and `gpt_p2_roas_chart_sheet.jpg` (the chart next to the `Sales` sheet). There is no ready frame of the `fx` bar. Open `northstar_2025_EN.xlsx`, type `=` on an empty sheet and click two cells. It takes 30 seconds.

**Optional, 90 seconds, if time allows.** If you have Claude for Excel or Copilot in Excel, open `northstar_2025_EN.xlsx` and type the same request into the side panel. Say: “This is what it looks like with a licence. Without one you do the same thing through a chat.” Claude for Excel is on paid plans only.

**Audience task (Teams chat):** which of the model’s five questions would your manager ask?

---

## Demo 2 — chat with a file (slide 9, 12 minutes, 37:00–49:00)

Same chat, the file is already uploaded. Plan: P3 — 3 minutes • P4 — 4 minutes • P5 — 4 minutes • 1 minute spare.
The demo answers question 3 from the P1 answer and the third question in Anna’s e-mail: why so many returns in the autumn.
After each answer open the code: in ChatGPT it is the “Analysis complete” block or the “Show code” button above the result. Say: “The numbers come from a program the model wrote. You can open it.”

### P3 — return-rate heatmap (3 min)

```
Compute the return rate by region and category for September–December and show it as a heatmap.
```

Russian group:

```
Посчитай долю возвратов по регионам и категориям за сентябрь–декабрь и покажи тепловой картой.
```

**Look for:**
* a 4 × 4 grid: regions × categories;
* one dark cell: North × Electronics — 24.8 %. This is warehouse N2: in P4 the model will find it by itself;
* the other cells at 4.5–5.4 %;
* the rate is calculated from orders (`returns / orders`).

**If the answer differs:**
* **It used the whole year.** The dark cell will be paler. Ask: “September–December only.”
* **It divides returns by revenue.** Ask: “Return rate means returns divided by orders.”
* **One cell is off by 0.1.** In the run North × Sports came out 5.3 %, the reference says 5.4 %. That is rounding; don’t stop on it.
* **It takes longer than 90 seconds.** Show `gpt_p3_heatmap.jpg`.

### P4 — review themes (4 min)

```
For the warehouse with the highest return rate, sort the reviews into themes and compare it with the other warehouses. Show 5 example reviews.
```

Russian group:

```
Для склада с самой высокой долей возвратов разложи отзывы на темы и сравни с остальными складами. Покажи 5 примеров отзывов.
```

**Look for:**
* the model picks N2. In the run it explained this itself: N2 has the highest return rate, while S1 leads only on the number of returns. Say it aloud: “Rate and count are different questions”;
* N2 has 87 reviews for September–December (matches the reference), the other warehouses 116;
* packaging / damage is N2’s top theme: 49 % vs 12 % in the run;
* five example reviews. In the run the model showed examples from other warehouses (C1, S1, N1). If you want N2 examples, ask separately;
* the model’s caveat. In the run it said the theme also includes praise for packaging (“Neatly packed, everything intact”). Read it aloud. You will need it in P5.

**If the answer differs:**
* **Different percentages.** The model splits themes its own way each time. What matters is that N2’s damage theme is several times higher than elsewhere. For reference: by the generator’s labels 53 of N2’s 87 reviews are about damage (61 %); outside N2 it is 8 of 270 for the year.
* **It picked another warehouse.** Ask: “Did you choose by return rate or by number of returns?”
* **It takes longer than 90 seconds.** Show `gpt_p3_themes_before.jpg`, then `gpt_p3_examples_caveat.jpg`.

### P5 — rework the chart for a slide (4 min)

Show P5 live; on slide 11 you will show the same pair large. If time is short, send the prompt and move to slide 10 without waiting for the answer.

```
Rework this chart for a slide: the title states the finding, bars sorted, value labels on the bars, no legend and no gridlines, one accent colour for N2, everything else grey. Explain in 3 points what you changed.
```

Russian group:

```
Переделай этот график для слайда: заголовок — вывод, столбцы отсортированы, подписи значений на столбцах, без легенды и сетки, один акцентный цвет для N2, остальное серым. Объясни в 3 пунктах, что поменял.
```

**Look for:**
* a finding as the title, with numbers. In the run: “N2 has almost 9 times more damage complaints: 46 % vs 5 %”;
* bars in descending order, labels on the bars, N2 in blue, the rest grey, no legend or gridlines;
* three “what I changed” points. In the run the answer took 36 seconds.

**What to say.** Ask the audience: “What changed apart from the colours?” Answer: the numbers. It was 49 % vs 12 %; now it is 46 % vs 5 %. The model recounted the theme: it moved praise for packaging into “Product OK” (N2 went from 18 % to 21 % there). We only asked for a restyle. In the final report (P6) the same theme becomes 44 % vs 4 %. We go through the numbers on slide 12; here one sentence is enough: after every rework, compare two numbers with the previous version.

**If the answer differs:**
* **The numbers did not move.** Good. Say that in our run they did, and show `gpt_p4_what_changed.jpg`.
* **The title has no number.** Ask: “The title needs a finding with a number.”
* **It takes longer than 90 seconds.** Show `gpt_p4_themes_after.jpg`, then `gpt_p4_what_changed.jpg`.

---

## Slide 12 — the 60-second check (3 minutes)

The slide has four numbers — the share of N2 reviews about damage, September–December: **49 %** (first chart), **46 %** (after restyling), **44 %** (in the Word report) and **61 %** by the labels the file was built from (53 of 87 N2 reviews). The model searches by keywords and misses complaints written in other words. The N2 conclusion stays; the number for the manager changes.

Show three actions on the file and on the demo results:

1. **Compare rows before and after.** `Sales` has 1261 rows. After removing the duplicate — 1260. The `10/05/2025` date is fixed by format; the row stays. Ask the model: “How many rows were there, and how many now?”
2. **One point: against the source and the previous version.** Open `northstar_2025_EN.xlsx`, filter December, select the `revenue` column. Excel’s status bar shows the sum $373,435 — the same point as on the monthly revenue chart. Against the previous version it works the same way: 49 % on the first chart, 46 % after the rework.
3. **Ask “percent of what?”.** December is +161.7 % vs January and +15.1 % vs November — the same December number. 46 % is a share of N2’s 87 reviews for September–December. Out of all 357 reviews it would be a different number.

For the notes, one sentence: in the old version of the lesson the model, with no code, got the total right but “repaired” 66 returns into “probably 6”, while the source said 4.

---

## Slide 15 — report and recipe (5 minutes, 68:00–73:00, one live prompt)

**When to send.** In the run the answer took 3 min 34 s. Send P6 at the start of slide 14 (“Where data comes from”, around 65:00) and talk through that slide while the model works. By slide 15 the file will be ready. If not, show the frames.

```
Build a one-page report for a manager in Word: the question, 3 charts (revenue by month, ad return, N2 complaints), 3 findings and one point on “what this data does not prove”. And give me a short Python script that builds the same 3 charts from next month’s file.
```

Russian group:

```
Собери одностраничный отчёт для руководителя в Word: вопрос, 3 графика (выручка по месяцам, отдача рекламы, жалобы N2), 3 вывода и один пункт «чего эти данные не доказывают». И дай короткий Python-скрипт, который построит те же 3 графика по файлу следующего месяца.
```

**Step 1. Show the preview in the chat.** In the run ChatGPT showed a thumbnail of a stock picture: “Business Report”, “Series A–E”, January–June, “million USD” (`gpt_p5_report_answer_small.jpg`, full size `gpt_p5_fake_report_preview.jpg`). None of our data is there. Ask: “Is this our report?”

**Step 2. Download and open the file.** In the run the downloaded .docx was correct (`gpt_p5_report_top_script.jpg`, `gpt_p5_report_bottom.jpg`):
* title “How did sales go in 2025?” (in Russian in the run);
* annual revenue $2,520,078, December $373,435, orders 47,989;
* three charts: revenue by month, Search vs Social, N2 complaints;
* three findings: December $373,435 vs January $142,712; Search ≈ 5.2, Social fell from about 4.0 to 2.0 from July; 44 % of N2 reviews are about damage vs 4 % elsewhere, N2 returns 24.8 % in September–December;
* a “what the data does not prove” point: the cause of the damage and the profit from advertising.

Check two numbers against the reference: $2,520,078 and $373,435. Say: “The preview is a picture. We send the file, and only after we have opened it.”

**Step 3. The recipe.** Show the script in the chat (`gpt_p5_report_top_script.jpg`): `pip install pandas openpyxl matplotlib`, then `python rebuild_northstar_charts.py next_month.xlsx`. The output is a `charts` folder with `01_revenue.png`, `02_roas.png`, `03_reviews_N2.png`.
Our next-month file is `northstar_sales_2026-01.csv`: CSV format, sales only, no reviews. The script from the run expects an `.xlsx` with two sheets. If you have a minute, upload the CSV to the chat and ask: “Run the script on this file. If something is missing, tell me what.” Expect the model to fix how the CSV is read; the reviews chart won’t rebuild — the file has no reviews; the monthly revenue chart will have one point, January. No minute to spare — say it in words.

**If the answer differs:**
* **The preview is correct straight away.** Good. Show `gpt_p5_fake_report_preview.jpg`: “In our run it looked like this.”
* **The report runs to two pages.** Ask: “Fit it on one A4 page.”
* **No “what the data does not prove” point.** Ask for it.
* **Not ready by slide 15.** Show the frames in order: preview, report top with the script, report bottom.

---

## If something goes wrong

| Problem | What to do |
|---|---|
| A prompt takes longer than 90 seconds | Ready frame from the table at the top; move on |
| The code or download button looks different | Don’t hunt for it aloud. “The interface changes; the steps stay the same” |
| Upload limit or sign-in error | Run every demo from the ready frames, in the order of the table at the top |
| The model gives numbers that differ from the reference | Ask about the duplicate and the `10/05/2025` date. If that does not help, show the frame and say we check two numbers |
| Someone wants to upload their own data | Practice file only. Traffic light — slide 17 |
| The downloaded .xlsx won’t open | Excel for the web or Google Sheets. If that fails — `gpt_p2_roas_table.jpg` |
