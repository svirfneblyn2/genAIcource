"""Vertex AI Image Generator (Nano Banana Pro / gemini-3-pro-image)
Connects directly to Google Cloud Vertex AI using service-account credentials
from existing projects without IDE rate limits.
"""

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional

from google.auth.transport.requests import Request
from google.oauth2 import service_account

# Candidate credential paths discovered across the workspace
CANDIDATE_SA_PATHS = [
    os.environ.get("GOOGLE_VERTEX_CREDENTIALS"),
    r"D:\Repos\dark-factory\dark-factory-lab\secrets\vertex-sa.json",
    r"D:\Repos\eatzy reciepes\secrets\vertex-sa.json",
]

DEFAULT_MODEL = os.environ.get("VERTEX_IMAGE_MODEL", "gemini-3-pro-image")
DEFAULT_LOCATION = os.environ.get("GOOGLE_VERTEX_LOCATION", "global")


def find_credentials_path() -> Path:
    for candidate in CANDIDATE_SA_PATHS:
        if candidate and os.path.isfile(candidate):
            return Path(candidate)
    raise FileNotFoundError(
        "Could not find Vertex AI service-account JSON in environment or standard project paths."
    )


def get_vertex_token(sa_path: Path):
    creds = service_account.Credentials.from_service_account_file(
        str(sa_path),
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    creds.refresh(Request())
    return creds.token, creds.project_id


def generate_vertex_image(
    prompt: str,
    output_path: str,
    aspect_ratio: str = "16:9",
    model: str = DEFAULT_MODEL,
    location: str = DEFAULT_LOCATION,
    ref_image_path: Optional[str] = None,
) -> Path:
    """Generates an image using Vertex AI gemini-3-pro-image and saves it to output_path."""
    sa_path = find_credentials_path()
    token, project_id = get_vertex_token(sa_path)

    hostname = (
        "aiplatform.googleapis.com"
        if location == "global"
        else f"{location}-aiplatform.googleapis.com"
    )
    url = f"https://{hostname}/v1/projects/{project_id}/locations/{location}/publishers/google/models/{model}:generateContent"

    parts = []
    if ref_image_path and os.path.isfile(ref_image_path):
        ext = Path(ref_image_path).suffix.lower()
        mime_type = "image/png" if ext == ".png" else "image/webp" if ext == ".webp" else "image/jpeg"
        with open(ref_image_path, "rb") as f:
            ref_b64 = base64.b64encode(f.read()).decode("utf-8")
        parts.append({"inlineData": {"mimeType": mime_type, "data": ref_b64}})

    parts.append({"text": prompt})

    payload = {
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {"aspectRatio": aspect_ratio},
        },
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        raise RuntimeError(f"Vertex AI HTTP {e.code}: {body}") from e

    candidates = data.get("candidates", [])
    if not candidates:
        raise RuntimeError(f"Vertex AI returned no candidates: {data}")

    parts = candidates[0].get("content", {}).get("parts", [])
    image_bytes = None
    for p in parts:
        if "inlineData" in p and "data" in p["inlineData"]:
            image_bytes = base64.b64decode(p["inlineData"]["data"])
            break

    if not image_bytes:
        text_snippets = [p.get("text", "") for p in parts if "text" in p]
        raise RuntimeError(
            f"No image data returned from model. Text response: {' '.join(text_snippets)}"
        )

    out_file = Path(output_path).resolve()
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_bytes(image_bytes)
    return out_file


def main():
    parser = argparse.ArgumentParser(description="Generate image via Vertex AI (Nano Banana Pro)")
    parser.add_argument("--prompt", "-p", required=True, help="Image generation prompt")
    parser.add_argument("--output", "-o", required=True, help="Output image file path (.png/.jpg)")
    parser.add_argument(
        "--aspect-ratio",
        "-a",
        default="16:9",
        choices=["16:9", "1:1", "4:3", "9:16", "3:2", "2:3"],
        help="Aspect ratio",
    )
    parser.add_argument("--ref", "-r", help="Optional reference image for restyle/editing")
    args = parser.parse_args()

    print(f"Generating image via Vertex AI ({DEFAULT_MODEL})...")
    out = generate_vertex_image(
        prompt=args.prompt,
        output_path=args.output,
        aspect_ratio=args.aspect_ratio,
        ref_image_path=args.ref,
    )
    print(f"Saved successfully: {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
