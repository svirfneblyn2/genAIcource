# Lesson 07 • Live Demo Runbook
## Three Demos: Brief, Code, Windows. Exact Prompts, Expected Output, Fallback

**Course:** GenAI Basics • Lesson 07 of 16  
**Instructor:** Ihar Rubanovich (EPAM Systems • `ihar_rubanovich@epam.com`)  
**Tools (October 2026):** Copilot in Word or free Copilot Chat (Edge, web, Windows app) • VS Code + the GitHub Copilot extension (Free plan) • Notepad + Copilot in Windows.  
**Data:** synthetic only, from `demo_courier_copilot/`. No real mail, chats, files or customers.  
**Total:** 14 minutes inside slides 6, 10–11 and 17. The other slides run without a demo.

> **Mapping to the deck (21 slides):** demo A → slides 5–6 • demo B → slides 9–13 • demo C → slides 16–17.  
> **Main rule:** look at the **diff and the tests**, not at the word “done”. Copilot answers differently every time; your result does not have to match the expected one word for word, it has to pass the checks.

---

## 1. Before Class

### One day before
- [ ] Accounts: a demo **GitHub** account (the Free plan is enough); a **Microsoft** account for Copilot Chat (personal or Microsoft 365 work). A Copilot licence for Word is not required: the free chat is the fallback.
- [ ] **VS Code** installed, the **GitHub Copilot** extension (and Copilot Chat) installed, and you are **signed in** with the demo account. Open the Copilot chat panel and ask anything: an answer arrives.
- [ ] **Training on your data is off** for a personal GitHub account: Settings → Copilot → “Allow GitHub to use my data for AI model training” = **Disabled**. Work accounts (Business, Enterprise) are not used for training, but check which account you are signed in with.
- [ ] **Repo cloned** (see “Repo setup for demo B” below), and `python smoke_check.py` prints `BASELINE TESTS PASS` (4 tests).
- [ ] On the demo PC check: the Copilot key (or `Win+C`), the Copilot app, Vision, file search. What is missing is missing: the fallback is described in demo C.
- [ ] `meeting_notes.md` and `release_checklist.txt` open; Notepad is ready on screen.
- [ ] Python 3 is installed and the terminal opens in the repo folder.
- [ ] Read `demo_courier_copilot/surface_preflight.md` (10 minutes before class).

### 10 minutes before class (Teams)
- [ ] Share your **whole screen**, not one window. Close mail, messengers, notifications.
- [ ] Large font in VS Code and the terminal (Ctrl `+`) so it reads in Teams.
- [ ] Tabs already open: Edge with Copilot Chat, VS Code with the repo folder, Notepad with `release_checklist.txt`, slides 6, 11, 17 (fallback results).
- [ ] `fallback_outputs/` at hand (three files).

### Repo setup for demo B
```bash
cp -r demo_courier_copilot/sample_repo ~/courier-app-demo
cd ~/courier-app-demo
mv expected_solution ../expected_solution_L07     # hide the ready solution
git init && git add -A && git commit -m "base"    # no commit, no git diff
python smoke_check.py                              # FIXTURES OK ... BASELINE TESTS PASS
```
The ready solution lives elsewhere; you need it only to compare Copilot’s diff with the real one (slide 11).

---

## 2. The 90-Second Rule

If a button is missing, the interface is different or Copilot is silent: **do not fix it in front of the class**.
1. Say: **“The button moved, the rule did not.”**
2. At most **90 seconds** of searching. Time it.
3. Show the ready result: a slide (6, 11 or 17) or a file from `fallback_outputs/`.
4. Say aloud that it is a prepared result, not AI output.
5. Move on; debug after class.

The universal fallback for any Copilot: **paste the text into free chat**.

---

## 3. Demo A. A Brief from Notes (slide 6, 3 minutes)

**Goal:** show the move “give the source, ask for a structure, demand a mark on what was invented”.  
**Where:** Copilot in Word, or free Copilot Chat in Edge with the text of `meeting_notes.md` pasted in.  
**Input:** `demo_courier_copilot/meeting_notes.md` (meeting “Prime delivery rule”, 5 October 2026, Anna, Pavel, Ola).

