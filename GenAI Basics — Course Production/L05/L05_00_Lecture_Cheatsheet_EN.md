# 1-Page Speaker Cheatsheet • Lesson 05 (v2: 19 Slides • 90 Minutes)
*Speaker: Ihar Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*  
*Topic: Video Generation — from a key frame to a finished clip • facts as of 2026-10-12*  
*Presentation: `presentation_L05_Video_Generation_EN_v2.html` (PDF: `presentation_L05_Video_Generation_EN_v2.pdf`) • full script: `L05_02_Instructor_Script_90MIN_EN.md`*  
*Homework: `L05_05_Homework_EN.md` • Repo: `genai-homeworks/L05/` • Collaborator: `ihar_rubanovich@epam.com`*

---

### Teams: what to click before you start
* Share screen → **“Optimize for motion and video”**. Share the browser window with the deck; do not share computer sound.
* Deck: `F` fullscreen, `←/→` navigate, `N` notes, `G` slide grid. Videos play **on click**, **muted**. The PDF shows a poster “▶ video in the HTML version” instead.
* What to click: **sl. 2** `final` (23 s, may play twice) • **sl. 4** `trainwreck` (8 s) • **sl. 5** `trainwreck`, then `shot1` • **sl. 8** `shot2` • **sl. 11** `final` again • **sl. 12** timer “Start” button.

---

### Part 1 (00:00 — 51:00)
* **01 Cover (2 min, 00–02):** in L04 we made images — today we bring them to life. Lesson plan.
* **02 Hook (4 min, 02–06):** click `final`. Chat question: how many “takes”, where are the cuts? Answer: 3 Veo 3.1 clips of 8 s made from ready frames (I2V), **8+8+8 → 23 s** (two 0.5 s transitions), **≈ $10** at list price (3 × 8 × $0.40), retries not counted. Sound in one sentence: it’s there; covered in L06.
* **03 How a model makes video (5 min, 06–11):** noise → step-by-step cleanup for all frames at once → 24 frames/s. **No physics engine** — errors in contacts (hands, bag), text, long scenes (Physics-IQ, 2025).
* **04 Failure gallery (6 min, 11–17):** click `trainwreck`. 00:02 action skipped • 00:03 details drift (“Glono”) • 00:05 space breaks • 00:07 pseudo-text “Admest”. Cause: 3 scenes and 5 actions in 8 s.
* **05 T2V vs I2V (6 min, 17–23):** two clips one after another. T2V — “what is in frame + how it moves” at once; I2V — motion only. Rule: lock appearance in the image.
* **06 References (4 min, 23–27):** character sheet, 4 anchors. Veo 3.1 — up to 3 references; Kling 3.0 Elements — 2–4. More stable, not guaranteed.
* **07 Key frame in chat (4 min, 27–31):** sprite → draft → approved with one edit. Image — seconds and cents; video — minutes and $0.40/s.
* **08 Director’s prompt (6 min, 31–37):** 6 slots: camera · who · action · where/when · motion details · light. Click `shot2`. Rules: motion verbs; don’t retell the frame; say what should happen (negative prompt exists in Kling, Wan; in Veo phrase positively).
* **09 Camera language (5 min, 37–42):** Static, Pan, Tilt, Dolly, Tracking, Orbit, Crane, Handheld. One move per shot. Chats — words only; studios (Runway, Kling, Luma) — also controls.
* **10 Precise control (4 min, 42–46):** Motion Brush (Kling 1.x–2.x, up to 6 elements + static zone; not in Kling 3.0). First+last frame (Veo 3.1, Omni, Kling 3.0); extend: Veo 3.1 +7 s up to 148 s, Omni +10 s up to 40 s.
* **11 Editing (5 min, 46–51):** timeline 8+8+8 − 0.5 − 0.5 = **23 s**. The model makes a shot; a person builds the story (CapCut, DaVinci Resolve, ffmpeg). Click `final`.

### Break (51:00 — 56:00)
* **12 Break (5 min):** press “Start” on the timer. No tasks.

### Part 2 (56:00 — 90:00)
* **13 Market, October 2026 (7 min, 56–63):** audio is standard; clips are 10–30 s. Google’s lead model — **Gemini Omni 1.1 Flash** (#1 LMArena, 21.09.2026); **Veo 3.1** — in the API, our clips; #1 Artificial Analysis with audio — **Wan 3.0**. Also Kling 3.0 (15 s; 4.0 up to 30 s — early access), Seedance 2.5, Hailuo H3, Luma Ray3.2 (no audio). Open weights: Wan 2.2, LTX-2. **Sora is shut down:** app 26.04.2026, API 24.09.2026, no replacement; ChatGPT does not make video. *Before class: has the full Kling 4.0 shipped?*
* **14 Code (3 min, 63–66):** reference only. `google-genai`: send → wait (~11 s – ~6 min) → download. The homework needs no code.
* **15 Economics (5 min, 66–71):** numbers below. Stress: the number of tries is an assumption.
* **16 Quality check (5 min, 71–76):** our defects: shot 3 — timer 0:28 → 0:45, “Mep”, a moped instead of a bicycle; shot 2 — “THABIK” sign. 6-item checklist = **homework rubric**. Add text and numbers in editing.
* **17 Risks (6 min, 76–82):** traffic light: own characters — with an AI label; other brands — with permission and company lawyers; real people — only with written consent. SynthID (in pixels, usually survives) vs C2PA (in metadata, easily lost). SynthID check — in the Gemini app (up to 100 MB / 90 s); may not recognise other services.
* **18 Homework (5 min, 82–87):** Track A product (5 s, orbit/dolly-in) / Track B courier (camera alongside). T2V for comparison + I2V in two services → `videos/`, `video_spec.md`, `video_qa.md`. We grade awareness, not beauty.
* **19 Summary (3 min, 87–90):** 4 rules: frame first; one shot — one action; director’s prompt; check and count. L06 teaser: models already make sound themselves. Questions.

---

### Key numbers (checked 2026-10-12)
| What | Value |
|---|---|
| Veo 3.1 / Fast / Lite, 720p | **$0.40 / $0.10 / $0.05 per second** (Gemini API; no free tier; only successful videos billed) |
| 8-second clip | $3.20 / $0.80 / $0.40 |
| Our clip | **8+8+8 → 23 s** (two 0.5 s transitions), ≈ $10 at Veo 3.1 list price, retries not counted |
| Economics (sl. 15) | T2V trial and error 10×3×$3.20 = **$96** • frame + I2V 3×3×$3.20 = **$28.80** • same on Fast 3×3×$0.80 = **$7.20**. *The number of tries is an assumption for the estimate.* |
| Veo 3.1 | clips 4/6/8 s; extend +7 s per step up to 148 s; up to 3 references; SynthID on every video |
| Gemini Omni 1.1 Flash | 3–10 s; extend +10 s up to 40 s; 360p draft ≈ ⅓ of the 720p price |
| Sora | shutdown announced 24.03.2026 • app closed **26.04.2026** • API closed **24.09.2026**, no replacement |
| EU AI Act | **Art. 50**; applies from **02.08.2026**; **50(4)** — whoever publishes a deepfake labels it; **50(2)** — machine-readable mark from the model provider (systems released earlier — from **02.12.2026**); fines **€15M / 3%** of turnover |
| US | TAKE IT DOWN Act — removal of intimate deepfakes within 48 h, FTC enforcement since 19.05.2026 |
