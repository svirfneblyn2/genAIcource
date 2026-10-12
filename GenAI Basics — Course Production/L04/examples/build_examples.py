"""Builds the L04 example gallery with Nano Banana Pro (Vertex AI, gemini-3-pro-image).

Every image shown on the L04 slides is produced by this script from the prompts in
prompts.json, so the instructor can rerun any step live or show the exact prompt.

Usage:
    python build_examples.py              # build missing images
    python build_examples.py --only C2    # rebuild one example
    python build_examples.py --force      # rebuild everything
"""

import argparse
import base64
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]
sys.path.insert(0, str(REPO_ROOT / "tools"))

from image_generator import (  # noqa: E402
    DEFAULT_LOCATION,
    DEFAULT_MODEL,
    find_credentials_path,
    get_vertex_token,
)

OUT_DIR = HERE.parent / "assets" / "examples"


def mime_of(path: Path) -> str:
    ext = path.suffix.lower()
    return {".png": "image/png", ".webp": "image/webp"}.get(ext, "image/jpeg")


def generate(prompt: str, refs: list[Path], aspect: str, out: Path) -> None:
    sa = find_credentials_path()
    token, project = get_vertex_token(sa)
    host = "aiplatform.googleapis.com" if DEFAULT_LOCATION == "global" else f"{DEFAULT_LOCATION}-aiplatform.googleapis.com"
    url = f"https://{host}/v1/projects/{project}/locations/{DEFAULT_LOCATION}/publishers/google/models/{DEFAULT_MODEL}:generateContent"

    parts = [
        {"inlineData": {"mimeType": mime_of(r), "data": base64.b64encode(r.read_bytes()).decode()}}
        for r in refs
    ]
    parts.append({"text": prompt})
    payload = {
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {"aspectRatio": aspect},
        },
    }

    for attempt in range(5):
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode())
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 503) and attempt < 4:
                wait = 20 * (attempt + 1)
                print(f"  HTTP {e.code}, retry in {wait}s")
                time.sleep(wait)
                continue
            raise RuntimeError(f"HTTP {e.code}: {e.read().decode()[:500]}") from e

    for p in data["candidates"][0]["content"]["parts"]:
        if "inlineData" in p:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(base64.b64decode(p["inlineData"]["data"]))
            return
    texts = " ".join(p.get("text", "") for p in data["candidates"][0]["content"]["parts"])
    raise RuntimeError(f"No image returned. Text: {texts[:400]}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="example ids to build")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    spec = json.loads((HERE / "prompts.json").read_text(encoding="utf-8"))
    for ex in spec["examples"]:
        if args.only and ex["id"] not in args.only:
            continue
        out = OUT_DIR / f"{ex['id']}.png"
        if out.exists() and not args.force and not args.only:
            print(f"[skip] {ex['id']}")
            continue
        refs = [OUT_DIR / f"{r}.png" for r in ex.get("refs", [])]
        missing = [r for r in refs if not r.exists()]
        if missing:
            print(f"[wait] {ex['id']}: missing refs {[m.name for m in missing]}")
            continue
        print(f"[gen ] {ex['id']} ({ex['title']}) refs={[r.stem for r in refs]}")
        t0 = time.time()
        generate(ex["prompt"], refs, ex.get("aspect", "1:1"), out)
        print(f"       ok in {time.time() - t0:.0f}s -> {out.name}")


if __name__ == "__main__":
    main()
