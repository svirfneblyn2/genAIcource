# Lesson 08 • Homework: the Northstar 2025 analysis pack

**Course:** GenAI Basics • Lesson 08 “AI for Data Analysis” • Module 3: AI assistants at work
**File:** `demo_v2/student_starter/northstar_2025_EN.xlsx` (Russian-speaking group: `northstar_2025.xlsx`). Practice, fictional data — fine to upload to any service.
**Next month’s file:** `demo_v2/student_starter/northstar_sales_2026-01.csv` (for the recipe, step 5).
**Templates:** `report_template.md` and `checks_template.md` in the same `student_starter/` folder.
**Tools:** any chat where you can upload a file and download the result: ChatGPT, Claude, Gemini. You do not need a paid AI licence in Excel; the whole assignment works through a chat. If you have Copilot in Excel or Claude for Excel, you can use the side panel instead.
**Submit:** an `analysis_pack/` folder in your homework repository (`genai-homeworks/L08/`).

---

## The situation

You work at the Northstar online shop. Anna, the Commercial Director, writes:
**“Hi! How did sales go this year? Why did advertising pay off worse in the second half? And why so many returns in the autumn? I need one page by Friday.”**

The file has two sheets:
* `Sales`: 1261 rows. Columns: date, channel, category, region, warehouse, orders, revenue, ad spend, returns. One row is one day of sales for one “channel × category × region × warehouse” combination. It is not a single order.
* `Reviews`: 357 reviews with date, warehouse, a 1–5 rating and text.

The data has a couple of errors. Find them in the first step and write down what you did with them.

## Three questions for the report

You can pick your own three from the five questions the model suggests. If you are not sure, take these:

1. How did revenue change month by month? How much higher is December than January, and than November?
2. How much revenue does $1 of advertising bring in Search and in Social, month by month? What changed from July?
3. Where is the return rate above normal in September–December? What do reviews say about that warehouse?

## Steps

Do everything in one chat, so the model remembers the file and earlier answers. Free plans limit uploads per day, so upload the file once.

1. **Ask the model to describe the file.** Upload `northstar_2025_EN.xlsx` and send the lesson’s first prompt:
   ```
   Describe this file: what one row is, how many rows, what period, what data problems.
   Suggest 5 questions a manager would ask. Don’t change anything yet.
   ```
   Check the row count and the period against the file. If the model calls zeros “missing values”, ask again: Email and Organic buy no advertising, so a zero in `ad_spend` is normal for them. The model can also miss an error. In the lesson it missed one of them, so read the answer yourself and ask again if something doesn’t add up.
2. **Build the Excel workbook.** Ask the model to add a sheet with a formula (for example, revenue per $1 of ads = revenue / spend), a month × channel pivot and a chart. Ask it to use Excel formulas. Download the `.xlsx`, open it in Excel and click a result cell. The `fx` bar should show a formula, not a number.
3. **Build 3 charts**, one per question. The chart title is a finding with a number. Rework one chart for a slide. The prompt from the lesson:
   ```
   Rework this chart for a slide: the title states the finding, bars sorted, value labels on the bars,
   no legend and no gridlines, one accent colour for [what to highlight], everything else grey. Explain in 3 points what you changed.
   ```
   Keep both versions: before and after. After the rework, compare two numbers on the chart with the previous version. In the lesson the model re-sorted the review themes during the rework, and 49 % became 46 %.
4. **Build the report page** from `report_template.md`: question, 3 charts, 3 findings, 1 point on “what this data does not prove”. Ask for a Word or PDF file. Download it and open it. The chat preview may show someone else’s picture: in the lesson ChatGPT previewed a stock report with “Series A/B/C”, while the downloaded file was correct.
5. **Ask for a recipe.** You need the prompt plus a short Python script that builds the same charts from next month’s file `northstar_sales_2026-01.csv`. You do not have to run Python yourself: upload the script and the January file to the chat and ask it to run them. The January file has sales only, no reviews. So the script cannot rebuild the reviews chart. Say so in the recipe. If the script did not work, write where it broke.
6. **Run the 60-second check** with `checks_template.md`: compare row counts before and after cleaning, check one chart point against the source file and the previous version, name what each percentage is calculated from.

## What to submit

```
analysis_pack/
  analysis.xlsx       # a sheet with a formula written by AI; month × channel pivot; a chart
  charts/
    01_revenue.png    # chart 1
    02_before.png     # chart 2 before the rework
    02_after.png      # the same chart after the rework
    03_returns.png    # chart 3
  report.docx         # or report.pdf: one page, from the template
  recipe.md           # prompt + script (or recipe.py next to it); or a note on why it did not work
  checks.md           # 60-second check + one plausible claim the data does not prove
```

PNG names can differ. You need three charts plus a before/after pair for one of them.

### What each file must contain

* **analysis.xlsx.** The formula sits in a cell and shows in the `fx` bar. The month × channel summary is a real Excel PivotTable or built with `SUMIFS` formulas. A table of typed-in numbers with no formulas does not count. The chart lives in the same workbook.
* **charts/.** Each chart answers one question. Period and units are labelled. The before/after pair shows what changed.
* **report.** One page. Every finding has a number, a period and a base: “December +15.1 % vs November”. A bare “growth” is not enough.
* **recipe.** The full prompt text and the script. If the recipe did not rebuild all three charts, say which one and why.
* **checks.md.** The filled-in template and one claim that sounds plausible but the data does not support. For example: “If we cut the Social budget, revenue won’t drop.” Write how you would test it: for example, a test in some regions.

## Option B: your own work data

You may use your own table instead of Northstar if you are allowed to use it and it has no names, phone numbers, emails or other personal data. Check it against the traffic light from slide 29:

| Colour | What data | What is allowed |
|---|---|---|
| Green | practice and fictional, like Northstar | any service |
| Yellow | work data, no personal data, use is permitted | only in a work account your company approved |
| Red | personal: customers, staff, salaries, health | not without approval; only in an environment your company approved |

The pack and the rubric stay the same. Add one line to `checks.md`: where the data comes from and who allowed you to use it. In doubt — use Northstar.

## Bonus question (optional)

**“Where does the data live in your job, and what is the system’s official export?”** Answer in 3–5 lines at the end of `checks.md`: the system (CRM, ERP, BI, Jira…), the button or report that exports it, the file format, whether there is an official API. No points for the bonus, but it will be useful in Lesson 09.

## Rubric (0 — missing, 1 — partial, 2 — strong)

| Criterion | 2 points means |
|---|---|
| File description | you state what one row is, how many rows and the period; you found the duplicate and the text date; you wrote what you did with them |
| Formula and pivot | in `analysis.xlsx` the formula shows in the `fx` bar; the month × channel pivot matches the total; the chart is in the workbook |
| Charts | three charts, each answers its own question; the title is a finding with a number; the before/after pair shows the changes |
| Report | one page from the template; every finding has a number, a period and a base; there is a “what the data does not prove” point |
| Recipe | the prompt and script rebuild the charts on the January file, or a clear note says what failed and why |
| Check | rows before/after, one point against the source and the previous version, “percent of what”; a plausible claim and a way to test it |

Maximum 12 points. Pass from 8.

## Don’t

* Don’t upload customer, staff or company financial data to a chat without permission. The red zone — only with approval and in an approved environment; for this homework — never.
* Don’t submit a chat screenshot instead of the files.
* Don’t trust the report preview in the chat. Open the downloaded file.
* Don’t write generic lines like “AI transforms business”. Every finding has a number.
