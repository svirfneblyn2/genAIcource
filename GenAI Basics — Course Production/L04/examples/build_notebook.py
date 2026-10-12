"""Generates notebooks/L04_Image_Generation_Prompts_and_Patterns.ipynb (+ a copy in L04/).

The notebook mirrors the lesson: free-form vs structured prompt, must-have details,
"change only X" edits, a consistent character, a product photo shoot, multi-reference
composition, a prompt template and a homework export. Prompts are the ones from
examples/prompts.json so students reproduce the slide images.

    python examples/build_notebook.py
"""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
NAME = "L04_Image_Generation_Prompts_and_Patterns.ipynb"
P = {e["id"]: e["prompt"] for e in json.loads((HERE / "prompts.json").read_text(encoding="utf-8"))["examples"]}

cells = []


def md(text: str) -> None:
    cells.append({"cell_type": "markdown", "metadata": {}, "source": text.strip("\n")})


def code(text: str) -> None:
    cells.append({"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": text.strip("\n")})


def pyq(s: str) -> str:
    """Python triple-quoted literal for a prompt."""
    return '"""' + s.replace("\\", "\\\\").replace('"""', '\\"\\"\\"') + '"""'


md(f"""<a href="https://colab.research.google.com/github/svirfneblyn2/genAIcource/blob/main/notebooks/{NAME}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>""")

md("""
# Lesson 04: Image Generation — Prompt Techniques and Control Patterns
**Course:** GenAI Basics | **Instructor:** Igor Rubanovich (EPAM Systems) | **Model:** Nano Banana 2 (`gemini-3.1-flash-image`)

Every pattern from the lesson slides, in code. The prompts are the same ones that produced the slide images, so you can compare your results with the deck.

| Step | Pattern | What you will see |
|---|---|---|
| 1 | Free-form vs structured prompt | Six words let the model decide everything; six slots put you in control |
| 2 | Must-have details and text | Exact text, counts and positions survive when you list them explicitly |
| 3 | Edit: "change only X" | Swap one object, keep the rest of the scene pixel-stable |
| 4 | Consistent character | Character sheet → the same person in new scenes |
| 5 | Product photo shoot | One packshot (yours or generated) → a shot list |
| 6 | Multi-reference composition | Character + product in one scene |
| 7 | Your turn: prompt template | Build prompts from a dict instead of free text |
| 8 | Homework export | `prompts.md` + images, ready to commit |

**How to use:** run cells top to bottom (**Shift + Enter**). Images are probabilistic: yours will differ from the slides — compare *what was preserved*, not pixels.

> 💳 **Billing note.** Image generation through the API may require a billing-enabled key, depending on your account and region. If a call fails with a quota or billing error, run the same prompts in the **Gemini app** or **[AI Studio](https://aistudio.google.com)** — the lesson patterns work identically there.
""")

md("""
## Step 0: Connect (same as L03)
1. Create a key at **[aistudio.google.com/apikey](https://aistudio.google.com/apikey)**.
2. In Colab: 🔑 **Secrets** → **+ Add new secret** → name `GEMINI_API_KEY`, paste the key, switch on **Notebook access**.
3. Run the cell below. It also defines one helper, `generate()`, used by every step: it sends text + optional reference images, shows the result, saves it to `out/` and writes an entry to a **generation log** (model, prompt, references, time) — the reproducibility record from the lesson.
""")

code('''
!pip install -q -U google-genai pillow

import datetime, json, pathlib
from google import genai
from google.genai import types
from google.colab import userdata
from PIL import Image
from IPython.display import display

MODEL = "gemini-3.1-flash-image"        # Nano Banana 2. Cheaper/faster: "gemini-3.1-flash-lite-image"

client = genai.Client(
    api_key=userdata.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(
        timeout=120_000,                                                    # images take longer than text
        # image quotas are tight: retry 429 / 5xx with long, growing pauses (5 s, 10 s, 20 s, ... up to 60 s)
        retry_options=types.HttpRetryOptions(attempts=7, initial_delay=5, max_delay=60),
    ),
)

OUT = pathlib.Path("out"); OUT.mkdir(exist_ok=True)
LOG = []   # generation log: one dict per image


def generate(name, prompt, refs=(), aspect="1:1", show_width=520):
    """Text (+ reference images) -> one image. Saves out/<name>.png and logs the call."""
    ref_images = [Image.open(OUT / f"{r}.png") if isinstance(r, str) else r for r in refs]
    resp = client.models.generate_content(
        model=MODEL,
        contents=[*ref_images, prompt],                       # references first, then the instruction
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(aspect_ratio=aspect),
        ),
    )
    image_parts = [p for p in (resp.parts or []) if p.inline_data]
    if not image_parts:
        raise RuntimeError(f"No image returned (blocked or refused). Text: {resp.text}")
    path = OUT / f"{name}.png"
    image_parts[0].as_image().save(str(path))
    LOG.append({
        "name": name, "model": MODEL, "aspect": aspect, "prompt": prompt,
        "refs": [r if isinstance(r, str) else "uploaded" for r in refs],
        "time": datetime.datetime.now().isoformat(timespec="seconds"),
        "output_tokens": resp.usage_metadata.candidates_token_count,
    })
    img = Image.open(path)
    img.thumbnail((show_width, show_width)); display(img)
    print(f"saved {path}  |  output tokens: {resp.usage_metadata.candidates_token_count}")
    return path

print(f"Client ready. Model: {MODEL}")
''')

