Lecture 04 — Workshop and Homework

Hands-on visual control, QA and reproducibility


# In-class workshop — Image Workflow Pack

The goal is not to produce the prettiest image. The goal is to design a controllable request, evaluate candidates against a brief and produce a reproducible decision record.

# Choose one scenario

- E-commerce: preserve a product while changing background/season.
- Event: create a wide hero background with safe space for deterministic typography.
- Character: maintain identity while changing pose/environment.
- Travel/content: generate a hero visual with a specific composition and ratio.
- App/product: create one onboarding illustration and a second variation in the same visual language.
# Visual Generation Canvas


# Workshop steps

- Complete the canvas.
- Write one generation or edit prompt that contains explicit preservation rules.
- Produce or inspect two candidate outputs.
- Score both candidates using the rubric below.
- Choose one candidate and write one targeted revision instruction based on the observed defect.
- Submit the canvas, prompt, references, candidate scores and selected output.
# QA scorecard


# Homework — Reproducible Image Workflow Pack

- README.md: use case, provider/model used, date, target channel and run instructions.
- brief.md: completed Visual Generation Canvas.
- input/ or references/: source images you are allowed to use.
- prompt_v1.txt and prompt_v2.txt: initial and revised instructions.
- candidates/: at least two outputs or instructor-provided samples.
- qa.csv or qa.md: rubric scores and short notes.
- selected/: final accepted image.
- reflection.md: 5–8 sentences on what was controlled by text, what required a reference and what remains non-deterministic.
# Rubric




| Field | What students write |
| --- | --- |
| Business outcome | Where the image will be used and what it must communicate. |
| Target format | Aspect ratio, size, transparency/background requirement. |
| Sacred attributes | What must not change: product, face, logo, palette, pose, etc. |
| Allowed changes | Background, lighting, style, props, camera, season, crop. |
| References | Which images are needed and what each reference controls. |
| Composition | Subject placement, viewpoint, negative space, framing. |
| Style / light | Observable visual decisions, not vague adjectives. |
| Forbidden artifacts | Extra limbs/objects, text, watermark, geometry drift, etc. |
| QA criteria | Five concrete checks before acceptance. |



| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Instruction fidelity | Misses core request | Partially correct | Matches brief |
| Preservation | Critical drift | Minor drift | Sacred attributes preserved |
| Composition | Unusable crop/layout | Usable with compromise | Channel-ready |
| Artifacts | Visible blockers | Small repairable issue | Clean at review size |
| Text / marks | Wrong or unwanted | Minor issue | Correct / intentionally absent |
| Delivery | Wrong file/ratio | Needs conversion | Ready to use |



| Area | Weight |
| --- | --- |
| Visual specification is concrete and channel-aware | 20% |
| Preservation rules / reference strategy | 20% |
| Prompt or edit instruction is operational, not adjective-heavy | 20% |
| QA catches real defects and justifies selection | 20% |
| Reproducibility: files, versions/date, inputs and outputs are organized | 20% |

