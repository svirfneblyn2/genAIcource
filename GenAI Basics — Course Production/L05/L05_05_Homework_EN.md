# Lesson 05 • Homework Assignment: Bring an L04 Frame to Life (Product or Courier)

**Course:** GenAI Basics • Module 2 (Multimodality)  
**Submission:** Folder `genai-homeworks/L05/` in your personal GitHub repository  
**Inspector / Reviewer:** Igor Rubanovich (`ihar_rubanovich@epam.com`)  
**Estimated Time:** 1.5–2 hours  
**Code:** not needed — everything is done in the services’ web interfaces.  
**Matches:** slides 16 (acceptance checklist) and 18 (homework) of `presentation_L05_Video_Generation_EN_v2.html`. Service facts as of 2026-10-12.

---

## Assignment Goals

1. See for yourself the difference between **T2V** (video from text only) and **I2V** (video from a ready image + text about motion).
2. Set one clear camera move (orbit, dolly-in, or “camera moves alongside”).
3. Keep your L04 hero or product consistent throughout the clip.
4. Check the clip against the 6-item checklist and describe honestly where and why the model went wrong.

We grade **awareness, not beauty**: can you show where and why the model went wrong.

---

## Choose One of Two Tracks

### Track A — product
1. **Source frame:** your approved L04 packshot (e.g. `D0_packshot.png` or `A3_details.jpg`).
2. **What to make:** a promo of about **5 seconds** (if the service has no 5 s option, use the nearest length, 4–6 s). Camera: **orbit** or **dolly-in**, one move per clip.
3. **Requirement:** the product’s shape, proportions, colour and text **don’t drift**.

### Track B — courier (Glovo case from L01 & L04)
1. **Source frame:** your approved L04 courier frame (e.g. `C2_rain.jpg`).
2. **What to make:** a riding shot of about **5 seconds** — the **camera moves alongside** the courier (tracking shot); wheels turn forward.
3. **Requirement:** face and uniform **match the reference**. Don’t add logos or other brands to the frame: Glovo is just the name of the training case.

---

## What to Submit (Both Tracks)

| # | Task | Deliverable |
|---|---|---|
| **1** | An honest **T2V attempt in one prompt** — for comparison. Let it break: that is part of the experiment. | `videos/01_t2v_trap.mp4` |
| **2** | **I2V** with your L04 frame in **service #1**. | `videos/02_i2v_serviceA.mp4` |
| **3** | **I2V** with the same frame and the same prompt in **service #2** (a different service or a different model). | `videos/03_i2v_serviceB.mp4` |
| **4** | Prompts and settings for all three attempts. | `video_spec.md` |
| **5** | Check both I2V clips against the **6-item checklist** (slide 16), with timecodes. | `video_qa.md` |

How to write the I2V prompt (slide 8): **camera + action + motion details**; don’t retell what is already in the image — one short anchor for the hero is enough; say what *should* happen.

---

## Which Services You Can Use (October 2026)

Any **two** services that can do image-to-video. Free-access terms change often — check before you start.

| Service / model | What matters for this homework | Free? |
|---|---|---|
| **Kling 3.0** (kling.ai, Kuaishou) | I2V, first + last frame, Elements (2–4 references); clips 3–15 s; audio | Daily free credits exist (amount per third-party sources — **verify**) |
| **Gemini app / Flow** (Google) with **Veo 3.1** and **Gemini Omni** | I2V from an image; Flow — first + last frame, extend; Omni — 360p draft | Flow — in Google AI Plus / Pro / Ultra plans; free video access in the Gemini app — **not confirmed** |
| **Runway Gen-4.5** | I2V (first frame); camera by words or controls; Runway also hosts other models (Veo, Kling, Seedance, Wan, Hailuo) | Gen-4.5 is on paid plans; trial credits — **not confirmed** |
| **Luma Ray3.2** (Dream Machine) | I2V, 5 or 10 s clips, cheap 360p draft; **no audio**; camera moves as ready-made “concepts” (Orbit left/right etc.) | Free tier — **not confirmed** |
| **Hailuo H3** (MiniMax) | I2V, first + last frame, 5–15 s clips; Hailuo models are also on Leonardo | Free tier — **not confirmed** |
| **Wan 2.2** (open weights, Alibaba) | run locally via ComfyUI; the TI2V-5B model — 720p, 5 s, needs a 24 GB GPU | Free if you have your own GPU |
| **Veo 3.1 via API** (optional) | code as on slide 14; Fast — $0.10/s, Lite — $0.05/s (720p) | **Paid**; no free tier for Veo in the API |

