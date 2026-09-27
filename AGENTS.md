# Antigravity Agent Guidelines — GenAI Course Production

This repository is maintained by autonomous coding agents and human instructors. When assisting in this repository, you must strictly follow these instructions.

---

## 1. Operating Instructions

1. **Read Rules First:** Always consult `GEMINI.md` before generating slide content, editing HTML presentations, or writing instructor scripts.
2. **Use Specialized Skill:** For any presentation or curriculum task, activate the `.agents/skills/course-deck-producer/SKILL.md` skill.
3. **No Fluff Guarantee:** Write like a Principal Systems Engineer at OpenAI or EPAM. Do not use motivational, generic, or conversational AI filler.
4. **Corporate Compliance:** NEVER refer to the instructor as "Founder of Creator Tools". Always use "Architect & Developer of Creator Tools (Hands-on AI R&D pet-project)".
5. **Anchoring Case Study:** The primary enterprise success story is **EPAM CodeMie @ Dawn Foods** (35% SDLC acceleration).
6. **Homework Benchmark:** The reference use-case for homework is the **Glovo Food Delivery Courier** case study.

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
