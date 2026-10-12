# 1-Page Speaker Cheatsheet • Lesson 05 (v2: 21 Slides • 90 Minutes)
*Speaker: Ihar Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*  
*Topic: Video Generation. From a key frame to a video of several shots • facts as of 2026-10-12*  
*Presentation: `presentation_L05_Video_Generation_EN_v2.html` (PDF: `presentation_L05_Video_Generation_EN_v2.pdf`) • source: `deck_v2/build.py` • full script: `L05_02_Instructor_Script_90MIN_EN.md`*  
*Homework: `L05_05_Homework_EN.md` • Repo: `genai-homeworks/L05/` • Collaborator: `ihar_rubanovich@epam.com`*

---

### Teams: before you start
* Share screen → **“Optimize for motion and video”**. Share the browser window; do not share computer sound.
* Deck: `F` fullscreen, `←/→` navigate, `N` notes, `G` slide grid. Videos play **on click**, **muted**. The PDF shows a poster “▶ video in the HTML version”.
* Clicks: **sl. 2** `final` (23 s, may play twice) • **sl. 5** `trainwreck` (8 s) • **sl. 6** `trainwreck`, then `shot1` • **sl. 10** `shot2` • **sl. 13** `final` again • **sl. 15** timer “Start”.
* Pipeline (6 steps): **1** storyboard (sl. 7) • **2** references (sl. 8) • **3** key frame (sl. 9) • **4** prompt + camera (sl. 10–11) • **5** controls (sl. 12) • **6** editing (sl. 13).

---

### Part 1 (00:00–58:00)
* **01 Cover (2 min, 00–02):** L04 made images; today we generate video from them. Plan: example, layers, how it works, failures, 6 steps, market.
* **02 Example (3 min, 02–05):** click `final`. Chat: how many clips, where are the cuts? 3 Veo 3.1 clips of 8 s from key frames (image-to-video), **8+8+8 → 23 s** (two 0.5 s transitions), **≈ $10** (3 × 8 × $0.40), failed attempts not included. Audio exists; covered in L06.
* **03 Where to generate (4 min, 05–09):** **chat apps** (Gemini app = Gemini Omni, Google Flow = Omni 1.1 Flash + Veo 3.1, Grok Imagine): prompt only, subscription, start with Gemini app • **web studios** (Kling, Leonardo, Dreamina / CapCut with Seedance, Runway, Luma, Hailuo): camera settings, first/last frame, references, several shots per generation, credits, small free allowance, start with Kling • **API** (Gemini API / Vertex AI, Kling API, Runway API, xAI API): per second, batch jobs, start with Gemini API. Veo is in Flow, Leonardo, Runway, Gemini API. **ChatGPT has no video.**
* **04 How diffusion makes frames (4 min, 09–13):** noise for all frames at once → dozens of denoising steps on patches “place × time”, guided by text and first frame → 24 fps. **No physics engine:** errors in hand/object contact, text, long scenes (Physics-IQ, 2025).
* **05 Anti-pattern (5 min, 13–18):** click `trainwreck`. 00:02 action skipped • 00:03 details drift (“Glono”) • 00:05 scene geometry breaks • 00:07 garbled text “Admest”. Root cause: **3 scenes and 5 actions in 8 s**. One shot = one scene, one action.
* **06 Text-to-video vs image-to-video (3 min, 18–21):** text-to-video decides look + motion; image-to-video decides motion only. Rule: fix appearance, light, composition in the image.
* **07 Step 1 storyboard (7 min, 21–28):** shots of 4–8 s; one row = one key frame + one prompt + one generation. Rows: 1 cafe pickup, 0–8 s, medium shot, slow dolly in, `shot1_cafe_pickup.png` • 2 bike in rain, 7.5–15.5 s, tracking, low angle, `shot2_bike_rain.png` • 3 map route, 15–23 s, slow digital zoom, slight tilt, `shot3_map_route.png`. Creator Tools template, 7 columns: shot/timing, visual, voice-over, image prompt, video prompt, SFX, music. 1 min ≈ 8 shots; 1 h ≈ 450 shots. **Exercise (2 min):** propose shot 4 as one row.
* **08 Step 2 references (3 min, 28–31):** character sheet, 4 anchors. Veo 3.1 up to 3 references; Kling 3.0 Elements 2–4. More stable, not guaranteed.
* **09 Step 3 key frame (4 min, 31–35):** sprite → draft → approved after one edit. Image edit: seconds, cents. Video regeneration: minutes, $0.40/s.
* **10 Step 4 prompt (6 min, 35–41):** 6 slots: camera · who · action · where/when · motion details · light. Click `shot2`. Rules: motion verbs; do not describe the frame again; describe what should happen (negative prompt only in Kling, Wan).
* **11 Step 4 camera (4 min, 41–45):** Static, Pan, Tilt, Dolly, Tracking, Orbit, Crane, Handheld. One move per shot. Chats: words only; Runway, Kling, Luma: also controls.
* **12 Step 5 controls (3 min, 45–48):** Motion Brush (Kling 1.x–2.x, up to 6 elements + static zone; not in 3.0). First + last frame: Veo 3.1, Omni, Kling 3.0. Extend: Veo 3.1 +7 s up to 148 s (720p, not Lite); Omni +10 s up to 40 s. References: Veo 3.1 / Fast up to 3 images (8 s clip); Kling Elements 2–4.
* **13 Step 6 editing (7 min, 48–55):** 8+8+8 − 0.5 − 0.5 = **23 s**, wipe + fade to black; CapCut, DaVinci Resolve or one `ffmpeg xfade` command (offsets 7.5 and 15). Model makes a shot; a person builds the story. Click `final`.
* **14 Market (3 min, 55–58):** audio is standard; clips 10–30 s. Omni 1.1 Flash 10 s (+40 s), #1 LMArena 21.09.2026 • Veo 3.1 8 s (+148 s) • Kling 3.0 15 s (4.0 Flash 20 s, beta) • Seedance 2.5 30 s • Wan 3.0 30 s, #1 Artificial Analysis with audio • Hailuo H3 15 s • Ray3.2 10 s, no audio • LTX-2 20 s, open weights • Wan 2.2 5 s, open weights. **Sora shut down.** *Before class: has full Kling 4.0 shipped?*

