import os, base64, argparse
from pathlib import Path
from google import genai

parser = argparse.ArgumentParser()
parser.add_argument("--mode", choices=["vague","controlled"], default="controlled")
args = parser.parse_args()
MODEL = os.getenv("GEMINI_IMAGE_MODEL", "gemini-3.1-flash-image")

prompts = {
    "vague": "Make this mug photo look like a premium campaign image in a beautiful warm studio.",
    "controlled": (
        "Replace only the background and supporting surface with a warm sunlit travertine studio. "
        "Preserve the mug shape, speckled glaze, handle position, proportions and camera angle. "
        "Single mug only. No text, watermark or extra objects."
    ),
}
input_path = Path("input_product.png")
image_b64 = base64.b64encode(input_path.read_bytes()).decode("utf-8")
client = genai.Client()
interaction = client.interactions.create(
    model=MODEL,
    input=[
        {"type":"text", "text":prompts[args.mode]},
        {"type":"image", "mime_type":"image/png", "data":image_b64},
    ],
    response_format={"type":"image", "aspect_ratio":"3:4", "image_size":"2K"},
)
out = Path(f"out/edit_{args.mode}.png")
out.parent.mkdir(exist_ok=True)
out.write_bytes(base64.b64decode(interaction.output_image.data))
print(out)
