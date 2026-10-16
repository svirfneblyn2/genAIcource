# Lesson 14 • Homework: a prototype and feedback from three real people

**Course:** GenAI Basics • Module 6 (Idea to Product)  
**Submit:** the `genai-homeworks/L14/` folder in your personal GitHub repository  
**Reviewer:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)  
**Time:** 3–4 hours  
**Matches:** slide 16 of `presentation_L14_Streamlit_Rapid_Prototyping_EN_v2.html`, plus slides 4–8 (Streamlit and the agent), 9 (publishing), 10–11 (builders), 14 (security). Facts as of 16.10.2026.

---

## Steps

### 1. Idea (15 min)
One sentence: who the prototype is for and what it does. Example: “A helper for new warehouse staff that answers safety questions”.

### 2. Data (20 min)
Prepare `faq.md` — 10–20 questions and answers. **Synthetic or anonymised text only.**

### 3. Build (1–2 hours) — pick a path
- **Streamlit with an agent:** the slide 7 prompt (Claude Code, Codex or Antigravity). Python 3.11+. Key only in `.streamlit/secrets.toml`, the file in `.gitignore`. A demo mode without a key is required.
- **No code:** Google AI Studio → Build → describe the app and paste the FAQ.

### 4. Feedback (1 hour)
Show the prototype to three colleagues (Teams screen share, or a link if the data is synthetic). For each, record in `feedback.md`: what they asked, what they liked, what broke, what was missing.

### 5. Conclusions (15 min)
In `README.md`: three changes you would make based on the feedback, and whether the idea is worth turning into a product.

### Optional
Publish the Streamlit prototype on Community Cloud (synthetic data only, key in Secrets, a spending limit in the API console).

---

## What to submit

```
genai-homeworks/L14/
├─ README.md      # idea, how it was built, 3 changes, conclusion
├─ app.py         # or a link to the AI Studio prototype
├─ faq.md         # synthetic data
├─ feedback.md    # feedback from 3 people
└─ demo.png       # prototype screenshot
```

**Do not submit** `secrets.toml` or keys. If you include `app.py`, include `secrets.example.toml` with a placeholder.

## Grading (10 points)

| Criterion | Points |
|---|---|
| The idea in one sentence; clear who it is for | 1 |
| A working prototype (screenshot or link) | 3 |
| Concrete feedback from three people | 3 |
| Three changes from the feedback and a conclusion | 2 |
| Security: synthetic data, no key in code | 1 |

**Common mistakes:** a key in `app.py` or the repo; real data behind a public link; “they liked it” feedback with no details.
