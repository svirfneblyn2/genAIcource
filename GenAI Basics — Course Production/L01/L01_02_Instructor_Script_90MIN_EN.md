# Lesson 01: Complete Engineering Lecture Script (90 Minutes • 21 Slides)
**Curriculum:** GenAI Basics  
**Instructor:** Ihar Rubanovich (Engineering Manager II & AI Ambassador, EPAM Systems)  
**Homework Review Email:** `ihar_rubanovich@epam.com`  
**Slide Deck:** `presentation_L01_AI_ML_GenAI_EN.html` (21 interactive slides)

---

## Session Timing Breakdown (90 Minutes)

| Section | Timing | Slides | Focus |
| :--- | :---: | :---: | :--- |
| **Part 1: Foundations & Setup** | 00:00 — 12:00 (12 min) | 01 – 04 | Engineering sobriety, instructor bio, 16-lesson roadmap (vision & baseline), Git workflow |
| **Part 2: Real-World AI & Taxonomy** | 12:00 — 29:00 (17 min) | 05 – 08 | Everyday AI systems, taxonomy (Matryoshka doll), Classical ML vs GenAI architectures |
| **Part 3: Paradigms & LLM Physics** | 29:00 — 55:00 (26 min) | 09 – 14 | Karpathy (1.0➔3.0), AI-First trap, 4 real-world tasks, Tokens, T9, RAG vs Hallucination |
| **Midpoint: Coffee Break** | 55:00 — 60:00 (5 min) | 15 | Live 5-minute interactive timer, mental recharge |
| **Part 4: Production Architecture & Risk** | 60:00 — 70:00 (10 min) | 16 – 17 | Architectural Iceberg (10% vs 90%), Blast Radius (Risk Traffic Light) |
| **Part 5: Production Case Studies & Logic** | 70:00 — 80:00 (10 min) | 18 – 19 | 4 industry failures vs 4 wins (EPAM CodeMie @ Dawn Foods), Decision Tree |
| **Part 6: Homework Assignment & Q&A** | 80:00 — 90:00 (10 min) | 20 – 21 | Benchmark case walkthrough (Glovo Courier), selecting workplace tasks, open mic |

---

## Slide-by-Slide Instructor Walkthrough

### Slide 01: Title Cover (AI, ML & Generative AI)
- **Timing:** 00:00 — 03:00 (3 min)
- **Objective:** Strip away marketing hype and set a rigorous engineering tone from minute one.
- **Speaker Track:**
  > "Hello everyone, and welcome to the foundational lecture of the GenAI Basics curriculum: 'AI, ML & Generative AI: Engineering Mental Models, System Architecture & Production Realities.'  
  > We deliberately begin this course not with consumer enthusiasm around ChatGPT, and not by writing poetry. Our objective today is uncompromising engineering sobriety.  
  > There is an immense amount of hype across the tech industry: every button, every formula, and every basic script is marketed as 'Artificial Intelligence'. But for an engineer, treating everything as AI is fatal—you cannot architect a dependable or scalable system with that mindset.  
  > Look at the core axiom on the screen: the foundation model itself is only 10% of a production system. The remaining 90% is data contracts, schema validation, security guardrails, failure handling, and infrastructure.  
  > Quick question in the chat for calibration: drop a '1' if you have already integrated LLM APIs into your code, or '2' if you have only interacted with web chat interfaces so far."

---

### Slide 02: Instructor Profile (Ihar Rubanovich)
- **Timing:** 03:00 — 06:00 (3 min)
- **Objective:** Establish instructor authority, professional background, and provide the official homework email.
- **Speaker Track:**
  > "A quick background on myself: my name is Ihar Rubanovich, Engineering Manager II and AI Ambassador at EPAM Systems.  
  > I have been in software engineering for over 10 years, progressing from distributed backend systems to leading enterprise delivery teams.  
  > My core focus today is AI-Assisted Engineering: the systematic adoption of autonomous coding agents—such as CodeMie, Cursor, and Antigravity—into real-world software delivery workflows.  
  > As part of my hands-on AI R&D, I built Creator Tools—a suite of AI tools for YouTube creators designed to automate content preparation, streamline workflows, and increase channel earnings. This practical pet-project gave me firsthand experience integrating diverse AI models into a working applied product.  
  > Please take note of my work email highlighted on the slide: `ihar_rubanovich@epam.com`. This is the exact handle you will add as a collaborator in your GitHub repositories to submit your homework. I will review all practical assignments personally."

---

