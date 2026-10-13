# Lesson 06 • Homework: Voice Your L05 Video (Product or Courier)

**Course:** GenAI Basics • Module 2 (Multimodality)  
**Submission:** folder `genai-homeworks/L06/` in your personal GitHub repository  
**Reviewer:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)  
**Estimated time:** 3–4 hours  
**Code:** not needed. Every step has a no-code tool below. Code and open-weight models are optional (slides 13 and 16, `deck_v2/make_audio.py`, `deck_v2/make_clone.py`).  
**Matches:** slide 20 (homework) of `presentation_L06_Speech_and_Audio_EN_v2.html`, plus slides 7–12 (the 6 pipeline steps), slide 17 (cost), slide 18 (acceptance checklist = rubric), slide 19 (consent). Service facts as of 2026-10-12.

---

## Goals

1. Run the 6-step pipeline from the lesson on your own video: 1 script, 2 spoken text, 3 voice, 4 background (effects or music), 5 mix, 6 check.
2. Compare the same three lines in two voice services.
3. Mix to a streaming loudness target and prove it with a meter screenshot.
4. Check the result with speech-to-text and by ear, and explain every error: was it the voice, the mix or the transcriber?
5. Record what it cost and under which licence each piece of audio can be used.

Grading is based on the error analysis. A voice-over with errors that are found and explained scores higher than a clean-sounding one without analysis. Perfect sound is not required.

---

## Choose One Track

### Track A: product
- **Video:** your L05 `final.mp4` (product promo, 15–25 s).
- **Lines:** 3 short lines: the product name, one feature, a call to action. Brand words and numbers are your critical terms.

### Track B: courier (Glovo case from L01, L04 and L05)
- **Video:** your L05 `final.mp4` (pickup, ride, delivery).
- **Lines:** 3 short dispatcher-style lines: order number and time, the route, the arrival estimate and the courier’s name.
- **Rule:** Glovo is only the name of the training case. Do not imitate any real brand voice or jingle.

**No L05 video?** Use the lesson’s courier video `GenAI Basics — Course Production/L05/demo_veo_showcase/courier_delivery_final.mp4`.  
**Your video has no sound** (for example Luma or Leonardo Motion)? Build the background from sound effects or music (step 4).

---

## What to Do (6 Steps = 6 Lesson Steps)

| Step | Task | Deliverable |
|---|---|---|
| **1 Script** | 3 lines, one per shot. Word budget: speech window = shot length − 2 s; words ≤ window × 2–2.5 (Russian: × 1.8–2.2). List your critical terms (numbers, times, names, brand words). Slide 7. | `script.md` |
| **2 Spoken text** | Next to each line, write the spoken text: numbers, times and names as words, decided by you (for example, is 417 “four hundred seventeen” or “four one seven”?). Add one style instruction. Slide 8. | columns in `script.md` |
| **3 Voice** | Generate the same 3 lines in **two** services, one file per line. Library or designed voices only; your own voice is allowed; nobody else’s. Keep the better version by checklist items 1–2. Slide 9. | `audio/voiceA_line1.mp3` … `audio/voiceB_line3.mp3` |
| **4 Background** | Use the video’s own sound, or generate sound effects or music. Write the source and licence of every track. Slide 10. | `audio/bed.*`, licence table in `audio_spec.md` |
| **5 Mix** | Voice on top, background ducked, −14 ± 1 LUFS, true peak ≤ −1 dBTP. Put the mix on the video. Screenshot the loudness meter. Slide 11. | `final_voiced.mp4`, `audio/mix.wav`, `qa/loudness.png` |
| **6 Check** | Run `final_voiced.mp4` (or `mix.wav`) through speech-to-text, save the raw output unedited. Fill in the slide 18 checklist with evidence and timecodes. Add the cost table. Slides 12, 17, 18. | `transcript.txt`, `audio_qa.md`, `audio_spec.md` |

Add an end caption to the video: **“Voice and music: AI-generated (service names)”**, and the same line in `audio_spec.md` (slide 19).

---

## Tools per Step (October 2026, free options first)

**Free allowances are small and change often. Verify the current terms before you start.**

