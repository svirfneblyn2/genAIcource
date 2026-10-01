# Lecture 04 demo — Image Generation and Editing APIs

Purpose: demonstrate a repeatable image workflow, not “prompt roulette”.

## Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Set `GEMINI_API_KEY` in your environment. Optionally set `GEMINI_IMAGE_MODEL` to a currently supported image model.

## Run

```bash
python 00_smoke_check.py
python 01_generate.py
python 02_edit.py --mode vague
python 02_edit.py --mode controlled
python 03_build_prompt.py
```

Outputs are saved under `out/`. Never commit API keys or private/reference images without rights.
