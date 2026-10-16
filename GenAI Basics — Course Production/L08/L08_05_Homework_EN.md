# Lesson 08 • Homework: a verified analysis pack

**Course:** GenAI Basics • Lesson 08 “AI for Data Analysis” • Module 3: AI assistants at work
**File:** `demo_assets/student_starter/northstar_sales_messy.csv` (practice, fictional data — fine to upload to any service)
**Tools:** any chat assistant that analyses files (ChatGPT, Claude, Gemini), or Copilot/ChatGPT/Claude in Excel, or Colab. You do not need to write code yourself.
**Submit:** a `verified_analysis_pack/` folder in your homework repository (`genai-homeworks/L08/`).

---

## The situation

You are an analyst at the Northstar online shop. Management asks:
**“What changed in sales from January to June, and what should we check next?”**

You have a 73-row export. It contains errors — find them yourself. Your job is not “a nice answer from the chat” but a small evidence pack another person can check in 5 minutes.

## In class (pairs, 20–25 minutes)

* One person drives the AI chat; the other checks: opens the code, compares numbers, asks “where does this come from?”.
* Swap roles halfway.
* Start with the profile prompt from slide 6, then use the analyst prompt from slide 8 (it is in the cheatsheet `L08_00_Lecture_Cheatsheet_EN.md`).

## What to submit (5 files)

```
verified_analysis_pack/
  cleaning_log.md     # rows before/after, every fix: what, where, why, how the total moved
  analysis_brief.md   # 3–5 claims; each with metric, period and base
  chart.png           # one chart = one claim; axes, units and period labelled
  cleaned_data.csv    # or a script that does the cleaning
  verification.md     # at least 3 checks + 1 statement you refused to make
```

Templates `analysis_brief_template.md` and `verification_template.md` are in `demo_assets/student_starter/`.

## Questions to answer

1. How did monthly revenue change from January to June?
2. Which channel brought the most revenue over six months? Which grew fastest? (These are different questions.)
3. For paid channels (Search, Social): how much revenue per $1 of advertising? Label it as a description of the past.
4. Which data problem would have changed the headline number if nobody had noticed it?
5. What can you **not** say about next month’s budget from this data alone?

## Required

* **Do not silently fix impossible values.** If a value cannot be recovered from the file, keep the row, flag it in the log and say who must confirm it.
* **At least three checks**, each a different way: row counts before/after; total by month = total by channel; one row found by eye in the source file; the chart matches the table.
* **One refusal:** a statement that sounds plausible but is not supported by the data. For example: “If we double the Search budget, revenue will grow.” Explain what data you would need to test it (e.g. a test in some regions).

## Rubric (0 — missing, 1 — partial, 2 — strong)

| Criterion | 2 points means |
|---|---|
| Data passport | you state what one row is, the key, the period, the units |
| Cleaning | every fix is logged; the impossible value is flagged, not “fixed” |
| Calculation | numbers are repeatable (code shown or script attached), totals reconcile |
| Chart | one chart answers one named question; axes and units labelled |
| Checks | 3+ independent checks, one of them manual |
| Limit of the claim | a specific refusal + what it would take to test it |

Maximum 12 points. Pass from 8.

## Stretch (optional)

After peer review, improve the pack and write `stakeholder_note.md` (150–250 words) for a manager, separating: what is verified; which assumptions were made; which data problems are unresolved; what to analyse next.

## Don’t

* Don’t upload real customer, staff or company financial data to a chat — only the practice file.
* Don’t submit a chat screenshot instead of the pack.
* Don’t write generic lines like “AI transforms business”.
