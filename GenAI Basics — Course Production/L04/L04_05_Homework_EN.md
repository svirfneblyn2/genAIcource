# Lesson 04 • Homework: a product photo shoot or a courier character

**Course:** GenAI Basics • Module 2 (Multimodality)
**Submit:** the `genai-homeworks/L04/` folder in your repository (collaborator `ihar_rubanovich@epam.com`)
**Time:** 1.5–2 hours
**Tools:** any two services from the lesson ecosystem (we recommend comparing across different tiers: e.g., Tier 2 Creative Canvas — **Leonardo.ai** vs. Tier 3 Multimodal Chat — **ChatGPT** or **Gemini / Nano Banana**; Midjourney, Sintx, Kling are also valid). Free tiers are sufficient. The lesson Colab (`notebooks/L04_Image_Generation_Prompts_and_Patterns.ipynb`) is optional.

---

## Goal

Apply three skills from the lesson to your own task:
1. moving from a free-form prompt to a structured one;
2. the "change only X, keep the rest" edit;
3. consistency: the same product or character across several shots.

## Pick a track

### Track A — AI product photo shoot

1. **Master shot.** Photograph your own object on a plain background with a phone (a mug, headphones, a book, a backpack) or generate a packshot.
2. **Product traits.** List 4–6 traits that must not change (shape, color, material, pattern, proportions, details).
3. **Shot list of 4:** lifestyle • top-down flat lay • product in hands • banner with text (exact phrase in quotes).
4. Each shot: master shot as reference + product traits + new scene + camera and light + the line "do not change the shape, color, pattern or proportions".

### Track B — courier character (the Glovo food delivery courier case from L01)

1. **Character sheet:** your courier from 3–4 angles on a neutral background, 4–6 distinctive anchor traits (clothes, bag color, hair, an accessory).
2. **Three scenes from a working day** (e.g. on the road, at a customer's door, on a break). The sheet is the reference; traits are repeated in words in every prompt.
3. **One targeted edit** of any scene: an object swap or a time-of-day change using "change only X, keep the rest".

> No logos or names of real brands in the images: a brand is someone else's trademark (the red zone of the lesson's traffic light).

## Common part (both tracks)

| # | Task | Where |
|---|---|---|
| 1 | One shot with two prompts: free-form (one phrase) and structured (slots: subject, setting, composition and camera, lighting, style, must-have details, constraints) | `images/01_free.png`, `images/02_structured.png` |
| 2 | The same structured prompt in **two different services** | `images/03_<service>.png` ×2 and a row in `qa.md` |
| 3 | Record every prompt | `prompts.md` |
| 4 | Assess the result honestly against the checklist | `qa.md` |

## Folder structure

```
genai-homeworks/
└── L04/
    ├── images/          # all final images, numbered: 01_free.png, 02_structured.png, ...
    ├── prompts.md       # the prompt for every image (template below)
    └── qa.md            # checklist and service comparison (template below)
```

If you used Colab: Step 8 of the notebook builds `prompts.md` and packs the images into `L04_homework.zip`.

## `prompts.md` template

````markdown
## 02_structured.png
- Service / model: Gemini app (Nano Banana 2)
- Date: 2026-10-10
- References: —
- Aspect: 16:9

```text
Subject: ...
Setting: ...
Composition and camera: ...
Lighting: ...
Style: ...
Must-have details: ...
Constraints: ...
```
````

## `qa.md` template

```markdown
# L04 QA

## Track: A / B

## Traits that must be preserved
1. ...
2. ...

## Per-shot check
| Image | Traits preserved (✓/✗ each) | What drifted | Iterations needed |
|---|---|---|---|
| 03_kitchen.png | 1 ✓ 2 ✓ 3 ✗ 4 ✓ | pattern got smaller | 3 |

## Free-form vs structured
What the model decided on its own in the free-form version (3–5 items): ...

## Two services, one prompt
| Criterion | Service 1 | Service 2 |
|---|---|---|
| Prompt following | | |
| Text in image | | |
| Product/character preserved | | |
| Aesthetics | | |
| Verdict: which one I'd pick for this task and why | | |
```

## Grading

| Criterion | What we check |
|---|---|
| Prompt structure | Slots are visible; must-have details and constraints are present |
| Free-form ↔ structured | `qa.md` lists what the model decided on its own |
| Consistency | The product or character is recognizable in every shot; traits checked against the list |
| Edit | One thing changed, the rest preserved (Track B) / the product unchanged across scenes (Track A) |
| Reproducibility | Every image has service, model, date and prompt |
| Honest QA | Drifted details are recorded. That is an observation, not a penalty |

## Tips

- Write the prompt as connected sentences by slot, most important first.
- Text in the image goes in quotes, with *exactly*, and short.
- One edit per turn. If the image degrades after 6–8 edits, start a new chat with the best version as a reference.
- For a character, distinctive traits (turquoise backpack, reflective stripe) hold better than "a regular jacket".
- Midjourney: parameters go at the end of the prompt (`--ar 4:5 --s 100 --raw`); use the Edit tool for edits.
- Leonardo.ai: leverage Canvas and Inpainting for precise brush-based replacements, keeping Guidance Scale around 7–9.
- ChatGPT / Gemini (Nano Banana): instruct the edit with conversational natural language ("change only X, keep the rest"), relying on the model's strong scene semantics.
