# Slide 07: Time-Travel Debugging & State Forking
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 7,
    "kicker": "PRODUCTION RELIABILITY",
    "title": "Time-Travel Debugging: Replaying and Forking State",
    "lead": "Every checkpoint produces an immutable snapshot, allowing developers to rewind, modify, and branch execution.",
    "section": "State & Persistence",
    "takeaway": "Time-travel eliminates non-reproducible bugs: replay the exact state snapshot that caused a failure.",
    "notes": {
        "goal": "Explain how immutable checkpoints enable developers to rewind execution histories, edit state, and branch new paths.",
        "talkTrack": "One of the most powerful features of graph-based persistence is time-travel. In a traditional app, when an exception throws on step 5, you have to rerun from step 1 and hope the stochastic model reproduces the error. In LangGraph, each super-step creates an immutable checkpoint. You can load checkpoint 3, inspect the exact variables, modify an argument, and resume execution down a new branch.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Timeline Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1e2c42"/>
        {render_icon("timeline", 15, 10, size=24, color="#60a5fa")}
        <text x="48" y="28" class="text-h1" fill="#60a5fa">Checkpoint Thread Timeline &amp; State Forking Blueprint</text>

        <!-- Top Timeline: The Failing Run -->
        <g transform="translate(30, 65)">
          <text x="0" y="16" class="text-mono-coral" font-size="11">ORIGINAL EXECUTION RUN (FAULT ON STEP 3):</text>
          
          <!-- CP 1 -->
          <g transform="translate(0, 30)">
            <rect x="0" y="0" width="210" height="70" rx="6" class="node-box"/>
            <text x="12" y="22" class="text-mono" font-size="10">CHECKPOINT: cp_01</text>
            <text x="12" y="42" class="text-h2">User Ingress</text>
            <text x="12" y="58" class="text-dim">Reconcile Invoice 401</text>
          </g>

          <path d="M 210 65 L 290 65" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

          <!-- CP 2 -->
          <g transform="translate(290, 30)">
            <rect x="0" y="0" width="240" height="70" rx="6" class="node-box-active"/>
            <text x="12" y="22" class="text-mono" font-size="10">CHECKPOINT: cp_02 (TARGET)</text>
            <text x="12" y="42" class="text-h2">Model Reasoning</text>
            <text x="12" y="58" class="text-dim">tool_call: erp_lookup(id='INV-401')</text>
          </g>

          <path d="M 530 65 L 610 65" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

          <!-- CP 3 (Fault) -->
          <g transform="translate(610, 30)">
            <rect x="0" y="0" width="240" height="70" rx="6" class="node-box-active-coral"/>
            <text x="12" y="22" class="text-mono-coral" font-size="10">CHECKPOINT: cp_03 (CRASH)</text>
            <text x="12" y="42" class="text-h2" fill="#d98585">Tool Error</text>
            <text x="12" y="58" class="text-mono-coral" font-size="9.5">DB connection timeout (504)</text>
          </g>

          <!-- Branch Rewind Arrow -->
          <path d="M 410 100 Q 410 160 410 175" stroke="#e0c58e" stroke-width="2.5" fill="none" marker-end="url(#arr-amber)"/>
          
          <rect x="290" y="130" width="240" height="26" rx="4" fill="#2d2516" stroke="#e0c58e"/>
          <text x="410" y="147" text-anchor="middle" class="text-mono-amber" font-size="10">TIME-TRAVEL: REWIND TO cp_02</text>
        </g>

        <!-- Bottom Timeline: The Forked Run -->
        <g transform="translate(30, 255)">
          <text x="0" y="14" class="text-mono-green" font-size="11">FORKED EXECUTION BRANCH (RESUMED WITH CORRECTED STATE):</text>

          <!-- Forked Node 1 -->
          <g transform="translate(290, 25)">
            <rect x="0" y="0" width="240" height="70" rx="6" class="node-box-active-amber"/>
            <text x="12" y="22" class="text-mono-amber" font-size="10">CHECKPOINT: cp_02_fork</text>
            <text x="12" y="42" class="text-h2">State Mutation</text>
            <text x="12" y="58" class="text-mono-green" font-size="9.5">update_state(retry_with_mock=True)</text>
          </g>

          <path d="M 530 60 L 610 60" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>

          <!-- Forked Tool Node -->
          <g transform="translate(610, 25)">
            <rect x="0" y="0" width="240" height="70" rx="6" class="node-box-active-green"/>
            <text x="12" y="22" class="text-mono-green" font-size="10">CHECKPOINT: cp_03_fixed</text>
            <text x="12" y="42" class="text-h2">Tool Sandbox OK</text>
            <text x="12" y="58" class="text-dim">ERP query returned record: 200 OK</text>
          </g>

          <path d="M 850 60 L 930 60" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>

          <!-- Terminal Success -->
          <g transform="translate(930, 25)">
            <rect x="0" y="0" width="240" height="70" rx="6" class="node-box-active-green"/>
            <text x="12" y="22" class="text-mono-green" font-size="10">CHECKPOINT: cp_04_terminal</text>
            <text x="12" y="42" class="text-h2">Reconciliation Passed</text>
            <text x="12" y="58" class="text-dim">Invoice matched to PO 8912</text>
          </g>
        </g>
      </g>
    """)
}
