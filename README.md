# GenAI Courses Production Repository

Central repository consolidating all production assets, slide builders, scripts, deliverables, and demo applications for both **GenAI Basics** and **Advanced GenAI** courses.

---

## Directory Architecture

```
d:\Repos\genAIcource\
├── .gitignore
├── README.md
├── COURSE_STATUS.md                      # Canonical status & artifact matrix
│
├── GenAI Basics — Course Production\     # Foundational course (L01 - L16)
│   ├── L01\                              # AI, ML & GenAI Overview
│   │   ├── presentation_L01_AI_ML_GenAI.html
│   │   ├── presentation_L01_AI_ML_GenAI.pdf
│   │   ├── L01_v7_AUDITED_NATIVE_EDITABLE_Slide_Deck.pptx
│   │   └── L01_*.docx                    # Script, Homework, Runbook
│   ├── L02\                              # LLM Fundamentals (Tokens, Prompting, Grounding)
│   │   ├── presentation_L02_LLM_Fundamentals.html
│   │   ├── presentation_L02_LLM_Fundamentals.pdf
│   │   └── STATUS.md                     # ⚠ QA FIXES: Missing canonical script
│   └── L03\                              # LLM API with Python (Gemini API, google-genai, Colab)
│       ├── README.md                     # Source of truth & links
│       ├── presentation_L03_LLM_API(_EN).html / .pdf   # 25-slide decks RU/EN
│       ├── L03_01_Lecture_Text_READY.md (+ _EN)        # Full lecture text
│       ├── L03_02_Full_Instructor_Script_READY.md (+ _EN)
│       ├── L03_00_Lecture_Cheatsheet(_EN).md
│       └── L03_First_API_Call_and_Prompt_Patterns.ipynb  # copy of notebooks/ (Colab)
│
└── Advanced GenAI — Course Production\   # Advanced engineering course (M01 - M07)
    ├── M01\                              # Cloud AI Capabilities Overview (AWS Bedrock, Azure Foundry, Vertex AI)
    │   ├── deck_builder\                 # Automated modular HTML & PDF slide builder (27 slides)
    │   ├── presentation_M01_Cloud_AI_Overview.html / .pdf
    │   ├── M01_01_Lecture_Text_FINAL.md / .docx
    │   ├── M01_02_Full_Instructor_Script_FINAL.md / .docx
    │   └── M01_Instructor_Console_Click_Guide_and_Homework.md / .docx
    ├── M02\                              # Agent Frameworks & Orchestration (State Machines, LangGraph, HITL)
    │   ├── deck_builder\                 # Automated modular HTML & PDF slide builder (27 slides)
    │   ├── presentation_M02_Agent_Frameworks.html / .pdf
    │   ├── M02_01_Lecture_Text_READY.md / .docx
    │   ├── M02_02_Full_Instructor_Script_READY.md / .docx
    │   ├── M02_Instructor_Console_Click_Guide_and_Homework.md / .docx
    │   ├── M02_Instructor_Live_Demo_Kit.zip
    │   └── m02_live_demo_package\        # Turnkey Accounts Payable Agent (Web UI & CLI modes)
    └── M03\                              # Vector Stores and RAG (HNSW, BM25+Dense RRF, Lost-in-the-Middle)
        ├── deck_builder\                 # Automated modular HTML & PDF slide builder (26 slides)
        ├── presentation_M03_Vector_Stores_and_RAG.html / .pdf
        ├── M03_01_Lecture_Text_FINAL.md / .docx
        ├── M03_02_Full_Instructor_Script_FINAL.md / .docx
        ├── homework_M03.md               # 2-track homework (Architecture vs Python)
        ├── instructor_prep_M03_ru.html   # Visual instructor prep guide
        ├── M03_Instructor_Live_Demo_Kit.zip
        └── m03_live_demo\                # Offline 4-act Python enterprise RAG demo suite
```

---

## Slide Deck Builders (Advanced GenAI)

Each module in `Advanced GenAI — Course Production` features an automated deck builder engine:
- Modular Python slide files (`slides/slide_01.py` ... `slide_NN.py`)
- Anti-slop vocabulary validation
- Strict punctuation verification (zero unauthorized em/en-dashes)
- Headless Chrome 16:9 vector PDF export (`1440x810 pt`)
- Automated verification via PyMuPDF (`fitz`)

### Running a Slide Build:
```powershell
# Example: Building M03 Vector Stores and RAG
cd "Advanced GenAI — Course Production\M03\deck_builder"
python -c "import build; build.build()"
```

---

## Python Live Demos

- **GenAI Basics L03 (LLM API with Python):** run in Google Colab —
  [notebooks/L03_First_API_Call_and_Prompt_Patterns.ipynb](https://colab.research.google.com/github/svirfneblyn2/genAIcource/blob/main/notebooks/L03_First_API_Call_and_Prompt_Patterns.ipynb)
  (needs a `GEMINI_API_KEY` in Colab Secrets).

- **Advanced GenAI M03 (Vector Stores and RAG):**
  ```powershell
  cd "Advanced GenAI — Course Production\M03\m03_live_demo"
  python run_demo.py
  ```
