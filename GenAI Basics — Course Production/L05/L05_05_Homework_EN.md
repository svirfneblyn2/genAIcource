# Lesson 05 • Homework: A Three-Shot Mini Story (Product or Courier)

**Course:** GenAI Basics • Module 2 (Multimodality)  
**Submission:** folder `genai-homeworks/L05/` in your personal GitHub repository  
**Reviewer:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)  
**Estimated time:** 3–4 hours  
**Code:** not needed; everything is done in the services’ web interfaces. The API is optional (slide 16).  
**Matches:** slide 20 (homework) of `presentation_L05_Video_Generation_EN_v2.html`, plus slide 7 (storyboard), slide 10 (prompt), slide 11 (camera), slide 13 (editing), slide 17 (cost), slide 18 (acceptance checklist). Service facts as of 2026-10-12.

---

## Goals

1. Run the full 6-step pipeline from the lesson on a small story: storyboard, references, key frame, prompt and camera, controls, editing.
2. Compare text-to-video (text only) with image-to-video (approved key frame + text about motion) on the same story.
3. Compare the same shot in two different services.
4. Calculate what the video cost: attempts × seconds × price per second.
5. Review every shot and the shot joins with the 6-item checklist from slide 18 and describe where and why the model went wrong.

Grading is based on the defect analysis: where and why the model went wrong, with timecodes. A video with defects that are found and explained scores higher than a clean-looking video without analysis.

---

## Choose One Track

### Track A: product
- **Key frames:** your approved L04 product frames (e.g. `D0_packshot.png`, `A3_details.jpg`). Produce or edit a third frame in an image chat if you need one.
- **Three shots:** 1 reveal, 2 detail, 3 final shot.
- **Camera ideas:** slow orbit, slow dolly in, static camera. One camera move per shot.
- **Requirement:** the product’s shape, proportions, colour and text stay stable in every shot.

### Track B: courier (Glovo case from L01 and L04)
- **Key frames:** your approved L04 courier frames (e.g. `C3_door.jpg`, `C2_rain.jpg`, `C4_rest.jpg`), using the character sheet as the reference.
- **Three shots:** 1 pickup, 2 ride, 3 delivery.
- **Camera ideas:** medium shot with slow dolly in, tracking alongside, static or slow pan. One camera move per shot.
- **Requirement:** face and uniform match the reference in every shot. Do not add logos or other brands: Glovo is only the name of the training case.

---

## What to Do (Both Tracks)

| # | Task | Deliverable |
|---|---|---|
| **1** | **Storyboard** of 3 rows: #, time, action, camera, key frame file, prompt. Each shot 4–8 s, one action and one camera move per shot (slide 7). | `storyboard.md` |
| **2** | **Text-to-video baseline:** describe the whole three-shot story in **one prompt**, text only, and generate it once. Expect failures; this is the comparison point (slide 5). | `videos/00_t2v_baseline.mp4` |
| **3** | **Three image-to-video shots**, each from its approved L04 key frame, with a prompt built from the slots on slide 10 (camera + action + motion details). | `videos/shot1.mp4`, `videos/shot2.mp4`, `videos/shot3.mp4` |
| **4** | **Second service:** pick one of the three shots and generate it again in a different service with the same key frame and the same prompt. | `videos/shotN_service2.mp4` (N = shot number) |
| **5** | **Editing:** join the three shots into one video of **15–25 s** with transitions, in any editor (CapCut, DaVinci Resolve) or with ffmpeg (slide 13). | `videos/final.mp4` |
| **6** | **Specification:** prompts, settings and cost of every clip. Cost = attempts × seconds × $/s (slide 17). | `video_spec.md` |
| **7** | **Acceptance:** review each shot and the two shot joins with the 6-item checklist from slide 18, with timecodes. Item 6, shot joins, applies to your edit. | `video_qa.md` |

How to write an image-to-video prompt (slides 10 and 11): **camera + action + motion details**; do not describe the frame again (one identifying detail is enough); describe what should happen; one camera move per shot.

---

## Services You Can Use (October 2026)

You need image-to-video in **two** services. **Free allowances are small and change often. Verify the current terms before you start.** Do not plan the homework around free credits only.

