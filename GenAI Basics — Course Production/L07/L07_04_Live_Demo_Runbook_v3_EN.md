# Lesson 07 (v3) • Live Demo Runbook
## The Copilot App Briefly, Vision, Teams / Word / Excel via Screenshots + the Same Live in Copilot Chat, Optionally Your Own Agent. Exact Prompts, What to Check, Fallback

**Course:** GenAI Basics • Lesson 07 of 16  
**Instructor:** Ihar Rubanovich (EPAM Systems • `ihar_rubanovich@epam.com`)  
**Tools (as of 2026-10-13):** the **Microsoft Copilot** app with two sign-ins: the IT Park school account (**Copilot Chat (Basic)**, no licence; **the main tool for the live part**) and a personal Microsoft account • Notepad • Copilot in Windows (voice and Vision) • Agent Builder (Agents → New agent in the school account). Teams, Word and Excel with Copilot: **screenshots on slides 11–13 only**.  
**Data:** synthetic only, from `demo_courier_copilot/` (`meeting_notes.md`, `release_checklist.txt`, `orders.csv`). No real mail, chats, files or customers.  
**Total:** about 17 minutes of live demo inside the 22 minutes of slides 8, 9, 11, 12, 13 + up to 4 minutes of demo D (slide 19, optional).

> **Mapping to the deck (24 slides):** the Copilot app briefly, demo A → slide 8 (3 min) • demo B, Vision → slide 9 (3 min) • **demo C1, Teams: screenshots + the same in Copilot Chat → slide 11 (6 min)** • **demo C2, Word: screenshot + the same in Copilot Chat → slide 12 (5 min)** • **demo C3, Excel: screenshots + the same in Copilot Chat → slide 13 (5 min)** • optional **demo D, your own agent in Agent Builder → slide 19 (5 min)**.  
> **Main rule:** a Copilot answer is a draft. It answers differently every time; your result does not have to match ours word for word, it has to pass the checks against the source.  
> **The instructor's situation (verified 13 Oct 2026): no Microsoft 365 Copilot licence.** Personal account: no Microsoft 365 subscription; Word for the web shows no Copilot button, only “Buy Microsoft 365”. IT Park school account: **Copilot Chat (Basic)**; its app launcher shows no Word or Excel. The EPAM account is unusable on this PC. Copilot in Teams meetings (Facilitator, Recap), the Copilot pane in Word and in Excel all need a licence.  
> **Decision:** **no video clips in the lesson.** Teams, Word and Excel with Copilot are shown with the **screenshots on slides 11–13** (official Microsoft images and video frames). **The live part runs in free Copilot Chat on the IT Park school account**, which the students also have: the same thing, except we hand Copilot the text or the file ourselves. The licensed path is only a short note at the end of sections 5–7.

---

## 1. Before class

### A day before
- [ ] The **Microsoft Copilot** app opens; the account switcher (bottom left) has the **personal** and the **IT Park school** sign-in. Both answer a test question.
- [ ] School account: the **green shield** (enterprise data protection) shows in the chat header. Model: **Auto**.
- [ ] Personal account: a test “draw a picture” request works (the free tier has an image limit).
- [ ] Copilot in Windows: voice mode starts and the **Vision** button (Share screen / Share app) is there. If not, the fallback is in demo B.
- [ ] Teams and Copilot use the same microphone; check that Copilot hears you while a Teams call is running.
- [ ] `meeting_notes.md`, `release_checklist.txt`, `orders.csv` open and copy in full.
- [ ] The chat history of both accounts (left panel) holds nothing personal. Delete it or start from a clean “New chat”.
- [ ] The avatar and e-mail at the bottom left are in frame. If you prefer not to show them, keep that corner out of the shared area.
- [ ] **The Copilot app on the IT Park school account** (for slides 8, 11, 12, 13, 19): signed in, a new chat opens, a test question gets an answer.
- [ ] **File upload works:** in the IT Park chat, **+ → file** uploads `meeting_notes.md` and `orders.csv` (up to 20 files per chat, up to 50 MB each). If `.md` is not accepted, save a copy as `meeting_notes.txt`; if upload does not work at all, paste the text in class.
- [ ] **Check the day before: “create a Word file” from chat.** In the IT Park chat ask: `Write a one-page brief from these notes and create a Word file`. The docs describe this as an app feature; **we have not tested it on our account**. A `.docx` appears (downloads / opens) → show it in class. If not → in class the brief stays in the chat (section 6, fallback).
- [ ] **Files on the desktop:** `meeting_notes.md` and `orders.csv` are on the desktop (quick to find in the upload dialog) and open in Notepad (quick to copy the text).
- [ ] Teams, Word and Excel with Copilot are **not shown live**: no licence. Slides 11–13 with the screenshots open and the images show.
- [ ] **Demo D (optional):** the school account's left panel has **Agents → New agent**. If not, IT switched the feature off: show slides 18–19. Create a test agent in advance or make sure the button works; delete extra test agents (deletion is permanent: delete only your own test agents).

