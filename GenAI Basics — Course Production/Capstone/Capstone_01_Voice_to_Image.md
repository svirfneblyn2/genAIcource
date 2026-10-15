# Capstone 1 • "Voice Brief → Image"

**Course:** GenAI Basics  
**Weight:** 30 of 100 course points  
**When:** after Lesson L06  
**Time needed:** 2–3 hours  
**What you need:** a computer with the Chrome browser, a personal Google account (the same one you used in L03), a microphone or a phone  
**No payment. No API keys. No programming.**

> Use a **personal** Google account. Work and school accounts often block Colab and link sharing.

---

## 1. What you do, in two sentences

You play a client: you dictate a short brief for a picture ("I need a cover for a coffee shop menu…"). A ready-made Google Colab notebook turns your voice into text, the text into a professional prompt, and the prompt into an image, step by step; you check every step, fix mistakes and draw conclusions.

This is the same pipeline that real products build from three models:

```
your voice → [Whisper: speech to text] → transcript → [Gemini: rewrite as a prompt] → prompt → [SD-Turbo: image model] → image
```

| Step | Model | Where it was in the course |
|---|---|---|
| Speech → text | Whisper (open model, runs inside Colab) | L06 |
| Text → prompt | Gemini, built into Colab | L02, L03 |
| Prompt → image | SD-Turbo (open model, runs inside Colab) | L04 |

---

## 2. What "no programming" means

The notebook is already written. You only do three things:

- **Press the ▶ button** to the left of a cell. The cell runs. When it finishes, a green tick appears next to it. If the cell printed a message telling you what to do (for example `No file selected. Run the cell again.`), it shows a red mark instead: just do what the message says.
- **Fill in form fields** inside the cells: text fields and drop-down lists, like an ordinary form. Some text fields are one line long. That is fine: paste the whole text into them anyway.
- **Write answers in text cells** in plain English. To write in a text cell: double-click it (it opens for editing), type under the questions, then press `Shift+Enter` or click outside the cell.

**Do not change the code.** You will not see it unless you press "Show code". If you deleted something by accident, press `Ctrl+Z` (undo) at once. If that does not help, use **File → Revision history** and restore an earlier version. Start again from a new copy of the template only if nothing else helps.

---

## 3. Preparation (10 minutes)

1. Open the template: **https://colab.research.google.com/drive/1SV7rOo3or2exXhb8MmpFa3brgjJxSHqQ?usp=sharing**.
2. Click **File → Save a copy in Drive**. Your copy opens, named "Copy of …".
3. Rename your copy: click the name at the top and type `Capstone1_Surname_Name`.
4. **Work only in your copy.** Changes in the template are not saved.
5. Scroll through the **"Example"** section at the top. We did the whole assignment there with our own voice brief: this is what your result should look like. The Example contains only pictures and text. Nothing to run or delete there. You do your own work in the **"Your work"** section below it.
6. **Do not use "Run all".** Run the cells one at a time, top to bottom: in many of them you first need to fill in a form or press something.

> When you run the first cell, Colab may show the window "Warning: This notebook was not authored by Google". Press **"Run anyway"**. Only do this for the notebook your instructor gave you.


---

## 4. Think of your brief (10 minutes)

Imagine you are the client explaining to a designer what you need. Speak for **15–30 seconds** in normal language. Always mention:

1. **What the picture is and what it is for:** a cover, a poster, a banner, an illustration for a post.
2. **What is most important in it:** an object, a character, a place.
3. **Mood and style:** cozy, strict, cheerful; photo, watercolor, cartoon.
4. **One concrete detail:** a colour, the time of day, a caption. If you want a caption, keep it short (1–3 words). Image models often distort text. A distorted caption is fine if you notice it and describe it.

**Example:** "I need a cover image for the menu of a small coffee shop. Morning, a cup of cappuccino with latte art on a wooden table, and a croissant next to it. Warm, soft light from the window, cozy. At the top, the words Morning Menu."

Speak **English**. All three models work best with it.

**Do not:**
- name real people, other companies' logos or brands;
- say personal data in the recording: your surname, address, phone number or employer.

