import importlib.metadata as md
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

print(f"Python: {sys.version.split()[0]}")
for package in ("openai", "pydantic", "python-dotenv"):
    try:
        print(f"{package}: {md.version(package)}")
    except md.PackageNotFoundError:
        print(f"{package}: NOT INSTALLED")

model = os.getenv("OPENAI_MODEL", "gpt-5.6-terra")
key_present = bool(os.getenv("OPENAI_API_KEY"))
print(f"Model: {model}")
print(f"API key present: {key_present}")
print(f"Repo: {BASE_DIR}")
print("Preflight does not call the network.")
