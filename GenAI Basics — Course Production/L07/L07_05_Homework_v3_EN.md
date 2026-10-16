# Lesson 07 (v3) • Homework: The Courier Team's Week with Copilot

**Course:** GenAI Basics • Lesson 07 • Module 3: AI assistants at work  
**Submission:** folder `genai-homeworks/L07/` in your personal GitHub repository: one document with screenshots (see “Submission Checklist”)  
**Reviewer:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)  
**Code:** none. You need to check a Copilot answer against its source.  
**Tools:** free Copilot only: a **personal** Microsoft account or the **IT Park school account** (Copilot Chat). No credit card, no paid subscription, no work licence.  
**Matches:** slide 23 (homework) of `presentation_L07_Copilot_Ecosystem_EN_v3.html`, plus slides 8 (demo A), 12 (orders table), 2 (the Microsoft family map), 3 (new words), 20 (safety rules) and 16–17 (your own agent, bonus). Service facts as of 2026-10-13.

---

## Goals

1. Do three things from the lesson in free Copilot: a brief from notes, a conclusion from a table, a creative result.
2. Each time, **check the answer against the source**: what came from the file, what Copilot added itself, whether the numbers are right.
3. Draw **your own map**: which Copilot fits your tasks, what it sees and whether it is free.

Grading is based on six checks. An honestly found Copilot mistake is worth more than a polished answer nobody checked.

**Bonus (optional):** step 5, build your own agent in Agent Builder with the school account. The six-check rubric **does not change**: the bonus is not needed for full marks and is noted separately.

---

## Privacy: read before you start

- **Synthetic data only.** Use the files from `demo_courier_copilot/` (the courier team Anna, Pavel, Ola are characters, not people). No real customers, grades, mail, chats, passwords or keys: not in prompts, not in screenshots.
- **Blur names and e-mails in screenshots.** The Copilot app shows your avatar and e-mail at the bottom left and chat titles in the left panel. Blur or paint over them before you hand in (for example in Paint or the Snipping Tool).
- In step 4 (your map) describe tasks **in words**, without real documents or colleagues' names.
- If you pasted something personal or a secret by accident: delete the chat, change the key.

---

## What to do (4 steps + bonus step 5)

| Step | Task | Result in the document |
|---|---|---|
| **1 Brief** | Paste `meeting_notes.md` into Copilot with the demo A prompt: “Using only these notes, write a one-page brief: decisions, open questions, who does what. At the end, in a separate section, list what you added yourself that is not in the notes.” Compare the brief with the notes. | a screenshot of the brief; the “what Copilot added” list (in its words and from your check); **one invention or mistake you found** (or honestly: “none found, I checked lines …”) |
| **2 Table** | Paste `orders.csv` **as text** into the chat. Ask the slide 13 question **together with the rule** (prompt below). Work out the answer by hand from the file and compare. | a screenshot of Copilot's answer; your hand count (order numbers); whether it matched and where the mistake is |
| **3 Creative** | From the step 1 brief: text for **3 slides** for management **or** a launch picture of the feature (personal account). | the 3-slide text or the picture; one line on what you checked (the $75 figure, the words in the picture) |
| **4 Your map** | 5 tasks from your study or work. For each: which Copilot (or other Microsoft product from slide 2), what it **sees** while doing it, whether it is free. | a 5-row table (template below) |
| **5 Bonus: your own agent** *(optional)* | IT Park school account → the Copilot app → **Agents → New agent**. Describe the agent in words (role, rules, format, what not to do), as we did on slides 18–19. Check the draft in **Configure**, ask two questions in **Preview**: one tricky question covered by a rule, and one with missing data. Click **Create**: the agent stays **private**. | a screenshot of the agent's instructions; a screenshot of Preview with the two questions and answers; one line: did the agent follow the rule, and did it ask back when data was missing |

**Prompt for step 2:**
```text
Here are the courier app orders (CSV). Delivery rules: Prime subscribers get free delivery from $75 only in the CITY zone. From $100 delivery is free for everyone in any zone. Everyone else pays as before. Which zone has the most Prime orders from $75, and how many of them are free now? List the order numbers.
```
Then paste the whole content of `orders.csv` below the prompt.

