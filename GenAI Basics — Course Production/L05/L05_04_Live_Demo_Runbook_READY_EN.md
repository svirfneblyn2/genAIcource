# Lesson 05 • Live Demo Runbook & Prompt Copybook
## Curated Prompts and Workflows for Live AI Video Demonstrations

**Course:** GenAI Basics • Module 2 (Multimodality)  
**Instructor:** Igor Rubanovich (EPAM Systems • `ihar_rubanovich@epam.com`)  
**Platforms (October 2026):** Kling 3.0 (Web & API), Runway Gen-4.5, Google Veo 3.1 (Gemini API / Vertex AI) and Gemini Omni (Gemini app / Flow), Luma Ray3.2 (Dream Machine), HeyGen / Hedra. Sora is shut down (app 26.04.2026, API 24.09.2026).  
**Code:** a short `google-genai` (Veo) example: slide 16 and Block 9 below. The notebook `L05_Video_Generation_API_Pipeline.ipynb` uses the real Veo 3.1 API; paid calls are off by default (`RUN_PAID = False`).

This reference runbook allows instructors and students to copy prompts, paste them into their preferred platforms alongside reference keyframes from L04, and get more predictable results. There are no guarantees: check every clip against the acceptance checklist (slide 18).

> **Mapping to the v2 deck (21 slides):** Block 2 → slides 5, 6, 10 • Block 3 → slide 11 • Block 4 → slides 6, 10 • Blocks 5–6 → slide 12 • Block 7 → slide 20 (Track A) • Block 9 → slide 16 • Block 10 → slide 7 (storyboard template) and slide 17 (Kling credits) • Blocks 1, 8: outside the deck (extra material; sound and speech are in L06).  
> **In class** we show only the ready clips from `demo_veo_showcase/` (no new generations), on click and muted. In Microsoft Teams, turn on “Optimize for motion and video” when sharing your screen.

---

## Table of Contents