### Slide 03: Curriculum Roadmap (16 Applied Sessions)
- **Timing:** 06:00 — 09:00 (3 min)
- **Objective:** Position the course honestly: clear vision, practical mental models, and hands-on familiarity without overpromising.
- **Speaker Track:**
  > "Here is our full curriculum roadmap across 16 applied sessions divided into 6 modules:  
  > • Module 1 (Sessions 01–03): Foundations & API. Model physics, clean Python scripting, and basic API integrations.  
  > • Module 2 (Sessions 04–06): Multimodality. Practical tools for images, video, and audio.  
  > • Module 3 (Sessions 07–09): Developer Tooling. GitHub Copilot, enterprise Microsoft tools, and Claude Projects.  
  > • Module 4 (Session 10): Open-Source & Local Models. Open-weight LLMs (Llama, DeepSeek) running locally via Ollama and LM Studio.  
  > • Module 5 (Sessions 11–13): Agents & Tool Calling. The Function Calling concept, the Model Context Protocol (MCP), and SDKs.  
  > • Module 6 (Sessions 14–16): Prototyping & Interfaces. Fast UI assembly with Streamlit, foundational security, and coding assistants in Cursor.  
  > An important note on course positioning: this is a foundational introductory track. We do not make false promises that you will graduate in 16 lessons as senior MLOps engineers or neural network researchers. Our mission is to give you a clear systemic vision, dependable engineering mental models, and hands-on familiarity with the modern AI toolchain. Each module pairs an authoritative overview with essential hands-on practice, giving you a strong launchpad to dive deeper into specialized domains when your real projects require it."

---

### Slide 04: GitHub Workflow & Submission Rules
- **Timing:** 09:00 — 12:00 (3 min)
- **Objective:** Enforce professional repository standards and workflow expectations.
- **Speaker Track:**
  > "Our organizational standard is strictly professional: we do not accept homework submissions over Telegram, Word documents, or console screenshots.  
  > We operate on standard industry Git workflows:  
  > 1. You create a private repository named `genai-homeworks`.  
  > 2. You establish clean subdirectories: `L01/`, `L02/`, and so forth.  
  > 3. Each assignment is committed either as a structured Markdown document (`README.md`) or as runnable code.  
  > 4. In your repository `Settings` ➔ `Collaborators` ➔ `Add people`, invite `ihar_rubanovich@epam.com`.  
  > All feedback will be delivered via Pull Requests or commit reviews."

---

### Slide 05: Everyday Reality: Where AI Operates Today
- **Timing:** 12:00 — 16:00 (4 min)
- **Objective:** Demonstrate how everyday systems use fundamentally different mathematical foundations.
- **Speaker Track:**
  > "Let us examine six systems that you likely interact with every day:  
  > • FaceID on your phone—classical computer vision: infrared dot projection, facial embedding extraction, and vector similarity verification.  
  > • Gmail Spam Filtering—classical probabilistic classification processing terabytes of email in milliseconds.  
  > • YouTube & Spotify Recommendations—two-stage recommender architectures combining approximate nearest neighbor (ANN) search over dense vectors.  
  > • GPS Navigation—dynamic graph shortest-path algorithms with live traffic latency weighting.  
  > • ChatGPT & Copilot—autoregressive decoder-only transformers generating text and code token by token.  
  > • AI Assistants for YouTube Creators (like Creator Tools)—generating titles, metadata, and script research.  
  > All of these are blanketed under 'AI'. But under the hood, they operate on completely different mathematical paradigms and compute budgets."

---

### Slide 06: Taxonomy: How AI, ML, DL & GenAI Relate
- **Timing:** 16:00 — 19:00 (3 min)
- **Objective:** Establish the Matryoshka doll taxonomy hierarchy.
- **Speaker Track:**
  > "To eliminate ambiguity, let's map these concepts into a strict hierarchy (observe the Matryoshka diagram):  
  > 1. The outer boundary is Artificial Intelligence (AI). The broadest umbrella term—any software demonstrating intelligent behavior, including 1980s rule-based expert systems.  
  > 2. Inside AI lies Machine Learning (ML). Algorithms that discover statistical patterns from historical data without explicit logic hardcoding.  
  > 3. Inside ML sits Deep Learning (DL). Deep neural networks trained via backpropagation with many layers.  
  > 4. And inside Deep Learning sits Generative AI (GenAI). Models capable of synthesizing brand new data sequences: text, images, audio, or code.  
  > The core takeaway: all GenAI is a neural network, but only a fraction of business problems require GenAI. In fact, 80% of enterprise challenges are solved more reliably and cheaply at the outer layers."