**Prompt (paste the whole notes before it or attach the file):**
```text
Using only these notes, write a one-page brief: decisions, open questions, owners. At the end list which sentences are yours.
```

**Expected result** (a guide, `fallback_outputs/brief_expected.md`; Copilot’s words will differ):
> Approved change: Prime subscribers get free delivery from a $75 order inside the city zone. Free delivery from $100 stays for everyone. Deliveries outside the zone do not change. Pavel builds it behind a feature flag in staging, Ola updates the support reply, and the team watches the delivery-cost number for 24 hours after the release. Who owns the flag rollout is still open.

**What to check with the class (4 points):**
1. **$75 for Prime**, and **in the city only**.
2. **$100 for everyone stays.**
3. **Outside the zone nothing changes.**
4. **The flag owner is still open** (an open question stayed open).
Then read the list “which sentences are mine”. Such lines (for example “expected effect: more repeat orders”, as on slide 6) are **not in the notes**: delete or verify. This is check 1 of slide 18.

**Fallback:**
- No Copilot in Word: free Copilot Chat, paste the notes.
- No access at all: show `fallback_outputs/brief_expected.md` and slide 6. Say it is prepared text, not AI.

---

## 4. Demo B. Code in VS Code (slides 10–11, 8 minutes)

**Goal:** see exactly what Copilot changed and verify it with tests.  
**Where:** VS Code + GitHub Copilot Free, folder `~/courier-app-demo`.  
**Input:** `ISSUE.md` (issue #12), `.github/copilot-instructions.md` (5 rules), `delivery_fee.py`, `test_delivery_fee.py` (4 tests).

### Step 1. Plan (≈2 minutes)
Open the Copilot chat. Attach `ISSUE.md` and `.github/copilot-instructions.md` (or keep them open). Prompt 1:
```text
Read ISSUE.md and .github/copilot-instructions.md, propose a plan, do not edit.
```
**Expected:** a plan of a few points, no files change. Roughly as on slide 10: 1) a Prime branch for the city from 75, 2) leave the $100 rule, 3) three tests.  
**Check:** it mentions the $75 threshold, **city only**, the $100 rule, the 75 and 74.99 boundaries, a non-Prime test. If Copilot started editing files, undo and repeat the prompt.

### Step 2. Implement (≈3 minutes)
Prompt 2 (agent mode if available; mode names change, look for “Agent”):
```text
Implement it, add boundary tests, run the tests.
```
No agent? It is plain chat: copy the code from the answer into `delivery_fee.py` and `test_delivery_fee.py` by hand and run the tests yourself.

### Step 3. Check (≈3 minutes, the main part)
In the VS Code terminal:
```bash
git diff
python -m unittest -v
```
**Expected result** (a real run, `deck_v2/artifacts.json`, slide 11):
```diff
--- a/delivery_fee.py
+++ b/delivery_fee.py
@@ -14,6 +14,8 @@ def delivery_fee(order: Order) -> float:
         raise ValueError("subtotal must be non-negative")
     if order.subtotal >= 100:
         return 0.0
+    if order.zone.upper() == "CITY" and order.is_prime and order.subtotal >= 75:
+        return 0.0
     if order.zone.upper() == "CITY":
         return 7.50
     return 18.00
--- a/test_delivery_fee.py
+++ b/test_delivery_fee.py
@@ -12,6 +12,15 @@ class DeliveryFeeTests(unittest.TestCase):
     def test_free_delivery_from_100(self):
         self.assertEqual(delivery_fee(Order(100, "CITY")), 0.0)
 
+    def test_prime_free_at_75(self):
+        self.assertEqual(delivery_fee(Order(75, "CITY", True)), 0.0)
+
+    def test_prime_below_75_pays(self):
+        self.assertEqual(delivery_fee(Order(74.99, "CITY", True)), 7.50)
+
+    def test_non_prime_at_75_pays(self):
+        self.assertEqual(delivery_fee(Order(75, "CITY", False)), 7.50)
+
     def test_negative_subtotal_rejected(self):
         with self.assertRaises(ValueError):
             delivery_fee(Order(-1, "CITY"))
```
```text
test_city_standard ... ok
test_free_delivery_from_100 ... ok
test_negative_subtotal_rejected ... ok
test_non_prime_at_75_pays ... ok
test_outside_standard ... ok
test_prime_below_75_pays ... ok
test_prime_free_at_75 ... ok

Ran 7 tests
OK
```
*(Copilot’s test names may differ; what matters is at least 7 tests, all `ok`.)*