**Where your data goes:**
- your voice recording and the images are processed inside your Colab notebook (Whisper and SD-Turbo run there) and are not sent to any other service;
- the transcript and the prompt are sent to Gemini (Google); if you use a fallback or Bonus A, you paste the same text into gemini.google.com or ChatGPT yourself;
- the recording, transcript and images stay in your notebook, which you will share by link for grading.

---

## 5. Steps in the notebook

Run the cells **one at a time, strictly top to bottom**. After it runs, each cell shows its result and a log line, for example `[STEP 2] transcript: model whisper-small, 25.3 s`. Do not delete these outputs: we grade your work from them.

### Step 0. Setup (2–5 minutes, once)
Press ▶. The notebook installs Whisper and downloads the Whisper and SD-Turbo models. Grey and red warning lines during the download are normal. Wait for the green tick and the line `DONE. Go to step 1.`

### Step 1. Voice (2–5 minutes)
In the drop-down list **`method`**, choose one option.

**"Record here":**
1. Choose "Record here" and press ▶.
2. **The first time**, Colab shows the window "This cell is requesting browser permissions — Microphone". Press **"Accept"**. Under the cell you will see "The microphone did not turn on…". This is expected: **press ▶ again**.
3. The browser asks for microphone access (a small window near the address bar). Press **"Allow"**.
4. A **"● Record"** button appears. Press it, speak for 15–30 seconds, press **"■ Stop"**.
5. Nothing else to press: after a few seconds you see a player and the line `[STEP 1] recording: 23 s`.

If the "● Record" button does not appear within 30 seconds after point 3, press ■ (stop) to the left of the cell and use "Upload a file".

**"Upload a file":**
1. Record a voice note on your phone (mp3, m4a, wav or ogg, at most 60 seconds).
2. Send the file to your computer in any way, for example to yourself in a messenger or by e-mail, and download it.
3. Choose "Upload a file", press ▶ and pick the file with the **"Choose Files"** button. If you pressed "Cancel", the notebook says "No file selected". Just run the cell again.

You will see a player. **Listen to the recording.** If you hear nothing, record again.

### Step 2. Voice → text, Whisper (up to 1 minute)
Press ▶. The **transcript** appears: what the model heard.

**Compare the transcript with what you said.** Whisper sometimes gets single words wrong, drops a word, or changes punctuation and capital letters.

**If there are mistakes:**
1. copy the transcript into the form field **`corrected_transcript`**;
2. fix the mistakes by hand;
3. press ▶ for this cell again.

The cell runs again and shows the line `[STEP 2] using the corrected transcript`. From now on the corrected text goes through the pipeline.

**If there are no mistakes**, leave the field empty: Whisper's transcript goes on as it is.

In the text cell below, write **whether there were mistakes and which ones**. For example: "It wrote 'morning menu' in small letters and split 'Warm, soft light' into two sentences." Or: "No mistakes."

### Step 3. Text → prompt, Gemini (up to 1 minute)
In the form, choose:
- **`style`**: the same style you said in your recording. If you said another one, choose the closest from the list: photo, watercolor, 3D, flat illustration, anime. The form wins: Gemini uses it instead of what was in your speech;
- **`image_format`**: square, landscape 16:9 or portrait 9:16;
- **`manual_prompt`**: leave it empty (it is only for the fallback, section 10).

Press ▶. Gemini splits your text into parts, as we learned in L04 (**subject, details, style, composition, light, mood**), and writes one prompt from them.

**Read the prompt.** In the text cell below, answer:
- does it contain everything you asked for?
- does it contain anything you did not ask for?

### Step 4. Prompt → image, SD-Turbo (1–2 minutes)
Leave the **`source`** field as "SD-Turbo in Colab". Press ▶. The image appears.

If you see an error instead of the image, see section 10, **"If something does not work"**.

### Step 5. Edit in words (1–2 minutes)
Look at the image as the client: what would you ask the designer to change? Write **one** edit in the **`edit`** field, in one sentence, using the L04 pattern "change only X, keep everything else the same".

Examples:
- "make the background lighter, keep everything else the same";
- "add a croissant on the table, keep everything else the same".

Leave **`source`** and **`manual_prompt`** as they are. Press ▶. Gemini changes the prompt, and the new image appears next to the old one. You may try several edits: the last run of the cell is the final one, earlier results are replaced automatically.

