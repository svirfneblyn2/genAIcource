# Slide 17: Human-in-the-Loop (HITL) Gateways
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 17,
    "kicker": "GOVERNANCE & HITL",
    "title": "Human-in-the-Loop Gateways: Interrupt Architecture",
    "lead": "Halting execution before destructive side effects to mandate human authorization and compliance approval.",
    "section": "Production Reliability",
    "takeaway": "Deterministic graph interrupts eliminate unauthorized actions: state pauses at the edge, awaiting an external resume signal.",
    "notes": {
        "goal": "Explain how orchestrators enforce security barriers using interrupt_before and interrupt_after hooks.",
        "talkTrack": "In enterprise operations, you cannot allow an AI model to autonomously execute a wire transfer, delete a customer database, or send an unreviewed contract. Human-in-the-loop is not a separate UI hack; it is a core feature of the state machine. In LangGraph, compiling with interrupt_before=['execute_wire_transfer'] pauses the graph right before that node runs. State is safely frozen in Postgres. The system alerts a compliance officer and waits.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active-amber"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#2d2516"/>
        {render_icon("approval", 15, 10, size=24, color="#e0c58e")}
        <text x="48" y="28" class="text-h1" fill="#e0c58e">Human-in-the-Loop Gateway: Deterministic Breakpoints</text>

        <!-- Process Flow -->
        <g transform="translate(25, 65)">
          <!-- Step 1: Draft Action Node -->
          <g transform="translate(0, 30)">
            <rect x="0" y="0" width="260" height="180" rx="6" class="node-box-active"/>
            <rect x="0" y="0" width="260" height="30" rx="6" fill="#1e2c42"/>
            <text x="14" y="20" class="text-mono" font-size="10.5">NODE: draft_payment</text>

            <g transform="translate(14, 45)">
              <text x="0" y="16" class="text-h2">Model Prepares Payload:</text>
              <rect x="0" y="26" width="230" height="60" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="10" y="44" class="text-mono" font-size="9" fill="#e2e8f0">{{"vendor": "Acme Corp",</text>
              <text x="10" y="58" class="text-mono" font-size="9" fill="#e0c58e"> "amount": 14500.00,</text>
              <text x="10" y="72" class="text-mono" font-size="9" fill="#e2e8f0"> "invoice": "INV-891"}}</text>

              <text x="0" y="105" class="text-mono-coral" font-size="9.5">Amount &gt; $10,000 threshold</text>
            </g>
          </g>

          <!-- Connector to Barrier -->
          <path d="M 260 120 L 330 120" stroke="#e0c58e" stroke-width="2.5" fill="none" marker-end="url(#arr-amber)"/>

          <!-- Step 2: Interrupt Barrier Wall -->
          <g transform="translate(340, 10)">
            <rect x="0" y="0" width="230" height="220" rx="6" fill="#1e181c" stroke="#d98585" stroke-width="2" stroke-dasharray="6 4"/>
            <text x="115" y="28" text-anchor="middle" class="text-mono-coral" font-size="11">INTERRUPT BARRIER</text>
            
            <g transform="translate(14, 45)">
              <text x="0" y="18" class="text-mono" font-size="9.5" fill="#cbd5e1">compile(checkpointer=...,</text>
              <text x="0" y="34" class="text-mono-coral" font-size="9.5">  interrupt_before=[</text>
              <text x="10" y="50" class="text-mono-coral" font-size="9.5">    'execute_payment'])</text>

              <rect x="0" y="65" width="202" height="85" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="10" y="85" class="text-mono-amber" font-size="9.5">AUTOMATED ACTIONS:</text>
              <text x="10" y="102" class="text-p">&bull; Freeze execution thread</text>
              <text x="10" y="118" class="text-p">&bull; Save state to Postgres</text>
              <text x="10" y="134" class="text-p">&bull; Dispatch webhook event</text>
            </g>
          </g>

          <!-- Connector to Human Queue -->
          <path d="M 570 120 L 640 120" stroke="#e0c58e" stroke-width="2.5" fill="none" marker-end="url(#arr-amber)"/>

          <!-- Step 3: Human Review Gateway -->
          <g transform="translate(650, 20)">
            <rect x="0" y="0" width="310" height="200" rx="6" class="node-box-active-amber"/>
            <rect x="0" y="0" width="310" height="30" rx="6" fill="#2d2516"/>
            <text x="14" y="20" class="text-mono-amber" font-size="10.5">HUMAN REVIEW PORTAL</text>

            <g transform="translate(14, 45)">
              <text x="0" y="16" class="text-h2">Reviewer: Finance Director</text>
              <text x="0" y="36" class="text-p">Notification via Slack / ServiceNow ticket</text>
              
              <rect x="0" y="48" width="280" height="50" rx="4" fill="#141c28" stroke="#e0c58e"/>
              <text x="10" y="68" class="text-mono" font-size="9.5">Review Options:</text>
              <text x="10" y="86" class="text-mono-green" font-size="9.5">[Approve]  [Modify Amount]  [Reject]</text>

              <text x="0" y="118" class="text-dim" font-size="9.5">State remains paused indefinitely without CPU burn</text>
            </g>
          </g>

          <!-- Connector to Execution -->
          <path d="M 960 120 L 1030 120" stroke="#6ee7b7" stroke-width="2.5" fill="none" marker-end="url(#arr-green)"/>

          <!-- Step 4: Protected Action Node -->
          <g transform="translate(1040, 30)">
            <rect x="0" y="0" width="170" height="180" rx="6" class="node-box-active-green"/>
            <rect x="0" y="0" width="170" height="30" rx="6" fill="#152420"/>
            <text x="14" y="20" class="text-mono-green" font-size="10">execute_payment</text>

            <g transform="translate(12, 45)">
              <text x="0" y="16" class="text-h2">Protected Node</text>
              <text x="0" y="36" class="text-p">&bull; Executes API</text>
              <text x="0" y="56" class="text-p">&bull; Transfers funds</text>
              <text x="0" y="76" class="text-p">&bull; Logs to ledger</text>
              <text x="0" y="105" class="text-mono-green" font-size="9.5">Guaranteed Safe</text>
            </g>
          </g>
        </g>

        <!-- Bottom Invariant -->
        <g transform="translate(25, 315)">
          <rect x="0" y="0" width="1210" height="60" rx="6" fill="#111722" stroke="#253245"/>
          <text x="16" y="24" class="text-mono-amber" font-size="11">PRODUCTION SAFETY GUARANTEE:</text>
          <text x="16" y="44" class="text-p">The execute_payment node CANNOT run without a verified cryptographic signature or valid session approval payload from an authorized human operator.</text>
        </g>
      </g>
    """)
}