---

### Slide 07: Classical Machine Learning: Architecture & Properties
- **Timing:** 19:00 — 24:00 (5 min)
- **Objective:** Detail classical ML properties: tabular data, millisecond latency, and calibrated probabilities.
- **Speaker Track:**
  > "Look at the classical ML C4 architectural diagram.  
  > We have historical ground-truth data: a feature matrix X (user age, transaction count, days since last login) and a target label Y—whether the customer churned or not.  
  > During training, algorithms like XGBoost or CatBoost find optimal decision boundaries.  
  > In production inference, a lightweight microservice computes calibrated probabilities in 2 to 5 milliseconds: P(churn) = 0.84.  
  > Remember these properties:  
  > • Inference latency is in single-digit milliseconds.  
  > • Inference cost is essentially $0 (runs effortlessly on standard CPUs).  
  > • Output is strictly calibrated and deterministic.  
  > When dealing with structured tabular data, classical ML remains completely unmatched."

---

### Slide 08: Generative AI: Architecture & Nature
- **Timing:** 24:00 — 29:00 (5 min)
- **Objective:** Explain Foundation Model physics, token-by-token generation, and inherent trade-offs.
- **Speaker Track:**
  > "Now contrast that with the Generative AI architecture on the screen.  
  > Here, there is no predefined feature table. We feed unstructured input: developer instructions (System Prompt) and user queries (User Prompt).  
  > The model is a Foundation Model trained on petabytes of text to predict the next token.  
  > Inference is autoregressive: the model produces one token, appends it to its context window, and executes another forward pass for the next token.  
  > For this semantic flexibility, we pay three penalties:  
  > 1. Latency: seconds instead of milliseconds.  
  > 2. Cost: cloud providers meter every single token entering and exiting the model.  
  > 3. Stochastic uncertainty: the model does not guarantee ground truth and will hallucinate plausibly if ungrounded."

---

### Slide 09: Software Paradigms: Software 1.0 ➔ 2.0 ➔ 3.0 (Karpathy)
- **Timing:** 29:00 — 33:00 (4 min)
- **Objective:** Articulate Karpathy's software evolution and emphasize combining 1.0 with 3.0.
- **Speaker Track:**
  > "Andrej Karpathy introduced a powerful mental model for software evolution:  
  > • Software 1.0 is classical explicit code. Engineers write deterministic logic in Python, Java, or C++. Fully deterministic and validated via unit tests.  
  > • Software 2.0 is deep learning. Engineers curate datasets, allowing optimizers to solve for neural network weights.  
  > • Software 3.0 is foundation models. The model is pre-trained. Engineers program it using natural language prompts and context.  
  > But the enterprise lesson is paramount: Software 3.0 does not displace Software 1.0! A production-grade system wraps the deterministic guardrails of Software 1.0 around the probabilistic core of Software 3.0."

---

### Slide 10: The Hype Trap: Why 'AI First' Burns Engineering Budgets
- **Timing:** 33:00 — 37:00 (4 min)
- **Objective:** Warn against replacing deterministic code or SQL with LLMs.
- **Speaker Track:**
  > "The most common anti-pattern of recent years is the 'AI First for everything' craze.  
  > For example: calculating cart totals with discount coupon rules.  
  > A simple SQL query or Python function executes in 2 milliseconds with 100% accuracy and $0 cost.  
  > An LLM call takes 3 seconds, costs cents per call, and returns arithmetic hallucinations in 5% of requests because language models do not compute math—they predict statistically plausible digit tokens.  
  > Our engineering ethos is 'Problem First': classify the business problem, and if it is deterministic, write deterministic code. Reserve LLMs strictly for unstructured cognitive tasks."

---

### Slide 11: Four Real-World Tasks — Four Different Worlds
- **Timing:** 37:00 — 42:00 (5 min)
- **Objective:** Walk through four concrete tasks mapping to four distinct architecture classes.
- **Speaker Track:**
  > "Examine this matrix. Four standard enterprise tasks:  
  > 1. VAT Tax Calculation: Deterministic lookup. 5 lines of backend code. $0 cost, sub-millisecond execution.  
  > 2. Churn Prediction across 1M Subscribers: Classical ML. Tabular features fed to LightGBM or CatBoost. Fast, cheap, and calibrated.  
  > 3. Synthesizing 50 Customer Support Tickets: The sweet spot for Generative AI. Unstructured text in diverse human styles.  
  > 4. Automated Kubernetes Incident Rollback: An AI Agent with guarded tool access and required human sign-off.  
  > Never hire a poet to count warehouse inventory."

