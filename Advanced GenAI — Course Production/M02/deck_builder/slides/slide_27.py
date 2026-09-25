# Slide 27: Synthesis & Capstone Student Assignment
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon
from ..logos import render_logo_badge

SLIDE_DATA = {
    "index": 27,
    "kicker": "CAPSTONE STUDENT ASSIGNMENT",
    "title": "Capstone Lab: Resilient AP Invoice & Dispute Resolution Agent",
    "lead": "Build or specify an end-to-end cyclic state machine with SQLite checkpointer, tool circuit breaker, and HITL authorization.",
    "section": "Workshop & Homework",
    "takeaway": "The capstone cements production agent engineering: state schemas, database checkpointers, circuit breakers, and human-in-the-loop gates.",
    "notes": {
        "goal": "Clearly specify the final student capstone assignment, defining the exact business problem, state machine architecture, and grading deliverables.",
        "talkTrack": "Here is your Capstone Assignment. You will build an Autonomous Accounts Payable Agent for Apex Enterprise Systems. The agent receives vendor invoices, queries an ERP database, evaluates discrepancies, and executes ledger postings. If variance is zero, it auto-approves. If variance is positive, it hits a deterministic breakpoint for human review. If tools fail, a circuit breaker catches the error. You can submit either an Architecture Spec or a working Python prototype running 100% locally with zero cloud costs.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1e2c42"/>
        {render_icon("document", 15, 10, size=24, color="#60a5fa")}
        <text x="48" y="28" class="text-h1" fill="#60a5fa">Capstone Engineering Specification: Autonomous Accounts Payable Agent</text>

        <g transform="translate(15, 55)">
          
          <!-- Left Panel: The State Machine Architecture -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="580" height="245" rx="6" class="node-box"/>
            <rect x="0" y="0" width="580" height="30" rx="6" fill="#1b2434"/>
            <text x="14" y="20" class="text-mono" font-size="10.5" fill="#60a5fa">REQUIRED STATE MACHINE TOPOLOGY</text>

            <g transform="translate(14, 40)">
              <!-- Input State Box -->
              <rect x="0" y="0" width="120" height="48" rx="4" fill="#141c28" stroke="#3b82f6"/>
              <text x="60" y="18" text-anchor="middle" class="text-mono" font-size="9" fill="#93c5fd">Invoice Ingress</text>
              <text x="60" y="32" text-anchor="middle" class="text-dim" font-size="7.5">invoice_id, amt, vendor</text>

              <path d="M 120 24 L 145 24" stroke="#60a5fa" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>

              <!-- Node 1: ERP Lookup Tool -->
              <rect x="145" y="0" width="120" height="48" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="205" y="18" text-anchor="middle" class="text-h2" font-size="9.5">1. ERP Match</text>
              <text x="205" y="32" text-anchor="middle" class="text-dim" font-size="7.5">query_po(invoice_id)</text>

              <path d="M 265 24 L 290 24" stroke="#60a5fa" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>

              <!-- Node 2: Reconciliation Node -->
              <rect x="290" y="0" width="125" height="48" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="352" y="18" text-anchor="middle" class="text-h2" font-size="9.5">2. Reconcile</text>
              <text x="352" y="32" text-anchor="middle" class="text-dim" font-size="7.5">Compute Variance</text>

              <path d="M 415 24 L 440 24" stroke="#60a5fa" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>

              <!-- Decision Diamond -->
              <polygon points="480,24 515,40 480,56 445,40" fill="#1e293b" stroke="#e0c58e" stroke-width="1.2"/>
              <text x="480" y="43" text-anchor="middle" class="text-mono-amber" font-size="7.5">VARIANCE?</text>

              <!-- Branch 1: Auto-Approve -->
              <path d="M 515 40 L 530 40 L 530 75 L 430 75" stroke="#6ee7b7" stroke-width="1.2" fill="none" marker-end="url(#arr-green)"/>
              <rect x="280" y="62" width="145" height="28" rx="4" fill="#152420" stroke="#6ee7b7"/>
              <text x="352" y="78" text-anchor="middle" class="text-mono-green" font-size="8.5">Auto-Approve: Post Ledger</text>

              <!-- Branch 2: Discrepancy -> HITL -->
              <path d="M 480 56 L 480 110 L 430 110" stroke="#e0c58e" stroke-width="1.2" fill="none" marker-end="url(#arr-amber)"/>
              <rect x="230" y="96" width="195" height="30" rx="4" fill="#2d2516" stroke="#e0c58e"/>
              <text x="327" y="112" text-anchor="middle" class="text-mono-amber" font-size="8.5">HITL: interrupt_before</text>
              <text x="327" y="122" text-anchor="middle" class="text-dim" font-size="7">Awaits human update_state()</text>

              <!-- Circuit Breaker Retry Loop -->
              <path d="M 205 48 L 205 85 L 140 85 L 140 35" stroke="#d98585" stroke-width="1.2" stroke-dasharray="2 2" fill="none" marker-end="url(#arr-coral)"/>
              <text x="172" y="97" text-anchor="middle" class="text-mono-coral" font-size="7">Tool Retry (max 3)</text>

              <!-- State Checkpointer Note -->
              <rect x="0" y="140" width="550" height="52" rx="4" fill="#111722" stroke="#253245"/>
              <text x="12" y="158" class="text-mono-green" font-size="9">PERSISTENCE CONTRACT: SqliteSaver / PostgresSaver</text>
              <text x="12" y="174" class="text-p" font-size="8.5">&bull; State Schema: TypedDict with messages (add_messages), invoice, variance, retries.</text>
              <text x="12" y="186" class="text-p" font-size="8.5">&bull; Checkpoints written on every superstep. Resumption verified via thread_id.</text>
            </g>
          </g>

          <!-- Right Panel: Deliverable Options -->
          <g transform="translate(595, 0)">
            <rect x="0" y="0" width="635" height="245" rx="6" class="node-box"/>
            <rect x="0" y="0" width="635" height="30" rx="6" fill="#1b2434"/>
            <text x="14" y="20" class="text-mono" font-size="10.5" fill="#6ee7b7">CHOOSE ONE TRACK (100% ZERO-COST GUARANTEED)</text>

            <g transform="translate(14, 40)">
              <!-- Option A -->
              <rect x="0" y="0" width="295" height="190" rx="4" fill="#141c28" stroke="#253245"/>
              <rect x="0" y="0" width="295" height="26" rx="4" fill="#1e293b"/>
              <text x="10" y="18" class="text-mono" font-size="9" fill="#93c5fd">OPTION A: ARCHITECTURE SPEC</text>

              <g transform="translate(10, 34)">
                <text x="0" y="14" class="text-p" font-size="8.5">&bull; Target: Architects &amp; Technical Leads</text>
                <text x="0" y="30" class="text-p" font-size="8.5">&bull; Format: Markdown document + Mermaid</text>
                <text x="0" y="48" class="text-mono-green" font-size="8">Key Requirements:</text>
                <text x="0" y="64" class="text-dim" font-size="8">1. Mermaid state graph diagram</text>
                <text x="0" y="78" class="text-dim" font-size="8">2. Full TypedDict state schema</text>
                <text x="0" y="92" class="text-dim" font-size="8">3. Tool contract &amp; error matrix</text>
                <text x="0" y="106" class="text-dim" font-size="8">4. HITL sequence &amp; payload specs</text>
                <text x="0" y="120" class="text-dim" font-size="8">5. OTel span hierarchy plan</text>
                <text x="0" y="142" class="text-mono-amber" font-size="7.5">Requires zero code; pure engineering rigor</text>
              </g>

              <!-- Option B -->
              <rect x="310" y="0" width="295" height="190" rx="4" fill="#141c28" stroke="#253245"/>
              <rect x="0" y="0" width="295" height="26" rx="4" fill="#152420" transform="translate(310, 0)"/>
              <text x="320" y="18" class="text-mono-green" font-size="9">OPTION B: PYTHON PROTOTYPE</text>

              <g transform="translate(320, 34)">
                <text x="0" y="14" class="text-p" font-size="8.5">&bull; Target: Software &amp; AI Engineers</text>
                <text x="0" y="30" class="text-p" font-size="8.5">&bull; Format: Python repo (LangGraph)</text>
                <text x="0" y="48" class="text-mono-green" font-size="8">Key Requirements:</text>
                <text x="0" y="64" class="text-dim" font-size="8">1. state.py with TypedDict schema</text>
                <text x="0" y="78" class="text-dim" font-size="8">2. tools.py with mock SQLite DB</text>
                <text x="0" y="92" class="text-dim" font-size="8">3. graph.py with SqliteSaver</text>
                <text x="0" y="106" class="text-dim" font-size="8">4. interrupt_before and resume test</text>
                <text x="0" y="120" class="text-dim" font-size="8">5. Automated pytest suite passing</text>
                <text x="0" y="142" class="text-mono-green" font-size="7.5">Runs on laptop with Ollama or mock ($0)</text>
              </g>
            </g>
          </g>

        </g>

        <!-- Bottom 100-Point Rubric Strip -->
        <g transform="translate(15, 312)">
          <rect x="0" y="0" width="1230" height="65" rx="6" fill="#111722" stroke="#253245"/>
          <text x="16" y="22" class="text-mono-amber" font-size="10">CAPSTONE EVALUATION RUBRIC (100 POINTS TOTAL):</text>
          
          <g transform="translate(16, 42)">
            <text x="0" y="0" class="text-p" font-size="8.5">&bull; State Schema &amp; Reducers: 25 pts</text>
            <text x="210" y="0" class="text-p" font-size="8.5">&bull; Cyclic Recovery &amp; Circuit Breaker: 25 pts</text>
            <text x="490" y="0" class="text-p" font-size="8.5">&bull; Tool Sandbox &amp; Schemas: 20 pts</text>
            <text x="730" y="0" class="text-p" font-size="8.5">&bull; HITL Breakpoint &amp; Mutate: 15 pts</text>
            <text x="980" y="0" class="text-p" font-size="8.5">&bull; Telemetry &amp; Tests: 15 pts</text>
          </g>
        </g>
      </g>
    """)
}