**Don’t use:** Sora — shut down (app since 26.04.2026, API since 24.09.2026). ChatGPT does not make video.

---

## Directory Structure for Submission

Organize your submission repository strictly as follows:

```
genai-homeworks/
└── L05/
    ├── videos/
    │   ├── 01_t2v_trap.mp4        # T2V in one prompt (for comparison)
    │   ├── 02_i2v_serviceA.mp4    # I2V in service #1
    │   └── 03_i2v_serviceB.mp4    # I2V in service #2
    ├── video_spec.md              # prompts and settings
    └── video_qa.md                # check against the 6-item checklist
```

---

## Template: `video_spec.md`

```markdown
# Video Specification • Homework L05

**Student:** [Your Name / EPAM alias]  
**Track:** [A: product / B: courier]  
**Source frame from L04:** `assets/C2_rain.jpg` (or link)

---

## 1. T2V in one prompt (01_t2v_trap.mp4)
- **Service / model:** [e.g. Kling 3.0]
- **Prompt:** `a delivery courier riding a bicycle fast down a city street`
- **Duration:** [s]
- **What broke (with timecodes):** [e.g. 00:02 — face differs from L04; 00:04 — wheels spin backwards]

---

## 2. I2V in service #1 (02_i2v_serviceA.mp4)
- **Service / model:** [e.g. Kling 3.0]
- **Input frame:** `C2_rain.jpg`
- **Prompt (camera + action + motion details):** [your prompt]
- **Settings you changed:** [duration, resolution, camera controls — if the interface has them]
- **Attempts needed:** [number]
- **Seed:** [if available; remember a seed does not guarantee repeatable results in cloud services]

---

## 3. I2V in service #2 (03_i2v_serviceB.mp4)
- **Service / model:** [e.g. Runway Gen-4.5 / Luma Ray3.2 / Veo 3.1 in Flow]
- **Input frame:** `C2_rain.jpg`
- **Prompt:** [the same prompt]
- **Settings you changed:** [...]
- **Attempts needed:** [number]
```

---

## Template: `video_qa.md`

The checklist is the same as on slide 16. For each item: ✓ / ✗ / partly and the **timecode** where the problem is visible.

```markdown
# Video Check • Homework L05

| # | Checklist item | Service #1 | Service #2 | Notes (what and where, timecode) |
| :- | :--- | :---: | :---: | :--- |
| 1 | **Hands and objects** in contact — don’t merge or vanish | ✓ / ✗ / partly | ✓ / ✗ / partly | |
| 2 | **Text and numbers** — readable and stable | | | |
| 3 | **Face and clothes** (Track B) / **product shape and text** (Track A) — match the reference | | | |
| 4 | **Motion** — right speed and direction (wheels forward, camera moves as asked) | | | |
| 5 | **First frame** — matches the approved L04 frame | | | |
| 6 | **Shot joins** — light and colour match (if you joined clips; otherwise “n/a”) | | | |

### Comparison with T2V
[2–3 sentences: what broke in 01_t2v_trap and why I2V did better or worse]

### Conclusion
[3–4 sentences: which service handled your task better and why; what you would change — a different frame, prompt or camera move]
```

---

## How We Grade (rubric = slide 16 checklist)

| What we look at | Passes if |
|---|---|
| All 6 checklist items filled in for both I2V clips | every item has a rating, and every problem has a timecode |
| T2V vs I2V comparison | it is clear how the results differ and why (the frame locked the appearance) |
| Prompts | `video_spec.md` has all three prompts; the I2V prompt has camera, action and motion details |
| Conclusion | explains where and why the model went wrong and what you would change |

A perfect video is **not required**: a clip with errors found and described scores better than a “beautiful” clip with no analysis.

---

## Acceptance Checklist

1. [ ] Branch `feature/L05-video-homework` created and submitted via Pull Request to `main`.
2. [ ] Folder `videos/` contains 3 `.mp4` files (about 4–10 seconds each).
3. [ ] File `video_spec.md` lists the services, models and prompts of all three attempts.
4. [ ] File `video_qa.md` has the 6-item checklist filled in for both I2V clips, a comparison with T2V and a conclusion.
5. [ ] Instructor `ihar_rubanovich@epam.com` invited as repository collaborator.
