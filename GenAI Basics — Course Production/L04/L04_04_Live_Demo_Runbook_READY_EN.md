# Lesson 04 • Live Demo Runbook & Prompt Copybook
## Ready-to-Copy Prompts for Live Demonstrations and Hands-On Sessions

**Course:** GenAI Basics • Module 2 (Multimodality)  
**Instructor:** Igor Rubanovich (EPAM Systems)  
**Models / Services:** Google Gemini (Nano Banana Pro / 2), ChatGPT (GPT-4o Images), Leonardo.ai, Midjourney v6.1  

This document is designed for quick, single-click copy-pasting during lectures and workshops. Each prompt has been tested and verified against the lesson's visual assets.

---

## Table of Contents

1. [Block 1: Free-form vs Structured Prompt (ChatGPT / Gemini)](#block-1-free-form-vs-structured-prompt)
2. [Block 2: Precise Text and Must-Have Details](#block-2-precise-text-and-must-have-details)
3. [Block 3: Delta Edits ("Change only X, keep the rest")](#block-3-delta-edits)
4. [Block 4: Leonardo.ai Demo (Canvas, Inpainting, Guidance Scale)](#block-4-leonardoai-demo)
5. [Block 5: Consistent Character (Glovo Delivery Courier Benchmark)](#block-5-consistent-character)
6. [Block 6: E-Commerce Product Photoshoot (Ceramic Mug)](#block-6-e-commerce-product-photoshoot)
7. [Block 7: Multi-Reference Composition (Character + Product)](#block-7-multi-reference-composition)
8. [Block 8: Photographer's Vocabulary (Optics and Lighting)](#block-8-photographers-vocabulary)
9. [Block 9: Interactive Hook (6 Historical Faces 2014–2026)](#block-9-interactive-hook)

---

## Block 1: Free-form vs Structured Prompt

> **Demo Goal:** Demonstrate how the model invents 80% of unspecified parameters in free-form mode, whereas structured prompting (6 slots) gives engineering-grade predictability.  
> **Where to paste:** ChatGPT, Gemini app, or Colab.  
> **Aspect Ratio:** 16:9.  

### 1.1. Free-form Prompt
```text
a cozy coffee shop in the morning
```
*Discussion point:* The model arbitrarily picks camera angle, people, furnishings, lighting, and mood. Complete loss of control.

### 1.2. Structured Engineering Prompt (6 Architectural Slots)
```text
Subject: a speckled cream ceramic mug of black coffee with a thin wisp of steam, standing on a worn oak counter in the right third of the frame.
Setting: a small Scandinavian-style coffee shop at 7 a.m., empty, chairs still up on two tables in the soft-focus background, a brass espresso machine on the left.
Composition and camera: eye-level, 35mm lens, f/2.0, shallow depth of field, the mug is the sharpest object.
Lighting: low warm sunlight from a window on the left, long soft shadows, dust visible in the light beam.
Style: realistic editorial photography, natural colors, slight film grain.
Constraints: no people, no text, no logos.
```
*Checklist:* Empty coffee shop? Chairs up on tables? Mug in right third? Light from left? Every slot is obeyed.

---

## Block 2: Precise Text and Must-Have Details

> **Demo Goal:** Show zero-typo text rendering and small object retention.  
> **Where to paste:** ChatGPT, Gemini app (Nano Banana Pro), or AI Studio.  
> **Aspect Ratio:** 16:9.  

```text
Subject: a speckled cream ceramic mug of black coffee with a thin wisp of steam, standing on a worn oak counter in the right third of the frame.
Setting: a small Scandinavian-style coffee shop at 7 a.m., empty, chairs still up on two tables in the soft-focus background, a brass espresso machine on the left.
Composition and camera: eye-level, 35mm lens, f/2.0, shallow depth of field, the mug is the sharpest object.
Lighting: low warm sunlight from a window on the left, long soft shadows, dust visible in the light beam.
Style: realistic editorial photography, natural colors, slight film grain.
Must-have details: next to the mug, a small black chalkboard sign written in white chalk handwriting that reads exactly "FLAT WHITE 3.50" on the first line and "OPEN 7:00" on the second line; a single croissant on a white plate behind the mug; a sprig of dried lavender in a tiny glass vase.
Constraints: no people, no other text, no logos.
```
*Rule:* Exact text must be enclosed in **quotes**, accompanied by the word *exactly*, concise, with no ambiguity.

---

## Block 3: Delta Edits

> **Demo Goal:** Avoid rerolling the entire image. Pass the previous output as a reference image and change exactly one variable.  
> **Where to paste:** ChatGPT (same thread) or Gemini app (attach Block 1.2 output).  

### 3.1. Object Swap
**Reference:** Attach `A2_structured.png` (or Block 1.2 output).
```text
Edit this photo. Replace only the ceramic mug with a tall glass of iced latte with visible layers of coffee and milk and a few ice cubes. Keep everything else exactly the same: camera angle, framing, counter, espresso machine, background, light direction and shadows. The new glass must cast a matching shadow on the counter.
```

### 3.2. Relighting & Atmosphere
**Reference:** Attach `A2_structured.png`.
```text
Edit this photo. Change only the time of day to a rainy evening: dark blue dusk outside the window, raindrops on the glass, warm interior pendant lamps switched on. Keep the exact same composition, objects, mug and camera angle.
```

---

## Block 4: Leonardo.ai Demo

> **Demo Goal:** Demonstrate Tier 2 Creative Canvas capabilities: inpainting brush, precise Guidance Scale, and negative prompting.  
> **Where to open:** [leonardo.ai](https://leonardo.ai) $\to$ **Canvas Editor** (or Image Generation).  

### 4.1. Generation in Leonardo (Photoreal / Phoenix)
* **Prompt:**
```text
cinematic medium shot of an artisanal coffee corner, raw wooden table, ceramic tableware, soft morning haze, 50mm f/1.4, hyperrealistic, high fidelity
```
* **Negative Prompt:**
```text
blurry, low quality, cartoon, oversaturated, deformed hands, duplicate objects, plastic skin, watermark, signature
```
* **Panel Settings:**
  - Model: Leonardo Phoenix or Kino XL
  - Guidance Scale: `7.0` (setting it to 14 causes high-contrast saturation burn; setting it to 3 ignores prompt semantics)
  - Aspect Ratio: `16:9`

### 4.2. Inpainting in Canvas (Brush Masking)
1. Load the generated shot onto the Canvas.
2. Select **Mask Tool (Brush)** and paint over only the mug / foreground item.
3. Align the Bounding Box over the masked region.
4. Input replacement prompt:
```text
a vintage bronze mechanical alarm clock, intricate gears, ticking bells, soft warm reflection
```
5. Click **Generate** to produce 4 tailored inpainting options.

---

## Block 5: Consistent Character

> **Benchmark:** The Glovo food delivery courier case study from L01.  
> **Where to paste:** ChatGPT, Gemini (Nano Banana Pro), or Midjourney.  

### 5.1. Master Reference: Character Sheet
```text
Character reference sheet on a plain light grey background: the same young woman food delivery courier shown four times in a row - front view, three-quarter view, side profile, back view - full body, standing neutral pose. Fixed appearance: about 28 years old, short curly dark-brown hair, light-brown skin, small silver hoop earring in the left ear, bright yellow waterproof jacket with a reflective grey stripe across the chest, black cargo trousers, white sneakers, a square turquoise thermal delivery backpack. No brand names, no logos, no text. Clean, evenly lit studio photography.
```
*Save output as `C1_sheet.png`.*

### 5.2. Scene 1: Bicycle in the Rain
**Reference:** Attach `C1_sheet.png`.
```text
Use the attached character sheet as the identity reference. The same courier (same face, hair, earring, yellow jacket with grey stripe, turquoise backpack) is riding a city bicycle through a rainy evening street with wet cobblestones reflecting shop lights. Medium shot, 50mm lens, motion blur in the background. Realistic photography. No logos, no text.
```

### 5.3. Scene 2: Handing Order at Customer Door
**Reference:** Attach `C1_sheet.png`.
```text
Use the attached character sheet as the identity reference. The same courier (same face, hair, earring, yellow jacket with grey stripe, turquoise backpack on her back) is standing at an apartment door and handing a brown paper food bag to a customer, whose hands only are visible. Warm hallway light, eye-level, 35mm lens. Realistic photography. No logos, no text.
```

### 5.4. Scene 3: Park Bench Break
**Reference:** Attach `C1_sheet.png`.
```text
Use the attached character sheet as the identity reference. Close-up portrait of the same courier (same face, curly hair, silver hoop earring, yellow jacket with grey stripe) sitting on a park bench during a break, smiling at her phone, turquoise backpack beside her. Golden-hour backlight, 85mm lens, f/1.8. Realistic photography. No logos, no text.
```

---

## Block 6: E-Commerce Product Photoshoot

> **Case:** Handmade ceramic artisan mug.  
> **Aspect Ratio:** 1:1 (catalog/marketplace standard).  

### 6.1. Master Packshot on Pure White
```text
Studio e-commerce packshot of a single handmade ceramic mug: cylindrical body, speckled cream glaze with small brown dots, unglazed terracotta-brown band at the base, round C-shaped handle on the right. Centered, three-quarter front view, pure white seamless background, soft even light, subtle contact shadow. No text, no logo.
```
*Save output as `D0_packshot.png`.*

### 6.2. Shot 1: Lifestyle Kitchen Counter
**Reference:** Attach `D0_packshot.png`.
```text
Product photo session. Place exactly this mug (same shape, speckled cream glaze, terracotta base band, handle on the right) on a light travertine kitchen counter next to a window in the morning. A moka pot and a linen towel out of focus behind. Soft natural light, 50mm lens, f/2.8. Do not change the mug's shape, color, glaze pattern or proportions.
```

### 6.3. Shot 2: Top-down Flat Lay
**Reference:** Attach `D0_packshot.png`.
```text
Product photo session. Overhead flat lay, top-down view: exactly this mug (same speckled cream glaze and terracotta base) filled with cappuccino with latte art, on a sage-green linen cloth, surrounded by scattered coffee beans, an open notebook and a small spoon. Even diffused light. Do not change the mug's design.
```

### 6.4. Shot 3: In Hands at Outdoor Cafe
**Reference:** Attach `D0_packshot.png`.
```text
Product photo session. Two hands in a knitted beige sweater hold exactly this mug (same speckled cream glaze, terracotta base band, handle shape) at an outdoor cafe table on an autumn morning; blurred street and fallen leaves in the background. 85mm lens, f/1.8, warm tones. Keep the mug design identical.
```

### 6.5. Shot 4: Minimalist Ad Banner with Typography
**Reference:** Attach `D0_packshot.png`.
```text
Minimalist advertising banner. Exactly this mug on a dark charcoal stone surface, dramatic side light from the left, a soft curl of steam. Large clean sans-serif headline in the upper area that reads exactly "MORNING RITUAL" and a smaller line below it that reads exactly "Handmade ceramics". Generous negative space. Keep the mug design identical.
```

---

## Block 7: Multi-Reference Composition

> **Demo Goal:** Provide **two distinct reference images** and explicitly assign their roles (Identity Reference vs Product Reference).  
> **References:** Attach `C1_sheet.png` (Reference 1) and `D0_packshot.png` (Reference 2).  
> **Where to paste:** Google Gemini (Nano Banana Pro) or ChatGPT Images.  
> **Aspect Ratio:** 16:9.  

```text
Combine the two references. Image 1 is the character (identity reference), image 2 is the product (product reference). The same courier from image 1, in her yellow jacket with grey stripe, sits at a coffee shop window counter on her break and drinks from exactly the mug from image 2 (same speckled cream glaze and terracotta base). Her turquoise backpack is on the floor next to her stool. Morning light, 35mm lens, realistic photography. No logos, no text.
```

---

## Block 8: Photographer's Vocabulary

> **Demo Goal:** Demonstrate how optics and lighting terminology control composition without changing character identity.  
> **Reference:** Attach `C1_sheet.png`.  
> **Aspect Ratio:** 4:3.  

### 8.1. 24mm Wide Angle (Environmental Context)
```text
Use the attached character sheet as the identity reference: the same courier (same face, curly hair, yellow jacket with grey stripe, turquoise backpack), standing next to her city bicycle on a quiet street. Realistic photography. No logos, no text. Camera: 24mm wide-angle lens, wide shot, the courier small in the frame, the whole street and buildings visible.
```

### 8.2. 85mm Portrait Lens (f/1.8 Bokeh Blur)
```text
Use the attached character sheet as the identity reference: the same courier (same face, curly hair, yellow jacket with grey stripe, turquoise backpack), standing next to her city bicycle on a quiet street. Realistic photography. No logos, no text. Camera: 85mm portrait lens, f/1.8, head-and-shoulders close-up, strongly blurred background bokeh.
```

### 8.3. Low Angle (Hero Shot)
```text
Use the attached character sheet as the identity reference: the same courier (same face, curly hair, yellow jacket with grey stripe, turquoise backpack), standing next to her city bicycle on a quiet street. Realistic photography. No logos, no text. Camera: low angle shot from knee height looking up, 35mm lens.
```

### 8.4. Golden Hour (Warm Rim Light)
```text
Use the attached character sheet as the identity reference: the same courier (same face, curly hair, yellow jacket with grey stripe, turquoise backpack), standing next to her city bicycle on a quiet street. Realistic photography. No logos, no text. Light: golden hour, low warm sun behind her, rim light on her hair, long shadows. Medium shot, 50mm.
```

---

## Block 9: Interactive Hook

> Prompts used to generate the 2014–2026 historical portrait sequence:

### 9.1. GAN 2014 (Early Pixel Era)
```text
A low-resolution 64x64 pixelated blurry face of a person, early GAN 2014 era, extreme pixelation, distorted blurry features, monochrome grey and muted sepia colors, retro CRT monitor macro texture. No text, no letters.
```

### 9.2. StyleGAN 2018 (Ear Artifact & Plastic Skin)
```text
Headshot of a smiling young man generated by early StyleGAN in 2018. Slightly plastic skin texture, perfectly centered face, blurred ambiguous background with colorful bokeh artifacts, subtle asymmetry in the left ear structure. No text.
```

### 9.3. Stable Diffusion 2022 (Airbrushed Gloss)
```text
A studio portrait of a woman with smooth glossy plastic skin, characteristic of Stable Diffusion 1.5 in 2022, slightly airbrushed look, cinematic lighting, oversaturated digital art style, soft focus background. No text.
```

### 9.4. Midjourney v5 2023 (Cinematic Chiaroscuro)
```text
Cinematic 35mm portrait of a middle-aged craftsman in a leather apron, dramatic chiaroscuro Rembrandt lighting, rich color grading, sharp detailed stubble and eyes, moody atmospheric background, Midjourney aesthetic. No text.
```

### 9.5. FLUX.1 2024 (Photorealistic Pores & Wrinkles)
```text
Ultra-realistic candid close-up portrait of an elderly fisherman with deep wrinkles, weathered skin with visible pores and sunspots, natural daylight, grey beard, wool beanie, authentic unedited raw photography. No text.
```

### 9.6. Nano Banana Pro 2026 (Candid Smartphone Reality)
```text
An authentic smartphone photo taken in October 2026: a young woman laughing in a crowded outdoor cafe, holding a matcha latte, natural messy windblown hair, candid imperfect expression, realistic skin imperfections, authentic daylight, subtle lens distortion of a modern phone camera. No text.
```

---

## Service Parameters Quick Reference

| Service | Key Parameters | Core Production Trick |
|---|---|---|
| **ChatGPT** | Conversational chat | "Change only X, keep the rest". Enclose exact text in quotes `""`. |
| **Gemini / Nano Banana** | Multi-reference input (up to 3) | "Image 1 is character, Image 2 is product". Top-tier typo-free text rendering. |
| **Leonardo.ai** | Guidance Scale `7–9`, Canvas Inpainting | Mask only the modified area with brush; keep background fixed. |
| **Midjourney** | `--ar 16:9`, `--v 6.1`, `--style raw`, `--s 100` | Click **Vary (Region)** for inpainting; use `--cref <url>` for character consistency. |
