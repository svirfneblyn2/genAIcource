import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


def get_model() -> str:
    return os.getenv("OPENAI_MODEL", "gpt-5.6-terra")


def build_client() -> OpenAI:
    # Explicit limits make the demo policy visible instead of relying on defaults.
    return OpenAI(timeout=20.0, max_retries=2)