In the text cell, answer: **did the edit work, and what else changed that you did not ask for?**

> The model draws the image again from scratch, so other details may change together with your edit (the notebook keeps the same random seed, so usually the composition stays similar and only some details change). Small image models are also bad at counting objects and writing text, so an edit like "only one cup" may not work at all. This is expected. Just describe honestly what happened.

### Step 6. "As said" vs "after rewriting" (1–2 minutes)
Leave **`source`** as "SD-Turbo in Colab". Press ▶. The notebook sends your transcript to the image model **without rewriting** (the corrected one, if you corrected it) and shows two images side by side:
- **left**: a new image from the transcript "as said";
- **right**: the image from step 4, the same one, not a new one.

In the text cell, answer three questions, 1–2 sentences each, with a concrete example:
1. Which image is closer to what you wanted?
2. What exactly did the step 3 prompt add: light, composition, style, details?
3. What did the model get wrong in both images?

### Step 7. Final conclusions
In the last text cell, write **4–6 sentences with concrete examples from your work** (quote words from the transcript, the prompt and the edit):
- at which step there were the most mistakes, and why;
- what you fixed by hand;
- what you would do differently next time.

If you used a fallback (section 10), say so here.

---

## 6. Bonus (optional, pick one)

**Bonus A. Another service.**
1. Copy the prompt from step 3.
2. Open **Gemini** (gemini.google.com, it works with your Google account), type "Draw an image:" and paste the prompt. If you already have a ChatGPT account, you may use it instead. Do not create a new account.
3. Download the image and upload it in the **"Bonus A"** cell: press ▶ and use "Choose Files".
4. Write 2–3 sentences: which service did better, and why.

If in step 4 you already took your image from Gemini via the fallback, do Bonus A with ChatGPT (only if you already have an account). If you do not have one, choose Bonus B.

**Bonus B. Series (3–6 minutes).**
1. In the **"Bonus B"** cell, write three short scenes, 3–8 words each, in the fields **`scene_1`**, **`scene_2`**, **`scene_3`**. For example: "coffee on a table", "coffee in a barista's hands", "takeaway coffee on the street".
2. Press ▶. The notebook takes the description of the hero or object from your step 3 prompt and puts the same description into all three images.
3. Write 2–3 sentences: is the hero recognisable in all three images, and what drifted? This is the "consistent character" technique from L04.

Bonus B needs the image model in Colab. If you had to use the image fallback in step 4, choose Bonus A.

---


## 7. What we check

Your capstone is **accepted** when the notebook opens from your link and shows all of this:

1. **Your own recording** (step 1) with its player and the `[STEP 1]` log line. Not the instructor's example.
2. **The transcript** (step 2) and your answer: were there mistakes, and which ones.
3. **The prompt** (step 3) and your answer: is everything you asked for in it, and is there anything you did not ask for.
4. **The image** (step 4).
5. **One edit** (step 5) written as "change only X, keep everything else the same", the two images side by side, and your answer: did it work, and what else changed.
6. **The comparison** (step 6): the two images side by side and your answers to the three questions.
7. **Conclusions** (step 7): 4–6 sentences with concrete examples from your work.
8. **Log lines** `[STEP 1]`–`[STEP 6]` visible under the cells.

**What matters:** not how beautiful the image is, but **whether you understand what each model does and where it makes mistakes**. A bad image with an honest analysis is a better result than a beautiful one without conclusions. General answers like "it worked well" are not enough: give a concrete example each time.

**Using a fallback (section 10) is fine.** Just say so in step 7.

**If something is missing**, the instructor returns the work with a comment, and you have **2 days** to fix it.

---

## 8. How to submit

1. Check that the cells of **steps 0–6** have run and **step 7** is written; for a bonus, also the **bonus cell**. Each of them must show its result: images, transcript, prompt, log lines.
2. Check the setting **Edit → Notebook settings**. The box **"Omit code cell output when saving this notebook"** must be **unticked**, otherwise the images are not saved.
3. Click **File → Save** or press `Ctrl+S`.
4. Click **Share** at the top right. Under "General access", choose **"Anyone with the link"**, role **"Viewer"**, then **"Copy link"**.
5. **Check the link:** open it in an incognito window (`Ctrl+Shift+N`). If you see the notebook with images, it is correct. If it asks you to sign in or says you have no access, repeat point 4.
6. Send the link through the submission form: **[SUBMISSION FORM LINK — provided by the instructor]**.

