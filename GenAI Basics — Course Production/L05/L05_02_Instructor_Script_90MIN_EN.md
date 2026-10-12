# Instructor Script • Lesson 05: Video Generation. From a Key Frame to a Video of Several Shots (90 Minutes)

**Course:** GenAI Basics • Module 2 (Multimodality) • Lesson 05 of 16  
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems  
**Audience:** GenAI beginners from many roles. Plain language, no formulas; code only as one short reference example.  
**Format:** 21 slides (`presentation_L05_Video_Generation_EN_v2.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 15  
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen. Videos start **on click** and play **muted**.  
**Source of truth:** `deck_v2/build.py` (visible text and speaker notes for every slide). If this script and the deck differ, the deck wins.  
**Materials:** ready clips from `demo_veo_showcase/` (Veo 3.1, 8 s each: shots 1–3, final `courier_delivery_final.mp4` = 23 s, failure `trainwreck_naive_t2v.mp4`), the character sheet and key frames from L04, homework `L05_05_Homework_EN.md`.  
**Models in this lesson (facts as of October 2026):** Veo 3.1 / Fast / Lite (our clips), Gemini Omni 1.1 Flash, Kling 3.0, Seedance 2.5, Wan 3.0, Hailuo H3, Luma Ray3.2, LTX-2, Wan 2.2, Runway Gen-4.5, Grok Imagine 1.5. Sora 2 is **shut down** (app 26.04.2026, API 24.09.2026); ChatGPT does not generate video.

**Terms used in this lesson:** *shot* = one row of the storyboard; *clip* = one generated file; *key frame* = the approved input image for a shot; *attempt* = one generation of a shot.

**Lesson objective:** students understand how a video model generates motion and why one prompt for a whole story fails; can produce a short multi-shot video with a 6-step pipeline (1 storyboard, 2 references, 3 key frame, 4 prompt and camera, 5 controls, 6 editing); know where to generate (chat, web studio, API), what a second, a minute and an hour of video cost, how to accept a clip with a checklist, and the legal risks of generated video.

> **Before you start (Teams):** when sharing your screen, turn on **“Optimize for motion and video”**, otherwise the clips will stutter. Share the browser window with the deck. Do not share computer sound: clips are shown muted.

---

## Timing (21 slides • 90 minutes incl. a 5-minute break)

| Slide | Block | Time | Min | On screen | Key point |
|---|---|---|---|---|---|
| **01** | Cover | 00:00–02:00 | 2 | Frame from shot 2, title, lesson scope | Today the L04 images become video. |
| **02** | Example video | 02:00–05:00 | 3 | `final` video (23 s) + 3 numbers | 3 shots, 8+8+8 → 23 s, ≈ $10 at list price. |
| **03** | Where to generate | 05:00–09:00 | 4 | Three columns: chat apps, web studios, API | One model is often available on all three layers. ChatGPT has no video. |
| **04** | How diffusion makes frames | 09:00–13:00 | 4 | Noise → denoising → frames; “no physics engine” plaque | The model knows what motion usually looks like; it does not compute physics. |
| **05** | Anti-pattern: text-to-video | 13:00–18:00 | 5 | `trainwreck` video + 4 frames with timecodes | 3 scenes and 5 actions in 8 s give 4 failure types. |
| **06** | Text-to-video vs image-to-video | 18:00–21:00 | 3 | Two videos side by side + two flow diagrams | Fix appearance in an image; the video model handles motion only. |
| **07** | Step 1: storyboard | 21:00–28:00 | 7 | 3-row storyboard table + 7-column template | Split the story into 4–8 s shots before the first generation. |
| **08** | Step 2: references | 28:00–31:00 | 3 | Character sheet with 4 callouts + frames of shots 1 and 2 | A reference narrows the model’s choices; more stable, not guaranteed. |
| **09** | Step 3: key frame | 31:00–35:00 | 4 | Sprite → draft → approved frame | An image edit costs seconds and cents; a video regeneration costs minutes and $0.40/s. |
| **10** | Step 4: prompt | 35:00–41:00 | 6 | Shot 2 prompt with 6 colour-coded slots + `shot2` video | Motion verbs; do not describe the frame again; describe what should happen. |
| **11** | Step 4: camera | 41:00–45:00 | 4 | 8 camera-move diagrams with prompt phrases | Models know camera terms. One camera move per shot. |
| **12** | Step 5: controls | 45:00–48:00 | 3 | Motion Brush illustration + 3 tiles | First/last frame, extension, character references. |
| **13** | Step 6: editing | 48:00–55:00 | 7 | Timeline 8+8+8 − 0.5 − 0.5 = 23 s, ffmpeg command, `final` video | The model makes one short shot; a person builds the story in editing. |
| **14** | Market, October 2026 | 55:00–58:00 | 3 | Max clip length bars + capability chips; Sora 2 shut down | Audio is standard; clips are 10–30 s; leaderboards change monthly. |
| **15** | **Break** | **58:00–63:00** | **5** | **Timer** | **Rest only.** |
| **16** | Code (reference) | 63:00–66:00 | 3 | ~15 lines of `google-genai` | Submit → poll status → download. Same pattern in other APIs. |
| **17** | Cost | 66:00–71:00 | 5 | Table: $/s, 8 s clip, 1 minute, 1 hour, 1 hour with 3 attempts | 1 hour = 450 shots of 8 s = $1,440 on Veo 3.1 with one attempt per shot. |
| **18** | Acceptance checklist | 71:00–76:00 | 5 | Defects from our shots 2 and 3 + 6-item checklist | Review is a separate step; the checklist is the homework rubric. |
| **19** | Risks | 76:00–80:00 | 4 | Traffic light, SynthID vs C2PA, EU AI Act Art. 50 | Label AI content; other brands need permission; real people need written consent. |
| **20** | Homework | 80:00–87:00 | 7 | Track A (product) / Track B (courier), 5 deliverables, repo tree | A three-shot mini story through the whole pipeline. |
| **21** | Summary | 87:00–90:00 | 3 | 5 rules + final frame + L06 note | Storyboard, key frame, one action per shot, structured prompt, acceptance and budget. |

Part 1 (slides 01–14, 00:00–58:00): where and how video is generated, why one prompt fails, and the 6-step pipeline. Break (slide 15, 58:00–63:00). Part 2 (slides 16–21, 63:00–90:00): code, cost, acceptance, risks, homework, summary.

---

## Part 1: Generation basics and the 6-step pipeline (00:00–58:00)

---

### Slide 01 (00:00–02:00) • Cover

**On screen:** Background: a frame from shot 2 (the courier in the rain). Kicker: `GenAI Basics • Lesson 05 • Module 2: multimodality`. Title: `Video Generation`. Subtitle: `From a key frame to a video of several shots`. Text: `How a video model generates motion, why one long prompt fails, and how to build a story from short shots. Veo, Gemini Omni, Kling, Seedance, Runway, Leonardo. Data as of October 2026.` Key hints at the bottom.

*(Before you begin: Teams screen sharing is on with “Optimize for motion and video”. The deck is open in the browser in fullscreen, key `F`.)*

#### Speaker
> "Hello everyone. This is the second lesson of the multimodality module.
>
> In L04 we generated images: the courier, the character sheet, a product packshot. Today we generate video from those images.
>
> The plan. First a finished video, then where you can generate video at all, then how a video model works inside, and what typically goes wrong. After that, a pipeline of six steps that we follow for every video, and a short overview of the market. After the break: a code example, cost, how to accept a clip, legal risks and the homework.
>
> One technical note: I start every clip with a click and show it muted. If the video stutters on your side, write in the chat."

---

### Slide 02 (02:00–05:00) • Example: a 23-second video built from three 8-second shots

**On screen:** Left: the `final` video (23 s, click to play, muted). Right: three numbers:
- `3 shots`: each generated from an approved key frame (image-to-video);
- `8+8+8 → 23 s`: joined with two 0.5 s transitions;
- `≈ $10`: 3 × 8 s × $0.40, Veo 3.1 list price, 720p, failed attempts not included.

Bottom note: `Next: where to generate, how the model works, why one prompt for the whole story fails, and a 6-step pipeline.`

#### Speaker
> "We start with the result. This video is 23 seconds long."

*(Click the video. Let it play to the end; you may play it twice.)*

> "Question for the chat: what do you see? How many separate clips do you think this is made of, and where are the cuts?"

*(Pause 20–30 seconds and read the answers.)*

> "Answer: three separate 8-second clips, all generated by Google Veo 3.1. Each clip was generated from a prepared image, not from text alone. That mode is called image-to-video.
>
> The clips were then joined with two half-second transitions. The transitions overlap the clip edges, so 8 + 8 + 8 gives 23 seconds, not 24.
>
> Cost: Veo 3.1 charges 40 cents per second of 720p video. Three 8-second clips are about 10 dollars. That does not include failed attempts; we will count those on the cost slide after the break.
>
> One sentence on sound: these clips do have audio, because current models generate it together with the picture. Today we watch muted; sound is the topic of L06."

---

### Slide 03 (05:00–09:00) • Three access layers for video models: chat, web studio, API

**On screen:** Three columns, each with tool chips and four rows (Control, Billing, Use for, Start with):

| | Chat apps | Web studios | API |
|---|---|---|---|
| Tools | Gemini app, Google Flow, Grok Imagine | Kling, Leonardo, Dreamina / CapCut (Seedance), Runway, Luma, Hailuo | Gemini API / Vertex AI, Kling API, Runway API, xAI API |
| Control | prompt text only; Flow adds first/last frame and extension | camera settings, first/last frame, references, several shots per generation | everything as request parameters; batch jobs |
| Billing | subscription | credits; small free allowance | per second of video |
| Use for | ideas, quick drafts | individual videos, homework | pipelines, products |
| Start with | Gemini app | Kling | Gemini API |

Bottom note: `One model is often available on all three layers: Veo is in Flow, Leonardo, Runway and the Gemini API (the Gemini app now runs Gemini Omni). ChatGPT does not generate video: Sora has been shut down.`

#### Speaker
> "Before we look inside the model, where do you actually generate video? The structure is the same as for images in L04: three layers.
>
> The first layer is chat apps. The Gemini app, which now runs Google’s Gemini Omni model. Google Flow, which runs Omni 1.1 Flash and Veo 3.1 and adds scenes, a first and last frame, and clip extension. And Grok Imagine from xAI. In a chat you control the result only with the text of the prompt, including the camera. You pay with a subscription. This layer is good for ideas and quick drafts; start with the Gemini app.
>
> The second layer is web studios: interfaces built for video. Kling, with model 3.0, character references called Elements, and several shots per generation. Leonardo, with its own Motion 2.0 model and hosted models from other vendors: Veo, Kling, Seedance, Hailuo. Dreamina and CapCut from ByteDance with the Seedance model. Runway with Gen-4.5 and hosted models. Luma Ray3.2 and Hailuo. Here you get camera settings, first and last frame, and references. You pay in credits. Free accounts get a small allowance; Kling, for example, gives free accounts a small monthly credit grant. The homework is done on this layer; start with Kling.
>
> The third layer is the API: code and automation. The Gemini API and Vertex AI for Veo 3.1 and Gemini Omni, the Kling API, the Runway API, which also serves Seedance, Veo, Wan and Hailuo, and the xAI API for Grok Imagine, where version 1.5 costs 8 cents per second and the Lite version 2 cents. Every setting is a request parameter, you can run batch jobs, and you pay per second of video.
>
> The note at the bottom matters: one model is often available on all three layers. Veo is in Flow, in Leonardo, in Runway and in the Gemini API. And ChatGPT does not generate video: OpenAI shut Sora down, the app in April and the API on 24 September 2026."

---

### Slide 04 (09:00–13:00) • How a diffusion model generates video frames

**On screen:** Three steps, each shown as a stack of frames along a time axis:
1. `Noise`: random noise for all frames of the clip at once.
2. `Denoising, step by step`: the video is cut into pieces “place in frame × moment in time”. Dozens of steps remove noise; the text and the first frame guide every step.
3. `Frames`: 24 frames per second that are consistent with each other, so motion looks smooth.

Plaque: `There is no physics engine inside. The model has seen millions of videos and knows what motion usually looks like. So it fails where exact rules matter: hands and objects in contact, text, long scenes.` Caption: `Schematic: frames from our shot 2, noise added for illustration.`

#### Speaker
> "How does a model produce video? Recall L04: an image was produced from noise in dozens of steps. At each step the model removed part of the noise until a picture appeared.
>
> Video works the same way. The difference is that the model denoises the whole stack of frames of the clip at once, not one frame. That is why neighbouring frames agree with each other and the motion looks smooth.
>
> To make this computable, the video is split into small patches: this region of the frame at this moment in time. The text prompt and, if we provide one, the first frame guide the model at every step.
>
> The main point is the plaque at the bottom. There is no physics engine inside. The model does not compute physics. It has seen many videos of steam, rain and splashes and learned to draw them convincingly. Research such as the Physics-IQ benchmark from 2025 shows that realistic-looking output is not the same as physically correct output.
>
> In practice: expect errors where exact rules matter. Hands holding an object. Text and numbers. Long scenes with many events. The next slide shows all three."

---

### Slide 05 (13:00–18:00) • Text-to-video, the whole story in one prompt: 4 failure types

**On screen:** Left: badge `text-to-video`, `Veo 3.1 • 8 s • text only`, the `trainwreck` video, and the shortened prompt with `then cuts to` and `and then` highlighted. Right: 4 frames with timecodes:
- `00:02` **Action skipped**: the bag stays on the counter and never goes into the backpack;
- `00:03` **Details drift after the cut**: the logo on the box changes: “Glono” → “Glovo”;
- `00:05` **Scene geometry breaks**: handlebars with a phone slide in while the courier is still riding ahead;
- `00:07` **Garbled text**: “Delivery Admest” instead of “Delivery Address”.

Bottom: `Root cause: 3 scenes and 5 actions requested in 8 seconds.`

#### Speaker
> "This is what happens when you brief a model the way you brief a person. Look at the prompt: the courier walks into a cafe, picks up a bag, puts it into the backpack, *then* rides a bicycle in the rain, *and then* the camera moves in on a phone map. One paragraph, text only. The clip is 8 seconds."

*(Click the video and let it play to the end.)*

> "Four frames, four failure types.
>
> One: the action is skipped. The bag stays on the counter; nobody puts it into the backpack.
>
> Two: details drift after the cut. The logo on the box changes from one moment to the next. This also shows how a model damages a brand: ‘Glono’ appears instead of the name. In a commercial video that is a reject. Glovo is only the name of our training case, as in the L04 homework; the logo in the clip is an example of what not to do.
>
> Three: scene geometry breaks. Instead of a clean cut to a new shot, the handlebars with a phone slide over the picture while the courier is still riding ahead.
>
> Four: garbled text. The phone screen says ‘Delivery Admest’ instead of ‘Delivery Address’. The model knows what letters look like, but it does not spell.
>
> The root cause is the same for all four: we asked for three scenes and five actions in eight seconds. The model does not perform cuts between scenes because the prompt asks for them. The rule: one shot contains one scene and one action."

*(Optional chat question: “Which of the four failures would you notice first as a viewer?”)*

---

### Slide 06 (18:00–21:00) • Text-to-video vs image-to-video

**On screen:** Two columns.
- Left: badge `text-to-video`, `input: text only`, the `trainwreck` video. Flow: `Text → The model decides what is in frame and how it moves → ✗ two tasks at once`.
- Right: badge `image-to-video`, `input: key frame + text`, the `shot1` video. Flow: `Frame ✓ + text about motion → The model decides only how it moves → ✓ one task`.

Plaque: `Rule: fix appearance, light and composition in an image (the L04 skill). The video model handles only the motion.`

#### Speaker
> "Two generation modes. I will play both clips one after the other."

*(Click the left video, then the right one. 8 seconds each.)*

> "Left: text only, the clip we just analysed. Right: the same courier story, but the model received a ready first image.
>
> In text-to-video the model has to decide two things at once: how everything looks, meaning face, clothes, light and the cafe, and how it moves. Two unknowns, and it can get either one wrong.
>
> In image-to-video the first question is already answered by an image that a person approved. Only motion is left. So there are fewer errors, and the errors are more predictable.
>
> Some tools abbreviate the modes as T2V and I2V; in this course we write the full names.
>
> We already know how to produce and edit images; that is L04. So the rule is: fix appearance, light and composition in the image, and leave only motion to the video model. Now the pipeline, step by step."

---

### Slide 07 (21:00–28:00) • Step 1: storyboard. The whole story before the first generation

**On screen:** Lead: `The story is split into shots of 4–8 seconds. Each row = one key frame + one prompt + one generation.` Table with a preview image per row:

| # | Time | Action | Camera | Key frame file |
|---|---|---|---|---|
| 1 | 0–8 s | Courier takes the bag from the barista and turns to the exit | medium shot, slow dolly in | `shot1_cafe_pickup.png` |
| 2 | 7.5–15.5 s | Rides a bicycle down a wet street at dusk | tracking alongside, low angle | `shot2_bike_rain.png` |
| 3 | 15–23 s | The map route animates towards the destination pin | slow digital zoom in, slight tilt | `shot3_map_route.png` |

Below: `Full template (Creator Tools)` with 7 column chips: `Shot / timing`, `Visual`, `Voice-over`, `Image prompt`, `Video prompt`, `SFX (sound effects)`, `Music`. Note: `Why short shots: a long or extended clip accumulates drift, and any defect means regenerating all of it. A short shot is more stable, only that shot is redone, and the budget stays predictable.` Small print: `Times include the 0.5 s transition overlaps. 1 minute ≈ 8 shots of 8 s; 1 hour ≈ 450 shots. Keep the storyboard in a spreadsheet (Google Sheets, Excel): it is the work plan, the budget and the acceptance list.`

#### Speaker
> "Step one happens before any generation: the storyboard. The story is split into shots of 4 to 8 seconds, and each shot becomes one row of a table.
>
> Our video is three rows. Row one: the courier takes the bag from the barista and turns to the exit; medium shot, slow dolly in. Row two: she rides down a wet street at dusk; the camera tracks alongside at a low angle. Row three: the route on the map animates towards the destination pin; slow digital zoom in with a slight tilt.
>
> Each row has a time range, one action, one camera move and the name of a key frame file. The time ranges overlap by half a second because of the transitions: 0 to 8, 7.5 to 15.5, 15 to 23.
>
> Read the lead line again: one row is one key frame, one prompt and one generation. That is the unit of work for the rest of the lesson.
>
> Why short shots instead of one long or extended clip? A long clip accumulates drift: the face, the clothes, the light slowly change. And any defect in a long clip means you regenerate all of it. A short shot is more stable, you redo only the shot that failed, and the budget is predictable because you know the number of seconds in advance.
>
> Below the table is the full production template from Creator Tools, my R&D pet project, which I used for the Giant Stories series. It has seven columns: shot and timing, visual, voice-over, image prompt, video prompt, sound effects and music. Today we use only the visual columns; sound is L06.
>
> Scale: one minute of video is about 8 shots of 8 seconds; one hour is about 450 shots. That is why the storyboard lives in a spreadsheet. It is the work plan, it is the basis of the budget on the cost slide, and it is the list you check during acceptance."

*(Exercise, 2 minutes, chat: “Propose shot 4 for this story as one table row: time, action, camera, key frame file.” Read two or three answers. Check: one action, one camera move, 4–8 seconds.)*

---

### Slide 08 (28:00–31:00) • Step 2: references. Character sheet as the reference for every shot

**On screen:** The L04 character sheet (one courier from four angles) with four callouts: `face, short curly hair`, `turquoise box backpack`, `yellow jacket, reflective stripe`, `black trousers, white sneakers`. Right:
- A reference narrows the model’s choices for appearance.
- Veo 3.1: up to 3 reference images. Kling 3.0: Elements, 2–4 images.
- More stable, not guaranteed: review every shot.

Below: frames from shots 1 and 2. Caption: `Result: the same courier in shots 1 and 2.`

#### Speaker
> "Step two: references. We made this character sheet in L04: one person from four angles.
>
> The callouts are the details viewers use to recognise the character: face and short curly hair, the yellow jacket with a reflective stripe, the turquoise box backpack, black trousers and white sneakers. If the jacket turns green in one shot, viewers will think it is a different person.
>
> A reference narrows the model’s choices: there are fewer ways for it to draw the character differently.
>
> Where it exists: Veo 3.1 accepts up to three reference images. Kling 3.0 calls it Elements, two to four images.
>
> The result is more stable but not guaranteed, so every shot is still reviewed; the acceptance checklist comes after the break. At the bottom right are frames from our shots 1 and 2: the courier is recognisable."

---

### Slide 09 (31:00–35:00) • Step 3: finalise the key frame in an image chat before generating video

**On screen:** Three frames: `Sprite` (game source art) → `Draft` (prompt: “Make a realistic 16:9 frame from this sprite”; wrong helmet and tabard) → `Approved ✓` (edit: “Bare hands, tabard in white and blue rectangles, a flat ‘kettle’ helmet”; first frame for the video). Below, two blocks: `Image edit: seconds, cents` (one image edit in chat) and `Video regeneration: minutes, $0.40 per second` (one video regeneration, Veo 3.1, 720p).

#### Speaker
> "Step three: the key frame. A short example in the style of L04. We take a small knight sprite from a game and ask an image chat for a realistic 16:9 frame based on it.
>
> The first version is close, but the helmet and the tabard are wrong. We do not start over. We write one precise edit: bare hands, a tabard in white and blue rectangles, a flat helmet shaped like a kettle. The frame is approved, and it becomes the first frame of the video.
>
> Why this matters for video: look at the two blocks below. One image edit costs seconds and cents. One video regeneration costs minutes of waiting and, on Veo 3.1, 40 cents for every second of the clip.
>
> So every appearance error is fixed in the image, where it is cheap. The frame is approved first; only then do we animate it. In our storyboard, the key frame file column is exactly this approved image."

---

### Slide 10 (35:00–41:00) • Step 4: video prompt structure, 6 slots

**On screen:** Legend of 6 colour-coded slots: `1 Camera`, `2 Who`, `3 Action`, `4 Where & when`, `5 Motion details`, `6 Light`. The actual shot 2 prompt (Veo 3.1, image-to-video), each part highlighted in its slot colour:

```text
Dynamic tracking shot moving forward alongside the courier. The same courier with short cropped curly hair pedals her bicycle forward through the rain-slicked city avenue at twilight. Wheels spinning smoothly forward with water spray cutting through shallow puddles. Wet cobblestones reflecting warm shop lights and streetlamps.
```

Right: the `shot2` video, caption `Output: shot 2`. Three rules below:
- **Motion verbs** (pedals, spinning, moving forward): the model needs to know what changes.
- **Do not describe the frame again:** it is already the input. One identifying detail is enough.
- **Describe what should happen.** A negative prompt field (what must not appear) exists only in some tools (Kling, Wan).

#### Speaker
> "Step four has two parts: the prompt and the camera. First the prompt. This is the actual prompt used for our shot 2, coloured by slot.
>
> Slot one, camera: a tracking shot moving forward alongside the courier. Slot two, who: the same courier with short cropped curly hair. Slot three, action: pedals her bicycle forward. Slot four, where and when: a rain-slicked city avenue at twilight. Slot five, motion details: wheels spinning forward, water spray from the puddles. Slot six, light: wet cobblestones reflecting shop lights and streetlamps.
>
> In L04 image prompts also had six slots. For video the important ones are camera, action and motion details. Here is the result."

*(Click the video on the right, 8 seconds.)*

> "Three rules.
>
> First, motion verbs: pedals, spinning, moving forward. The model has to know what changes over time. ‘A courier in the rain’ describes a picture, not a video.
>
> Second, in image-to-video do not describe the frame again. The model already receives the image. There is no need to repeat the jacket, the backpack and the sneakers. One identifying detail, here ‘short cropped curly hair’, is enough.
>
> Third, describe what should happen. A separate field for what must not appear, the negative prompt, exists only in some tools, for example Kling and Wan. In Veo, positive phrasing works better: write ‘smooth steady camera’ instead of ‘no shake’.
>
> In the storyboard this text goes into the prompt column of the row."

---

### Slide 11 (41:00–45:00) • Step 4: camera moves and the prompt terms for them

**On screen:** Grid of 8 diagrams (camera in blue, subject in yellow, motion as a green arrow), each with a name, a plain description and a prompt phrase:
`Static` (fixed camera): “static camera, locked-off shot” · `Pan` (rotate in place): “slow pan left across the street” · `Tilt` (tilt up / down): “tilt up to the rooftops” · `Dolly in / out` (move closer / away): “slow dolly in to her face” · `Tracking` (move alongside the subject): “tracking shot alongside the courier” · `Orbit` (circle around the subject): “slow orbit around the mug” · `Crane` (camera rises): “crane up over the street” · `Handheld` (slight shake): “handheld, slight shake”.

Note: `Models were trained on captioned video, so they understand camera terms. In chat apps you set the camera with words only; web studios also have dedicated controls (Runway, Kling, Luma).` Small print: diagrams are top view (Pan, Dolly, Tracking, Orbit) and side view (Static, Tilt, Crane).

#### Speaker
> "The second part of step four is the camera. These are eight basic moves from standard camera vocabulary. Blue is the camera, yellow is the subject, the green arrow shows how the camera moves.
>
> Static: the camera does not move. Pan: the camera rotates in place, like turning your head. Tilt: the camera tilts up or down. Dolly: the camera moves towards the subject or away from it. Tracking: the camera moves alongside the subject, as in our shot 2. Orbit: the camera circles the subject; useful for the product track in the homework. Crane: the camera rises. Handheld: a slight shake, as if held by hand.
>
> Under each diagram is a ready English phrase for the prompt.
>
> Why models understand these words: they were trained on videos with text descriptions that used them.
>
> One camera move per shot. ‘Pan plus dolly plus orbit’ in one clip usually produces incoherent motion. In the storyboard the camera column holds exactly one move per row.
>
> Where you set it: in chat apps such as Gemini and Flow, only with words in the prompt. Web studios also have dedicated controls: Runway has direction and strength per axis, Kling has camera parameters, Luma has preset motion ‘concepts’."

*(Chat question if time allows: “Which camera move would you use for a mug commercial? For the courier?” Expected: orbit or dolly in; tracking.)*

---

### Slide 12 (45:00–48:00) • Step 5: controls beyond the prompt. Frames, extension, references

**On screen:** Left: illustration of local control on the courier frame: a green trajectory arrow (`where the courier goes`), arrows for `splashes from the puddle`, a red dashed area (`static zone: background stays still`). Caption: `Motion Brush (Kling): up to 6 selected elements, each with its own arrow, plus a static zone. Available on Kling 1.x–2.x models; not in the Kling 3.0 feature list.` Right: three tiles:
- `First + last frame`: the model fills in the motion between two images. Veo 3.1, Gemini Omni, Kling 3.0;
- `Extend a clip`: Veo 3.1: +7 s per step, up to 148 s (720p, not Lite); Gemini Omni: +10 s per step, up to 40 s;
- `Character references`: Veo 3.1 / Fast: up to 3 images, 8 s clip; Kling 3.0 Elements: 2–4 images.

#### Speaker
> "Step five: controls other than the prompt.
>
> On the left is the idea of local control. You brush over parts of the frame and draw an arrow for where each part moves: the courier rides forward, splashes go up from the puddle. The background is marked as a static zone that must not move. That is how Kling’s Motion Brush works: up to six selected elements, each with its own arrow drawn on the image, plus a static zone. It belongs to Kling 1.x and 2.x models; the Kling 3.0 feature list does not include it. The overlay on the slide illustrates the idea; it is not an interface screenshot.
>
> On the right is what is widely available in 2026.
>
> First and last frame: you provide a start image and an end image, and the model builds the motion between them. Veo 3.1, Gemini Omni and Kling 3.0 support it.
>
> Extension: the model continues an existing clip. Veo 3.1 adds 7 seconds per step, up to 148 seconds, at 720p and not on the Lite model. Gemini Omni adds 10 seconds per step, up to 40 seconds. Remember the storyboard slide: an extended clip accumulates drift, so for a story we still prefer separate short shots.
>
> Character references, which we covered in step two: up to three images in Veo 3.1 and Veo 3.1 Fast, with an 8-second clip; two to four images in Kling 3.0 Elements."

---

### Slide 13 (48:00–55:00) • Step 6: editing. Three shots into one 23-second video

**On screen:** Timeline from the real files: `Shot 1 · cafe · 8 s`, `Shot 2 · rain · 8 s`, `Shot 3 · map · 8 s`, two `0.5 s transition` bands, scale 0–23 s. Below: stat `8 + 8 + 8 − 0.5 − 0.5 = 23 s` (three Veo 3.1 shots and two transitions: a wipe and a fade to black). Note: `Join in any editor (CapCut, DaVinci Resolve) or with one command:`

```bash
ffmpeg -i shot1.mp4 -i shot2.mp4 -i shot3.mp4 -filter_complex \
 "[0][1]xfade=transition=wipeleft:duration=0.5:offset=7.5[a];
  [a][2]xfade=transition=fadeblack:duration=0.5:offset=15" final.mp4
```

Right: the `final` video.

#### Speaker
> "Step six: editing. This is the timeline of our final video, built from the real files.
>
> Three 8-second clips: cafe, rain, map. Between them are two half-second transitions, a wipe and a fade to black. Each transition overlaps the edges of the neighbouring clips. That is why 8 plus 8 plus 8 gives 23 seconds, and why the storyboard rows had overlapping times.
>
> The key point of the lesson: a model is good at one short shot. A multi-shot story is built by a person, in editing, following the storyboard. Film production works the same way: a film is a sequence of separate shots.
>
> This has two practical benefits. Short shots are more stable than long ones. And if one shot fails acceptance, we regenerate only that shot, not the whole video.
>
> The tool does not matter. Any editor works: CapCut, DaVinci Resolve. Or one ffmpeg command, shown here: the offsets 7.5 and 15 are the transition start times from the storyboard. Let’s watch the result once more; now you know how it was made."

*(Click the video on the right, 23 seconds.)*

> "That completes the pipeline: storyboard, references, key frame, prompt and camera, controls, editing."

*(If time allows: “Which of the six steps would you skip on a tight deadline, and what would it cost you?” Expected: skipping the storyboard or the key frame increases the number of attempts.)*

---

### Slide 14 (55:00–58:00) • Market, October 2026: maximum clip length and capabilities

**On screen:** Bars for “maximum length per generation” (0–30 s scale) and capability chips `audio` / `image-to-video` / `API` / `open weights`:
- Gemini Omni 1.1 Flash (Google): 10 s, + extend to 40 s · #1 LMArena · audio*;
- Veo 3.1 (Google): 8 s, + extend to 148 s · used for our clips;
- Kling 3.0 (Kuaishou): 15 s · 4.0 Flash: 20 s (beta);
- Seedance 2.5 (ByteDance): 30 s;
- Wan 3.0 (Alibaba): 30 s · #1 with audio;
- Hailuo H3 (MiniMax): 15 s;
- Ray3.2 (Luma): 10 s, no audio;
- LTX-2 (Lightricks): 20 s, audio, image-to-video, API, open weights;
- Wan 2.2 (Alibaba): 5 s, image-to-video, open weights.

Separate row: `Sora 2 (OpenAI): shut down: app 26.04.2026, API 24.09.2026, no replacement.` Footnote: highlighted chip means yes, grey means no or not confirmed; * Omni audio per third-party reviews; rankings: LMArena (21.09.2026), Artificial Analysis with-audio category (October 2026).

#### Speaker
> "A short look at the market. The bar is how many seconds one generation produces; the chips on the right show what the model supports.
>
> Two changes over the past year. Audio became standard: almost every model generates it with the picture. And clips became longer: typical length grew from 5–10 seconds to 10–30 seconds.
>
> Leaders. Google’s main model is now Gemini Omni 1.1 Flash, number one on LMArena as of 21 September 2026. Veo 3.1, which generated our clips, is still available in the API and can extend a clip to 148 seconds. On the Artificial Analysis leaderboard with audio, Wan 3.0 from Alibaba is first. Also on the list: Kling 3.0, Seedance 2.5, Hailuo H3 and Luma Ray3.2, which has no audio. Leaderboards disagree and change every month, so always check the date and which leaderboard it is.
>
> Open weights, meaning models you can download and run yourself: Wan 2.2 and LTX-2. Newer Wan versions, 2.5 to 3.0, are API-only.
>
> The last row: OpenAI’s Sora is shut down. The app closed on 26 April 2026 and the API on 24 September 2026, with no replacement. ChatGPT does not generate video. If older materials describe Sora as a current tool, they are out of date."

*(Before class: check whether the full Kling 4.0 (up to 30 s) has shipped. It was announced for October 2026; since 28 September only 4.0 Flash (up to 20 s, 720p) is in early access. If it has shipped, mention it in one sentence.)*

---

### Slide 15 (58:00–63:00) • Break

**On screen:** Kicker `Break`. Title: `5 minutes for coffee and resting your eyes`. Timer `05:00`, buttons `START 5 MIN` / `RESET`. Caption: `Next: code, cost, acceptance, risks and homework.`

#### Speaker
> "Five-minute break. No tasks in the chat; rest your eyes.
>
> After the break: a code example, cost, acceptance, risks and the homework.
>
> Starting the timer."

*(Press “Start”. You can mute your microphone for 5 minutes.)*

---

## Part 2: Code, cost, acceptance, risks, homework (63:00–90:00)

---

### Slide 16 (63:00–66:00) • Gemini API: image-to-video in Python

**On screen:** Kicker `Reference • google-genai`. Left: ~15 lines of Python: create a client (key from `GEMINI_API_KEY`) → `generate_videos` with model `veo-3.1-fast-generate-preview`, prompt `"Tracking shot alongside the courier"` and image `shot2.png` → loop `while not op.done` with `time.sleep(10)` (comment: wait ~11 s to ~6 min) → download and save `shot2.mp4`. Right: `Long-running operation: submit → poll status → download. Generation takes seconds to minutes.` `Same pattern in other APIs`: Kling API, Runway API, xAI API (Grok Imagine). Small print: `Gemini API, October 2026. No free tier for Veo. Prices are on the next slide.`

#### Speaker
> "Welcome back. This slide is for reference; we do not go through the code line by line.
>
> We use the same google-genai Python library as in L03 and L04. We send an image and a prompt, wait until the video is ready, and download the file.
>
> The difference from images is time. A video takes from tens of seconds to several minutes. So the service immediately returns an operation, a kind of ticket, and the program asks every 10 seconds whether it is done. When it is, we download the file.
>
> The same pattern, submit, poll, download, is used by the Kling API, the Runway API and the xAI API for Grok Imagine.
>
> There is no free tier for Veo in the Gemini API; you pay per second of generated video. Prices are on the next slide. The homework does not need code; it is done in web studios."

---

### Slide 17 (66:00–71:00) • Generation cost: per clip, per minute, per hour of video

**On screen:** Lead: `Priced per second of generated video, 720p. One hour of finished video = 3600 s = 450 shots of 8 seconds.` Table:

| Model | Where | $ per second | 8 s clip | 1 minute | 1 hour | 1 hour, 3 attempts per shot |
|---|---|---|---|---|---|---|
| Veo 3.1 Lite | Gemini API | $0.05 | $0.40 | $3.00 | $180 | $540 |
| Grok Imagine 1.5 | xAI API | $0.08 | $0.64 | $4.80 | $288 | $864 |
| Veo 3.1 Fast | Gemini API | $0.10 | $0.80 | $6.00 | $360 | $1,080 |
| Runway Gen-4.5 | Runway API | $0.12 | $0.96 | $7.20 | $432 | $1,296 |
| Seedance 2.5 | Runway API, starting price | $0.20 | $1.60 | $12.00 | $720 | $2,160 |
| Veo 3.1 | Gemini API | $0.40 | $3.20 | $24.00 | $1,440 | $4,320 |

Two notes: `Our 23 s video: 3 shots × 8 s × 3 attempts = 72 s generated: $28.80 on Veo 3.1, $7.20 on Fast. With 3 attempts per shot you generate three times what you keep.` and `Kling (web): 3.0, 1080p with audio = 12 credits/s, i.e. 43,200 credits per hour; credit price depends on the plan. Chat apps: subscription, no per-second price.` Small print: Gemini API, xAI API and Runway API prices, October 2026; Gemini Omni 1.1 Flash ≈$0.10/s (720p, token-billed), Grok Imagine Lite $0.02/s; only successful generations are billed. Not included: key frame images, editing, audio, people’s time. 3 attempts per shot is an assumption for the estimate.

#### Speaker
> "The point of this slide is scale. All prices are per second of generated video at 720p.
>
> One second costs cents: from 5 cents on Veo 3.1 Lite to 40 cents on Veo 3.1. An 8-second clip costs from 40 cents to $3.20. A minute of video, from $3 to $24.
>
> Now the hour. One hour of finished video is 3,600 seconds, which is 450 shots of 8 seconds; that is the same 450 rows we mentioned on the storyboard slide. On Veo 3.1 that is $1,440 if every shot is accepted on the first attempt. In practice a shot takes several attempts. With 3 attempts per shot the hour costs $4,320 on Veo 3.1 and $1,080 on Veo 3.1 Fast.
>
> Apply it to our own 23-second video: 3 shots, 8 seconds each, 3 attempts per shot is 72 seconds of generation. That is $28.80 on Veo 3.1 or $7.20 on Fast. With 3 attempts you generate three times the length you keep.
>
> Other options. Gemini Omni 1.1 Flash is billed in tokens, roughly 10 cents per second at 720p. Grok Imagine Lite is 2 cents per second. Kling’s web app bills in credits: 12 credits per second for Kling 3.0 at 1080p with audio, which is 43,200 credits for an hour; the price of a credit depends on the plan. Chat apps are on a subscription, with no per-second price.
>
> How to use this: cheaper models such as Veo 3.1 Lite and Fast, Grok Imagine Lite or Omni 360p drafts are fine for drafts. Final shots go to whichever model passes acceptance.
>
> Not included: images for the key frames, editing, audio and people’s time. The 3 attempts are an assumption for the estimate. Prices change; check the price lists before class. In the homework you calculate the cost the same way: attempts × seconds × price per second."

---

### Slide 18 (71:00–76:00) • Acceptance checklist for a generated clip

**On screen:** Lead: `Even a good image-to-video clip gets a frame-by-frame review. Defects from our shots 2 and 3:` Left: two frames of shot 3, 1.5 seconds apart, with circled areas; caption: `Shot 3, 1.5 seconds apart: the timer jumps 0:28 → 0:45, “Mep” instead of “Map”, the icon is a moped while the courier rides a bicycle.` Below: a frame of shot 2; caption: `Shot 2: the “THABIK” sign is random letters.` Right: `Acceptance checklist`:
1. **Hands and objects** in contact: no merging or vanishing;
2. **Text and numbers**: readable and stable;
3. **Face and clothes**: match the reference;
4. **Motion**: speed and direction (wheels forward);
5. **First frame**: matches the approved one;
6. **Shot joins**: light and colour match.

Note: `The same checklist is the homework rubric.`

#### Speaker
> "Our accepted shots are not defect-free either.
>
> Look at two frames of shot 3, one and a half seconds apart. The on-screen timer jumps from 0:28 to 0:45. The label says ‘Mep’ instead of ‘Map’. The icon shows a moped, although the courier rides a bicycle. And in shot 2 the shop sign reads ‘THABIK’, which is random letters.
>
> A viewer may not notice. A client will.
>
> So acceptance is a separate step, with six checklist items. One: hands and objects in contact do not merge or vanish. Two: text and numbers are readable and stable. Three: face and clothes match the reference. Four: motion has the right speed and direction, for example the wheels turn forward. Five: the first frame matches the approved key frame. Six: at the joins between shots, light and colour match; this item applies once you edit several shots together.
>
> How to review: paused and frame by frame, not once at full speed. If an item fails, regenerate only that shot; the storyboard tells you which row it is.
>
> A practical tip: add on-screen text and numbers during editing instead of asking the model to generate them.
>
> And for the homework: this checklist is the grading rubric."

---

### Slide 19 (76:00–80:00) • Rights, labelling and origin marks

**On screen:** Left: traffic light:
- green: **Your own frames and characters**: allowed, with an “AI-generated” label;
- amber: **Other brands, logos, styles**: only with permission and after review by company lawyers;
- red: **Real people without consent**: employees, clients, public figures: only with written consent.

Right: `How a mark survives re-saving`: `Video from Veo (and other Google models)` → **SynthID** (invisible mark in the pixels) → re-encoding, cropping, screenshot → `✓ usually survives`; **C2PA** (Content Credentials: signature in the file metadata) → `✗ easily lost`. Note: `SynthID check: upload the video to the Gemini app (up to 100 MB, 90 s). It detects SynthID only; videos from other services may not be recognised.` Bottom plaque: `EU AI Act, Art. 50: from 2 August 2026, whoever publishes a deepfake must label it, and the model provider must add a machine-readable mark. Fines up to €15M or 3% of turnover.`

#### Speaker
> "Risks. On the left is a traffic light.
>
> Green: your own generated frames and characters. Allowed, labelled as AI-generated.
>
> Amber: other companies’ brands, logos and recognisable styles. Only with permission and after a review by company lawyers. Remember ‘Glono’ from the failure slide: the model inserted a near-copy of a logo on its own.
>
> Red: real people, meaning colleagues, clients, public figures. Only with written consent.
>
> On the right: how to tell that a video is AI-generated. Google adds SynthID to every Veo video: an invisible mark in the pixels. It usually survives compression, cropping and screenshots. C2PA, also called Content Credentials, is a signature in the file metadata. It is easily lost when the file is re-saved, re-encoded or captured as a screenshot.
>
> You can check SynthID yourself by uploading a video to the Gemini app, up to 100 megabytes and 90 seconds. The check finds only SynthID, so videos from other services may not be recognised. ‘No mark found’ does not mean the video was filmed with a camera.
>
> The law. In the EU, Article 50 of the AI Act applies from 2 August 2026. Under paragraph 50(4), whoever publishes a deepfake must label it; that is us. Under paragraph 50(2), the model provider adds a machine-readable mark. Fines go up to 15 million euros or 3% of turnover. In the US, since May 2026 platforms must remove intimate deepfakes within 48 hours under the TAKE IT DOWN Act.
>
> For work: label generated video, do not use other people’s faces or brands without permission, and when in doubt ask the company lawyers."

---

### Slide 20 (80:00–87:00) • Homework 5: a three-shot mini story

**On screen:** Left: two tracks:
- **Track A · product:** 3 promo shots from your L04 frames: reveal, detail, final shot. Shape and text stay stable.
- **Track B · courier:** 3 shots of the courier story: pickup, ride, delivery. Face and uniform match the reference.

Right: five deliverables:
1. **Storyboard**, 3 rows → `storyboard.md`;
2. **Text-to-video** with one prompt, as a baseline;
3. 3 **image-to-video** shots; one of them also in a **second service**;
4. Edit into `final.mp4`, 15–25 s;
5. Prompts, settings, cost → `video_spec.md`; review with slide 18 → `video_qa.md`.

Repo tree: `genai-homeworks/L05/` → `storyboard.md`, `videos/` (shots + `final.mp4`), `video_spec.md`, `video_qa.md`. Small print: `Reviewer: ihar_rubanovich@epam.com. Free allowances are small and change often: check before you start (table in the homework file).`

#### Speaker
> "The homework repeats the whole pipeline of today’s lesson on a small story of three shots. Choose one of two tracks; both continue L04.
>
> Track A, product: three promo shots from your L04 frames. A reveal, a detail, a final shot. The product’s shape and text must stay stable.
>
> Track B, courier: three shots of the courier story. Pickup, ride, delivery. Face and uniform must match the reference.
>
> The order of work.
>
> One: a storyboard of three rows in `storyboard.md`. Number, time, action, camera, key frame file, prompt. Same structure as slide 7.
>
> Two: a text-to-video baseline. Describe the whole three-shot story in one prompt and generate it once. Expect it to break; that is the comparison point.
>
> Three: three image-to-video shots, each from an approved L04 frame, with a prompt built from the slots on slide 10. Then take one of the three shots and generate it again in a second service, with the same frame and the same prompt, to compare the two.
>
> Four: edit the three shots into `final.mp4`, 15 to 25 seconds, in any editor or with the ffmpeg command from slide 13.
>
> Five: `video_spec.md` with prompts, settings and cost, calculated as attempts × seconds × price per second, as on slide 17. And `video_qa.md` with the six-item checklist from slide 18. Item six, shot joins, now applies because you edit three shots together.
>
> Grading is based on the defect analysis: where and why the model went wrong, with timecodes. A clean-looking video without analysis scores lower than a video with defects that are found and explained.
>
> No code is needed; everything is done in web studios. Free allowances are small and change often. Kling, for example, gives free accounts only a small monthly credit grant. Check the current terms before you start; the services table is in the homework file. Submit to `genai-homeworks/L05/`; the reviewer is me, `ihar_rubanovich@epam.com`. Templates are in `L05_05_Homework_EN.md`."

---

### Slide 21 (87:00–90:00) • Lesson summary

**On screen:** Five rules:
1. **Storyboard first**: the story is split into shots before any generation;
2. **Approved key frame before video generation**: image-to-video from an approved frame;
3. **One action per shot**: 4–8 seconds; the story comes from the storyboard and editing;
4. **Structured prompt**: camera + action + motion details;
5. **Acceptance and budget**: a checklist for every clip; cost is per second.

Right: a frame of the final video and a note: `Lesson 06: sound and speech. Current video models generate audio themselves. Controlling it is covered in L06.`

#### Speaker
> "Summary, five rules.
>
> One: storyboard first. The story is split into shots before any generation.
>
> Two: an approved key frame before video generation. We use image-to-video from a frame we have already checked.
>
> Three: one action per shot, 4 to 8 seconds. The story comes from the storyboard and editing.
>
> Four: a structured prompt: camera, action, motion details.
>
> Five: acceptance and budget. A checklist for every clip, and cost is counted per second.
>
> Next lesson: our clips actually have sound, generated by Veo 3.1 itself. How to control sound and speech is L06.
>
> Questions, by voice or in the Teams chat."

*(Open microphone until the end of the slot.)*
