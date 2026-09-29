# Homework Assignment 01: AI Use-Case Memo

* **Course:** GenAI Basics — Engineering Track
* **Lecture:** Lesson 01 — Introduction to AI, ML & GenAI: Systemic Vision
* **Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)
* **Length:** 300–500 words (single-page document)

---

## 1. The Assignment (What You Need to Do)

The most common failure in enterprise AI adoption is the **"AI-First" Trap**: attempting to solve a problem with an expensive, probabilistic Large Language Model (LLM) when a simple formula, deterministic SQL, or classical Machine Learning would solve it at $0 cost and 0ms latency.

**Your Goal:**  
Pick **one real, repetitive task** from your daily work, studies, or pet-project, and author an architectural evaluation document: the **AI Use-Case Memo**.

> [!NOTE]
> You do **not** write code for this assignment. Your objective is to practice the senior engineering decision: deciding *which parts of a system require deterministic software, which require classical ML, where Generative AI is genuinely justified, and where the human safety boundary must be placed.*

### Required Document Structure
Your memo must cover these 6 sections:
1. **Problem Framing & Friction Point:** What is the routine? Who performs it? How much time/effort does it waste today?
2. **Technology Classification:** Why is this problem a fit for Software 1.0 (code/SQL), Software 2.0 (classical ML), Software 3.0 (GenAI with review), or Software 4.0 (Autonomous Agent)?
3. **Data Contracts:** What exact data enters the system (Inputs)? What exact format comes out (Expected Output)?
4. **Blast Radius (Risk Tier):** Is this Green (internal draft, zero risk), Yellow (copilot, human verifies), or Red (critical DB/financial action, strictly prohibited for direct LLM execution)?
5. **Human-in-the-Loop Gate:** Exactly how does a human review and approve the output before it reaches production or clients?
6. **Architectural Taboo:** Name at least one critical action that the AI model is **strictly forbidden** from executing autonomously.

---

## 2. Benchmark Example (Reference Submission)

Use this verified lecture case study as your quality benchmark for depth, conciseness, and engineering tone:

```markdown
# AI Use-Case Memo: Glovo Food Delivery Courier Co-pilot

## 1. Problem Framing & Friction Point
Food delivery couriers pick up orders from restaurants and deliver them to customer locations.
Operational friction frequently occurs during last-mile delivery: restaurant runs out of an ingredient, residential gate codes are missing, or intercom systems fail.
Couriers operate on foot, bicycles, or scooters. Typing lengthy, polite explanations on mobile touchscreens while navigating traffic is slow, frustrating, and unsafe. Calling customers causes communication anxiety, disrupts route momentum, and inflates delivery cycle times, jeopardizing SLA targets.

## 2. Technology Classification
This system is architected as a hybrid pipeline:
- Route optimization and Estimated Time of Arrival (ETA): Classical graph traversal + Classical ML (Software 1.0 & 2.0). 
  Using an LLM here is strictly prohibited: it is non-deterministic, introduces hundreds of milliseconds of latency, and incurs needless token costs.
- Contextual customer messaging: Generative AI (Software 3.0 with Human-in-the-Loop review). 
  Foundation models excel at semantic tone adaptation, localized phrasing, and handling customer language preferences.

## 3. Data Contracts (Inputs & Outputs)
- Inputs: 
  1) One-tap courier trigger (selected incident type, e.g., "intercom code invalid");
  2) Customer first name;
  3) Customer interface language preference;
  4) Delivery address context;
  5) Real-time estimated delay calculated by navigation ML.
- Expected Output:
  Polite, localized text message (under 25 words) in the customer's native language proposing an immediate resolution.

## 4. Blast Radius & Risk Tier
- Risk Tier: 🟡 Yellow Zone (Human-in-the-Loop Co-pilot).
- Potential Failure Modes: Model hallucinating incorrect incident reasons or adopting an inappropriate tone.
- Mitigation Guardrails: Few-shot prompting template with fixed greedy decoding (`temperature=0.0`) to guarantee deterministic phrasing.

## 5. Human-in-the-Loop Control Gate
The drafted notification appears on the courier's active mobile screen:
1. The courier taps a large green "Send" button (single-action dispatch);
2. The courier can tap to edit any word inline;
3. The courier can cancel and initiate a phone call.
Without an explicit tap from the courier, zero characters are transmitted to the customer.

## 6. Architectural Taboo (What Will NEVER Be Automated)
The language model is strictly prohibited from:
1. Offering promotional codes, discounts, fee waivers, or monetary compensation.
2. Unilaterally canceling active orders or altering transaction amounts.
All financial, transaction, and refund capabilities are strictly isolated within the deterministic billing microservice and require human customer support authorization.
```

---

## 3. Where and How to Submit Your Homework

All homework assignments in this course are submitted **strictly via GitHub repositories**. Submitting files via email attachments, Slack, or Telegram is not accepted.

### Expected Repository Path:
Your deliverable must live at this exact path inside your repository:
```text
genai-homeworks/
├── L01/
│   └── README.md    <-- Your AI Use-Case Memo goes here
└── README.md        <-- Course overview table of contents
```

### Two Submission Methods (Pick One):

#### Method 1: In the Browser (No Git installation needed)
1. Open your `genai-homeworks` repository on [github.com](https://github.com).
2. Click **Add file** ➔ **Create new file**.
3. In the filename box, type: `L01/README.md` *(typing the slash `/` automatically creates the `L01` folder)*.
4. Paste your completed memo into the text editor.
5. Scroll down and click the green **Commit changes** button.

#### Method 2: Via Antigravity / Git CLI
1. Open your local `genai-homeworks` folder in Antigravity or your editor.
2. Create `L01/README.md` and write your memo.
3. In the terminal (or by asking the AI Agent in `Ctrl + L`), run:
   ```bash
   git add .
   git commit -m "feat(L01): add use-case memo"
   git push origin main
   ```

### Mandatory Final Step: Adding the Reviewer
To ensure the instructor can access and grade your work:
1. Go to your repository on GitHub.
2. Navigate to **Settings** ➔ **Collaborators** ➔ **Add people**.
3. Add the instructor's email:
   ```
   ihar_rubanovich@epam.com
   ```
4. Copy your repository URL (e.g., `https://github.com/your-username/genai-homeworks`) and paste it into the course tracking portal.