**What to check with the class (checks 3 and 4 of slide 18):**
1. **The diff is small:** 2 lines of logic, no new dependencies (rule 2 of the instructions).
2. The condition is **city + Prime + from 75**, placed **after** the “from $100 for everyone” rule.
3. **Outside the zone 18.00 is untouched**, the error for a negative subtotal is still there.
4. Tests for **75, 74.99 and non-Prime**; **7 of 7 green**.
5. Compare with `../expected_solution_L07/delivery_fee.py`: Copilot’s solution may differ, but the behavior is the same.

**Fallback:**
- Copilot is silent, the limit is used up or not signed in: **slide 11** already carries the real diff and test output. Copy the solution: `cp ../expected_solution_L07/*.py .` and run `python -m unittest -v`: you get the same 7 ok.
- No agent: chat + manual paste (see step 2).
- Tests are red: show it to the class. That is the point of checking: “done” in the chat proves nothing. Ask Copilot to fix it, one attempt at most; otherwise the fallback.
- A description of a good solution: `fallback_outputs/review_expected.md` (5 points).

---

## 5. Demo C. Windows and the Checklist (slide 17, 3 minutes)

**Goal:** show that a local file becomes the context, and that Copilot sees only the window you shared (slide 16).  
**Where:** Notepad with `release_checklist.txt` + Copilot in Windows (the Copilot key or `Win+C`).  
**Input:** `demo_courier_copilot/release_checklist.txt` (6 items).

**Steps:** open the file in Notepad → press the Copilot key → turn on **Vision** and pick the Notepad window (or paste the file text into the chat) → ask.

**Prompt:**
```text
Which item catches an outside-zone fee change?
```
**Expected result** (`fallback_outputs/checklist_answer.md`):
> Item 6, “Roll back the flag if outside-zone fees change unexpectedly.”

**Check:** the answer **quotes item 6** rather than paraphrasing loosely. Ask the class: why did Copilot answer from this file? Because the file is **open and shared**.

**Fallback:**
- No Copilot key: `Win+C` or open the Copilot app.
- No Vision (device, region, Windows version): **paste the file text** into the chat.
- Work account: the app opens the web chat (normal, see slide 16); paste the text there.
- Nothing opens: `fallback_outputs/checklist_answer.md` and slide 17. “The button moved, the rule did not.”
- Copilot+ PC and Recall: one line at most: some features need such a PC, Recall is off by default, you may not have it.

---

## 6. When Something Goes Wrong

| Symptom | What to do |
|---|---|
| Copilot used a different number than the notes | Show check 2 of slide 18: numbers are checked against the source. Fix with a prompt or by hand. |
| Copilot changed the outside-zone fee | `test_outside_standard` will show it. A good example of why tests exist. |
| The agent changed more files than needed | Check 3: “the change is small”. Undo, repeat prompt 2 with “change only delivery_fee.py and the tests”. |
| The Free chat limit is used up | Switch to fallback B (slide 11) and tell the class. |
| Sign-in dropped | Do not sign in again on screen: use the fallback results. |
| A secret or someone’s data appeared in an answer | Stop; remind rule 5: no secrets or customer data in a request. Here the data is synthetic. |

## 7. Demo Wrap-Up (30 seconds)
“Three different windows, one move: we showed it the right thing, asked for a structure, and **checked against the diff, the tests and the source**.”

*Files:* `demo_courier_copilot/` (`sample_repo/`, `meeting_notes.md`, `release_checklist.txt`, `fallback_outputs/`, `surface_preflight.md`), `deck_v2/artifacts.json`. Recheck within 24 hours: the list at the end of `L07_00_Lecture_Cheatsheet_EN.md`.