**Step 5 (bonus): what to know.**
- You need the **IT Park school account** (free Copilot Chat). Agent Builder is not officially confirmed for personal Microsoft accounts. Agent Builder is not on the phone: use the Copilot app on a PC or the browser.
- If there is no **New agent** button, IT switched it off; skip the bonus, it does not affect your grade.
- **Field limits:** name up to **30 characters**, description up to **1,000**, instructions up to **8,000** characters.
- **Knowledge on free Copilot Chat:** instructions, the web and **up to 4 public sites**. **You cannot upload a file or connect SharePoint** (the organisation needs pay-as-you-go billing); mail and Teams need a licence. So write the rules **straight into the instructions**.
- Skills (code, Word / Excel / PowerPoint files, images) are on by default.
- **Do not share the agent** with the organisation (Share → Org-wide sharing). Synthetic data only.
- Ideas: a support helper for the delivery rules (like ours), a course tutor, a rubric checker, a RU ↔ EN ↔ UZ translator, a post writer, an FAQ on study rules.

**Tip (not graded):** the Agent Store in Copilot Chat has **Prompt Coach**: ask it to improve your step 1 prompt and compare the answers.

---

## Tools (as of 2026-10-13, free only)

| Step | Free tool | Notes |
|---|---|---|
| 1, 2 | **Copilot Chat** on the IT Park school account (green shield in the chat) or personal Copilot | No Microsoft 365 Copilot licence needed: you paste the text yourself |
| 3 | Personal Copilot: images and the editor (erase, background, crop) | The free tier has an image limit. Used up? Choose the “3 slides” option |
| 4 | The slide 2 map and the cheatsheet | Badges: free / work licence / preview / US only / Copilot+ PC |
| 5 (bonus) | **Agent Builder** on the IT Park school account (Agents → New agent) | Knowledge from the instructions and the web only (up to 4 sites); no file upload |
| Screenshots | Snipping Tool (Win+Shift+S), Paint for blurring | |

**Not needed for this homework:** licensed Copilot in Word, Excel, Teams, Microsoft 365 Premium, credit-billed agents, GitHub.

---

## Directory Structure for Submission

```
genai-homeworks/
└── L07/
    ├── L07_copilot_week.md      # one document: 4 steps (+ bonus) + the six-check table
    └── img/
        ├── 1_brief.png          # the brief and the "what I added" section
        ├── 2_orders.png         # Copilot's answer on the orders
        ├── 3_creative.png       # the 3-slide text or the picture
        ├── 5_agent_instructions.png  # bonus: the agent's instructions
        ├── 5_agent_preview.png       # bonus: two questions in Preview
        └── ...                  # optional; names and e-mails blurred
```
You may hand in the document as `.docx` or `.pdf` instead of `.md`: what matters is one file with the screenshots inside.

---

## Template: `L07_copilot_week.md`

```markdown
# L07 • The courier team's week with Copilot

**Student:** [name / alias]  **Account:** [personal Copilot / IT Park school Copilot Chat]

## 1. Brief
![brief](img/1_brief.png)
**Source:** demo_courier_copilot/meeting_notes.md
**What Copilot added (in its words):** ...
**What I found when checking:** [brief line]: not in the notes / the notes say otherwise: ...

## 2. Orders table
![orders](img/2_orders.png)
**Copilot's answer:** ...
**My hand count:** CITY: [numbers] • OUTSIDE free: [numbers]
**Matched?** yes / no, the mistake is in ...

## 3. Creative
[3-slide text or the picture]
**What I checked:** ...

## 4. My map
| # | Task | Which Copilot | What it sees | Free? |
|---|---|---|---|---|
| 1 | Summary of a lecture from my notes | Copilot Chat (school) | only the text I pasted | yes |
| 2 | ... | | | |

## 5. Bonus: my agent (optional)
![agent](img/5_agent_instructions.png)
![preview](img/5_agent_preview.png)
**Agent name and role:** ...
**Question covered by a rule → answer:** ... (right / wrong)
**Question with missing data → did it ask back?** yes / no

## Six checks
| # | Check | ✓ / ✗ | Where to see it |
|---|---|:-:|---|
| 1 | Source named | | |
| 2 | Inventions marked | | |
| 3 | Numbers checked by hand | | |
| 4 | Real screenshots | | |
| 5 | The map names the product and what it sees | | |
| 6 | No names, e-mails, secrets | | |
```

---

## Grading Criteria (the 6 checks of slide 23)