### Break (58:00–63:00)
* **15 Break (5 min):** press “Start”. Rest only, no chat tasks.

### Part 2 (63:00–90:00)
* **16 Code (3 min, 63–66):** reference only. `google-genai`, `veo-3.1-fast-generate-preview`: submit → poll every 10 s (~11 s to ~6 min) → download. Same pattern: Kling API, Runway API, xAI API. No free tier for Veo. Homework needs no code.
* **17 Cost (5 min, 66–71):** table below. 1 h = 3600 s = **450 shots of 8 s**. Our video: 3 × 8 s × 3 attempts = **72 s** = **$28.80** (Veo 3.1) / **$7.20** (Fast). Drafts on cheap models; finals on the model that passes acceptance.
* **18 Acceptance (5 min, 71–76):** shot 3: timer 0:28 → 0:45, “Mep”, moped instead of bicycle; shot 2: “THABIK”. Checklist: 1 hands and objects • 2 text and numbers • 3 face and clothes • 4 motion • 5 first frame • 6 shot joins. = **homework rubric**. Add text in editing.
* **19 Risks (4 min, 76–80):** own characters with AI label; other brands with permission and lawyers; real people with written consent. SynthID (pixels, usually survives) vs C2PA (metadata, easily lost); SynthID check in Gemini app (≤100 MB, ≤90 s). EU AI Act Art. 50.
* **20 Homework (7 min, 80–87):** three-shot mini story. Track A product (reveal, detail, final) / Track B courier (pickup, ride, delivery). `storyboard.md` (3 rows) → text-to-video baseline → 3 image-to-video shots, one repeated in a second service → `final.mp4` 15–25 s → `video_spec.md` (cost) + `video_qa.md` (slide 18 checklist). Free allowances are small and change: verify.
* **21 Summary (3 min, 87–90):** 5 rules: storyboard first; approved key frame before video; one action per shot (4–8 s); structured prompt; acceptance and budget. L06: sound and speech.

---

### Key numbers (checked 2026-10-12)
| What | Value |
|---|---|
| Cost per second, 720p | Veo 3.1 Lite **$0.05** • Grok Imagine 1.5 **$0.08** • Veo 3.1 Fast **$0.10** • Runway Gen-4.5 **$0.12** • Seedance 2.5 from **$0.20** (Runway API) • Veo 3.1 **$0.40** |
| 8 s clip / 1 min / 1 h | Lite $0.40 / $3.00 / $180 • Grok $0.64 / $4.80 / $288 • Fast $0.80 / $6.00 / $360 • Runway $0.96 / $7.20 / $432 • Seedance $1.60 / $12.00 / $720 • Veo 3.1 $3.20 / $24.00 / $1,440 |
| 1 h, 3 attempts per shot | $540 • $864 • $1,080 • $1,296 • $2,160 • $4,320 |
| Other prices | Gemini Omni 1.1 Flash ≈ $0.10/s (720p, token-billed) • Grok Imagine Lite $0.02/s • Kling 3.0 web, 1080p + audio: 12 credits/s = 43,200 credits/h • chat apps: subscription |
| Our video | 3 shots × 8 s, two 0.5 s transitions = **23 s**; ≈ $10 list price; with 3 attempts: 72 s = $28.80 (Veo 3.1) / $7.20 (Fast) |
| Scale | 1 min ≈ 8 shots of 8 s • 1 h = 3600 s = 450 shots |
| Veo 3.1 | clips 4/6/8 s; extend +7 s per step up to 148 s (720p, not Lite); up to 3 references; SynthID on every video; no free tier in API |
| Gemini Omni 1.1 Flash | 3–10 s; extend +10 s up to 40 s; runs in Gemini app and Flow |
| Sora | app closed **26.04.2026** • API closed **24.09.2026** • no replacement • ChatGPT has no video |
| EU AI Act | **Art. 50**, from **02.08.2026**: **50(4)** publisher labels a deepfake; **50(2)** provider adds a machine-readable mark; fines **€15M / 3%** of turnover |
| US | TAKE IT DOWN Act: intimate deepfakes removed within 48 h, since May 2026 |