No separate report, no GitHub, no screenshots: everything is visible in the notebook.

After you receive your grade, you may turn off link sharing.

**Deadline:** [DATE — provided by the instructor].

---

## 9. Frequently asked questions

**Do I need to understand code?** No. Press ▶, fill in the form fields and write answers.

**Can I record again?** Yes, as many times as you like. After a new recording, run steps 2–6 again: the notebook forgets the old transcript, prompt and images, and the old outputs under those cells no longer belong to your final recording.

**Can I try several edits?** Yes, but the submission must contain one final edit with its image.

**My image is ugly. Is that a problem?** No, if you explain why it happened and what you tried to fix.

**Can I use paid services?** You may, but you do not need to: the whole assignment is free.

**How many times can I generate an image?** As many as you need. There are no limits inside your notebook.

---

## 10. If something does not work

| What you see | What to do |
|---|---|
| A cell runs longer than its step says: step 0 longer than 8 minutes, steps 2–6 longer than 5 minutes, Bonus B longer than 10 minutes | Press ■ (stop) to the left of the cell and run it again |
| `Error: image not created` | Run the cell again. If it fails 3 times, use the **image fallback** below |
| The top right corner says "Connecting" for more than 5 minutes and no cell starts | Click **Runtime → Disconnect and delete runtime**, then **Yes**, and press ▶ in step 0 again. If it still does not connect, try again in an hour: free Colab is sometimes busy |
| `Gemini error` | Wait 1 minute and run the cell again. If it fails 3 times, use the **prompt fallback** below |
| Colab says "Runtime disconnected" | Press "Connect" and run the cells again **from step 0**. You will have to record or upload your voice again (step 1). Answers you already wrote and form fields you already filled in are kept |
| `Run step 0 first.` (shown in red, as an error) | The runtime restarted. Run the cells again from step 0 |
| `Run step 2 first.` (or another step number) | A later cell needs the result of that step. Run that step and the steps after it again |
| `Could not read this file.` | Your voice file has an unusual format. Record it again as mp3, m4a, wav or ogg |
| The browser does not give access to the microphone | In step 1, choose "Upload a file" |
| The transcript is empty or makes no sense | Listen to the recording. If it is too quiet or noisy, record again closer to the microphone |

### Prompt fallback (if Gemini in Colab does not work)

**Step 3:**
1. Open gemini.google.com.
2. Paste: "Rewrite this brief as one English image prompt of 30–50 words covering subject, details, style, composition, light and mood. Style: [your style]. Format: [your format]. Brief: [your transcript]".
3. Copy the answer into the **`manual_prompt`** field in the step 3 cell and press ▶.

**Step 5:**
1. At gemini.google.com, write: "Here is a prompt: [prompt from step 3]. Change only [your edit], keep everything else the same. Return only the new prompt."
2. Fill in the **`edit`** field as usual (it is graded), paste Gemini's answer into the **`manual_prompt`** field in the step 5 cell and press ▶.

### Image fallback (if the image model does not work)

**Step 4:**
1. Copy the prompt from step 3.
2. Open gemini.google.com, type "Draw an image:" and paste the prompt.
3. Download the image (the download icon under the image).
4. In the step 4 cell, set **`source` = "upload manually"**, press ▶ and pick the downloaded file.

**Step 5:**
1. Fill in `edit` and set **`source` = "upload manually"**. Press ▶. Gemini shows the changed prompt first, then the notebook asks for a file: press **"Cancel"** for now. The notebook says "No file selected".
2. Copy the changed prompt to gemini.google.com, type "Draw an image:" before it, and download the result.
3. Press ▶ again (the notebook reuses the same changed prompt) and pick the downloaded file.

**Step 6:** at gemini.google.com, type "Draw an image:" and paste **your transcript as it is**. Download the image. In the step 6 cell, set **`source` = "upload manually"**, press ▶ and pick the file. The right image is taken from step 4 automatically.
