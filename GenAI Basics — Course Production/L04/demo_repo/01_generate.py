import os, base64
from pathlib import Path
from google import genai

MODEL = os.getenv("GEMINI_IMAGE_MODEL", "gemini-3.1-flash-image")
PROMPT = (
    "Premium product photograph of one speckled ceramic coffee mug on pale travertine. "
    "Warm late-afternoon side light, soft natural shadow, shallow depth of field. "
    "Single hero object, clean negative space on the right, natural editorial photography, "
    "no text, no watermark, no duplicate mug, no extra handle."
)

client = genai.Client()
interaction = client.interactions.create(
    model=MODEL,
    input=PROMPT,
    response_format={"type":"image", "aspect_ratio":"16:9", "image_size":"2K"},
)
out = Path("out/generated_product_hero.png")
out.parent.mkdir(exist_ok=True)
out.write_bytes(base64.b64decode(interaction.output_image.data))
print(out)
