# Antigravity Agent Guidelines — GenAI Course Production

This repository is maintained by autonomous coding agents and human instructors. When assisting in this repository, you must strictly follow these instructions.

---

## 1. Operating Instructions

1. **Read Rules First:** Always consult `GEMINI.md` before generating slide content, editing HTML presentations, or writing instructor scripts.
2. **Use Specialized Skill:** For any presentation or curriculum task, activate the `.agents/skills/course-deck-producer/SKILL.md` skill.
3. **No Fluff Guarantee:** Write like a Principal Systems Engineer at OpenAI or EPAM. Do not use motivational, generic, or conversational AI filler.
4. **Course Mission:** GenAI Basics is a foundational track focusing on mental models, systemic vision, and essential practice. Do not overpromise senior MLOps/research depth in 16 lessons.
5. **Corporate Compliance:** NEVER refer to the instructor as "Founder of Creator Tools" or mention voice cloning. Use "Architect & Developer of Creator Tools — AI suite for YouTube creators (Hands-on AI R&D pet-project)".
6. **Break vs Homework Boundary:** Slide 15 (Midpoint Break) is for resting only. Do not solicit routine tasks in chat. Routine workflows belong strictly in Slide 20 (Homework Memo).
7. **Anchoring Case Study:** The primary enterprise success story is **EPAM CodeMie @ Dawn Foods** (35% SDLC acceleration).
8. **Homework Benchmark:** The reference use-case for homework is the **Glovo Food Delivery Courier** case study.

---

## 2. Image Generation Protocol

* Tool: `python tools/image_generator.py --prompt "<PROMPT>" --output "<OUTPUT_PATH>" --aspect-ratio 16:9`
* Style: Technical C4 architectural diagrams, dark engineering theme (`#0b0f17`), crisp English text, high-density system nodes.
* Never use built-in IDE `generate_image`.

---

## 3. Verification & Build Commands

* **Screenshot Capture:**
  ```bash
  msedge --headless --disable-gpu --window-size=1540,866 --screenshot=<output.png> <file.html>
  ```
* **PDF Export:**
  ```bash
  msedge --headless --disable-gpu --no-margins --print-to-pdf=<output.pdf> <file.html>
  ```
* Always inspect generated screenshots using `view_file` before asking for user approval.

## Image and video generation: genai-assets (shared local service)

Do not call Vertex / Gemini / OpenAI image or video APIs directly for new generation work.
Use the shared service in `D:\Repos\genai-assets` (README there). It tries subscriptions
first (ChatGPT via Codex → Google via Antigravity) and pays Vertex last. Video is Vertex Veo.

- Python: `pip install -e D:\Repos\genai-assets` or `sys.path.insert(0, r"D:\Repos\genai-assets")`, then
  `from genai_assets.client import GenaiAssets` and
  `GenaiAssets().image("...", client="<project>", aspect_ratio="16:9", references=[...], out=r"D:\...\x.png")`
  or `.video("...", client="<project>", references=[still], duration_seconds=4, out=r"D:\...\x.mp4")`.
- CLI, from `D:\Repos\genai-assets`:
  `python -m genai_assets generate --client <project> --prompt "..." --out D:\...\x.png`
  (add `--kind video --duration 4 --ref still.png` for video, `--no-paid` to stay on subscriptions).
- Nothing to start by hand. The client starts the server on demand (`127.0.0.1:8765`), and the
  server exits after 30 minutes idle. Manual commands: `python -m genai_assets ensure | providers | spend | stop`.
- `client` = your project name; paid spend is tracked per client. Caps: $2 per request,
  $5 per day. Images are 1K by default; 2K/4K go straight to Vertex.
- Several projects share the server: never kill or restart it while jobs run. Use
  `python -m genai_assets stop` (drains), then `ensure`.
- Does not apply inside `D:\Repos\genai-assets` itself: its own Codex/Antigravity attempts
  generate directly.
