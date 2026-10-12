# Instructor Script • Lesson 05: Video Generation — From a Key Frame to a Finished Clip (90 Minutes)

**Course:** GenAI Basics • Module 2 (Multimodality) • Lesson 05 of 16  
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems  
**Audience:** GenAI beginners from many roles. Plain language, no formulas or jargon; code only as one short reference example.  
**Format:** 19 slides (`presentation_L05_Video_Generation_EN_v2.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 12  
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen. Videos start **on click** and play **muted**.  
**Materials:** ready clips from `demo_veo_showcase/` (Veo 3.1, 8 s each: shots 1–3, final `courier_delivery_final.mp4` = 23 s, failure `trainwreck_naive_t2v.mp4`), the character sheet and frames from L04, homework `L05_05_Homework_EN.md`  
**Models in this lesson (facts as of October 2026):** Veo 3.1 / Fast / Lite (our clips), Gemini Omni 1.1 Flash, Kling 3.0, Runway Gen-4.5, Luma Ray3.2, Seedance 2.5, Hailuo H3, Wan 3.0, open-weight Wan 2.2 and LTX-2. Sora 2 is **shut down** (app 26.04.2026, API 24.09.2026).

**Lesson objective:** students understand how a video model creates motion and why “everything in one prompt” breaks; can build a clip step by step — references → key frame → director’s prompt (camera + action + motion details) → short shots → editing; know what is on the market now, what a second of video costs, how to check a clip with a checklist, and what the risks of generated video are.

> **Before you start (Teams):** when sharing your screen, turn on **“Optimize for motion and video”**, otherwise the clips will stutter. Share the browser window with the deck. Do not share computer sound — clips are shown muted.

---

## Lesson Roadmap & Timing (19 slides • 90 minutes incl. a 5-minute break)

| Slide | Block | Timing | Min | On screen | Key takeaway |
|---|---|---|---|---|---|
| **01** | Cover | 00:00 — 02:00 | 2 | Frame from shot 2 | Today we bring the L04 images to life. |
| **02** | Hook: the finished clip | 02:00 — 06:00 | 4 | `final` video (23 s) + 3 numbers | 3 shots, 8+8+8 → 23 s, ≈ $10 at list price. We take every step apart. |
| **03** | How a model makes video | 06:00 — 11:00 | 5 | Noise → step-by-step cleanup → frames; “no physics engine” plaque | The model knows what motion *looks like*; it does not compute physics. |
| **04** | Failure gallery | 11:00 — 17:00 | 6 | `trainwreck` video + 4 frames | 3 scenes and 5 actions in 8 seconds → 4 typical failures. |
| **05** | T2V vs I2V | 17:00 — 23:00 | 6 | Two videos side by side + two flow diagrams | First the frame, then the motion. |
| **06** | References | 23:00 — 27:00 | 4 | Character sheet with callouts | A reference narrows the model’s choices; more stable, not guaranteed. |
| **07** | Key frame in chat | 27:00 — 31:00 | 4 | Sprite → draft → approved | An image edit costs seconds and cents; video costs minutes and $0.40/s. |
| **08** | Director’s prompt | 31:00 — 37:00 | 6 | Shot 2 prompt with 6 colour-coded slots + `shot2` video | Motion verbs; don’t retell the frame; say what should happen. |
| **09** | Camera language | 37:00 — 42:00 | 5 | 8 static camera-move diagrams | Models understand camera terms. One move per shot. |
| **10** | Precise control | 42:00 — 46:00 | 4 | Motion Brush illustration + 3 tiles | First/last frame, extend, references — what really exists in 2026. |
| **11** | Editing | 46:00 — 51:00 | 5 | 8+8+8 timeline with 0.5 s transitions = 23 s + `final` video | The model makes a shot; a person builds the story. |
| **12** | **Break** | **51:00 — 56:00** | **5** | **Timer** | **Rest only.** |
| **13** | Market, October 2026 | 56:00 — 63:00 | 7 | Clip-length bars + capability chips; Sora 2 shut down | Audio is standard, clips are 10–30 s; rankings change — check the date. |
| **14** | Code (for reference) | 63:00 — 66:00 | 3 | ~15 lines of `google-genai` + price per second | Send → wait → download. You pay per second. |
| **15** | Economics | 66:00 — 71:00 | 5 | Bar chart $96 / $28.80 / $7.20 | Count seconds, not attempts. |
| **16** | Quality check | 71:00 — 76:00 | 5 | Defects from our shots 2–3 + 6-item checklist | Checking is a separate step; the checklist = homework rubric. |
| **17** | Risks & provenance | 76:00 — 82:00 | 6 | Traffic light + SynthID vs C2PA; EU AI Act Art. 50 | Own characters — yes; other brands — with permission; real people — only with consent. |
| **18** | Homework | 82:00 — 87:00 | 5 | Track A (product) / Track B (courier) | T2V for comparison, I2V in two services, `video_spec.md`, `video_qa.md`. |
| **19** | Summary + L06 teaser | 87:00 — 90:00 | 3 | 4 rules + final frame | Models already make sound themselves — covered in L06. |

---

## Detailed Script & Talk Tracks (Slides 01 — 19)

### Part 1: How video works and how to build a clip step by step (00:00 — 51:00)

---

### Slide 01 (00:00 — 02:00) • Cover: Video Generation
**On Screen:** Background — a frame from shot 2 (the courier in the rain). Kicker: `GenAI Basics • Lesson 05 • Module 2: multimodality`. Title: `Video Generation`. Subtitle: `From a key frame to a finished clip`. Caption: the lesson’s models — Veo, Gemini Omni, Kling, Runway, Luma, Wan — as of October 2026. Key hints at the bottom.

*(Before you begin: Teams screen sharing is already on with “Optimize for motion and video”. The deck is open in the browser in fullscreen — key `F`.)*

#### Speaker's Talk Track:
> "Hi everyone! We are continuing the second module — multimodality.
> 
> Last time we made images: the courier, the character sheet, a product packshot. Today those images come to life — we make video.
> 
> The plan is simple. First we watch a finished clip. Then we see how a model actually makes video. Next, a real failure: what you get if you ask for everything in one prompt. And then we build the clip properly, step by step. After the break: what is on the market now, a tiny bit of code, money, how to check a finished video, and the risks.
> 
> One technical note: today I start every clip with a click and show it muted. If the picture stutters for you, write in the chat."

---

### Slide 02 (02:00 — 06:00) • Hook: start with the result
**On Screen:** Left — the `final` video (23 s, click to play, muted). Right — three numbers:
- `3 shots` — each made from a ready key frame (image-to-video);
- `8+8+8 → 23 s` — joined with two 0.5 s transitions;
- `≈ $10` — 3 × 8 s × $0.40, Veo 3.1 list price, 720p, retries not counted.

Bottom plaque: `Today we take it apart step by step. And we start with a failure: what happens if you ask for all of it in one prompt.`

#### Speaker's Talk Track:
> "Let’s start with the result. I’ll play a short clip — 23 seconds."

*(Click the video. Let it play to the end. Optionally play it a second time.)*

> "Question for the chat: what did you see? How many separate ‘takes’ do you think there were, and where are the cuts?"

*(Pause 20–30 seconds, read the answers in the Teams chat.)*

> "Answer: these are three separate 8-second clips. All three were made by Google’s Veo 3.1. And an important detail: the model made each clip not from text but from a prepared image — that mode is called image-to-video.
> 
> Then the clips were joined with two half-second transitions. That is why 8 + 8 + 8 gives 23 seconds, not 24.
> 
> What does it cost? At Veo 3.1 list price, one second of 720p video is 40 cents. Three 8-second clips — about ten dollars. That is without failed attempts; we’ll talk about those separately.
> 
> One sentence about sound: these clips actually have audio — modern models generate it themselves. Today we watch muted; sound is covered in detail in Lesson 06.
> 
> Today we take every step of this clip apart. But we start with a failure."

---

### Slide 03 (06:00 — 11:00) • How a model makes a video
**On Screen:** A three-step diagram (no formulas):
1. `Noise` — start: random noise for all frames of the clip at once.
2. `Step-by-step cleanup` — the video is cut into pieces “place in frame × moment in time”; dozens of steps remove noise; the text and the first frame guide every step.
3. `Frames` — 24 frames per second that agree with each other.

Plaque: `There is no physics engine inside. The model has seen millions of videos and knows what motion usually looks like. So it fails where exact rules matter: hands and objects in contact, text, long scenes.` Caption: schematic made from frames of our shot 2, noise added for illustration.

#### Speaker's Talk Track:
> "How does a model make video at all? No formulas.
> 
> Remember L04: an image was born from noise in dozens of steps. Step by step the model removed noise until a picture appeared.
> 
> Video is the same. The only difference: the model cleans not one frame but the whole stack of frames in the clip at once. That is why neighbouring frames agree with each other and the motion looks smooth.
> 
> To make this manageable, the video is cut into small pieces: ‘this corner of the frame at this moment in time’. The prompt text and, if we gave one, the first frame tell the model at every step what should come out.
> 
> Now the most important thing on this slide — the yellow plaque. **There is no physics engine inside.** The model does not compute the laws of physics. It has seen a huge number of videos with steam, rain and splashes and learned to draw them convincingly. Research confirms this — for example, the 2025 Physics-IQ test: realistic-looking is not the same as physically correct.
> 
> The practical takeaway: expect mistakes where exact rules matter. Hands holding an object. Text and numbers. Long scenes with a lot going on. On the next slide we see all of this live."

---

### Slide 04 (11:00 — 17:00) • Failure gallery: everything in one prompt
**On Screen:** Left — the `trainwreck` video (Veo 3.1, 8 s, text only) and the shortened prompt with `then cuts to` / `and then` highlighted. Right — 4 frames with timecodes:
- `00:02` **Action skipped** — the bag stays on the counter; it never goes into the backpack;
- `00:03` **Details drift after the cut** — the logo on the box changes: “Glono” → “Glovo”;
- `00:05` **Space breaks** — handlebars with a phone slide in while the courier is still riding ahead;
- `00:07` **Pseudo-text** — “Delivery Admest” instead of “Delivery Address”.

Bottom: `One cause: the model got 3 scenes and 5 actions for 8 seconds.`

#### Speaker's Talk Track:
> "This is what you get when you brief a model the way you brief a person. Look at the prompt on the left: the courier walks into a cafe, picks up a bag, puts it in the backpack, *then* rides a bicycle in the rain, *and then* the camera moves in on a phone map. All in one paragraph. Playing it — 8 seconds."

*(Click the video, let it play to the end.)*

> "Now let’s go through the four frames.
> 
> One — **the action is skipped**. The bag stays on the counter. Nobody puts it into the backpack.
> 
> Two — **details drift after the cut**. The logo on the box changes before your eyes. It also shows how a model damages a brand: ‘Glono’ appears instead of the name. In a commercial clip that is a reject. Glovo is just the name of our training case, as in the L04 homework. The logo in the clip is an example of what not to do.
> 
> Three — **space breaks**. Instead of a clean cut, the handlebars with a phone just slide over the shot while the courier is still riding ahead.
> 
> Four — **pseudo-text**. The phone screen says ‘Delivery Admest’ instead of ‘Delivery Address’. The model knows what letters *look like* but cannot write.
> 
> All four failures have one cause: in 8 seconds we gave the model three scenes and five actions. A model cannot edit a film because the text asks it to. Hence the first rule: **one clip — one scene and one action.**"

*(Chat question if time allows: “Which of the four failures would you notice first as a viewer?”)*

---

### Slide 05 (17:00 — 23:00) • First the frame, then the motion (T2V vs I2V)
**On Screen:** Two videos side by side.
- Left: `T2V` badge — text-to-video, text only (`trainwreck` video). Diagram: `Text → The model decides what is in frame and how it moves → ✗ two tasks at once`.
- Right: `I2V` badge — image-to-video, ready frame + text (`shot1` video). Diagram: `Frame ✓ + text about motion → The model decides only how it moves → ✓ one task`.

Plaque: `Rule: lock appearance, light and composition in an image (the L04 skill). Leave only motion to the video model.`

#### Speaker's Talk Track:
> "This is the key technique of the lesson. I’ll play both clips one after another."

*(Click the left video, then the right one. 8 seconds each.)*

> "On the left is what we have already seen: text only. On the right is the same courier story, but the model got a ready first image.
> 
> Two terms we’ll use for the rest of the lesson. **T2V** — text-to-video, video from text. **I2V** — image-to-video, video from an image plus text.
> 
> What’s the difference? In T2V the model solves two tasks at once: it invents *how everything looks* — face, clothes, light, the cafe — and *how it moves*. Two unknowns at the same time, and it can get either one wrong.
> 
> In I2V the first task is already solved: a person approved the image. Only motion is left for the model. So there are fewer errors, and they are more predictable.
> 
> And we already know how to make images — that’s the L04 skill. The rule on the plaque: lock appearance, light and composition in the image, and leave only motion to the video model.
> 
> Next we go step by step: references, key frame, prompt, camera, control, editing."

---

### Slide 06 (23:00 — 27:00) • Step 1: references and the character sheet
**On Screen:** The L04 character sheet (one courier from four angles) with anchor callouts: `face, short curly hair`, `turquoise box backpack`, `yellow jacket, reflective stripe`, `black trousers, white sneakers`. Right:
- A reference narrows the model’s choices: less room to “invent” the look.
- Veo 3.1 — up to 3 reference images; Kling 3.0 — Elements, 2–4 images.
- More stable, but not guaranteed — check every shot by eye.

Bottom right — frames from shots 1 and 2: the same courier.

#### Speaker's Talk Track:
> "Step one — references. You remember this character sheet from L04: the same person from four angles.
> 
> The callouts are anchors viewers use to recognise the hero: face and short curls, the yellow jacket with a reflective stripe, the turquoise box backpack, black trousers and white sneakers. If the jacket suddenly turns green in one shot, viewers will think it is a different person.
> 
> What does a reference do? No magic. It simply **narrows the model’s choices**: there is less room to invent how the hero looks.
> 
> Where it exists today: Veo 3.1 takes up to three reference images. In Kling 3.0 it is called Elements — two to four images.
> 
> And honestly: the result is more stable but **not guaranteed**. So we still check every shot by eye — there is a checklist at the end of the lesson. Bottom right are frames from our shots 1 and 2 — the courier is recognisable."

---

### Slide 07 (27:00 — 31:00) • Step 2: perfect the key frame in chat
**On Screen:** A strip of three frames: `Sprite` (game source art) → `Draft` (prompt: “Make a realistic 16:9 frame from this sprite”; wrong helmet and tabard) → `Approved ✓` (edit: “Bare hands, tabard in white and blue rectangles, a flat ‘kettle’ helmet”; the first frame for video). Below, two blocks: `seconds · cents` — one image edit in chat; `minutes · $0.40/s` — one video regeneration (Veo 3.1, 720p).

#### Speaker's Talk Track:
> "Step two — the key frame. A short example in the style of L04: we take a tiny knight sprite from an old game and ask the chat for a realistic 16:9 frame based on it.
> 
> The first version is close, but the helmet and tabard are wrong. We don’t start over — we write one precise edit: bare hands, a tabard in white and blue rectangles, a flat helmet like a kettle. And the frame is approved. That becomes the first frame for the video.
> 
> Why does this matter for video specifically? Look at the two blocks below. One image edit in chat costs seconds and cents. One video regeneration costs minutes of waiting and, for example, 40 cents for *every second* in Veo 3.1.
> 
> So the rule: fix any appearance mistake in the image while it is cheap. Get the frame to ‘yes’ first, and only then animate it."

---

### Slide 08 (31:00 — 37:00) • Step 3: the director’s prompt — 6 motion slots
**On Screen:** A legend of 6 coloured slots: `1 Camera`, `2 Who`, `3 Action`, `4 Where & when`, `5 Motion details`, `6 Light`. In large type — the actual prompt of shot 2 (Veo 3.1, I2V), each part highlighted in its colour:

```text
Dynamic tracking shot moving forward alongside the courier. The same courier with short cropped curly hair pedals her bicycle forward through the rain-slicked city avenue at twilight. Wheels spinning smoothly forward with water spray cutting through shallow puddles. Wet cobblestones reflecting warm shop lights and streetlamps.
```

Right — the `shot2` video (the result). Below, three rules: motion verbs; don’t retell the frame; say what should happen (a separate negative prompt field exists only in some tools — Kling, Wan).

#### Speaker's Talk Track:
> "Step three — the prompt. This is the actual prompt used for our shot 2. Let’s go through it by colour.
> 
> First, blue — **camera**: the camera moves forward alongside the courier. Second — **who**: the same courier with short curly hair. Third — **action**: pedals her bicycle. Fourth — **where and when**: a wet avenue at twilight. Fifth — **motion details**: wheels spinning forward, water spraying from puddles. Sixth — **light**: wet cobblestones reflecting shop lights and streetlamps.
> 
> In L04 images also had six slots. For video the key ones are camera, action and motion details. Here is the result."

*(Click the video on the right, 8 seconds.)*

> "Three rules.
> 
> First — **motion verbs**: pedals, spinning, tracks. The model needs to know what changes over time. ‘A beautiful courier in the rain’ is a picture, not a video.
> 
> Second — **don’t retell the frame**. In I2V the image is already there and the model sees it. No need to describe the jacket, backpack and sneakers again. One short anchor for the hero — ‘with short curly hair’ — is enough to keep the look from drifting.
> 
> Third — **say what should happen**, not what shouldn’t. A separate ‘what not to show’ field — the negative prompt — exists only in some tools, for example Kling and Wan. In Veo positive phrasing works better: not ‘no shake’ but ‘smooth camera’."

---

### Slide 09 (37:00 — 42:00) • 8 camera moves that models understand
**On Screen:** A grid of 8 static diagrams (camera is blue, subject is yellow, motion is the green arrow), each with a prompt phrase:
`Static` — static camera, locked-off shot · `Pan` — slow pan left across the street · `Tilt` — tilt up to the rooftops · `Dolly in / out` — slow dolly in to her face · `Tracking` — tracking shot alongside the courier · `Orbit` — slow orbit around the mug · `Crane` — crane up over the street · `Handheld` — handheld, slight shake.

Below: models were trained on captioned video, so they understand camera terms. In chat apps you set the camera with words only; video studios also have dedicated controls (Runway, Kling, Luma).

#### Speaker's Talk Track:
> "Eight basic camera moves — a camera operator’s vocabulary. Let’s walk through the diagrams: blue is the camera, yellow is the subject, the green arrow shows how the camera moves.
> 
> **Static** — the camera stays put. **Pan** — the camera turns in place, like a head. **Tilt** — tilts up or down. **Dolly** — the camera moves towards the subject or away from it. **Tracking** — the camera moves alongside the hero, as in our shot 2. **Orbit** — the camera circles the subject; useful for the product in the homework. **Crane** — the camera rises up. **Handheld** — shot from the hand, slight shake.
> 
> Under each diagram is a ready English phrase for the prompt.
> 
> Why do models understand this? They learned from videos with text descriptions that used these words. No magic — just words the model has seen.
> 
> Tip: **one camera move per shot**. ‘Pan plus dolly plus orbit’ in one clip often turns to mush.
> 
> Where you set it: in chats — Gemini, Flow — only with words in the prompt. Video studios have dedicated controls: Runway — direction and strength per axis, Kling — camera parameters, Luma — ready-made motion ‘concepts’."

*(Chat question: “Which camera move would you pick for a mug commercial? And for the courier?” Expected: orbit or dolly in; tracking.)*

---

### Slide 10 (42:00 — 46:00) • Step 4: what you can control more precisely than with words
**On Screen:** Left — an illustration of local control on the courier frame: a green trajectory arrow “where the courier goes”, arrows “splashes from the puddle”, a red dashed area “static zone: background stays still”. Caption: `Motion Brush (Kling): up to 6 selected elements, each with its own arrow, plus a static zone. Available on Kling 1.x–2.x models; not in the Kling 3.0 feature list.` Right — three tiles:
- `First + last frame` — the model fills in the motion between two images: Veo 3.1, Gemini Omni, Kling 3.0;
- `Extend a clip` — Veo 3.1: +7 s per step, up to 148 s; Gemini Omni: +10 s per step, up to 40 s;
- `Hero references` — Veo 3.1: up to 3 images; Kling 3.0 Elements: 2–4 images.

#### Speaker's Talk Track:
> "Words are not the only steering wheel.
> 
> On the left is the idea of local control. You brush over part of the frame and draw an arrow for where it should move: the courier rides to the right, splashes fly up from the puddle. And you mark the background as a static zone — it must not move. That is how Kling’s Motion Brush works: up to six selected elements, each with its own arrow drawn on the image, plus a static zone.
> 
> To be honest: this belongs to earlier Kling models, 1.x and 2.x. Kling 3.0’s description doesn’t list it. And the picture on the slide illustrates the idea; it is not an interface screenshot.
> 
> On the right is what many tools have in 2026.
> 
> **First and last frame**: you give two images — ‘start’ and ‘end’ — and the model builds the motion between them. Available in Veo 3.1, Gemini Omni and Kling 3.0.
> 
> **Extend a clip**: the model continues a finished video. Veo 3.1 — 7 seconds per step, up to 148 seconds. Gemini Omni — 10 seconds per step, up to 40.
> 
> **Hero references** — what we discussed in step one."

---

### Slide 11 (46:00 — 51:00) • Step 5: editing — short shots + joining
**On Screen:** A timeline built from the real files: `Shot 1 · cafe · 8 s`, `Shot 2 · rain · 8 s`, `Shot 3 · map · 8 s`; two 0.5 s transitions (yellow bands); a 0–23 s scale. Below: `8 + 8 + 8 − 0.5 − 0.5 = 23 s` — three Veo 3.1 clips and two transitions: a wipe and a fade through black. Plaque: `You can join clips in any editor (CapCut, DaVinci Resolve) or with one ffmpeg command. A person does the editing, not the model.` Right — the `final` video.

#### Speaker's Talk Track:
> "Step five — editing. This is the timeline of our final clip, built from the real files.
> 
> Three 8-second clips: cafe, rain, map. Between them, two half-second transitions — a wipe and a fade through black. A transition overlaps the edges of neighbouring clips, which is why 8 + 8 + 8 gives 23 seconds, not 24.
> 
> The lesson’s key point here: **a model is good at one short shot. A person builds a story out of several shots.** Ordinary cinema works the same way: a film is made of separate shots.
> 
> The benefits: short shots are more stable than long ones. And if one shot fails, we redo only that one, not the whole clip.
> 
> You can join clips in any editor — CapCut, DaVinci Resolve — or with a single ffmpeg command. Let’s watch the final clip once more — now you know what it is made of."

*(Click the video on the right, 23 seconds.)*

> "That ends part one: we went all the way from the failure to the finished clip."

---

### Slide 12 (51:00 — 56:00) • Break
**On Screen:** Kicker `Break`. Title: `5 minutes for coffee and resting your eyes`. Timer `05:00`, buttons `START 5 MIN` / `RESET`. Caption: `Next: the model market, what it looks like in code, what it costs, how to check video and what the risks are.`

#### Speaker's Talk Track:
> "Five-minute break. No chat tasks — just rest, grab a coffee, give your eyes a break from the screen.
> 
> After the break: which models are on the market now, what it looks like in code, what it costs, how to check video and what the risks are.
> 
> Starting the timer."

*(Press “Start”. You can mute your microphone for 5 minutes.)*

---

### Part 2: Market, money, quality check, risks and homework (56:00 — 90:00)

---

### Slide 13 (56:00 — 63:00) • Market, October 2026
**On Screen:** Bars for “maximum length of one clip per generation” (0–30 s scale) and capability chips `audio` / `image→video` / `API` / `open weights`:
- Gemini Omni 1.1 Flash (Google) — 10 s, + extend to 40 s · #1 LMArena · audio*;
- Veo 3.1 (Google) — 8 s, + extend to 148 s · our clips;
- Kling 3.0 (Kuaishou) — 15 s · 4.0 up to 30 s — early access;
- Seedance 2.5 (ByteDance) — 30 s;
- Wan 3.0 (Alibaba) — 30 s · #1 Artificial Analysis with audio;
- Hailuo H3 (MiniMax) — 15 s;
- Ray3.2 (Luma) — 10 s, no audio;
- LTX-2 (Lightricks) — 20 s, open weights;
- Wan 2.2 (Alibaba) — 5 s, open weights.

Separate row: `Sora 2 (OpenAI) — shut down: app 26.04.2026, API 24.09.2026, no replacement.` Footnote: * Omni audio per third-party reviews; LMArena ranking 21.09.2026, Artificial Analysis October 2026; Runway and Leonardo are platforms that host many of these models.

#### Speaker's Talk Track:
> "Welcome back! Let’s look at the market. How to read the slide: the bar is how many seconds of video one generation gives. On the right are chips: does it have audio, can you give it your own image, is there an API for developers, can you download the model and run it yourself.
> 
> What changed over the last year. First: **audio became standard** — almost every model generates it together with the picture. Second: **clips got longer** — typical length grew from 5–10 to 10–30 seconds.
> 
> Leaders. Google’s main model is now **Gemini Omni 1.1 Flash**, number one on the LMArena ranking as of 21 September 2026. **Veo 3.1**, which made our clips, still runs in the API and can extend a clip to 148 seconds. On another ranking, Artificial Analysis with audio, first place belongs to **Wan 3.0** from Alibaba. Alongside them: Kling 3.0, Seedance 2.5, Hailuo H3, Luma Ray3.2.
> 
> Note: rankings disagree and change almost every month. So always check the date and which ranking it is.
> 
> **Open weights** are models you can download and run on your own machine: Wan 2.2 and LTX-2. Newer Wan versions — 2.5 up to 3.0 — are available only through an API.
> 
> And the last row — **OpenAI’s Sora is shut down**. The app closed on 26 April 2026, the API on 24 September 2026, with no replacement. ChatGPT does not make video. If older materials present Sora as a current tool — that is history now.
> 
> One more thing: Runway and Leonardo today are platforms where many of these models are available in one place."

*(Before class, check whether the full Kling 4.0 has shipped — it was planned for October 2026. If it has, mention it in one sentence.)*

---

### Slide 14 (63:00 — 66:00) • What it looks like in code (for reference)
**On Screen:** ~15 lines of Python with the `google-genai` library: create a client (key from `GEMINI_API_KEY`) → `generate_videos` with model `veo-3.1-fast-generate-preview`, a prompt and the image `shot2.png` → a loop “wait until `op.done`” (~11 s to ~6 min) → download and save `shot2.mp4`. Right: `Three steps: send → wait → download.` Price per second, 720p: Veo 3.1 — $0.40 (8 s = $3.20), Fast — $0.10 (8 s = $0.80), Lite — $0.05 (8 s = $0.40). Footnote: Gemini API, October 2026; no free tier for Veo; you pay only for successful videos.

#### Speaker's Talk Track:
> "This slide is for reference. We don’t go through the code line by line — just see what it looks like.
> 
> We use the same google-genai Python library as in L03 and L04. Three steps: **send** an image and a prompt — **wait** — **download** the file.
> 
> The one difference from images: video takes a while — from tens of seconds to several minutes. So the service immediately returns a ‘ticket’, and the program asks every 10 seconds: is it ready? When it is, we download.
> 
> On the right are the prices. You pay per second of video: Veo 3.1 — 40 cents, Fast — 10, Lite — 5 cents at 720p. An 8-second clip costs $3.20, $0.80 or $0.40. There is no free tier for Veo in the API, but you pay only for successful generations.
> 
> The homework needs no code — everything is done in web interfaces."

---

### Slide 15 (66:00 — 71:00) • Economics: count seconds, not attempts
**On Screen:** Lead: `A clip like ours: 3 shots of 8 seconds, Veo 3.1, 720p.` Bar chart:
- `T2V trial and error` — 10 tries per shot × 3 shots × $3.20 = **$96**;
- `Frame in chat + I2V` — 3 tries per shot × 3 shots × $3.20 = **$28.80**;
- `Same on Veo 3.1 Fast` — 3 tries × 3 shots × $0.80 = **$7.20**.

Two plaques: `The approved frame saves money: fewer tries per shot. Images for key frames cost cents.` and `Drafts on a cheap model: Veo 3.1 Lite — $0.05/s, Gemini Omni 360p — about a third of the 720p price.` Footnote: `The number of tries is an assumption for the estimate. Gemini API prices as of October 2026; only successful generations are billed.`

#### Speaker's Talk Track:
> "Let’s do simple maths. In video you pay for every second, so every failed attempt costs money.
> 
> Take a clip like ours: three 8-second shots on Veo 3.1. One 8-second clip costs $3.20.
> 
> If you do T2V trial and error — write text, don’t like it, change a word, generate again — 10 times per shot, the clip costs about **$96**.
> 
> If you first perfect the frame in chat — that costs cents — and use I2V, two or three attempts are usually enough. Three attempts per shot — about **$29**.
> 
> And draft attempts can run on a cheaper model. The same volume on Veo 3.1 Fast — **$7.20**.
> 
> To avoid illusions: **the number of attempts is our assumption** for the estimate; you may need more or fewer. The prices are real, from the Gemini API price list as of October 2026.
> 
> Two takeaways on the plaques. The approved frame saves money — fewer attempts per shot. And make drafts on a cheap model: Veo 3.1 Lite is 5 cents per second, and Gemini Omni has a 360p draft mode at about a third of the 720p price."

---

### Slide 16 (71:00 — 76:00) • Checking a video is a separate step
**On Screen:** Lead: `Even a good I2V clip needs a frame-by-frame look. Defects from our own shots 2 and 3.` Left — two frames of shot 3, 1.5 seconds apart: the timer jumps 0:28 → 0:45, “Mep” instead of “Map”, the icon is a moped while the courier rides a bicycle; below — shot 2: the “THABIK” sign is random letters. Right — the acceptance checklist:
1. **Hands and objects** in contact — don’t merge or vanish;
2. **Text and numbers** — readable and stable;
3. **Face and clothes** — match the reference;
4. **Motion** — right speed and direction (wheels forward);
5. **First frame** — matches the approved one;
6. **Shot joins** — light and colour match.

Plaque: `This checklist is also the homework rubric.`

#### Speaker's Talk Track:
> "An honest moment. Our ‘good’ clip is not perfect either.
> 
> Look at two frames of shot 3, one and a half seconds apart. The on-screen timer jumps from 0:28 to 0:45. It says ‘Mep’ instead of ‘Map’. The icon shows a moped, although the courier rides a bicycle. And in shot 2 the shop sign reads ‘THABIK’ — just random letters.
> 
> Viewers may not notice. A client will.
> 
> So **checking is a separate step**. The six checklist items on the right: hands and objects; text and numbers; face and clothes; motion — speed and direction, for example wheels turning forward; the first frame matches the approved one; light and colour match at the shot joins.
> 
> How to watch: paused and frame by frame, not once at full speed. If an item fails, redo only that shot.
> 
> A practical tip: add on-screen text and numbers during editing rather than asking the model for them.
> 
> And important for you: **this checklist is also the homework rubric.**"

---

### Slide 17 (76:00 — 82:00) • Risks and provenance
**On Screen:** Left — a traffic light:
- 🟢 **Your own frames and characters** — OK, with an “AI-generated” label;
- 🟡 **Other brands, logos, styles** — only with permission and after company lawyers review;
- 🔴 **Real people without consent** — no: employees, clients, public figures — only with written consent.

Right — “how a mark survives re-saving”: `Video from Veo` → **SynthID** (invisible mark in the pixels) → re-encoding / cropping / screenshot → `✓ usually survives`; **C2PA** (signature in the file metadata) → `✗ easily lost`. Plaque: `SynthID check: upload the video to the Gemini app (up to 100 MB / 90 s). It only finds SynthID — videos from other services may go unrecognised.` Bottom: `EU AI Act, Art. 50: since 2 August 2026 deepfakes must be labelled; machine-readable marking for systems released earlier — from 2 December 2026. Fines up to €15M or 3% of turnover.`

#### Speaker's Talk Track:
> "Let’s talk about risks. On the left is a traffic light.
> 
> **Green**: your own generated frames and characters. Fine, but label them as AI-made.
> 
> **Amber**: other companies’ brands, logos, recognisable styles. Only with permission, and company lawyers decide. Remember ‘Glono’ from our failure — the model inserted a near-logo all by itself.
> 
> **Red**: real people — colleagues, clients, celebrities. Only with written consent.
> 
> On the right: how to tell a video is AI-made. Google gives every Veo video **SynthID** — an invisible mark right in the pixels. It usually survives compression, cropping and even a screenshot. **C2PA** is a signature in the file metadata. It is easily lost: re-save, re-encode, take a screenshot — and the signature is gone.
> 
> You can check SynthID yourself: upload the video to the Gemini app — up to 100 megabytes and 90 seconds. Note: the check only finds SynthID, so it may not recognise videos from other services. ‘No mark found’ does not mean ‘filmed with a camera’.
> 
> And the law. In the EU — **Article 50 of the AI Act**. Since 2 August 2026 deepfakes must be labelled. Machine-readable marking for systems that were on the market earlier is due by 2 December 2026. Fines up to 15 million euros or 3% of turnover. In the US, since May 2026 platforms must remove intimate deepfakes within 48 hours — that is the TAKE IT DOWN Act.
> 
> The practical takeaway for work: label it, don’t use other people’s faces or brands without permission, and when in doubt, go to the company lawyers."

---

### Slide 18 (82:00 — 87:00) • Homework #5: bring an L04 frame to life
**On Screen:** Left — two tracks:
- **Track A · product** (L04 packshot): 5-second promo — an orbit or dolly-in. The product’s shape and text don’t drift.
- **Track B · courier** (L04 frame): a riding shot — the camera moves alongside. Face and uniform match the reference.

Right — what to submit:
1. **T2V** in one prompt — for comparison;
2. **I2V** with your L04 frame in **two services**;
3. Prompts and settings → `video_spec.md`;
4. Check against the slide 16 checklist → `video_qa.md`.

Structure: `genai-homeworks/L05/` → `videos/` (01_t2v_trap, 02/03_i2v), `video_spec.md`, `video_qa.md`. Reviewer: `ihar_rubanovich@epam.com`. Free service credits are enough.

#### Speaker's Talk Track:
> "Homework. Two tracks to choose from; both continue L04.
> 
> **Track A — product.** Take your L04 packshot and make a 5-second promo: the camera orbits the product or smoothly moves in. The main requirement: the product’s shape and text must not drift.
> 
> **Track B — courier.** Take the courier frame from L04 and make a riding shot: the camera moves alongside. Face and uniform must stay as in the reference.
> 
> What to submit — the four items on the right.
> 
> One: an honest **T2V attempt in one prompt** — for comparison. Let it break — that’s fine, that is the experiment.
> 
> Two: **I2V with your L04 frame in two different services.** For example Kling and Gemini/Flow, or Runway and Luma — the list of options is in the homework file.
> 
> Three: prompts and settings go into `video_spec.md`.
> 
> Four: the check against the slide 16 checklist goes into `video_qa.md`.
> 
> How we grade: not beauty but awareness. Can you show where and why the model went wrong — with timecodes.
> 
> No code is needed; everything is done in web interfaces. Free service credits are usually enough — but terms change, details are in the file. Submit to `genai-homeworks/L05/`; the reviewer is me, `ihar_rubanovich@epam.com`. File templates are in `L05_05_Homework_EN.md`."

---

### Slide 19 (87:00 — 90:00) • Summary: four rules of video + bridge to L06
**On Screen:** Four rules:
1. **First the frame, then the motion** — I2V with an approved image instead of T2V;
2. **One shot — one action** — 4–8 seconds; the story is built in editing;
3. **The director’s prompt** — camera + action + motion details;
4. **Check and count** — a checklist for every clip; you pay per second.

Right — a frame of the final clip and a plaque: `Lesson 06: sound and speech. Modern video models already generate sound themselves — how to control it is in L06.`

#### Speaker's Talk Track:
> "Let’s sum up. Four rules, one line each.
> 
> One: **first the frame, then the motion.** Prepare and approve the image, then animate it.
> 
> Two: **one shot — one action.** 4–8 seconds, and the story is built in editing.
> 
> Three: **the director’s prompt** — camera, action, motion details.
> 
> Four: **check and count.** A checklist for every clip, and remember you pay per second.
> 
> And a teaser. Our clips actually have sound — Veo 3.1 made it by itself. How to control sound and speech is the next lesson, L06.
> 
> Thank you! Questions — by voice or in the Teams chat."

*(Open microphone until the end of the slot.)*