---

### Slide 12: What the Model Sees: Text Tokenization
- **Timing:** 42:00 — 46:00 (4 min)
- **Objective:** Demystify BPE tokenization and its direct connection to cost and latency.
- **Speaker Track:**
  > "Foundation models never see characters, words, or whitespace. They operate strictly on tokens.  
  > Algorithms like Byte-Pair Encoding (BPE) split text into statistical subwords.  
  > In English, 1 token is roughly 4 characters or 0.75 words.  
  > In Cyrillic and other Unicode-heavy alphabets, words often fragment into 2, 3, or even 4 tokens per word.  
  > Token length directly determines cloud spend and latency."

---

### Slide 13: Under the Hood: 'T9 on Steroids' & Probabilities
- **Timing:** 46:00 — 50:00 (4 min)
- **Objective:** Explain next-token probability distributions and temperature mechanics.
- **Speaker Track:**
  > "At a physical level, foundation models are next-token predictors—T9 on supercomputers.  
  > Given 'The capital of France is...', the model calculates probability distributions across its vocabulary.  
  > How does the model choose? Through the Temperature parameter:  
  > • At Temperature = 0.0 (Greedy Decoding), the model strictly picks the top-1 highest probability token. This is mandatory for code, JSON schemas, and structured data.  
  > • At Temperature = 0.7 to 1.0, the distribution flattens, introducing stochastic diversity for creative writing.  
  > Rule of thumb: for production JSON generation, Temperature is always set to 0.0."

---

### Slide 14: Eloquence ≠ Truth: Hallucinations vs. RAG
- **Timing:** 50:00 — 55:00 (5 min)
- **Objective:** Contrast ungrounded generation with Retrieval-Augmented Generation (RAG).
- **Speaker Track:**
  > "Study the architectural contrast on this slide:  
  > On the left: Ungrounded Generation. The model relies solely on frozen parametric weights. If facts are missing, the model will generate an eloquent, confident, but fabricated answer—a hallucination.  
  > On the right: Retrieval-Augmented Generation (RAG). We query an authoritative knowledge base, retrieve the exact verified snippet, and inject it into the prompt with strict instructions: 'Answer strictly using this context.'  
  > Engineering law: fluency has zero correlation with truth. Accuracy requires architectural grounding."

---

### Slide 15: Midpoint Coffee Break (Interactive 5-Min Timer)
- **Timing:** 55:00 — 60:00 (5 min)
- **Objective:** Mental recharge and attention reset.
- **Speaker Track:**
  > "We have reached our midpoint!  
  > I am triggering the interactive 5-minute timer directly on the slide. Grab some water or coffee and reset your attention.  
  > When we return for Part 2, we will explore the submerged part of the architectural iceberg, risk governance (Blast Radius), real industry failures, our decision tree, and Homework Assignment #1.  
  > See you in 5 minutes!"  
  *(Instructor clicks '▶ Start 5 Min' on the slide)*.

---

### Slide 16: Model ≠ Product: The Architectural Iceberg
- **Timing:** 60:00 — 65:00 (5 min)
- **Objective:** Detail the 90% engineering scaffolding needed below the waterline.
- **Speaker Track:**
  > "Welcome back! Look closely at this architectural iceberg.  
  > The 10% above the waterline is the simple 3-line Python API call shown in demo tutorials. That takes 10 minutes.  
  > But the 90% submerged represents enterprise software engineering:  
  > • Output Validation: parsing schemas with Pydantic and preventing malformed JSON.  
  > • Resiliency: exponential backoff for HTTP 429 rate limits and fallback models.  
  > • Security: prompt injection sanitization and PII redaction.  
  > • Economics & Telemetry: token cost tracking and latency budgets.  
  > Understanding this submerged 90% is what separates an engineer from a casual consumer."

---

### Slide 17: Blast Radius: Risk Traffic Light Matrix
- **Timing:** 65:00 — 70:00 (5 min)
- **Objective:** Establish the Blast Radius framework and define boundaries of AI autonomy.
- **Speaker Track:**
  > "To safeguard business integrity, we apply the Blast Radius matrix:  
  > • 🟢 Green Zone (Low Risk): Internal documentation summaries, email drafts, test brainstorming. Cost of error is $0 because a human consumes it. High autonomy is permitted.  
  > • 🟡 Yellow Zone (Medium Risk): Developer code assistants (Copilot) or customer support drafts. The model generates proposals, but a human approves before deployment (Human-in-the-Loop).  
  > • 🔴 Red Zone (Critical Risk): Financial debits, modifying production database records, triggering cluster restarts.  
  > Architectural Taboo: direct write access from an LLM to critical systems is strictly forbidden! Models propose actions, but deterministic systems execute only upon verified human approval."