| # | Check | Passes if |
|---|---|---|
| 1 | **Source named** | the brief and the table answer name the source file; step 3 shows the text or picture was made from the brief |
| 2 | **Inventions marked** | there is a “what Copilot added” list and at least one invention or mistake found, or an honest note of which lines were checked with nothing found |
| 3 | **Numbers checked by hand** | step 2 has your hand count with order numbers and a verdict on whether Copilot's answer matched |
| 4 | **Real screenshots** | screenshots from your own Copilot (not from the slides or others' work); your prompt and the answer are visible |
| 5 | **The map names the product and what it sees** | each of the 5 rows names a specific product (not just “Copilot”), what it sees, and whether it is free |
| 6 | **No names, e-mails, secrets** | avatar, e-mail and unrelated chat titles are blurred in screenshots; no real data or keys |

Completeness (required, not graded separately): all 4 steps present, one document, synthetic data.

**The bonus (step 5) does not change the rubric.** The six checks and completeness count steps 1–4 only. The bonus is noted separately (“+ bonus”) when both screenshots (instructions and Preview with two questions) and the one-line verdict are there. Check 6 applies to the bonus too: no names, e-mails or real data in the screenshots.

---

## Submission Checklist

1. [ ] Branch `feature/L07-copilot-homework` created and submitted via Pull Request to `main`.
2. [ ] `genai-homeworks/L07/` holds one document with all 4 steps and the `img/` folder.
3. [ ] Step 1 has the “what Copilot added” list and an invention or mistake you found.
4. [ ] Step 2 has Copilot's answer **and** your hand count with order numbers.
5. [ ] Step 4 has a 5-row table: product, what it sees, whether it is free.
6. [ ] The six-check table is filled in.
6a. [ ] *(Optional)* Bonus: two agent screenshots (instructions and Preview) and the one-line verdict; the agent is not shared with the whole organisation.
7. [ ] Names, e-mails, avatars and unrelated chats are blurred in screenshots; no real data.
8. [ ] Reviewer `ihar_rubanovich@epam.com` invited as repository collaborator.

---

## Instructor only: answer key for steps 1, 2 and the bonus

> **Do not publish to students.** Remove this section from the copy that goes to the group.

### Step 2: correct answer (from `demo_courier_copilot/orders.csv`, 12 orders)

| Order | Zone | Prime | Subtotal | Free? | Why |
|---|---|---|---|---|---|
| 1001 | CITY | yes | $82.40 | **yes** | Prime, city, from $75 |
| 1004 | CITY | yes | $75.00 | **yes** | Prime, city, exactly at the threshold |
| 1006 | CITY | yes | $120.00 | **yes** | Prime, city (and from $100) |
| 1009 | CITY | yes | $99.99 | **yes** | Prime, city, from $75 |
| 1007 | CITY | yes | $64.90 | no | below $75 |
| 1012 | CITY | yes | $74.99 | no | 1 cent below $75 |
| 1003 | OUTSIDE | yes | $91.10 | no | the Prime rule does not apply outside the zone |
| 1008 | OUTSIDE | yes | $79.50 | no | the Prime rule does not apply outside the zone |
| 1011 | OUTSIDE | yes | $130.00 | **yes** | the general “from $100 for all” rule |

- **Answer:** the most Prime orders from $75 are in **CITY**: 4 (1001, 1004, 1006, 1009), all free. Outside the zone there are 3 Prime orders from $75 (1003, 1008, 1011), but **only 1011** is free.
- For reference (not asked): 1010 (CITY, not Prime, $105) is also free, under the “from $100” rule.
- **Typical Copilot mistake:** “3 free outside the zone”. That is what free Copilot Chat answered in our 13 Oct 2026 run when the rule was not in the prompt, twice in a row. With the rule in the prompt the answer should be right; if a student still got a mistake with the rule and **found it**, check 3 passes in full.

### Step 1: what the notes contain (for comparison)
Decisions: Prime is free from $75 in the city only; free from $100 for everyone stays; outside the zone unchanged; release behind a flag first, Ola wants a short explanation for support before the release. Open questions: who owns the flag rollout; which number shows early that delivery costs went up unexpectedly. Action items: Pavel, the rule and tests; Anna, the brief and the issue; Ola, the support reply after the staging check.  
Anything not on this list (deadlines, an “expected effect”, percentages, new names, an assigned flag owner) was added by Copilot and must be marked. “Nothing added” is not a mistake in itself, but the student must check it rather than take it on trust.

### Bonus (step 5): what to look for
Reference: our run of 13 Oct 2026 (slides 18–19, `L07_04_Live_Demo_Runbook_v3_EN.md`, section 8): the “Courier support helper” agent with the rules in its instructions (Prime free from $75 only in CITY; free from $100 for everyone; city $7.50, outside $18.00). “Prime, $80, outside the city” → **$18.00** with the calculation; “how much is delivery for $70?” → the agent **asked back** for the zone and Prime.
Count the bonus if: the instructions hold a role and rules (not a single sentence); Preview has one question checkable against a rule and one with missing data; the student judged both answers. If the agent answered wrongly and the student **noticed**, the bonus counts. No New agent button (switched off by IT): no penalty.