| Step | No-code options | Notes |
|---|---|---|
| 3 Voice | **ElevenLabs** (web, free plan: 10,000 credits a month ≈ 10 minutes of speech; no commercial licence on Free) • **Google AI Studio** → speech generation (Gemini TTS) | Optional: Gemini API (code in the lesson README), OpenAI `gpt-4o-mini-tts` (shuts down 6 January 2027), open-weight Kokoro (EN), Piper (RU) or **Qwen3-TTS** with a clone of **your own** voice, installed by a coding agent with the prompt from slide 16 |
| 4 Background | Your video’s own sound • **ElevenLabs Sound Effects** (up to 30 s per generation) • **ElevenLabs Music** • **Gemini app** music (Lyria 3.5) • **Suno** (Free: Suno owns the song, non-commercial; fine for homework) • non-AI fallback: YouTube Audio Library (licence shown per track) | Write the licence of every track in `audio_spec.md` |
| 5 Mix | **Audacity** (free): import the lines and the background → select the background track → *Effect › Auto Duck* (or lower it by 10–15 dB where the voice speaks) → *Tracks › Mix and Render* → *Effect › Loudness Normalization* to −14 LUFS → *Limiter* with the limit at −2 dB (video encoding to AAC raises the peak by about 0.5 dB) → export WAV. Then in **CapCut**, **Clipchamp** or **DaVinci Resolve**: mute the clip’s own sound and place the WAV at 0:00. | Alternative: everything in DaVinci Resolve (Fairlight page). ffmpeg is optional (slide 11, `make_audio.py`). |
| 5 Measure | **Youlean Loudness Meter** (free, browser or app) or the **DaVinci Resolve** loudness meter. Read **Integrated** (−13 to −15 LUFS passes) and **True Peak** (must be ≤ −1.0 dBTP). Save a screenshot as `qa/loudness.png`. | With code: `ffmpeg -i mix.wav -af ebur128=peak=true -f null -` |
| 6 Speech-to-text | **ElevenLabs Speech to Text** • **Google AI Studio**: upload the file with the prompt *“Transcribe verbatim. Do not correct mistakes. Write numbers as you hear them.”* • **Buzz** (Whisper desktop app, offline) | **Never paste your script into the transcription prompt**: a language model will correct the transcript towards the script and hide the errors. Save the output unedited. |

**Do not use** for this homework: cloning anyone’s voice except your own, celebrity or colleague voices, imitations of real brand jingles.

---

## Directory Structure for Submission

```
genai-homeworks/
└── L06/
    ├── script.md               # lines, spoken text, timing, word budget, critical terms
    ├── audio/
    │   ├── voiceA_line1.mp3    # service A, one file per line
    │   ├── voiceB_line1.mp3    # service B, same lines
    │   ├── bed.mp3             # background: video sound, effects or music
    │   └── mix.wav             # final mix, −14 ± 1 LUFS
    ├── final_voiced.mp4        # your L05 video with the new sound and the AI caption
    ├── transcript.txt          # raw speech-to-text output, unedited
    ├── qa/loudness.png         # loudness meter screenshot
    ├── audio_spec.md           # services, settings, licences, cost
    └── audio_qa.md             # slide 18 checklist with evidence
```

---

## Template: `script.md`

```markdown
# Script • Homework L06

**Student:** [Your name / EPAM alias]  
**Track:** [A: product / B: courier (Glovo case)]  
**Video:** [L05 final.mp4, length … s]  
**Style instruction:** [e.g. Calm, friendly dispatcher. Medium pace. Short pause after each sentence.]  
**Budget rule:** speech window = shot length − 2 s; max words = window × 2–2.5 (Russian: × 1.8–2.2)

| # | Shot time | Speech window | Script (as the viewer reads it) | Spoken text (numbers and names as words) | Words / max | Sound effects | Music |
|---|---|---|---|---|---|---|---|
| 1 | 0–8 s | 0.6–6.6 s | 6:42. Order 417 is picked up, still hot. | Six forty-two. Order four one seven is picked up, still hot. | 11 / 15 | cafe noise | lo-fi bed, no vocals |
| 2 | 7.5–15.5 s | … | … | … | … | … | … |
| 3 | 15–23 s | … | … | … | … | … | … |

**Critical terms:** [e.g. 6:42, 417, 12 minutes, Anna]
```

---

## Template: `audio_spec.md`

