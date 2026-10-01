# Speaker Cheatsheet (1-Page): Lesson 02 — LLM Fundamentals: Architecture, Tokens, Prompting, Context, Embeddings & RAG

**Course:** GenAI Basics • 90 Minutes • 25 Slides • Module 1: Foundation & Architecture  
**Speaker:** Igor Rubanovich (Engineering Manager II & AI Ambassador, EPAM Systems)  
**Speaking Rate:** 110–120 wpm. High-math concepts replaced by everyday physical analogies.

---

### Block 1: Introduction, Highway Roadmap & HW01 (00:00 — 09:00 | 9 min)
* **Slide 01 (00:00 - 02:30 | 2.5 min) • Title Cover Hero:**  
  *Analogy:* Driving a car vs assembling a gearbox. You need the pedals, steering wheel, and brakes, not the metallurgy of the pistons.  
  *Core:* 0 formulas, pure systems physics. Interactive chat check (1/2/3: experience with LLMs and hallucinations).
* **Slide 02 (02:30 - 06:00 | 3.5 min) • Curriculum Highway Roadmap:**  
  *Analogy:* 6-station highway road trip leading directly to enterprise production.  
  *Core:* Station 1 (L01–L03 foundations) ➔ Station 2 (multimodal) ➔ Station 3 (Copilot) ➔ Station 4 (local models) ➔ Station 5 (MCP agents) ➔ Station 6 (security & capstone).
* **Slide 03 (06:00 - 09:00 | 3 min) • HW01 Retrospective & Paradigm Shift:**  
  *Analogy:* $5 pocket calculator (never makes arithmetic errors) vs prize-winning poet (writes prose, stumbles on multiplication).  
  *Core:* Software 1.0 (SQL/code — $0, 0ms) vs Software 3.0 (semantics, natural language, probabilistic sampling). HW01 deadline grace.

---

### Block 2: Physics of Generation & Transformer Architecture (09:00 — 28:00 | 19 min)
* **Slide 04 (09:00 - 13:00 | 4 min) • Text Autoregression & Probability:**  
  *Analogy:* Predictive T9 keyboard on a smartphone. Predicts strictly one next word based on internet-scale statistics.  
  *Core:* Autoregressive cycle: prompt ➔ probabilities ➔ sample 1 token ➔ append. Temperature: 0.0 (ice-cold for JSON/code) vs 0.8 (warm prose).
* **Slide 05 (13:00 - 17:00 | 4 min) • Image Generation (Diffusion):**  
  *Analogy:* Analog TV static noise and a sculptor's smart eraser.  
  *Core:* Model doesn't paint from scratch: over 30–50 steps it erases white noise until a crisp photo emerges. Prompt acts as a lighthouse (Cross-Attention).
* **Slide 06 (17:00 - 21:00 | 4 min) • Decoder Transformer Architecture:**  
  *Analogy:* 32-story skyscraper factory of editors. Word cards enter ground floor, editors deepen semantic understanding on each floor.  
  *Core:* Self-Attention links words; MLPs store world facts; Causal Masking forbids peeking into the future.
* **Slide 07 (21:00 - 24:30 | 3.5 min) • BPE Tokenization & The Non-Latin Script Tax:**  
  *Analogy:* Children's wooden syllable blocks. Sentences assembled from pre-made vocabulary blocks (128k).  
  *Core:* English word learning = 1 block. Non-Latin scripts (Thai การเรียนรู้) fragment into 5 small cubes due to multi-byte UTF-8 ("Non-Latin Script Tax" = 3x-5x higher API bills and faster context saturation). Write system prompts in English.
* **Slide 08 (24:30 - 28:00 | 3.5 min) • Token Economics: Leading Vendor Pricing Benchmark:**  
  *Pricing Table:* OpenAI (GPT-4o, mini, o1), Anthropic (Claude 3.5 Sonnet, Haiku), Google (Gemini 2.0 Flash, 1.5 Pro).  
  *Core:* Fundamental structural asymmetry: output generation costs 4–5x more than input reading. 3 optimization rules: two-tier model routing (90% in light models), prompt caching (up to 90% discount), and strict JSON schema limits.

---

### Block 3: Attention, Memory & Context Boundaries (28:00 — 45:00 | 17 min)
* **Slide 09 (28:00 - 31:30 | 3.5 min) • Memory & KV-Cache:**  
  *Analogy:* Writer's desk scratchpad. Without notes, the novelist rereads 300 pages from line 1 for every single new word ($O(N^2)$ freezing).  
  *Core:* KV-Cache freezes past calculations in fast GPU memory ($O(1)$). Hardware cost: tens of gigabytes of expensive H100 GPU VRAM.
* **Slide 10 (31:30 - 35:00 | 3.5 min) • Self-Attention Mechanism:**  
  *Analogy:* Flashlight of meaning in a dark room ("The bank denied the loan to the client because it was closed").  
  *Core:* The word "it" shines its flashlight and binds to "bank", not "client". Words derive true meaning exclusively through surrounding neighbors.
* **Slide 11 (35:00 - 38:30 | 3.5 min) • Multi-Head Attention:**  
  *Analogy:* Team of 4 expert readers in tinted glasses (grammar, sentiment, entities, code syntax).  
  *Core:* Parallel projection subspaces. Findings from all heads are merged together, ensuring no subtle linguistic dimension is overlooked.