md("""
---
## Step 1: Free-form vs structured prompt
**Free-form** is fine for ideas — but every word you do not write, the model fills with the most "average" option: time of day, people, props, framing, style.

**Structured** = six slots, most important first:

```
Subject → Setting → Composition & camera → Lighting → Style → Constraints
```
Run both and list what the model decided on its own in the first image.
""")
code(f'''
FREE = "a cozy coffee shop in the morning"
generate("A1_free", FREE, aspect="16:9")
''')
code(f'''
STRUCTURED = {pyq(P["A2_structured"])}
generate("A2_structured", STRUCTURED, aspect="16:9")
''')
md("""
**Check:** is the shop empty? chairs up on tables? mug in the right third? light from the left? Each slot you wrote should be visible.
""")

md("""
---
## Step 2: Must-have details and text in the image
Add a separate block with the details you will check one by one:
* text in **quotes** with the word *exactly*, one phrase per line;
* **counts as numbers** ("one croissant"), **positions explicitly** ("next to", "behind");
* forbid extras: "no other text".
""")
code(f'''
DETAILS = {pyq(P["A3_details"])}
generate("A3_details", DETAILS, aspect="16:9")
''')

md("""
---
## Step 3: Edit — "change only X, keep everything else"
Do not regenerate when 80% of the image works. Pass the image back as a **reference** and change **one** thing, naming what must stay.
""")
code(f'''
EDIT_SWAP = {pyq(P["B1_replace"])}
generate("B1_replace", EDIT_SWAP, refs=["A2_structured"], aspect="16:9")
''')
code(f'''
EDIT_LIGHT = {pyq(P["B2_relight"])}
generate("B2_relight", EDIT_LIGHT, refs=["A2_structured"], aspect="16:9")
''')
md("""
**Check:** compare with `A2_structured`. Did the background, chairs and camera angle stay? Anything else drift? One edit per turn makes this easy to see.
""")

md("""
---
## Step 4: Consistent character
Recipe from the lesson:
1. **Master reference** — a character sheet: several angles, neutral background, fixed traits.
2. **Anchor traits in words** — repeat 4–6 distinctive traits in every scene prompt.
3. **Scene** = reference + anchors + new action. 4. **Check** the traits.

Our character is the food delivery courier from the L01 homework case.
""")
code(f'''
SHEET = {pyq(P["C1_sheet"])}
generate("C1_sheet", SHEET, aspect="16:9", show_width=800)
''')
code(f'''
SCENE_RAIN = {pyq(P["C2_rain"])}
generate("C2_rain", SCENE_RAIN, refs=["C1_sheet"], aspect="4:3")

SCENE_DOOR = {pyq(P["C3_door"])}
generate("C3_door", SCENE_DOOR, refs=["C1_sheet"], aspect="4:3")
''')
md("""
**Check the anchors:** hair, earring, yellow jacket **with the grey stripe**, turquoise backpack. Distinctive traits hold better than generic ones.
""")