```markdown
# Audio Specification • Homework L06

**Student:** [Your name / EPAM alias]  **Track:** [A / B]

## 1. Voice
| | Service | Model | Voice name | Settings / style instruction | Attempts per line |
|---|---|---|---|---|---|
| A | [e.g. ElevenLabs] | [e.g. Eleven v3] | [...] | [...] | [...] |
| B | [e.g. Google AI Studio] | [e.g. Gemini 3.8 Flash TTS] | [...] | [...] | [...] |
**Kept:** [A or B] because [checklist items 1–2].

## 2. Background and licences
| Track | Source (service / video model / library) | Licence | Commercial use? | Attribution needed? |
|---|---|---|---|---|
| Voice | [...] | [plan terms] | [yes / no] | [...] |
| Background | [...] | [...] | [...] | [...] |

## 3. Mix
- **Tool and steps:** [e.g. Audacity: Auto Duck → Loudness Normalization −14 LUFS → Limiter −2 dB; CapCut for the video]
- **Result:** Integrated [… LUFS], True Peak [… dBTP] (screenshot `qa/loudness.png`)
- **AI label:** [where the caption appears, its exact text]

## 4. Cost
| Item | Unit (characters / minutes / tracks) | Quantity × attempts | List price | Cost at list price | Actually paid |
|---|---|---|---|---|---|
| Voice A | characters | [...] | [e.g. $0.08 / 1K characters] | [...] | [$0 on free tier] |
| Voice B | [...] | [...] | [...] | [...] | [...] |
| Background | [...] | [...] | [...] | [...] | [...] |
| Speech-to-text | minutes | [...] | [...] | [...] | [...] |
| **Total** | | | | [...] | [...] |

Example: 3 lines ≈ 150 characters × 2 services × 3 attempts ≈ 900 characters ≈ $0.07 at $0.08 per 1K characters; $0 paid on a free tier.
```

---

## Template: `audio_qa.md`

The checklist is the one on slide 18. For each item: ✓ / ✗ / partly, the **evidence**, the **timecode** and the **cause** (voice / mix / speech-to-text).

```markdown
# Audio Acceptance • Homework L06

| # | Checklist item | Result | Evidence | Timecode | Cause |
|:-|:---|:-:|:---|:-:|:---|
| 1 | **Words** match the script: speech-to-text + critical terms | | transcript.txt + table below | | |
| 2 | **Pronunciation** of names, numbers, terms (by ear) | | notes | | |
| 3 | **Timing**: each line fits its shot, not cut by a transition | | script.md word budget + timecodes | | |
| 4 | **Mix**: voice clear, background ducked, no stray speech (listen to the first and last 3 s) | | notes | | |
| 5 | **Loudness** −14 ± 1 LUFS, true peak ≤ −1 dBTP | | qa/loudness.png | | |
| 6 | **Rights**: voice and music licence, consent, “AI-generated” label | | audio_spec.md licence table + caption | | |

### Critical terms
| Term | Heard as (transcript.txt) | Correct? | After listening: voice error or speech-to-text format? |
|---|---|:-:|---|
| [6:42] | [642] | ✗ | [speech-to-text format: the voice said “six forty-two”] |

### Service A vs service B
[2–3 sentences, by checklist items 1–2]

### Conclusion
[3–4 sentences: what you would fix and how: rewrite a line, change the spoken text, another voice, mute the video sound at 0–3 s, re-mix]

Optional: word error rate = (substitutions + deletions + insertions) / words in the script, after writing numbers the same way in both texts.
```

---

## How We Grade (rubric = slide 18 checklist)

| # | Item | Passes if |
|---|---|---|
| 1 | Words | `transcript.txt` is the raw output; every critical term is checked and every mismatch is classified (voice, mix or speech-to-text) |
| 2 | Pronunciation | by-ear notes with timecodes for names, numbers and terms |
| 3 | Timing | every line is within its word budget (`script.md`) and not cut by a transition |
| 4 | Mix | voice is clear, background ducked, the first and last seconds checked for stray speech |
| 5 | Loudness | −14 ± 1 LUFS and true peak ≤ −1 dBTP, proven by `qa/loudness.png` |
| 6 | Rights | licence table filled; no cloned voice except your own; “AI-generated” caption present |

Completeness (required, not graded separately): `script.md` with spoken text, two voice services compared, cost table.

---

## Submission Checklist

1. [ ] Branch `feature/L06-audio-homework` created and submitted via Pull Request to `main`.
2. [ ] `script.md` has 3 lines with spoken text, word budget and critical terms.
3. [ ] `audio/` has the lines from both services, the background and `mix.wav`.
4. [ ] `final_voiced.mp4` has the new sound and the “AI-generated” caption.
5. [ ] `transcript.txt` (unedited) and `qa/loudness.png` are present.
6. [ ] `audio_spec.md` has services, licences, mix result and the cost table.
7. [ ] `audio_qa.md` has the 6-item checklist with evidence, the critical-terms table, the A vs B comparison and a conclusion.
8. [ ] Reviewer `ihar_rubanovich@epam.com` invited as repository collaborator.