### 10 minutes before (Teams)
- [ ] Share the **whole screen**, not one window (the slides, Copilot, Vision and Notepad are separate windows). Close mail, messengers, notifications.
- [ ] Zoom Copilot in (Ctrl `+`) so it reads in Teams.
- [ ] Open: Copilot (IT Park school account, new chat), Notepad with `release_checklist.txt`, `meeting_notes.md` and `orders.csv` (to copy from; the files themselves are on the desktop for upload), slides 8, 9, 11, 12, 13, 19.
- [ ] Teams polls ready for slides 2 and 22.

---

## 2. The 90-second rule

If a button is missing, the interface differs or Copilot stays silent: **do not troubleshoot in front of the class**.
1. Say: **“The button moved, the rule did not.”**
2. At most **90 seconds** of searching. Time it.
3. Show the ready result: slides 8, 13, 18–19 hold **our real captures** of 13 Oct 2026 (brief, picture, orders answer, the agent build); slides 11–13 hold official Microsoft screenshots (slide 13 also our capture of the orders answer); for slide 9 use `fallback_outputs/checklist_answer.md`.
4. Say out loud that this is a prepared result, not a live answer.
5. Move on; debug after class.

The universal fallback for any Copilot: **paste the text into free Copilot Chat**.

---

## 3. Demo A. The Copilot app, briefly: what is in it + the brief (slide 8, 3 minutes)

**Goal:** in 3 minutes, show what the app has and one move: “give the source, ask for structure, demand a list of what was added”. Do not tour the app in depth: we come back to this same chat on slides 11–13.  
**Input:** `demo_courier_copilot/meeting_notes.md` (meeting “Prime delivery rule”, 5 October 2026, Anna, Pavel, Ola).

### Step 1. Tour of the app (≈30 seconds)
IT Park school account: the **Home · Code · Autopilot** tabs at the top, the left panel (chats, **Agents**), the account switcher bottom left, the green shield in the chat header. One line: “This is the same app you have; the school sign-in is free.”

### Step 2. Brief in Copilot Chat (≈1.5 minutes)
New chat. Paste the prompt and, right below it, the whole text of `meeting_notes.md`:
```text
Here are the notes from the courier app team meeting. Using only these notes, write a one-page brief: decisions, open questions, who does what. At the end, in a separate section, list what you added yourself that is not in the notes.
```
*Russian version (as in our capture):* `Вот заметки со встречи команды курьерского приложения. Только по этим заметкам напиши бриф на одну страницу: решения, открытые вопросы, кто что делает. В конце отдельным разделом перечисли, что ты добавил сам, чего нет в заметках.`

**Expected result** (our run, slide 8): sections “Decisions”, “Open questions”, “Who does what” (Pavel, Anna, Ola) and “What I added”. On 13 Oct 2026 the same prompt gave two different answers: once “Nothing added”, another time Copilot listed the section structure and an explanation that rollout means a staged launch. Both are normal: that is why we check.

### Step 3. Check against the source out loud (≈1 minute)
1. **$75 only for Prime** and only **in the city**.
2. **Free from $100 for everyone** stays.
3. **Nothing changes outside the zone.**
4. **Who owns the flag is an open question** (it must not turn into a decision).

**The launch picture** (personal account) is **not done live**: show our picture on slide 8 and mention the editor (Erase, Upscale, Edit object, Background, Crop; formerly Designer) and the check: the amount in the picture is exactly **$75**. If time is left, the prompt for the personal account:
```text
Draw a launch picture for a courier app: "Prime: free delivery from $75 in the city". A courier on a bike in a city street, bright colours, no logos of real companies.
```
*RU:* `Нарисуй картинку-анонс для курьерского приложения: «Prime: бесплатная доставка от $75 в городе». Курьер на велосипеде на городской улице, яркие цвета, без логотипов настоящих компаний.`