| Service | Layer | What matters for this homework | Free access |
|---|---|---|---|
| **Gemini app** (Gemini Omni) / **Google Flow** (Omni 1.1 Flash, Veo 3.1) | chat app | image-to-video from a key frame; camera with words only; Flow adds first/last frame and extension | Flow is in Google AI Plus / Pro / Ultra plans; free video access in the Gemini app: **not confirmed, verify** |
| **Kling** (Kling 3.0, kling.ai) | web studio | image-to-video, first + last frame, Elements (2–4 references), several shots per generation, camera settings; clips 3–15 s; audio | free accounts get a **small monthly credit grant**; daily login credits are for subscribers during events. **Verify.** Web pricing: 12 credits/s for 3.0 at 1080p with audio |
| **Leonardo** | web studio | own Motion 2.0 (5 s, no audio) and hosted Veo, Kling, Seedance, Hailuo | **verify** |
| **Dreamina / CapCut** (ByteDance, Seedance) | web studio | image-to-video with Seedance; CapCut also works as the editor for step 5 | **verify** |
| **Runway** (Gen-4.5 and hosted models) | web studio / API | image-to-video (first frame); camera by words or direction/strength controls; also hosts Seedance, Veo, Wan, Hailuo | Gen-4.5 on paid plans; trial credits **not confirmed**. API: Gen-4.5 $0.12/s, Seedance 2.5 from $0.20/s |
| **Luma** (Ray3.2, Dream Machine) | web studio | image-to-video, 5 or 10 s clips, cheap 360p draft, preset camera “concepts”; **no audio** | **not confirmed, verify** |
| **Hailuo** (H3, MiniMax) | web studio | image-to-video, first + last frame, 5–15 s clips | **not confirmed, verify** |
| **Grok Imagine** (xAI) | chat app / API | image-to-video in the app; API `grok-imagine-video-1.5` $0.08/s, Lite $0.02/s | **not confirmed, verify** |
| **Veo via Gemini API** (optional) | API | code as on slide 16; Veo 3.1 Lite $0.05/s, Fast $0.10/s, Veo 3.1 $0.40/s (720p) | **paid only**; no free tier for Veo in the API |
| **Wan 2.2** (open weights, optional) | local | run locally via ComfyUI; TI2V-5B model: 720p, 5 s, needs a 24 GB GPU | free if you have your own GPU |

**Do not use:** Sora. It is shut down (app since 26.04.2026, API since 24.09.2026). ChatGPT does not generate video.

---

## Directory Structure for Submission

```
genai-homeworks/
└── L05/
    ├── storyboard.md                 # 3 rows: #, time, action, camera, key frame file, prompt
    ├── videos/
    │   ├── 00_t2v_baseline.mp4       # text-to-video, whole story in one prompt
    │   ├── shot1.mp4                 # image-to-video, shot 1
    │   ├── shot2.mp4                 # image-to-video, shot 2
    │   ├── shot3.mp4                 # image-to-video, shot 3
    │   ├── shotN_service2.mp4        # one shot repeated in a second service
    │   └── final.mp4                 # edited video, 15–25 s
    ├── video_spec.md                 # prompts, settings, cost
    └── video_qa.md                   # slide 18 checklist per shot and per join
```

Keep only the accepted attempt of each shot in `videos/`; record the number of attempts in `video_spec.md`.

---

## Template: `storyboard.md`

```markdown
# Storyboard • Homework L05

**Student:** [Your name / EPAM alias]  
**Track:** [A: product / B: courier]  
**Story in one sentence:** [e.g. The courier picks up an order, rides through the rain and hands it over at the door.]

| # | Time | Action | Camera | Key frame file | Prompt |
|---|---|---|---|---|---|
| 1 | 0–8 s | [one action] | [one move, e.g. medium shot, slow dolly in] | [path to approved L04 frame] | [camera + action + motion details] |
| 2 | 7.5–15.5 s | [one action] | [e.g. tracking alongside, low angle] | [...] | [...] |
| 3 | 15–23 s | [one action] | [e.g. static camera] | [...] | [...] |

Times include 0.5 s transition overlaps. Adjust to your shot lengths (4–8 s each, final 15–25 s).
```

---

## Template: `video_spec.md`

