# Lesson 11 • Homework: design an agent’s tools and test them in AI Studio

**Course:** GenAI Basics • Module 3 (Own Models and Agents)  
**Submit:** the `genai-homeworks/L11/` folder in your personal GitHub repository  
**Reviewer:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)  
**Time:** 2–3 hours  
**Code:** not required. Code and a real agent are optional (slides 11 and 13).  
**Matches:** slide 20 of `presentation_L11_Function_Calling_First_Agent_EN_v2.html`, plus slides 4 (function description), 5 (trust boundary), 6–7 (AI Studio demo), 16 (risks), 18 (rules = grading criteria). Facts as of 16.10.2026.

---

## Goals

1. Pick a task from your work where an agent needs data or actions.
2. Describe 2–3 tools by the lesson’s rules.
3. Check in Google AI Studio which calls the model proposes.
4. Decide where a human must confirm, what step limit to set and what to log.

---

## Steps

### 1. The task (15 min)
In 3–5 sentences: who uses the agent and what it must do. Examples: customer support (orders, returns), warehouse (stock, reservations), HR (leave, certificates), IT support (ticket status, password reset).

### 2. Tools (30 min)
For each of the 2–3 functions fill in:

| Field | Example |
|---|---|
| Name | `get_order_status` |
| Description: what, what for, when to call | “Current status, courier and ETA of ONE order by its number. Call when the customer asks where an order is.” |
| Parameters | `order_id` (string, required) |
| Risk | reads data / changes data / spends money |

At least one function must change something (for example `create_return`), so there is a place for a confirmation.

### 3. Test in AI Studio (40 min)
1. aistudio.google.com → new chat → model **Gemini 3.8 Flash** (free).
2. Run settings → Tools → **Function calling** → Edit → fill in your functions → Save.
3. Ask 5 questions:
   - 3 ordinary ones that need a tool;
   - 1 that needs no tool;
   - 1 “dangerous” one (asking for something the agent must not do).
4. For each call, paste a synthetic JSON answer into the “function response” field and look at the model’s final answer.
5. Screenshot at least one full loop (question → call → function response → model answer).

### 4. Risks (20 min)
In `risks.md` answer: which functions need a human confirmation; what step limit you would set; what to log; how the agent should react to the “dangerous” question.

### 5. Optional
Build a real agent with the slide 13 prompt (Claude Code, Codex or Antigravity) using your functions. A Gemini API key is free in AI Studio → Get API key; keep it in an environment variable.

---

## What to submit

```
genai-homeworks/L11/
├─ README.md   # task, who uses it, conclusion (5–10 lines)
├─ tools.md    # 2–3 functions: name, description, parameters, risk
├─ demo.png    # screenshot of a full loop in AI Studio
└─ risks.md    # confirmation, limit, log, reaction to the dangerous question
```

Add a table of the 5 questions to `README.md`: which call the model proposed and whether it was right.

---

## Grading (10 points) = the 4 rules from slide 18

| Criterion | Points |
|---|---|
| Narrow tools: one function, one job; the description answers “what, what for, when” | 3 |
| Testing: 5 questions, each marked right or wrong | 3 |
| A human confirms actions with consequences | 2 |
| Step limit and log described | 1 |
| Synthetic data only | 1 |

**Common mistakes:** one do-everything function; a two-word description; no question without a tool; the dangerous request executed without confirmation; real customer data.
