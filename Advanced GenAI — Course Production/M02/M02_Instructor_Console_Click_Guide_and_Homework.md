# Module 02: Instructor Console Click-Guide & Zero-Cost Homework Specification

Course: Advanced Generative AI for Engineers
Module 02: Agent Frameworks and Orchestration: State Machines, Multi-Agent Topologies, and Production Reliability

---

## Part 1: Instructor Console Click-by-Click Guide (15-Minute Tour)

### Pedagogical Goal
Demonstrate to students that production agents are deterministic state machines with verifiable state channels, persistent checkpoints, and human-in-the-loop gateways. You do NOT need expensive cloud clusters or billable vector stores. You use local LangGraph Studio, local Python trace inspectors, or LangSmith to anchor abstract graph theory in concrete execution tools.

### Preparation Before Lecture (Open 4 Browser Tabs / Windows)
1. Tab 1: Presentation deck (`presentation_M02_Agent_Frameworks.html`), opened to Slide 26.
2. Tab 2: LangGraph Studio UI / Local Inspector (`http://localhost:2024` or local trace visualizer).
3. Tab 3: LangSmith Tracing Dashboard (`https://smith.langchain.com/` or Arize Phoenix UI `http://localhost:6006`).
4. Tab 4: Local VS Code editor showing the accounts payable reconciliation graph script (`reconcile_graph.py`).

*Tip: Launch the local LangGraph Studio or Ollama server 10 minutes before class so local warmups do not introduce hesitation on screen.*

---

### Step 1: Graph Compilation & Canvas Overview (3 minutes)

#### Where to look:
1. **LangGraph Studio Canvas (Center Pane)**
   - What to show: The visual graph canvas showing compiled Nodes (`ocr_extraction`, `erp_lookup`, `reconciliation_node`, `post_to_ledger`), Directed Edges, and the Conditional Routing Diamond.
   - What to say:
     > "Notice how the orchestrator visualizes our application. This is not a hidden prompt loop or a black-box chain. It is a formal state automaton. Every rectangle is a Python function that takes a state snapshot and returns a state delta. The diamond is a conditional router that deterministically branches based on state variables."

2. **Left Sidebar: State Schema & Channels**
   - What to show: The defined state schema (`messages: Annotated[list, add_messages]`, `invoice_id: str`, `billed_amount: float`, `variance: float`, `retry_counter: int`).
   - What to say:
     > "This is Layer 1 of our architecture. Every node execution communicates solely through these typed channels. Overwriting is prevented by explicit append reducers."

---

### Step 2: Injecting Test Payload & Live Stepping (3 minutes)

#### Where to click:
1. **Studio Bottom Input Box -> Input JSON**
   - Paste the test payload:
     `{"invoice_id": "INV-8912", "vendor": "Acme Industrial", "billed_amount": 14500.00, "po_number": "PO-4011"}`
   - Click the green button **"Start Run"**.
   - What to show:
     - Watch Node 1 (`ocr_extraction`) illuminate in green as it completes.
     - Watch execution advance to Node 2 (`erp_lookup`).
     - Point out the active thread ID generated in the header (e.g. `thread_rec_9102`).
   - What to say:
     > "Observe the super-step progression. The model does not run unrestricted. The orchestrator executes Node 1, intercepts the state delta, saves an immutable checkpoint to Postgres or SQLite, and then triggers Node 2 to query the ERP sandbox."

---

### Step 3: Triggering the Breakpoint Barrier (3 minutes)

#### Where to look:
1. **Visual Canvas -> Interrupt Barrier before `post_to_ledger`**
   - Point out that execution has halted with status `INTERRUPTED`. Node 4 (`post_to_ledger`) is bordered in yellow/amber and has NOT fired.
   - What to show:
     - Open the **State Inspector Drawer** on the right side.
     - Show the computed state fields:
       - `billed_amount: 14500.00`
       - `po_authorized_amount: 14050.00`
       - `variance: 450.00`
       - `approval_status: "PENDING_CFO_AUTHORIZATION"`
   - What to say:
     > "This is Slide 17 in action. We compiled our graph with interrupt_before=['post_to_ledger']. Because the variance is $450.00, corporate policy mandates human review. Notice that our server process is completely idle. State is persisted in the checkpointer. No CPU is spinning; no tokens are burning. The graph waits safely for an external resume signal."

