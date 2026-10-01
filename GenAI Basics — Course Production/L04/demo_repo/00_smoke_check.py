import os
from pathlib import Path

model = os.getenv("GEMINI_IMAGE_MODEL", "gemini-3.1-flash-image")
key = os.getenv("GEMINI_API_KEY")
asset = Path("input_product.png")
print("model:", model)
print("GEMINI_API_KEY configured:", bool(key))
print("input_product.png exists:", asset.exists())
if not key:
    raise SystemExit("Set GEMINI_API_KEY before live API calls.")