**Fallback:** no sign-in or the network failed: slide 8 already shows **our real brief and our picture** (captures of 13 Oct 2026, names hidden). Do not troubleshoot for more than 90 seconds.

---

## 4. Demo B. Vision over the checklist (slide 9, ≈3 minutes)

**Goal:** the wow moment: Copilot looks at the window you chose by itself. It sees only that window and only while you share.  
**Where:** Copilot in Windows, **personal account** (Vision for work accounts is only rolling out: the “preview” badge).  
**Input:** `demo_courier_copilot/release_checklist.txt` (6 items).

**Steps:**
1. Open `release_checklist.txt` in **Notepad**.
2. Copilot → voice mode → **Vision** → **Share app** → pick the Notepad window (not the whole screen, so Copilot sees nothing extra).
3. Ask by voice:
```text
Which item catches a fee change outside the zone?
```
*RU:* `Какой пункт поймает изменение платы вне зоны?`

**Expected result** (`fallback_outputs/checklist_answer.md`):
> Item 6, “Roll back the flag if outside-zone fees change unexpectedly.”

**Check with the class:**
1. The answer names **item 6** instead of retelling the checklist loosely.
2. Copilot **points and highlights but clicks nothing** for you.
3. Stop sharing the window and show that Vision is off.

**Fallback:**
- No microphone, or Copilot cannot hear you because of Teams: **paste the checklist text into chat** and ask the same question. Same result: Copilot sees only what you show it.
- No Vision on this PC or in this region: the same paste-the-text move.
- Nothing opens: slide 9 (a frame of the Vision interface from Kevin Stratvert's video) + `fallback_outputs/checklist_answer.md`. Say it is a prepared answer.

---

## 5. Demo C1. Teams: screenshots + the same in Copilot Chat (slide 11, 6 minutes)

**Goal:** “This lesson runs in Teams, so we are already inside one of the Copilots.” Show how a meeting becomes decisions, open questions and tasks.  
**First, tell the class honestly:** “Copilot in Teams meetings is a paid Microsoft 365 Copilot licence. I do not have one, and neither do you. I will show what it looks like on the screenshots, then we do the same thing for free in Copilot Chat.”

### Step 1. The screenshots on slide 11 (≈1.5 minutes)
Left: **Facilitator** in a meeting (agenda, timer, live notes). Right: **Recap** after the meeting (AI notes, tasks, a question to Copilot). One line: “Copilot in Teams hears the meeting itself through the transcript. Without a licence, we give it the transcript.”

### Step 2. The same live in Copilot Chat, IT Park school account (≈4 minutes)
1. Switch to the Copilot app (IT Park) → **New chat**.
2. Paste the prompt and, below it, the whole text of `meeting_notes.md`: that is our “transcript”:
```text
This is a transcript of the courier app team meeting. What was decided? What is still open? Who does what? Answer only from the text, do not add anything of your own.
```
*RU:* `Это расшифровка встречи команды курьерского приложения. Что решили? Какие вопросы остались открытыми? Кто что делает? Отвечай только по тексту, ничего не добавляй от себя.`
3. **Expected result** (from `meeting_notes.md`): decisions: **$75 free only for Prime and only in the city**, **free from $100 for everyone stays**, **nothing changes outside the zone**; open questions: **who owns the flag rollout** and **which number will show an unexpected rise in delivery cost early**; tasks: **Pavel**: the rule and tests, **Anna**: the brief and the issue, **Ola**: the support answer after the staging check.
4. **Compare with the Recap screenshot** on slide 11: the same three blocks, recap, tasks, open questions. The only difference: Recap takes the transcript itself; here we gave it.
5. **Check:** the open question “who owns the flag” did not turn into a decision; no extra names or dates.
6. Takeaway out loud: “Without a licence Copilot does not hear the meeting itself, but give it the text and the recap is the same. **The button moved, the rule did not.**”

**Fallback:** the chat does not answer or the network fails: slide 11 with the screenshots and a spoken check against `meeting_notes.md`. 90 seconds, no more.

> **If you ever get a Microsoft 365 Copilot licence:** the day before, hold a rehearsal meeting (Meet now, 2–3 minutes, transcript on, read `meeting_notes.md` out loud), and in class open its **Recap** tab and ask “Which questions are still open, and who does what?”. Facilitator for the lesson itself only if the recap shows no student names or quotes.

---

## 6. Demo C2. Word: screenshot + the same in Copilot Chat (slide 12, 5 minutes)

**Goal:** the same brief as on slide 8, only as a document: a draft from a file and an edit on request.  
**First, tell the class:** “The Copilot pane inside Word is a licence too. My Word shows “Buy Microsoft 365” instead of Copilot. I show it on a frame from a Microsoft video, and live in Copilot Chat.”

### Step 1. The screenshot on slide 12 (≈1 minute)
A frame from an official Microsoft video: the prompt points to a file; on the right, the **“What I updated in the document”** report and the highlighted changes. That is level 2 from slide 5: Copilot edits the document itself.

### Step 2. The same live in Copilot Chat, IT Park school account (≈3.5 minutes)
1. New chat. **+ → file** → pick `meeting_notes.md` from the desktop (up to 20 files per chat, up to 50 MB each). If it does not upload, paste the file's text below the prompt.
2. Prompt:
```text
These are the notes from the courier app team meeting. Using only them, write a one-page brief: decisions, open questions, who does what. Mark what you added yourself. Create a Word file with this brief.
```
*RU:* `Это заметки со встречи команды курьерского приложения. Только по ним напиши бриф на одну страницу: решения, открытые вопросы, кто что делает. Отметь, что ты добавил сам. Создай файл Word с этим брифом.`
3. **“Create a Word file”: check the day before** (section 1). The docs describe it as an app feature; we have not tested it on our account. A file appears: open it and show it. No file: say “no file this time, the brief in chat is the same” and move on.
4. Edit on request:
```text
Shorten the Decisions section to three bullets.
```
*RU:* `Сократи раздел «Решения» до трёх пунктов.`
Show that only that section changed. If there was a Word file, ask for the file to be updated too.
5. **Check:** the same 4 points as in demo A ($75 Prime in the city only • $100 for all • outside the zone unchanged • flag owner is an open question). The three “Decisions” bullets must be exactly those three decisions.
6. Takeaway out loud: “This is level 1: Copilot answers and hands over a file. With a licence it edits the document right inside Word and shows what it changed: level 2 from the screenshot.”

**Fallback:** no upload: paste the text; no Word file: the brief in chat; nothing works: slide 8 (our real brief) + slide 12.

> **If you ever get a licence:** put `meeting_notes.docx` in the work account's OneDrive, open the **Copilot** pane in Word, prompt `Write a one-page brief from /meeting_notes: decisions, open questions, who does what. Mark what you added yourself.`, then select “Open questions” → `Turn this into a table: question, who decides`, and show the “what I updated” report.

---

## 7. Demo C3. Excel: screenshots + the same in Copilot Chat (slide 13, 5 minutes)

**Goal:** “Excel is where Copilot is strongest and most dangerous: numbers look convincing.” Show our real mistake and how a rule in the prompt fixes it.  
**Input:** `demo_courier_copilot/orders.csv` (12 made-up orders).

### Step 1. The screenshots on slide 13 (≈1 minute)
Left: the official screenshot of Copilot's three modes in Excel, **edit · plan · chat only** (licence needed). Right: **our real capture** from free Copilot Chat (13 Oct 2026) with the outside-zone mistake.

### Step 2. The same live in Copilot Chat, IT Park school account (≈3.5 minutes)
1. New chat. **+ → file** → `orders.csv` from the desktop, or paste the CSV text below the prompt.

**Prompt 1, the slide question, without the rule (as in our run):**
```text
Here are the courier app orders (CSV). Which zone has the most Prime orders from $75, and how many of them are free now?
```
*RU:* `Вот заказы курьерского приложения (CSV). В какой зоне больше всего Prime-заказов от $75 и сколько из них теперь бесплатно?`

**Expected: the first answer is wrong outside the zone.** Our run on 13 Oct 2026: CITY: 4 Prime orders from $75, all 4 free (**right**); OUTSIDE: 3, “3 of them free” (**wrong**). We ran it twice; the mistake repeated. Copilot did not know the Prime rule applies only in the city because we did not give it; it marked its assumption with an asterisk, but the conclusion is still wrong. If your first answer is right, that is fine too: ask “how do you know the rule?”.

**Prompt 2, add the rule (same as homework step 2):**
```text
Rule: Prime gets free delivery from $75 only in the CITY zone. From $100 delivery is free for everyone in any zone. Everyone else pays as before. Recalculate: which zone has the most Prime orders from $75, and how many of them are free now? List the order numbers.
```
*RU:* `Правило: Prime — бесплатная доставка от $75 только в зоне CITY. От $100 доставка бесплатна для всех в любой зоне. Остальные платят как раньше. Пересчитай: в какой зоне больше всего Prime-заказов от $75 и сколько из них теперь бесплатно? Перечисли номера заказов.`

**Compare the two answers. Correct answer (check by hand against `orders.csv`):**
- CITY: Prime from $75 = **1001, 1004, 1006, 1009** (4 orders), all free. 1007 ($64.90) and 1012 ($74.99) are below the threshold.
- OUTSIDE: Prime from $75 = 1003, 1008, 1011 (3 orders), but **only 1011** is free ($130, the “from $100 for all” rule). 1003 and 1008 pay as before.
- The most: **CITY**.

If Copilot gets it wrong even with the rule, show that to the class and check one row by hand. Takeaway: “Put the rule in the prompt and check a row or two by hand. It is free, and every one of you has it.”

**Fallback:** no answer: slide 13 (our capture) + the correct answer above.

> **If you ever get a licence:** the same question in Excel, the Copilot pane in **chat only** mode (changes nothing in the workbook); give the rule in the prompt the same way.

---

## 8. Optional: demo D. Your own agent in Agent Builder (slide 19, ≈4 minutes)

**Goal:** show that every student can build an agent **in the free Copilot Chat of the school account**, without a licence. And that a rule in the instructions fixes the mistake from slide 13.  
**Where:** the Copilot app, **IT Park school account** → left panel **Agents → New agent** (the “Build your own specialist agent” screen, the “Message Agent Builder” box). Not on the phone. Not for personal accounts (no official confirmation).  
**When to run it:** if slides 11–13 left spare time. No time or no button: show slides 18–19, which are **our real run of 13 Oct 2026**.

### Step 1. Describe the agent (≈1 minute)
Paste **exactly this prompt** into “Message Agent Builder” (our run of 13 Oct 2026 used the Russian version):
```text
Create a "Courier support helper" agent for a training courier app. It answers support staff questions from customers about delivery cost using these rules: Prime subscribers get free delivery from $75 only in the city zone (CITY); from $100 delivery is free for everyone; in the city delivery costs $7.50, outside the zone (OUTSIDE) $18.00. Answer briefly and politely, always show the calculation, and if the question is missing data (zone, amount, whether the customer has Prime), ask first. Do not invent discounts or rules that do not exist.
```
*RU (our run):* `Создай агента «Помощник поддержки курьеров» для учебного курьерского приложения. Он отвечает сотрудникам поддержки на вопросы клиентов о стоимости доставки по правилам: подписчики Prime получают бесплатную доставку от $75 только в городской зоне (CITY); от $100 доставка бесплатна для всех; в городе доставка стоит $7.50, вне зоны (OUTSIDE) $18.00. Отвечай коротко и вежливо, всегда показывай расчёт, а если в вопросе не хватает данных (зона, сумма, есть ли Prime) — сначала уточни. Не выдумывай скидок и правил, которых нет.`

While Agent Builder thinks (ours: “Reasoning completed in 4 steps”), walk through the four parts of an agent from slide 18.

### Step 2. Check the draft, Configure (≈30 seconds)
Agent Builder filled in: the **name** “Помощник поддержки курьеров” / “Courier support helper” (limit 30 characters), the **description** (up to 1,000), the **instructions** with “Purpose” and “Main rules” sections (up to 8,000) and **4 starter prompts**. Show that knowledge is the web only: free Copilot Chat cannot upload a file (the organisation needs pay-as-you-go billing), but up to 4 public sites are allowed.

### Step 3. Test in Preview (≈1.5 minutes)
Switch **Configure → Preview** at the top. Two questions:

**Question 1 (tricky):**
```text
A Prime customer, an $80 order, an address outside the city. Why were they charged for delivery?
```
*RU (our run):* `Клиент с подпиской Prime, заказ на $80, адрес за городом. Почему с него взяли плату за доставку?`  
**Expected answer:** **$18.00** with the calculation: $80 is below the $100 threshold; Prime gives free delivery from $75 only in the CITY zone; the address is OUTSIDE → the $18.00 rate. *(Correct in our run of 13 Oct 2026.)*

**Question 2 (missing data):**
```text
How much is delivery for a $70 order?
```
*RU (our run):* `Сколько стоит доставка заказа на $70?`  
**Expected answer:** the agent **does not guess, it asks back**: CITY or OUTSIDE, and does the customer have Prime. *(That is what happened in our run of 13 Oct 2026.)*  
Optionally reply `CITY, has Prime` → expected **$7.50** ($70 is below the $75 threshold, Prime does not help). We did not test this third answer live: check it against the rules.

**Detail:** in our Preview the answer was duplicated; the interface is still rough. Mention it if it happens again.

### Step 4. Create (≈30 seconds)
Click **Create**: “Your agent was created successfully! This agent is currently private…”. The agent is **private**. **Do not** turn on “Org-wide sharing” in class. Takeaway: “Compare with slide 13: there Copilot got it wrong because it did not know the rule; here the rule is in the instructions, and the answer is right.”

**Fallback:** no New agent button (IT switched it off), a long wait or an error: slides 18–19 (our captures of steps 1–4). 90 seconds, no more.

---

## 9. If something goes wrong

| Symptom | What to do |
|---|---|
| Copilot added a number or a decision that is not in the notes | Great for the lesson: show it, compare with `meeting_notes.md`, strike it out. “An answer is a draft.” |
| “What I added” = “nothing”, but something was added | Show the line and the source. That is homework step 1. |
| The wrong account opened | Switch at the bottom left. Work and personal data do not mix (slide 6). |
| The personal account's image limit is used up | Slide 8 with our picture. |
| Copilot does not hear your voice during the Teams call | Paste the checklist text into chat (demo B fallback). |
| Vision shows the whole screen | Stop, choose **Share app** and the single Notepad window. |
| A student asks “where is Copilot in my Teams / Word / Excel?” | That is a Microsoft 365 Copilot licence; the IT Park school account has none. Everything on slides 11–13 can be done in Copilot Chat: give it the text or the file. |
| **+** does not upload the file, or `.md` is not accepted | Upload `meeting_notes.txt` (a copy) or paste the text below the prompt. Same result. |
| Copilot Chat did not create a Word file | Do not troubleshoot: the brief in chat is the same; do the “shorten the Decisions section” edit there (section 6). |
| Copilot shortened the wrong section or rewrote the whole brief | Show the class: “we asked for one change, we check that only that changed”. That is how you check an edit. |
| The first orders answer is suddenly right | Ask “how do you know the Prime rule?” and still give the rule in prompt 2; show our capture on slide 13. |
| The IT Park chat does not answer / no sign-in | Slides 11–13 with the screenshots + the expected answers from sections 5–7. 90 seconds, no more. |
| The school account has no Agents → New agent | IT switched the feature off: slides 18–19. |
| Agent Builder refuses to upload a file | Expected on free Copilot Chat: files and SharePoint need pay-as-you-go. Put the rules in the instructions. |
| The agent answered question 2 with a number without asking back | Show the class: the instructions need sharpening (“if the zone or Prime is missing, ask first”). That is a lesson too. |
| An e-mail, a name or a notification got into the frame | Stop sharing, remove it, continue. Rule: no passwords, keys or customer data in chat. |
| Copilot gets the orders wrong even with the rule | Show the hand check against `orders.csv` (section 7): city 1001, 1004, 1006, 1009; outside only 1011. |

## 10. Demo wrap-up (30 seconds)
“One rule in every window: **show what is needed, ask for structure and an honest list of what was added, check against the source**. Without a licence Copilot sees only what you gave it (which is what we did for Teams, Word and Excel); with a licence, it reaches your meetings and files itself; an agent is the same thing with the rules written down once.”

*Files:* `demo_courier_copilot/` (`meeting_notes.md`, `release_checklist.txt`, `orders.csv`, `fallback_outputs/`), our captures `assets/v3/img/own_*` (including `own_ab_*`, the agent build). Agent Builder and Windows facts: `L07_13_Research_Windows_AgentBuilder_2026-10-13.md`. Verify before recording: `README.md`.