---

### Slide 18: Production Chronicles: 4 Costly Failures vs. 4 Enterprise Wins
- **Timing:** 70:00 — 76:00 (6 min)
- **Objective:** Analyze real-world industry failures and highlight the EPAM CodeMie @ Dawn Foods case.
- **Speaker Track:**
  > "Let's review documented industry battle scars:  
  > 1. Air Canada (2024): An airline chatbot hallucinated a retroactive bereavement discount policy. The tribunal rejected the claim that 'the bot is an independent entity' and ordered full compensation.  
  > 2. Chevrolet Tahoe for $1: A dealership chatbot accepted an offer to sell a $50k SUV for $1 due to unconstrained prompt injection.  
  > 3. DPD Delivery: A support chatbot cursed at users and wrote poems criticizing its own company after light prompting.  
  > 4. Mata v. Avianca: Lawyers submitted hallucinated federal case citations generated by ChatGPT and received severe judicial sanctions.  
  > And here is the positive enterprise benchmark from my personal delivery experience:  
  > I led the rollout of EPAM CodeMie across software delivery lifecycles at Dawn Foods—a premier global bakery ingredient manufacturer. We integrated AI orchestration into their SDLC: accelerating feature delivery and unit test generation by 35%, alongside automated documentation that preserved deep repository architecture context.  
  > Why did it succeed? Because code was validated by linters before commits, and human engineers remained firmly at the helm."

---

### Slide 19: Decision Tree: Do You Actually Need GenAI?
- **Timing:** 76:00 — 80:00 (4 min)
- **Objective:** Provide a 4-question decision algorithm using standard pre-set industry examples.
- **Speaker Track:**
  > "Here is our 4-step architectural decision tree:  
  > 1. Can the problem be solved deterministically? If YES ➔ write code and close the ticket (e.g., calculating invoice discounts).  
  > 2. Does it require semantic reasoning over unstructured data? If NO ➔ use classical ML (e.g., loan risk scoring on tabular data).  
  > 3. Is the cost of error high? If YES ➔ enforce strict Human-in-the-Loop gates (e.g., drafting customer service replies where human agents click Send).  
  > 4. Do you have an authoritative source of truth? If YES ➔ implement RAG grounded in enterprise knowledge.  
  > An engineer first classifies the problem, then chooses the tool."

---

### Slide 20: Homework Assignment #1: AI Use-Case Memo
- **Timing:** 80:00 — 85:00 (5 min)
- **Objective:** Walk through homework expectations using the Glovo Courier benchmark case.
- **Speaker Track:**
  > "Your first assignment is to author a 300–500 word AI Use-Case Memo.  
  > Select one real, routine workflow from your current day-to-day work and perform an architectural audit.  
  > Examine the benchmark example on the right side of the slide—the Glovo Food Delivery Courier use-case:  
  > 1. Business Problem: A food delivery courier arrives at a restaurant, but cheesecake is out of stock (or an intercom code is missing). Rapid customer coordination is required to avoid delivery delay.  
  > 2. Decision Tree:  
  >    • Route optimization and delivery ETA calculations belong to deterministic graphs and ML. Never use LLMs here.  
  >    • Customer messaging belongs to GenAI: polite, empathetic, concise, and generated in the customer's native language.  
  > 3. Blast Radius: Yellow Zone (Co-pilot). The model generates a draft, but the courier confirms sending with a single tap.  
  > 4. Architectural Taboo: The model is strictly prohibited from cancelling orders, issuing refunds, offering free meals, or altering invoices.  
  > Document a workflow from your own domain following this structure in `genai-homeworks/L01/README.md` and invite `ihar_rubanovich@epam.com`."

---

### Slide 21: Q&A and Lesson 02 Teaser
- **Timing:** 85:00 — 90:00 (5 min)
- **Objective:** Summarize takeaways, tease Lesson 02, and open the mic.
- **Speaker Track:**
  > "Today we established our baseline mental models and a realistic vision of the GenAI landscape.  
  > Next time in Lesson 02, we begin hands-on technical exploration: BPE tokenization, context windows, embeddings, vector search, and structured prompting.  
  > Thank you for your attention! The floor is now open for questions."
