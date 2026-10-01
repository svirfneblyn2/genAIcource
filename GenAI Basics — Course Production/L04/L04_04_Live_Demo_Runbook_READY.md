Lecture 04 — Live Demo Runbook

Generate and edit a product image with visible control decisions


# Goal

Show two things students can see immediately: (1) an image API returns binary image output rather than prose; (2) a source/reference image plus preservation rules gives a more controllable edit than a vague “make it nicer” instruction.

# Pre-class setup

- Python 3.10+; create and activate a clean virtual environment.
- Install: pip install -r requirements.txt.
- Set GEMINI_API_KEY in the environment. Never show the key in terminal history or slides.
- Confirm demo_assets/input_product.png opens correctly.
- Run 00_smoke_check.py. If the API/model is unavailable, switch to prepared outputs and teach the flow without pretending the live call succeeded.
- Close unrelated browser tabs and any folders containing private images.
# Demo 1 — text to image

python 01_generate.py
# output: out/generated_product_hero.png


- Before running, read the prompt fields aloud: subject, surface, composition, camera, lighting, style, constraints, ratio.
- After generation, do not say “looks nice”. Score it: instruction fidelity, crop/composition, artifacts, text/marks, delivery ratio.
- Point out that the code decodes base64 image bytes and writes a file. Connect this to response parsing from Lecture 03.
# Demo 2 — vague edit vs controlled edit

Vague prompt: “Make this mug photo look like a premium campaign image in a beautiful warm studio.”

Controlled prompt: “Replace only the background and supporting surface with a warm sunlit travertine studio. Preserve mug shape, speckled glaze, handle position and camera angle. Single mug only. No text, watermark or extra objects.”

python 02_edit.py --mode vague
python 02_edit.py --mode controlled
# outputs are written to out/


# What to inspect side by side


# Fallback plan

- Open demo_assets/input_product.png and demo_assets/expected_edit_example.png.
- Show the prepared product-workflow studio visual in the deck. Explain input → preservation rules → candidates → final selection.
- Use 03_build_prompt.py to print the exact structured prompt without making an API request.
- Never invent an API response. If the provider refuses or times out, label that failure and teach operational fallback.
# Teaching warnings

- Do not upload student/private photos without consent and a clear reason.
- Do not promise exact identity or logo preservation from a single prompt; inspect the output.
- Do not treat model refusal as a bug to “prompt around”.
- Do not let students copy volatile model IDs into long-lived code without a configuration layer.


| Area | Question |
| --- | --- |
| Product identity | Did shape, handle, texture or proportions drift? |
| Requested change | Did the background/surface change as asked? |
| Object count | Did the model invent another mug/prop? |
| Camera | Did angle/crop move unexpectedly? |
| Artifacts | Broken edges, duplicated handles, halos, impossible shadows? |
| Usefulness | Could the result ship without manual repair? |

