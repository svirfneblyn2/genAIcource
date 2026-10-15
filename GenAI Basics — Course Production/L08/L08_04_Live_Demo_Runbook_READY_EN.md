# Lesson 08 • Live demo runbook: from a messy CSV to a checked answer

**Slide:** 10 (after the break) • **Time:** 10 minutes • **Fallback:** 3 minutes
**File:** `demo_assets/northstar_sales_messy.csv` (73 rows, fictional data)
**Service:** any of ChatGPT (data analysis), Claude (code execution and file creation), Gemini — whichever your work account has.
**Reference:** `demo_assets/reference_analysis.py` → `demo_assets/local_outputs/`

---

## 10 minutes before class

1. Open the chat assistant in your **work** account and start a new chat. Check that file upload works (ChatGPT Free allows 3 uploads a day).
2. Put `northstar_sales_messy.csv` on the desktop.
3. In a terminal: `cd demo_assets && python reference_analysis.py` — 4 files should appear in `local_outputs/` plus the line `Total revenue (deduplicated) = $256,045.00`.
4. Keep `fallback_outputs/` (ready charts) and this runbook open.
5. **Teams:** share the browser window, not the whole screen. Page zoom 125–150 % so tables are readable.

## Expected result (reference)

| Check | Value |
|---|---|
| Rows in file / unique `order_id` | 73 / 72 |
| Duplicate | `1028` (Social, Books, 2026-03-04, $3,312) |
| Empty region | `1010` |
| Different date format | `1041`: `2026/04/22` (truth file: 2026-04-13) |
| Impossible value | `1055`: returns 66 > orders 62 (truth file: 4) |
| Revenue as in file / without the duplicate | $259,357 / **$256,045** |
| By month, $ | Jan 32,697 • Feb 36,596 • Mar 39,843 • Apr 44,106 • May 48,936 • Jun 53,867 (+64.7 %) |
| By channel, $ | Organic 67,580 • Email 66,261 • Social 63,009 • Search 59,195 |
| Growth January → June | Search +98.8 % • Email +64.5 % • Organic +55.5 % • Social +48.2 % |
| Revenue per $1 of ads | Search 5.52 • Social 3.84 • Email and Organic — no ad spend, not computed |

## Step 1 — profile (2 min)

Upload the file. Prompt:

```
Describe this file: what one row is, how many rows and unique order_ids,
where there are gaps, odd formats and impossible values. Do not fix anything yet.
```

**Show:** open the code (ChatGPT — the button next to the answer; Claude — the analysis block; Gemini — “show code”).
**Look for:** 73 / 72, four problems. If the model already “cleaned” something, ask it to undo and only describe first.

## Step 2 — fixes (2 min)

```
Split the problems into two groups:
A) mechanical fixes that do not change what the data means;
B) fixes that change the meaning. What do you suggest for each? Don't change anything yet.
```

**Look for:** duplicate, empty region, date — group A; row 1055 — group B, “keep and flag”.
**If the model suggests replacing 66 with 6:** don’t hide it — it is the best moment of the lesson. Ask “How do you know the correct value?” and show `northstar_sales_truth.csv`: it says 4.

## Step 3 — calculation and chart (3 min)

```
Apply the group A fixes and log them. Keep row 1055 as is and flag it.
Calculate revenue by month and by channel. Draw one line chart of revenue by month.
Reconcile: sum by month = sum by channel = grand total. Show the code.
```

**Look for:** total $256,045, the line rises from 32.7k to 53.9k, the reconciliation is printed.
**Spot check out loud:** find row 1063 in the CSV — Search, June, $5,425.

## Step 4 — the trap (2 min)

```
Which channel should get more budget in July?
```

**Good answer:** “This data cannot show that moving budget will increase revenue; it describes the past; you need a test.”
**If the model confidently recommends Search:** ask “What assumption are you making?” and go to slide 14.

## Audience task (in parallel)

In the Teams chat: one fix the model made; one problem it left alone; one check of the totals. Read 2–3 answers aloud on slide 11.

## If something goes wrong

| Problem | What to do |
|---|---|
| The service thinks for more than 90 seconds | Switch to the fallback, don’t wait |
| The analysis / code button looks different | Don’t hunt for it out loud: “the UI changes, the principle doesn’t” |
| The model silently fixed 1055 | Ask it to undo and explain — that is the lesson |
| The chart looks odd | Check the table first, then the chart; show `fallback_outputs/monthly_revenue.png` |
| Upload limit / sign-in error | Fallback |
| Someone wants to upload their own data | No: practice file only (slide 16) |

## Fallback (3 min)

```bash
cd demo_assets
python reference_analysis.py
```

Open `local_outputs/analysis_summary.txt`, `monthly_revenue.csv`, `channel_metrics.csv` and `fallback_outputs/*.png`.
Say: “Same analysis, except we ran the code ourselves instead of a cloud sandbox. The checking rules are the same.”
