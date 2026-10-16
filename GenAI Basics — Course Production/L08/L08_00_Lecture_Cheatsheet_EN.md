# One-page speaker cheatsheet • Lesson 08 (18 slides • 90 minutes)
*Speaker: Ihar Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*
*Topic: AI for Data Analysis — chat with a spreadsheet • facts as of 2026-10-13*
*Deck: `presentation_L08_AI_for_Data_Analysis_EN.html` (PDF alongside) • full text: `L08_02_Instructor_Script_90MIN_EN.md` • demo: `L08_04_Live_Demo_Runbook_READY_EN.md`*
*Homework: `L08_05_Homework_EN.md` • Repository: `genai-homeworks/L08/`*

---

### Before you start
* Teams: share the **browser window** with the deck; a second window has the chat assistant in your work account, zoom 125–150 %.
* `northstar_sales_messy.csv` on the desktop. Run `python demo_assets/reference_analysis.py` once → total **$256,045**.
* Deck: `F` fullscreen, `←/→`, `N` notes, `G` grid. No animations, no video.

### Part 1 (00:00 — 41:00)
* **01 Cover (2):** the model writes code, a sandbox calculates, you check. Practice file: Northstar.
* **02 Hook (5):** experiment on 13 Oct 2026: Haiku 5.5 and Sonnet 5.5 with no tools got the total **right** ($256,045). But: 66 returns → “probably 6” (source says **4**); “I checked” with no code; 100,000 rows won’t fit in a message. Question to the chat.
* **03 How it works (6):** you → model (writes code) ⇄ sandbox (calculates) → files. **Open the code.**
* **04 Where (6):** chat (ChatGPT ~50 MB; Claude all plans, 30 MB; Gemini 100 MB) • spreadsheet (Copilot “Edit with Copilot” + Python; ChatGPT/Claude for Excel; Gemini panel in Sheets, =AI() text only) • notebook (Colab, Jupyter) • API. =COPILOT() retired 14 Sep 2026.
* **05 Passport (5):** row, key, period, units, impossible values. **Row ≠ order ≠ customer.**
* **06 Profile (5):** 73 rows / 72 keys / 4 problems: 1010 empty region • 1028 duplicate (+$3,312) • 1041 `2026/04/22` • 1055 returns 66 > orders 62.
* **07 Cleaning (6):** mechanics (duplicate, UNKNOWN, date format) — fix and log; meaning (1055) — flag and ask the source. Source date for 1041 is 13 Apr: even a “safe” fix is an assumption.
* **08 Prompt (6):** question • profile first • cleaning rules • calculation with code • reconciliation • what to return (+ “what the data doesn’t prove”).

### Break (41:00 — 46:00) • slide 09, “Start”

### Part 2 (46:00 — 90:00)
* **10 Demo (10):** 4 prompts: profile → fixes A/B → calculation + chart + reconciliation → “which channel gets more budget in July?”. Audience posts: a fix / a problem left / a check. >90 s — fallback.
* **11 Result (5):** months $32.7k → $53.9k (**+64.7%**). Most revenue: **Organic $67,580**; fastest growth: **Search +99%** — from the lowest base.
* **12 Charts (4):** trend — line; comparison — bars from zero; distribution — histogram; relationship — scatter (≠ cause); shares — 100% bars.
* **13 Checking (6):** three paths to $256,045; rows 73 → 72; spot check **1063 = Search, June, $5,425**; base of a %; chart = table. DABstep 2025: best agent solved 14.55% of hard tasks.
* **14 Limit of a claim (6):** revenue per $1 of ads: Search **5.52**, Social **3.84**. Season, targeting, brand, attribution affect both. Answer — **a test**.
* **15 Code (3):** pandas — reference only; spot decisions, don’t write.
* **16 Privacy (4):** green — practice data; amber — work account; red — personal data only in an approved environment. Settings: ChatGPT “Improve the model…”, Gemini “Keep Activity”, Claude — only if you allowed it.
* **17 Homework (4):** 5-file pack, “driver / checker” pairs, a required “the data does not prove this”.
* **18 Summary (2):** 5 rules. L09 teaser: Claude and artifacts.

### Analyst prompt (copy)
```
Question: how did revenue change from January to June, and which channel grew fastest?
First describe the data: what one row is, how many rows and unique order_ids, gaps, odd values.
Mechanical fixes — do them and log them. If a fix changes the meaning — don't, ask me.
Calculate revenue by month and by channel, show the code.
Reconcile: sum by month = sum by channel = grand total.
Return: a table, one chart, the cleaning log and one thing this data does not prove.
```