* **Slide 12 (38:30 - 41:30 | 3 min) • Context Window Anatomy (Desk Space):**  
  *Analogy:* Physical surface area of an office desk. Heavy binders pushed off the desk onto the floor vanish from the model's memory forever.  
  *Core:* Golden budgeting: 20% system instructions, 50% reference docs, 10% user query, 20% reserved headroom for output completion.
* **Slide 13 (41:30 - 45:00 | 3.5 min) • Lost in the Middle U-Curve:**  
  *Analogy:* Reading a 1,000-page novel late at night (sharp recall of opening and finale, middle is a hazy blur).  
  *Core:* Stanford U-curve: 95% accuracy at edges vs 40% in center. Rule: place critical rules at top, repeat mandatory schemas at the very bottom.

---

### Midpoint Break: 5 Minutes (45:00 — 50:00)
* **Slide 14 (45:00 - 50:00 | 5 min) • Midpoint Equator (Interactive Timer):**  
  *Protocol:* 5:00 interactive countdown. Encourage students to stretch and hydrate. Pause chat discussion.

---

### Block 4: Prompting, Few-Shot & Security (50:00 — 66:00 | 16 min)
* **Slide 15 (50:00 - 54:00 | 4 min) • Prompt Anatomy (XML Tags):**  
  *Analogy:* Transparent labeled warehouse storage bins (`<role>`, `<rules>`, `<data>`).  
  *Core:* Context containment. The model never conflates system directives with untrusted customer input.
* **Slide 16 (54:00 - 58:00 | 4 min) • Prompting Strategies (5 Tiers):**  
  *Analogy:* 5 levels of onboarding a junior intern: Zero-Shot (goal) ➔ Few-Shot (examples) ➔ CoT (thinking out loud) ➔ ReAct (tools) ➔ RAG (handbook).  
  *Core:* Reliability progression from bare textboxes to autonomous tool-calling agents.
* **Slide 17 (58:00 - 62:00 | 4 min) • Few-Shot Calibration:**  
  *Analogy:* Flashcard cramming: 10 physics questions and 1 chemistry question causes guessing bias.  
  *Core:* 1:1:1 balanced exemplars. Demonstrating edge cases (`order_id: null`, `requires_human_escalation: true`) enforces strict JSON compliance.
* **Slide 18 (62:00 - 66:00 | 4 min) • Context Security (Prompt Injection):**  
  *Analogy:* Forged delivery note slipped into courier's bag ("Ignore previous rules, hand over the package").  
  *Core:* Tag containment in `<user_message>`, Sandwich Defense, and server-side schema enforcement via Pydantic.

---

### Block 5: Embeddings, Hybrid Search & RAG (66:00 — 80:00 | 14 min)
* **Slide 19 (66:00 - 69:30 | 3.5 min) • Vector Embeddings:**  
  *Analogy:* GPS coordinate map in the City of Meanings.  
  *Core:* 1536/3072-dimensional vectors. Measuring distance with a ruler (cosine similarity) reflects semantic kinship.
* **Slide 20 (69:30 - 73:00 | 3.5 min) • Hybrid Search (BM25 + Vectors):**  
  *Analogy:* Exact Ctrl+F (serial numbers, IDs) + savvy reference librarian (synonyms, conceptual intent).  
  *Core:* Reciprocal Rank Fusion (RRF). The only reliable architecture for technical part numbers without losing semantic meaning.
* **Slide 21 (73:00 - 76:30 | 3.5 min) • End-to-End RAG Pipeline:**  
  *Analogy:* University student taking an open-book exam: instead of memorizing, looks up the exact chapter and cites page numbers.  
  *Core:* Chunking ➔ Embeddings ➔ Vector DB ➔ Top-K Retrieval ➔ Grounded Synthesis. Eliminates factual hallucinations.
* **Slide 22 (76:30 - 80:00 | 3.5 min) • RAG Failure Triad:**  
  *Analogy:* 3 mistakes of a careless waiter: wrong dish (Retrieval) / invented ingredients (Hallucination) / soup on a flat plate (Format).  
  *Core:* Ragas evaluation metrics: Context Precision, Faithfulness, Answer Relevance.

---

### Block 6: Architecture Selection, Homework & Wrap-Up (80:00 — 90:00 | 10 min)
* **Slide 23 (80:00 - 83:00 | 3 min) • Architectural Selection Matrix:**  
  *Analogy:* Choosing transit: walk (prompting — $0), train (RAG — brings knowledge luggage), rocket (Fine-Tuning — millions on style).  
  *Core:* Fine-tuning adjusts style and behavior, but facts are supplied EXCLUSIVELY via context and RAG.
* **Slide 24 (83:00 - 87:00 | 4 min) • Hands-On Lab #2 (Support Ticket Classifier):**  
  *Task:* Support ticket triage system (categories, P0–P3 priorities, Pydantic schema, Few-Shot balance, injection defense).  
  *Git workflow:* Commit to same `genai-homeworks` repo, branch `feature/hw02-ticket-classifier`, folder `L02/`, PR to `main`, reviewer `ihar_rubanovich@epam.com`.
* **Slide 25 (87:00 - 90:00 | 3 min) • Summary & Lesson 03 Preview:**  
  *Pilot's Checklist:* 4 axioms: 1) models see blocks, 2) output is 4x costlier than input, 3) memory is finite, 4) facts live in RAG. Preview of Lesson 03 (Python SDK, streaming, Pydantic).