```markdown
# Video Specification • Homework L05

**Student:** [Your name / EPAM alias]  
**Track:** [A: product / B: courier]  
**Service 1:** [e.g. Kling 3.0]  **Service 2:** [e.g. Veo 3.1 Fast in Flow]

---

## 0. Text-to-video baseline (00_t2v_baseline.mp4)
- **Service / model:** [...]
- **Prompt (whole story):** [...]
- **Duration:** [s]
- **What broke (with timecodes):** [e.g. 00:02 action skipped; 00:05 face differs from L04]

## 1–3. Image-to-video shots (shot1.mp4, shot2.mp4, shot3.mp4)
For each shot:
- **Service / model:** [...]
- **Key frame:** [file]
- **Prompt:** [same as storyboard row]
- **Settings:** [duration, resolution, aspect ratio, camera controls, references, seed if available]
- **Attempts:** [number]; **what changed between attempts:** [prompt edit, new key frame, other setting]

## 4. Second service (shotN_service2.mp4)
- **Shot:** [N]  **Service / model:** [...]
- **Key frame and prompt:** same as shot N
- **Settings / attempts:** [...]

## 5. Editing (final.mp4)
- **Tool:** [CapCut / DaVinci Resolve / ffmpeg / other]
- **Transitions:** [type and length, e.g. two 0.5 s crossfades]
- **Final length:** [s]

## 6. Cost
Cost = attempts × seconds per attempt × price per second. For credit-based services, write credits and the plan’s price per credit.

| Clip | Service / model | Seconds per attempt | Attempts | $/s or credits/s | Cost |
|---|---|---|---|---|---|
| Baseline | [...] | 8 | 1 | [...] | [...] |
| Shot 1 | [...] | 8 | [...] | [...] | [...] |
| Shot 2 | [...] | 8 | [...] | [...] | [...] |
| Shot 3 | [...] | 8 | [...] | [...] | [...] |
| Shot N, service 2 | [...] | 8 | [...] | [...] | [...] |
| **Total** | | | | | [...] |

Example: shot 2 on Veo 3.1 Fast, 8 s, 3 attempts = 3 × 8 × $0.10 = $2.40.
```

---

## Template: `video_qa.md`

The checklist is the one on slide 18. For each item: ✓ / ✗ / partly, and the **timecode** where the problem is visible.

```markdown
# Video Acceptance • Homework L05

| # | Checklist item | Shot 1 | Shot 2 | Shot 3 | Shot N, service 2 | Notes (what, where, timecode) |
|:-|:---|:-:|:-:|:-:|:-:|:---|
| 1 | **Hands and objects** in contact: no merging or vanishing | | | | | |
| 2 | **Text and numbers**: readable and stable | | | | | |
| 3 | **Face and clothes** (Track B) / **product shape and text** (Track A): match the reference | | | | | |
| 4 | **Motion**: speed and direction (wheels forward, camera moves as asked) | | | | | |
| 5 | **First frame**: matches the approved key frame | | | | | |

| # | Checklist item | Join 1 → 2 | Join 2 → 3 | Notes (timecode in final.mp4) |
|:-|:---|:-:|:-:|:---|
| 6 | **Shot joins**: light and colour match | | | |

### Text-to-video baseline vs image-to-video
[2–3 sentences: what broke in 00_t2v_baseline.mp4, and why the image-to-video shots did better or worse]

### Service 1 vs service 2 (shot N)
[2–3 sentences: which service handled the shot better, by checklist item]

### Conclusion
[3–4 sentences: which defects you would fix and how (new key frame, prompt edit, different camera move, other service), and what you would change in the storyboard]
```

---

## How We Grade (rubric = slide 18 checklist + storyboard + editing)

| What we look at | Passes if |
|---|---|
| Storyboard | 3 rows with time, one action, one camera move, key frame file and prompt; the shots in `videos/` follow it |
| Checklist items 1–5 | filled in for all three shots and the second-service shot; every problem has a timecode |
| Checklist item 6 | both joins in `final.mp4` reviewed for light and colour |
| Editing | `final.mp4` is 15–25 s, contains the three shots in storyboard order, with transitions |
| Prompts and cost | `video_spec.md` has all prompts and settings; image-to-video prompts have camera, action and motion details; cost table filled as attempts × seconds × price |
| Comparisons | text-to-video baseline vs image-to-video, and service 1 vs service 2, explained by checklist items |
| Conclusion | explains where and why the model went wrong and what you would change |

A defect-free video is **not required**.

---

## Submission Checklist

1. [ ] Branch `feature/L05-video-homework` created and submitted via Pull Request to `main`.
2. [ ] `storyboard.md` has 3 rows.
3. [ ] `videos/` contains the baseline, 3 shots, the second-service shot and `final.mp4` (15–25 s).
4. [ ] `video_spec.md` lists services, models, prompts, settings, attempts and the cost table.
5. [ ] `video_qa.md` has the 6-item checklist for every shot and both joins, two comparisons and a conclusion.
6. [ ] Reviewer `ihar_rubanovich@epam.com` invited as repository collaborator.
