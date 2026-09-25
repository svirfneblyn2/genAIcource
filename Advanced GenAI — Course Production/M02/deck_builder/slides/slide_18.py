# Slide 18: Resume Signals & State Mutability
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 18,
    "kicker": "GOVERNANCE & HITL",
    "title": "Resumption Signals: Validating and Mutating Paused State",
    "lead": "Resuming paused graphs with human feedback, state overrides, or alternative execution pathways.",
    "section": "Production Reliability",
    "takeaway": "Human approval is not binary: reviewers can edit state variables before resuming, correcting model drift.",
    "notes": {
        "goal": "Demonstrate the concrete API mechanics for resuming paused graphs and mutating state variables before continuation.",
        "talkTrack": "Most people think Human-in-the-Loop is just clicking 'Yes' or 'No'. In production, human approval is state mutation. A reviewer might say: 'Yes, approve the wire transfer, but change the amount from $14,500 to $12,000 because of an invoice dispute'. With graph checkpointers, the reviewer invokes update_state() to overwrite the specific state field, and then invokes the graph with None to resume. The protected node runs with the human-corrected value.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1b2434"/>
        {render_icon("state_machine", 15, 10, size=24, color="#6ee7b7")}
        <text x="48" y="28" class="text-h1" fill="#6ee7b7">State Mutation on Resume: The 3 Approval Patterns</text>

        <!-- 3 Approval Patterns -->
        <g transform="translate(20, 60)">
          <!-- Pattern A: Plain Approve -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="390" height="235" rx="6" class="node-box-active-green"/>
            <rect x="0" y="0" width="390" height="30" rx="6" fill="#152420"/>
            <text x="14" y="20" class="text-mono-green" font-size="11">PATTERN A: UNMODIFIED APPROVAL</text>

            <g transform="translate(14, 45)">
              <rect x="0" y="0" width="360" height="60" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="12" y="22" class="text-mono" font-size="9.5" fill="#6ee7b7"># Resume with None input</text>
              <text x="12" y="38" class="text-mono" font-size="9.5" fill="#e2e8f0">app.invoke(</text>
              <text x="20" y="52" class="text-mono" font-size="9.5" fill="#cbd5e1">None, config={{"configurable": {{"thread_id": "tx_41"}}}})</text>

              <text x="0" y="80" class="text-mono-green" font-size="10.5">BEHAVIOR:</text>
              <text x="0" y="100" class="text-p">&bull; Checkpointer loads frozen state verbatim.</text>
              <text x="0" y="118" class="text-p">&bull; Execution advances past the interrupt barrier.</text>
              <text x="0" y="136" class="text-dim">&bull; Target node executes with original parameters.</text>
            </g>
          </g>

          <!-- Pattern B: State Mutation Override -->
          <g transform="translate(415, 0)">
            <rect x="0" y="0" width="390" height="235" rx="6" class="node-box-active-amber"/>
            <rect x="0" y="0" width="390" height="30" rx="6" fill="#2d2516"/>
            <text x="14" y="20" class="text-mono-amber" font-size="11">PATTERN B: STATE MUTATION OVERRIDE</text>

            <g transform="translate(14, 45)">
              <rect x="0" y="0" width="360" height="75" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="12" y="20" class="text-mono-amber" font-size="9"># 1. Update state prior to resume</text>
              <text x="12" y="34" class="text-mono" font-size="9" fill="#e2e8f0">app.update_state(config, {{</text>
              <text x="20" y="48" class="text-mono" font-size="9" fill="#e0c58e">  "amount": 12000.00, "override_by": "alice"}})</text>
              <text x="12" y="66" class="text-mono-green" font-size="9">app.invoke(None, config) # 2. Resume</text>

              <text x="0" y="95" class="text-mono-amber" font-size="10.5">BEHAVIOR:</text>
              <text x="0" y="115" class="text-p">&bull; Overwrites target state fields in checkpointer.</text>
              <text x="0" y="133" class="text-p">&bull; Intercepts model hallucination before side-effect.</text>
              <text x="0" y="151" class="text-dim">&bull; Node executes with human-sanitized value.</text>
            </g>
          </g>

          <!-- Pattern C: Rejection / Routing -->
          <g transform="translate(830, 0)">
            <rect x="0" y="0" width="390" height="235" rx="6" class="node-box-active-coral"/>
            <rect x="0" y="0" width="390" height="30" rx="6" fill="#24191d"/>
            <text x="14" y="20" class="text-mono-coral" font-size="11">PATTERN C: REJECTION &amp; ABORT</text>

            <g transform="translate(14, 45)">
              <rect x="0" y="0" width="360" height="60" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="12" y="22" class="text-mono-coral" font-size="9.5"># Inject rejection status</text>
              <text x="12" y="38" class="text-mono" font-size="9.5" fill="#e2e8f0">app.update_state(config, {{</text>
              <text x="20" y="52" class="text-mono" font-size="9.5" fill="#d98585">  "status": "REJECTED_BY_CFO"}})</text>

              <text x="0" y="80" class="text-mono-coral" font-size="10.5">BEHAVIOR:</text>
              <text x="0" y="100" class="text-p">&bull; Graph conditional edge routes to cancel_node.</text>
              <text x="0" y="118" class="text-p">&bull; Destructive node is completely bypassed.</text>
              <text x="0" y="136" class="text-dim">&bull; Audit entry logged to security event stream.</text>
            </g>
          </g>
        </g>

        <!-- Bottom Audit Standard -->
        <g transform="translate(20, 310)">
          <rect x="0" y="0" width="1220" height="65" rx="6" fill="#111722" stroke="#253245"/>
          <text x="16" y="24" class="text-mono-green" font-size="11">COMPLIANCE TRAIL IN PERSISTENT STORAGE:</text>
          <text x="16" y="46" class="text-p">Every state mutation creates a new sequential checkpoint. Auditors can inspect both what the LLM initially drafted and what the human reviewer edited before execution.</text>
        </g>
      </g>
    """)
}