---

### Step 4: Live State Mutation & Graph Resumption (3 minutes)

#### Where to click:
1. **State Inspector -> Edit Field**
   - Click the field `approved_by` and enter `"cfo_alice@enterprise.com"`.
   - Change `approved_amount` to `14050.00` (demonstrating early payment discount deduction).
   - Click **"Update State"**.
   - What to say:
     > "Notice this crucial architectural point: Human-in-the-Loop is not just a binary yes/no button. Human review is active state mutation. The CFO noticed an unapplied discount and edited the state directly in the checkpointer."

2. **Top Navigation -> Click "Resume"**
   - What to show:
     - The graph unlocks.
     - Node 4 (`post_to_ledger`) illuminates in green.
     - Final output displays: `Journal entry JE-9921 created for $14,050.00. Approved by cfo_alice@enterprise.com.`
   - What to say:
     > "The graph resumed with the sanitized human parameters. We have achieved complete operational safety without breaking automation."

---

### Step 5: Distributed Trace Waterfall Audit (3 minutes)

#### Where to click:
1. **Switch to Tab 3 (LangSmith / Arize Phoenix UI)**
   - Click the latest run matching `thread_rec_9102`.
   - What to show:
     - The complete 4-span waterfall trace.
     - Span 1: `supervisor_plan` (LLM call, 850ms, 1,200 tokens).
     - Span 2: `tool_ocr` (HTTP request, 1,150ms, 0 LLM tokens).
     - Span 3: `erp_lookup` (SQL query, 420ms, 0 LLM tokens).
     - Span 4: `post_to_ledger` (Execution post-resume, 310ms).
     - Total run metrics: Latency 2,730ms active compute, Total Cost: $0.018.
   - What to say:
     > "Here is full observability. Every decision, latency bottleneck, and token cost is accounted for. If a model hallucinates an argument, the trace captures the exact schema rejection before any downstream damage occurs."

---

## Part 2: Student Homework Specification (100% Zero-Cost Guarantee)

### Assignment Title
**Enterprise Agent Engineering Package: Autonomous Accounts Payable & Claims Reconciliation Agent**

### Deadline & Format
- **Format**: 1 Architecture Design Document (PDF or Markdown) OR 1 Local Python Repository with runnable code.
- **Cost Guarantee**: **$0.00 (Zero financial cost guaranteed)**. Students do NOT need cloud subscriptions, credit cards, or paid vector databases.

---

### Business Scenario
You are the Principal AI Engineer for *Apex Enterprise Systems*. The organization processes 25,000 vendor invoices per month. Currently, accounts payable teams manually cross-reference invoices against Purchase Orders in SAP, verify line-item arithmetic, and route discrepancies to finance managers.

Your objective is to design and build a resilient, cyclic, state-machine agent with:
1. **Centralized Typed State**: Explicit schema tracking messages, invoice metadata, line items, retry counts, and audit logs.
2. **Tool Sandboxing**: Isolated tool functions for database lookup and payment ledger posting with parameter validation.
3. **Cyclic Error Recovery**: Automatic reflection loop when database queries fail or parameters fail schema validation (max 3 retries).
4. **Human-in-the-Loop Gateway**: Deterministic breakpoint (`interrupt_before`) triggered whenever discrepancy variance exceeds $0.00 or confidence drops below 95%.
5. **State Mutability**: Capability to resume execution with human-edited approval fields.

---

### Zero-Cost Implementation Options for Students

Students must choose **Option A** (Architecture Track) or **Option B** (Coding Track). Both receive equal grading weight.

