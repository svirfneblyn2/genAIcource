# Slide 24: Trajectory Evaluation
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 24,
    "kicker": "EVALUATION & QA",
    "title": "Trajectory Evaluation: Auditing Intermediate Reasoning",
    "lead": "Why evaluating end-to-end answers fails in agents; verifying tool selection, arguments, and intermediate states.",
    "section": "Production Observability",
    "takeaway": "A correct final answer generated through invalid tool calls is an architectural defect, not a success.",
    "notes": {
        "goal": "Explain why evaluating agents requires trajectory scrutiny of intermediate tool choices rather than superficial final-answer testing.",
        "talkTrack": "In standard LLM applications, you evaluate input vs output using an LLM-as-a-Judge. In agentic systems, this is dangerous. An agent could hallucinate a tool argument, fail three times, query the wrong database, and accidentally stumble onto the correct answer. That is not a successful system; that is an accident waiting to fail in production. Trajectory evaluation audits every intermediate step: Did it pick the right tool? Were arguments valid? Did it reach the goal efficiently?",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1e2c42"/>
        {render_icon("evaluation", 15, 10, size=24, color="#60a5fa")}
        <text x="48" y="28" class="text-h1" fill="#60a5fa">Trajectory Evaluation: Intermediate Step Auditing Framework</text>

        <!-- Comparison Layout -->
        <g transform="translate(20, 60)">
          <!-- Left: The Flawed Approach (Final Answer Only) -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="460" height="320" rx="6" class="node-box"/>
            <rect x="0" y="0" width="460" height="34" rx="6" fill="#24191d"/>
            <text x="14" y="22" class="text-mono-coral" font-size="11">SUPERFICIAL: FINAL ANSWER ONLY (FLAWED)</text>

            <g transform="translate(16, 48)">
              <rect x="0" y="0" width="428" height="50" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="12" y="20" class="text-mono" font-size="9.5">Input: "Find invoice total for Acme Corp"</text>
              <text x="12" y="36" class="text-mono-green" font-size="9.5">Final Output: "$14,500.00" (Matches Ground Truth!)</text>

              <g transform="translate(0, 65)">
                <text x="0" y="16" class="text-mono-coral" font-size="10.5">HIDDEN ARCHITECTURAL DEFECTS:</text>
                <text x="0" y="36" class="text-p">&bull; Step 1: Model called web_search (unauthorized tool leak)</text>
                <text x="0" y="56" class="text-p">&bull; Step 2: Failed SQL query with syntax error (wasted tokens)</text>
                <text x="0" y="76" class="text-p">&bull; Step 3: Hardcoded invoice total from memory (hallucination)</text>
                <text x="0" y="96" class="text-p">&bull; Total latency: 14.8 seconds (SLA breach)</text>
              </g>

              <rect x="0" y="195" width="428" height="42" rx="4" fill="#24191d" stroke="#d98585"/>
              <text x="214" y="220" text-anchor="middle" class="text-mono-coral" font-size="11">VERDICT: FALSE POSITIVE (RISK HIGH)</text>
            </g>
          </g>

          <!-- Right: Rigorous Trajectory Evaluation -->
          <g transform="translate(490, 0)">
            <rect x="0" y="0" width="730" height="320" rx="6" class="node-box-active"/>
            <rect x="0" y="0" width="730" height="34" rx="6" fill="#1e2c42"/>
            <text x="14" y="22" class="text-mono-green" font-size="11">ENTERPRISE STANDARD: STEP-BY-STEP TRAJECTORY SCRUTINY</text>

            <g transform="translate(16, 48)">
              <!-- 4 Step Checkpoints -->
              <g transform="translate(0, 0)">
                <rect x="0" y="0" width="698" height="52" rx="4" fill="#152420" stroke="#6ee7b7"/>
                <text x="14" y="22" class="text-mono-green" font-size="10.5">1. TOOL SELECTION ACCURACY (SCORE: 1.0)</text>
                <text x="14" y="40" class="text-p">Did the model invoke erp_lookup rather than web_search or arbitrary SQL?</text>
              </g>

              <g transform="translate(0, 60)">
                <rect x="0" y="0" width="698" height="52" rx="4" fill="#152420" stroke="#6ee7b7"/>
                <text x="14" y="22" class="text-mono-green" font-size="10.5">2. ARGUMENT INTEGRITY (SCORE: 1.0)</text>
                <text x="14" y="40" class="text-p">Were parameters formatted to exact schema regex (vendor_id='V-891', date='2026-09-01')?</text>
              </g>

              <g transform="translate(0, 120)">
                <rect x="0" y="0" width="698" height="52" rx="4" fill="#152420" stroke="#6ee7b7"/>
                <text x="14" y="22" class="text-mono-green" font-size="10.5">3. INTERMEDIATE GROUNDING (SCORE: 1.0)</text>
                <text x="14" y="40" class="text-p">Did the agent's intermediate synthesis match tool return without hallucinating numbers?</text>
              </g>

              <g transform="translate(0, 180)">
                <rect x="0" y="0" width="698" height="52" rx="4" fill="#152420" stroke="#6ee7b7"/>
                <text x="14" y="22" class="text-mono-green" font-size="10.5">4. TRAJECTORY EFFICIENCY (SCORE: 0.95)</text>
                <text x="14" y="40" class="text-p">Did it reach the goal in the minimal 3 super-steps without redundant polling loops?</text>
              </g>
            </g>
          </g>
        </g>
      </g>
    """)
}