md("""
---
## Step 5: Product photo shoot
Use **your own product photo** (a mug, headphones, a book — anything on a plain background) or generate a packshot.
The pattern is the same as for the character: master reference + preserved traits + new scene from a shot list.
""")
code(f'''
USE_MY_PHOTO = False   # set True to upload your own product photo

if USE_MY_PHOTO:
    from google.colab import files
    uploaded = files.upload()                       # pick one image
    Image.open(next(iter(uploaded))).convert("RGB").save(OUT / "D0_packshot.png")
    display(Image.open(OUT / "D0_packshot.png").resize((360, 360)))
else:
    PACKSHOT = {pyq(P["D0_packshot"])}
    generate("D0_packshot", PACKSHOT, aspect="1:1", show_width=360)
''')
code('''
# Describe YOUR product's traits here if you uploaded your own photo.
PRODUCT_TRAITS = "same shape, speckled cream glaze, terracotta-brown base band, round handle"

SHOT_LIST = {
    "D1_kitchen": "on a light travertine kitchen counter next to a window in the morning, a moka pot out of focus behind; soft natural light, 50mm lens, f/2.8",
    "D2_flatlay": "overhead flat lay, top-down view, on a sage-green linen cloth with scattered coffee beans and an open notebook; even diffused light",
    "D4_banner":  'minimalist ad banner on dark charcoal stone, dramatic side light; large clean sans-serif headline that reads exactly "MORNING RITUAL"; generous negative space',
}

for name, scene in SHOT_LIST.items():
    prompt = (f"Product photo session. Place exactly this product ({PRODUCT_TRAITS}) {scene}. "
              "Do not change the product's shape, color, pattern or proportions.")
    generate(name, prompt, refs=["D0_packshot"], aspect="1:1", show_width=360)
''')
md("""
Note the structure: the **traits** and the **"do not change"** line are constant; only the scene varies. That is a template — Step 7 makes it explicit.
""")

md("""
---
## Step 6: Multi-reference composition
With several references, **number them and name each one's role** (character, product, style, background). "Combine these" alone is ambiguous.
""")
code(f'''
COMPOSE = {pyq(P["E1_compose"])}
generate("E1_compose", COMPOSE, refs=["C1_sheet", "D0_packshot"], aspect="16:9", show_width=800)
''')

md("""
---
## Step 7: Your turn — a prompt template
Treat a prompt as data: fill the slots, render the text. The same spec can be reused for a whole series and stored next to the result.
Change the values below to your own idea and run.
""")
code('''
SLOTS = ["subject", "setting", "composition", "lighting", "style", "must_have", "constraints"]

def build_prompt(spec: dict) -> str:
    labels = {"subject": "Subject", "setting": "Setting", "composition": "Composition and camera",
              "lighting": "Lighting", "style": "Style", "must_have": "Must-have details", "constraints": "Constraints"}
    return "\\n".join(f"{labels[k]}: {spec[k]}" for k in SLOTS if spec.get(k))

my_spec = {
    "subject": "a red city bicycle with a wicker basket full of sunflowers",
    "setting": "a narrow cobblestone street in Lisbon, early morning, empty",
    "composition": "eye-level, 35mm lens, bicycle in the left third, shallow depth of field",
    "lighting": "low warm sun from the right, long shadows",
    "style": "realistic travel photography, natural colors",
    "must_have": 'a small blue street sign on the wall that reads exactly "RUA DO SOL"',
    "constraints": "no people, no other text",
}

MY_PROMPT = build_prompt(my_spec)
print(MY_PROMPT, "\\n")
generate("my_image", MY_PROMPT, aspect="16:9")
''')

md("""
---
## Step 8: Export for homework
Writes `prompts.md` from the generation log (model, aspect, references, time, full prompt for every image) and packs it with the images into `L04_homework.zip`.
Download the zip (Files panel on the left → right-click → Download), unpack into `genai-homeworks/L04/`, add your `qa.md` and commit.
""")
code('''
import zipfile

lines = ["# L04 — generation log", ""]
for e in LOG:
    lines += [f"## {e['name']}",
              f"- model: `{e['model']}` • aspect: {e['aspect']} • refs: {', '.join(e['refs']) or '—'} • time: {e['time']}",
              "", "```text", e["prompt"], "```", ""]
pathlib.Path("prompts.md").write_text("\\n".join(lines), encoding="utf-8")
pathlib.Path("generation_log.json").write_text(json.dumps(LOG, indent=2, ensure_ascii=False), encoding="utf-8")

with zipfile.ZipFile("L04_homework.zip", "w") as z:
    z.write("prompts.md"); z.write("generation_log.json")
    for p in sorted(OUT.glob("*.png")):
        z.write(p, f"images/{p.name}")
print(f"{len(LOG)} images logged -> prompts.md, generation_log.json, L04_homework.zip")
''')

nb = {
    "cells": cells,
    "metadata": {"colab": {"name": NAME, "provenance": [], "include_colab_link": True},
                 "kernelspec": {"display_name": "Python 3", "name": "python3"}, "language_info": {"name": "python"}},
    "nbformat": 4, "nbformat_minor": 0,
}
for target in (REPO / "notebooks" / NAME, HERE.parent / NAME):
    target.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", target)
