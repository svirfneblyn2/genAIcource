# Lesson 10 • Homework: run an open model yourself and compare it honestly with the cloud

**Course:** GenAI Basics • Module 3 (Own Models and Agents)  
**Submit:** the `genai-homeworks/L10/` folder in your personal GitHub repository  
**Reviewer:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)  
**Time:** 2–3 hours (20–40 minutes of that is downloading)  
**Code:** not required. Code (slide 11) and an agent (slide 12) are optional.  
**Matches:** slide 20 of `presentation_L10_Open_Models_Local_and_RunPod_EN_v2.html`, plus slides 3 (Hugging Face), 6–8 (size, memory, speed), 9–10 (LM Studio), 13 (security), 19 (choosing). Facts as of 16.10.2026.

---

## Goals

1. Choose a model for your own computer and justify it: file size, memory, licence.
2. Run the model locally and measure its speed.
3. Compare the local model with a cloud model on three of your own tasks.
4. Decide where to run a model for your task: cloud API, laptop, RunPod Pod or Serverless.

Grading looks at an honest comparison and the reasoning, not at which model “won”.

---

## Steps

### 1. Choose a model (15 min)
- Find your memory: *Task Manager → Performance* (RAM and “Dedicated GPU memory”). On a Mac: *About This Mac*.
- Using slide 7, pick a model whose Q4 file + 20–30% fits the GPU memory (or RAM if there is no GPU).
- Hints:
  - no GPU, 16 GB RAM → `granite-4.2-3b` (2.2 GB) or Qwen3.5 4B (2.7 GB);
  - 6–8 GB GPU → Granite 4.2 8B or Qwen3.5 9B (5.3–5.6 GB);
  - 16 GB GPU or more → Gemma 4 12B (7.4 GB) or gpt-oss-20b (12.1 GB).
- Open the model card on Hugging Face and write down the licence.

### 2. Install and run (30–60 min)
- **Option A (no command line):** LM Studio from lmstudio.ai. On the download page take the classic **LM Studio**, not Bionic. Discover → find the model → Download (Q4_K_M) → pick the model in Chat.
- **Option B (command line or agent):** Ollama from ollama.com, then `ollama run <model name>`. You can hand the install to a coding agent with the slide 12 prompt; read the commands before approving.
- Take a screenshot: the model’s answer and the speed line (tokens per second). In LM Studio the speed is under the answer; in Ollama run `ollama run <model> --verbose`.
- Write down how much memory the model uses (Task Manager).

### 3. Three work tasks (40 min)
Make up three tasks from your job on **synthetic** data (no real customer emails):
1. classification (for example: topic and urgency of an email);
2. a summary (3 bullet points from a long text);
3. a reply to a customer or a draft email.

Give each task to the local model and to ChatGPT (or Gemini, Claude) with the same prompt. Score each answer 1–5: correctness, format, language.

### 4. Decision card (15 min)
For one real task of your team, answer the two questions from slide 19: may the data go to the model vendor, and how much work is there (requests per day)? Choose: cloud API, laptop, RunPod Serverless or RunPod Pod, and explain in 3–5 sentences.

### 5. Optional
- Turn on the LM Studio local server (Developer → Start server) and call the model with the slide 11 code. Server on `localhost` only.
- RunPod: only if you are ready to pay. Set a spending limit, and when done use **Terminate**, not Stop.

---

## What to submit

```
genai-homeworks/L10/
├─ README.md       # model, licence, computer memory, conclusion (5–10 lines)
├─ results.md      # 3 tasks × 2 models: prompt, answers, 1–5 scores
├─ speed.png       # screenshot with tokens per second
└─ decision.md     # decision card: API / laptop / Serverless / Pod and why
```

---

## Grading (10 points)

| Criterion | Points |
|---|---|
| Model chosen for the memory, “file + 20–30%” shown, licence recorded | 2 |
| Model runs; screenshot with speed and memory used | 2 |
| Three tasks, identical prompts, 1–5 scores with reasons | 3 |
| Decision card with arguments about data and volume | 2 |
| Security: synthetic data, server on localhost only, model from a known publisher | 1 |

**Common mistakes:** downloading Q8 or BF16 “for quality” so the model does not fit; not recording the licence; comparing different prompts; leaving a RunPod Pod in the Stop state.