1. [Block 1: Hook Quiz (4 Video Clips A–D)](#block-1-hook-quiz-4-video-clips-ad)
2. [Block 2: Free-form Prompt Trap vs 6-Slot Temporal Prompt](#block-2-free-form-prompt-trap-vs-6-slot-temporal-prompt)
3. [Block 3: Cinematographer's Camera Vocabulary (Pan, Dolly, Orbit, FPV)](#block-3-cinematographers-camera-vocabulary)
4. [Block 4: Image-to-Video Pipeline (Glovo Courier in Rain)](#block-4-image-to-video-pipeline-glovo-courier-in-rain)
5. [Block 5: Motion Brush (Bicycle Wheels & Splashes + Static Zone)](#block-5-motion-brush-regional-dynamics)
6. [Block 6: First & Last Frame Interpolation](#block-6-first--last-frame-interpolation)
7. [Block 7: E-Commerce Product Packshot (Coffee Mug: Orbit & Steam)](#block-7-e-commerce-product-packshot)
8. [Block 8: Talking Avatar & Audio Lip-Sync](#block-8-talking-avatar--audio-lip-sync)
9. [Block 9: Asynchronous Python SDK Pipeline](#block-9-asynchronous-python-sdk-pipeline)
10. [Block 10: The Production Storyboard Matrix (Creator Tools Studio Case)](#block-10-the-production-storyboard-matrix-creator-tools-studio-case)

---

## Block 1: Hook Quiz (4 Video Clips A–D)

> **Not used in the v2 deck:** the slide 2 hook is the finished `final` clip (23 s). This block is kept as extra material.  
> **Objective:** Interactive calibration of the audience's eye on microscopic physical flaws and temporal artifacts.  
> **Format:** 16:9, 24 fps, duration 4–5s.

### Clip [A] • Canyon FPV Drone Dive (Google Veo 3.1)
```text
High-speed cinematic FPV drone dive down a dramatic red sandstone canyon, skimming just inches above jagged rocks and desert brush, golden hour sunlight flaring across the camera lens, extreme motion blur on foreground rocks, perfectly smooth stabilization.
```

### Clip [B] • Macro Coffee Splash Slow-Mo (Runway Gen-4.5)
```text
Extreme macro close-up, 120fps high-speed phantom camera footage: dark rich espresso pouring into a ceramic mug, liquid creating a deep vortex, tiny microscopic droplets splashing upwards in zero-gravity slow motion, warm morning backlight illuminating steam particles.
```

### Clip [C] • Dialogue Close-Up (Kling 3.0 Omni)
```text
Cinematic tight portrait of a 28-year-old woman speaking passionately in an emotional dialogue, authentic natural eye blinks, subtle micro-movements of facial muscles and eyebrows, natural dental texture, shallow depth of field, 85mm portrait lens, 24fps.
```

### Clip [D] • Neon Tokyo Rain (Wan 2.2 MoE)
```text
A rainy night on a bustling Tokyo pedestrian crossing, pedestrians holding transparent umbrellas, neon signs reflecting coherently in deep asphalt puddles, camera smoothly tracking forward at waist height, anamorphic lens flares, wet reflective textures.
```

---

## Block 2: Free-form Prompt Trap vs Engineering Pipeline (Veo / Kling Showcase)

> **Objective:** Visually demonstrate how a naive stream-of-consciousness prompt in Text-to-Video catastrophically breaks physics, kinematics, and editorial cuts, and how an engineering 3-shot image-to-video decomposition produces broadcast-grade commercial output.  
> **Prepared Assets:** Folder `demo_veo_showcase/` with keyframes `shot1_cafe_pickup.png`, `shot2_bike_rain.png`, `shot3_map_route.png` and FFmpeg stitching script `assemble_montage.py`.

### 2.1. Naive Stream of Consciousness (Trainwreck, Text-to-Video)
```text
Our friendly Glovo delivery courier enters a warm cozy Scandinavian cafe, walks up to the wooden counter and picks up a brown paper food delivery bag, puts it securely inside her turquoise backpack, then cuts to her riding a city bicycle through the rainy avenue at dusk with glowing streetlights and wet cobblestones, and then camera zooms in to a digital smartphone map with a glowing navigation route arrow pointing to the delivery address.
```
*What to observe (4 typical failures, from the real clip `trainwreck_naive_t2v.mp4`, slide 5):*
1. **00:02, action skipped:** the bag stays on the counter; it never goes into the backpack.
2. **00:03, details drift after the cut:** the logo on the box changes (“Glono” → “Glovo”); also an example of brand damage.
3. **00:05, scene geometry breaks:** handlebars with a phone slide into the frame while the courier is still riding ahead.
4. **00:07, garbled text:** “Delivery Admest” instead of “Delivery Address”.

One cause: the model got 3 scenes and 5 actions for 8 seconds.

### 2.2. Professional 6-Slot Engineering Prompt (Single Shot)
```text
[Subject & State]: Young Glovo delivery courier wearing a vibrant yellow jacket with gray reflective stripe and a matte black helmet, seated on a gravel bicycle.
[Action Vector]: Pedals forward at a steady moderate rhythm, body leaning slightly forward, hands firmly gripping drop handlebars, wheels spinning smoothly forward.
[Camera Trajectory]: Smooth low-angle tracking shot moving parallel to the bicycle on the left, camera locked at wheel height, steady horizon, zero camera shake.
[Environment Dynamics]: Wet city street at dusk, tires cutting through shallow rainwater puddles with fine water spray, neon shop reflections shimmering on asphalt.
[Lighting & Tempo]: Cinematic twilight, warm sodium streetlights, 24fps film motion blur, natural momentum and deceleration.
[Negative Constraints]: No backwards wheel rotation, no morphing of bicycle frame, no extra limbs, no camera jitter, no unrealistic speed bursts.
```
*Note:* the “Negative” slot works where a separate negative prompt field exists (Kling, Wan). For Veo, rephrase positively (“wheels spinning forward”, “smooth steady camera”). The actual prompt of our shot 2 is on slide 10.

---

## Block 3: Cinematographer's Camera Vocabulary

> **Objective:** Demonstrate camera controllability using standardized cinematography terms.  
> **Service:** Runway Gen-4.5 (camera by words or direction/strength controls) / Kling 3.0 (camera parameters or words in the prompt) / Gemini, Flow (words only).  
> **Format:** 16:9, duration 5s (Veo 3.1: 4/6/8s). Tip: one camera move per shot.

### 3.1. Dolly In (Physical push-in with optical parallax)
```text
Cinematic slow Dolly In on an antique brass microscope standing on an oak laboratory table, foreground dust particles drifting, background bookshelf softly blurring, 35mm lens, steady camera movement forward.
```

### 3.2. Orbit / Arc Shot
```text
Smooth slow orbit arc shot revolving partway around a luxury mechanical wristwatch placed on dark volcanic stone, continuous smooth counter-clockwise camera circle, subtle glints of light reflecting off the sapphire glass.
```

### 3.3. Crane Up / Jib Shot
```text
Camera starts at ground level looking at autumn fallen leaves on wet cobblestones, then smoothly cranes upward 10 feet into the air to reveal a historic European cathedral square at sunrise.
```

---

## Block 4: Image-to-Video Pipeline (Glovo Courier in Rain)

> **Objective:** Master production workflow. Animating an approved static keyframe from L04 without identity drift.  
> **Source Asset:** `GenAI Basics — Course Production/L04/assets/examples/C2_rain.jpg`  
> **Input Slot:** the first-frame (image-to-video) field in Kling 3.0 / Runway Gen-4.5 / Flow (Veo 3.1).

### Motion Prompt (camera + action + motion details):
```text
The courier begins pedaling forward down the rainy street, bicycle wheels rotating smoothly forward cutting through puddles with realistic water spray. Soft rain streaks fall diagonally across the frame. Camera tracks steadily alongside at bicycle speed. Background urban buildings and streetlights blur with gentle motion bokeh. Maintain exact facial features, curly hair, earring, and yellow jacket colors unchanged.
```

*Recommended UI Parameters:*
* Camera: in words in the prompt (“tracking shot alongside”). Where dedicated controls exist (direction and strength in Runway, camera parameters in Kling), pick one horizontal move with no zoom.
* Duration: `5s` (Veo 3.1: `4/6/8s`).
* Exact numbers in the controls depend on the service; there are no universal values.

---

## Block 5: Motion Brush (Regional Dynamics)

> **Objective:** Set what moves in the frame and where, and keep the background still (slide 12).  
> **Platform:** Kling, Motion Brush tool, available on Kling 1.x–2.x models; not in the Kling 3.0 feature list. Officially: up to 6 selected elements, each with its own 2D trajectory arrow drawn on the frame, plus a Static Brush (static zone). There is no Z axis and no numeric speed.  
> **Source Asset:** `C2_rain.jpg`.

### Assignments:
1. **Element 1, the courier with the bicycle:** a trajectory arrow in the direction of travel (forward along the street).
2. **Element 2, splashes from the puddle by the wheel:** a short arrow from the puddle up and back.
3. **Static Brush, background (buildings, streetlights):** a static zone; the background does not move.

The courier’s appearance (face, jacket, backpack) is held by the approved first frame (image-to-video), not by a mask. Results are more stable but not guaranteed: check against the checklist.

---

## Block 6: First & Last Frame Interpolation

> **Objective:** A controlled narrative transition between two fixed story states (the model fills in the motion between two images).  
> **Platform:** “first + last frame” mode: Kling 3.0 / Veo 3.1 (Flow; `lastFrame` in the API) / Gemini Omni / Hailuo H3.  
> **Start Frame:** `C3_door.jpg` (Courier receiving bag at coffee counter).  
> **End Frame:** `C4_rest.jpg` (Courier exiting glass door onto sidewalk).

### Bridge Prompt:
```text
The courier nods politely to the barista, turns around with the paper bag securely held in one hand, walks smoothly across the polished wooden floor toward the glass entrance door, pushes the door open with his elbow, stepping out onto the street. Physically plausible human movement, natural weight shift, seamless transition between keyframes.
```

---

## Block 7: E-Commerce Product Packshot (Coffee Mug: Orbit & Steam)

> **Objective:** Commercial product reel created from a static L04 packshot (homework Track A, slide 20).  
> **Source Asset:** `D0_packshot.png` or `A3_details.jpg`.  
> **Platform:** Kling 3.0 / Luma Ray3.2 (Luma has ready-made Orbit left/right moves; there is no “360° orbit mode”) / Flow (Veo 3.1), image-to-video.

### Packshot Animation Prompt:
```text
Camera performs an elegant slow orbit arc around the ceramic coffee mug on the wooden counter, thin delicate wisp of aromatic steam rising and swirling gracefully from the hot dark coffee, warm morning sunlight creating shimmering caustic reflections inside the mug, premium cinematic commercial lighting, smooth steady motion.
```

---

## Block 8: Talking Avatar & Audio Lip-Sync

> **Not shown in the v2 deck:** sound and speech are covered in L06.  
> **Objective:** Talking avatar for enterprise training and customer support. Avatars/lip-sync are a separate niche; general video models (Veo 3.1, Kling 3.0, Seedance etc.) can also generate dialogue with audio.  
> **Platform:** HeyGen (Avatar V) / Hedra (Character-3, Omnia) / Kling 3.0 (dialogue with native audio).  
> **Source Image:** Close-up courier headshot or support representative portrait.  
> **Audio Track:** Synthesized speech clip (TTS or recorded audio).

### Dialogue Line for Phoneme Validation:
```text
"Hello! Your coffee order has been safely picked up. I am already en route to your address and should arrive in approximately twelve minutes. Please keep your phone handy!"
```
*Validation Points:* Labial consonant closure (B, P, M), organic eye blink cadence, absence of dental artifacts.

---

## Block 9: Asynchronous Python SDK Pipeline

> **Objective:** Show what it looks like in code (slide 16, reference only; the homework needs no code).  
> **Library:** `google-genai` (the same as in L03 and L04), key from the `GEMINI_API_KEY` variable. No free tier for Veo. At 720p: Veo 3.1 $0.40/s, Fast $0.10/s, Lite $0.05/s; only successful videos are billed.

```python
import time
from google import genai
from google.genai import types

client = genai.Client()  # key from GEMINI_API_KEY
op = client.models.generate_videos(
    model="veo-3.1-fast-generate-preview",
    prompt="Tracking shot alongside the courier",
    image=types.Image.from_file(location="shot2.png"),
)
while not op.done:  # wait: ~11 s to ~6 min
    time.sleep(10)
    op = client.operations.get(op)
video = op.response.generated_videos[0].video
client.files.download(file=video)
video.save("shot2.mp4")
```

Three steps: **send → wait → download**. Video takes a while, so the service immediately returns a “ticket” (an operation), and we ask every 10 seconds whether it is ready.

---

## Block 10: The Production Storyboard Matrix (Creator Tools Studio Case)

> **Objective:** Demonstrate the enterprise standard for engineering multi-shot generative videos (Multi-Shot Video Pipeline) using an authentic R&D production case from the speaker's portfolio: the 10-episode historical pseudo-documentary series *Giant Stories* (Creator Tools R&D lab).  
> **Key Insight:** Studio-grade generative video does not start in a diffusion playground; it begins inside a **7-column Storyboard Matrix**, where each 5-second cut is pre-linked to optical focal lengths, motion kinematics, Foley layers, and musical underscores.

### 10.1. The Standard 7-Column Storyboard Matrix

| # | Shot / Timing | Key Visual Hook | Voice-Over Line | IMAGE Prompt (Optics, Light, Style) | VIDEO Prompt (Kinematics, Dynamics, Artifacts) | Foley SFX Layer | Music Underscore Hook |
| :- | :- | :- | :- | :- | :- | :- | :- |
| **01** | `Sealed Crate 1929` (5s) | Sealed Customs crate `PECOS 1423` in customs vault | *“This crate was sealed by Customs in 1929, and no one has opened it since...”* | `16:9 cinematic aspect-ratio, grainy black-and-white archival still. Dim Customs vault, single brass gas-lamp overhead (2700K). Weathered pine crate stencilled "PECOS 1423 • CONFIDENTIAL". Cobweb traces, dust motes. Negative: no color, no modern barcodes, no LED.` | `16:9 archival motion, 5s. Handheld dolly-in (35mm) from darkness toward lamplit crate. Slow speed-ramp; subtle handheld micro-shake; gate-weave flicker. Negative: no morphing, no digital noise.` | Vault hum, dripping water, rat scuttle | Low bowed bass drone, muted brass swell |
| **02** | `Drill Strike` (5s) | Surveyors at oil rig strike fossilized titan bone | *“A routine oil survey struck something harder than granite...”* | `16:9 cinematic b&w still, 24mm wide lens. High-noon desert sun, Rio Grande brush. Three oil drillers in grease-stained coveralls frozen in shock around drill pit, massive fossilized bone exposed in clay.` | `16:9 crane-down, 5s, 24mm. Shot starts on dust-blown sky, smoothly descends toward excavation pit; soil crumbles, heat haze shimmers. Steady descent.` | Cicadas, shovel scraping stone, gasping breath | Deep tom hit → ominous sub-bass pulse every 2s |
| **03** | `Rotary Press` (5s) | Rotary newspaper printing press churning headlines | *“Papers from San Antonio to Houston screamed of a twelve-foot titan...”* | `16:9 overhead pressroom still, 40mm lens. Historic rotary printing press in full motion, fresh newspapers with bold headline "GIANT UNEARTHED", ink mist, harsh industrial pendants.` | `16:9 whip-pan, 5s, 40mm. Rapid whip-pan starting from spinning mechanical gears, landing crisp and locked on the moving paper headline. Frame jitter, paper flutter.` | Press clatter, ink hiss, stamp thud | Rising string tremolo |
| **04** | `Smithsonian Denial` (5s) | Government clerk typing denial letter | *“The Smithsonian swore the shipment never arrived...”* | `16:9 desk-level still, 50mm lens. Green banker lamp casting warm pool of light (2700K). Remington typewriter, typed official refusal letter, wax stamp, cigarette smoke curling.` | `16:9 macro push, 5s, 50mm. Slow push-in racking focus from typewriter keys to ink signature and red "DENIED" stamp. Zero camera shake.` | Typewriter clack, carriage bell, desk lamp hum | Solo cello mourning phrase, ticking metronome |

---

### 10.2. Precision Cinematography & Optical Lens Grammar

Specifying authentic optical properties (focal lengths, aperture, light Kelvin) drastically reduces diffusion ambiguity:

1. **24mm Wide-Angle (Epic Scale & Environmental Context):**
   * *Camera Prompt:* `16:9 crane-down, 24mm wide lens. Smooth descent from wide horizon down to foreground rocks; pronounced perspective distortion on edges, expansive depth of field.`
2. **35mm Cinematic Street/Action (Natural Human Eye POV):**
   * *Camera Prompt:* `16:9 handheld tracking shot, 35mm lens. Camera glides forward at waist height following the subject; gentle natural sway, balanced foreground/background relationship.`
3. **40mm Whip-Pan (Kinetic Scene Transition):**
   * *Camera Prompt:* `16:9 rapid whip-pan, 40mm lens. Fast directional camera sweep with intense horizontal motion blur, resolving instantly onto stationary subject.`
4. **45mm Parallax Slide (Dimensional Spatial Depth):**
   * *Camera Prompt:* `16:9 lateral parallax tracking slide, 45mm lens. Camera slides horizontally left to right; foreground objects move noticeably faster than background, creating tactile dimensional depth.`
5. **50mm Macro Push & Rack-Focus (Dramatic Detail Focus):**
   * *Camera Prompt:* `16:9 macro push, 50mm lens, f/2.0 shallow depth of field. Camera pushes forward 10 inches while racking focus smoothly from blurred foreground object to pin-sharp background detail.`
6. **60mm Orbit Arc (Product / Artifact Hero Showcase):**
   * *Camera Prompt:* `16:9 continuous 180-degree orbit, 60mm lens. Smooth circular tracking around the central subject, background slowly rotating with creamy bokeh.`

---

### 10.3. ChatGPT Script Generation Pattern (Self-Reflection Loop)

To prevent LLMs from emitting generic marketing fluff, use an iterative script generation prompt with an embedded self-critique step:

```text
Act as an elite documentary film director and visual showrunner.
Let's work step-by-step to generate a suspenseful 6-scene storyboard (each shot strictly 5 seconds).

For each scene:
1. Describe the key visual action and emotional beat.
2. Formulate the exact voice-over line (maximum 12 words, tense and cinematic).
3. Draft a 16:9 Image Prompt specifying lens focal length (mm), lighting temperature (Kelvin), and historical textures.
4. Draft a matching 16:9 Video Motion Prompt specifying exact camera kinematics (dolly, crane, whip-pan) and physical dynamics.
5. SELF-REFLECTION STEP: Before finalizing the scene, ask yourself: "What specific visual flaw or ambiguity would cause a video diffusion model to morph or hallucinate here?" Add explicit negative constraints to eliminate that risk.

Let's begin with Scene 1.
```

---

### 10.4. Production Economics & Token Efficiency in Kling AI

Hard-learned operational guidelines from Creator Tools production:
1. **Single Output Mode:** In Kling's web UI, 2 outputs per prompt are selected by default. Always toggle to **1 output** for initial iterations; this saves **50% of your credit budget**.
2. **Short segments instead of long ones:** Kling 3.0 can do 3–15 s per generation, but don’t start drafts with long clips: short shots are more stable than long ones, and mistakes in a long scene are more expensive to redo. Generate 5-second shots and join them in an editor (slide 13); an extended clip accumulates drift (slide 7).
3. **Watermark and labelling:** even if a service lets you download a clip without a visible watermark, keep the “AI-generated” label when you publish (EU AI Act, Art. 50, slide 19).
4. **Offline AI Upscaling:** Commercial cloud upscalers within video SaaS tools consume expensive credits and often blur high-frequency textures. The studio standard is generating at 1080p and applying local upscaling via Topaz Video AI (Proteus/Iris models) to preserve fine grain.