#### Option A: Architecture & State Design Specification (No Coding Required)
Ideal for System Architects, Technical Product Managers, and Solution Consultants.
- **Tools**: Mermaid.js, Draw.io, Markdown, or PDF editor. Cost: $0.00.
- **Deliverable Requirements**:
  1. **State Machine Blueprint**: A complete Mermaid graph diagram depicting all Nodes (`ocr_parser`, `erp_match`, `reconcile_evaluator`, `hitl_gate`, `post_ledger`, `fallback_handler`), Static Edges, and Conditional Router Diamonds with explicit branch labels.
  2. **State Schema Specification**: Concrete Python `TypedDict` and `Pydantic` schema definitions including channel types and message reducers (`Annotated[list, add_messages]`).
  3. **Tool Contract & Error Policy Matrix**: Table detailing input JSON schemas, Pydantic field constraints, and specific handling rules across the 4 fault tiers (Transient 5xx, Schema ValidationError, Permanent 401/403, and Dead-Letter Queue).
  4. **HITL Protocol Specification**: Sequence diagram demonstrating state freeze, webhook payload generation, human review interface schema, and resumption payload validation.
  5. **Observability Plan**: Specification of OpenTelemetry span names, attributes (`gen_ai.system`, `gen_ai.usage.input_tokens`), and loop governor threshold limits.

#### Option B: Working Local Python Prototype (Coding Track)
Ideal for Software Engineers, ML Engineers, and Backend Developers.
- **Tools**: Python 3.10+, LangGraph, LangChain Core, and a 100% free local model via Ollama (`llama3.2:3b` or `qwen2.5:7b`) OR Google AI Studio free tier API key. Cost: $0.00.
- **Deliverable Requirements**:
  1. **Source Code**: Clean Python repository containing:
     - `state.py`: TypedDict state definition with `add_messages` reducer.
     - `tools.py`: Mock ERP query tool and ledger posting tool with explicit Pydantic schemas.
     - `graph.py`: StateGraph definition with cyclic retry edge, conditional router, and `MemorySaver` / `SqliteSaver` checkpointer.
     - `main.py`: Executable demonstration script.
  2. **Execution Demonstration**:
     - Run 1 (Auto-Approve Path): Passes matching invoice ($0 variance), runs through to completion without pausing.
     - Run 2 (HITL Path): Passes discrepancy invoice ($450 variance), hits `interrupt_before`, demonstrates state inspection, applies `app.update_state()` to simulate approval, and resumes to completion.
  3. **README.md**: Setup instructions to run locally in under 3 minutes with zero API keys required (using Ollama).

---

### 100-Point Grading Rubric

| Criterion | Points | Excellent (Full Points) | Needs Improvement (Partial) | Unacceptable (Zero) |
| :--- | :--- | :--- | :--- | :--- |
| **1. State Schema Architecture** | **25 pts** | Explicit TypedDict/Pydantic schema with typed channels, append-only message reducers, and audit fields. | Generic untyped dictionary used; lacks explicit reducers or type hints. | Missing state schema; global variables or uncontrolled state. |
| **2. Cyclic Flow & Error Reflection** | **25 pts** | Cyclic graph edges enable self-correction; retry counter enforces hard cap (max 3); error payloads feed back to model. | Retries implemented as simple while-loop outside graph; lacks reflection feedback. | Forward-only DAG with no error recovery; crashes on failure. |
| **3. Tool Sandboxing & Contracts** | **20 pts** | Explicit JSON/Pydantic schemas with type constraints; tools wrapped in safe execution boundary with timeout. | Tools lack validation schemas; unhandled exceptions bubble to main process. | Model generates raw unparsed code with direct host execution. |
| **4. HITL Gateway & Mutability** | **15 pts** | Deterministic breakpoint before destructive action; state saved in checkpointer; demonstrates state mutation on resume. | Breakpoint pauses but cannot accept mutated state; resume logic is binary only. | No human-in-the-loop protection; autonomous execution of sensitive action. |
| **5. Observability & Governance** | **15 pts** | Recursion limits configured; cost/token governors defined; trace spans capture latency and token consumption. | Basic logging present but lacks span hierarchy or loop circuit breakers. | Zero telemetry, zero logging, and unbounded recursion depth. |
| **TOTAL** | **100 pts** | **Minimum Passing Score: 80 / 100** | | |

---

### Submission Guidelines
1. Package your work as a single zip archive or GitHub repository link.
2. Ensure all diagrams and code include zero proprietary corporate data.
3. Include a 2-minute screen recording (Loom or MP4) or a comprehensive markdown walkthrough verifying the execution paths.
