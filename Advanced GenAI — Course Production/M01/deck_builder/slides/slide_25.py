# Slide 25: Workshop: Claims-Processing Assistant
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 25,
    "kicker": "HANDS-ON WORKSHOP",
    "title": "Design Task: Medical Claims Processing Assistant",
    "lead": "Apply the 5-question framework to an end-to-end multimodal enterprise workload.",
    "section": "Student Workshop",
    "takeaway": "12 minutes to build, 3 minutes to defend: architecture under real enterprise constraints.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 20)">
        <!-- Left Side: Scenario Architecture Flow -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="560" height="395" rx="8" class="swimlane-bg"/>
          <rect x="15" y="12" width="220" height="26" rx="4" fill="#1b2434"/>
          <text x="25" y="29" class="text-mono" font-size="12">WORKSHOP SCENARIO PIPELINE</text>

          <!-- Step 1: Ingestion -->
          <g transform="translate(20, 50)">
            <rect x="0" y="0" width="150" height="90" rx="6" class="node-box"/>
            {render_icon("document", 12, 10, size=20, color="#60a5fa")}
            <text x="36" y="25" class="text-h2">Input Claim</text>
            <text x="12" y="50" class="text-dim">Scanned medical bill</text>
            <text x="12" y="72" class="text-mono" font-size="11">PDF / Image JPEG</text>
          </g>

          <path d="M 180 95 L 205 95" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>

          <!-- Step 2: OCR Extraction -->
          <g transform="translate(215, 50)">
            <rect x="0" y="0" width="150" height="90" rx="6" class="node-box"/>
            {render_icon("tool", 12, 10, size=20, color="#6ee7b7")}
            <text x="36" y="25" class="text-h2">OCR Extract</text>
            <text x="12" y="50" class="text-dim">Dates, Codes, Total</text>
            <text x="12" y="72" class="text-mono-green" font-size="11">Multimodal / DocAI</text>
          </g>

          <path d="M 375 95 L 400 95" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Step 3: Policy Validation -->
          <g transform="translate(410, 50)">
            <rect x="0" y="0" width="130" height="90" rx="6" class="node-box-active"/>
            {render_icon("search", 12, 10, size=20, color="#e0c58e")}
            <text x="36" y="25" class="text-h2" fill="#e0c58e">Policy RAG</text>
            <text x="12" y="50" class="text-dim">Match coverage</text>
            <text x="12" y="72" class="text-mono-amber" font-size="11">Vector Policy DB</text>
          </g>

          <!-- Step 4: Anomaly Check -->
          <g transform="translate(20, 165)">
            <rect x="0" y="0" width="240" height="90" rx="6" class="node-box" stroke="#b4a4e5"/>
            {render_icon("brain_model", 12, 10, size=20, color="#b4a4e5")}
            <text x="36" y="25" class="text-h2" fill="#b4a4e5">Anomaly Reasoning</text>
            <text x="12" y="50" class="text-p">Flag billing outliers or duplicate codes</text>
            <text x="12" y="72" class="text-mono-purple" font-size="11">Frontier Model Synthesis</text>
          </g>

          <path d="M 270 210 L 305 210" stroke="#b4a4e5" stroke-width="1.8" fill="none" marker-end="url(#arr-purple)"/>

          <!-- Step 5: Human Review Gate -->
          <g transform="translate(315, 165)">
            <rect x="0" y="0" width="225" height="90" rx="6" class="node-box" stroke="#d98585"/>
            {render_icon("approval", 12, 10, size=20, color="#d98585")}
            <text x="36" y="25" class="text-h2" fill="#d98585">Human Review Gate</text>
            <text x="12" y="50" class="text-p">Confidence &lt; 90% triggers nurse queue</text>
            <text x="12" y="72" class="text-mono-coral" font-size="11">Zero Blind Auto-Payment</text>
          </g>

          <!-- Constraints Bar -->
          <g transform="translate(20, 275)">
            <rect x="0" y="0" width="520" height="100" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="14" y="22" class="text-mono" font-size="11">ENTERPRISE CONSTRAINTS</text>
            <text x="14" y="44" class="text-p">&bull; Strict HIPAA / GDPR: patient names &amp; diagnoses must be redacted.</text>
            <text x="14" y="66" class="text-p">&bull; Volume: 120,000 claims/month (peak between 8 AM and 4 PM).</text>
            <text x="14" y="88" class="text-p">&bull; Core IT system: Existing insurance claims DB runs on Microsoft Azure.</text>
          </g>
        </g>

        <!-- Right Side: Deliverables Scorecard -->
        <g transform="translate(585, 0)">
          <rect x="0" y="0" width="455" height="395" rx="8" class="node-box"/>
          <rect x="0" y="0" width="455" height="42" rx="8" fill="#1b2434"/>
          <text x="22" y="26" class="text-h1" fill="#e0c58e">Student Deliverable Scorecard</text>

          <g transform="translate(20, 55)">
            <!-- Item 1 -->
            <g transform="translate(0, 0)">
              <rect x="0" y="0" width="415" height="46" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="12" y="18" class="text-mono" font-size="11">1. END-TO-END ARCHITECTURE DIAGRAM</text>
              <text x="12" y="36" class="text-p">Clear separation of ingestion OCR vs online validation.</text>
            </g>

            <!-- Item 2 -->
            <g transform="translate(0, 54)">
              <rect x="0" y="0" width="415" height="46" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="12" y="18" class="text-mono-green" font-size="11">2. PLATFORM SELECTION &amp; RATIONALE</text>
              <text x="12" y="36" class="text-p">Concrete vendor choice defending data gravity &amp; identity.</text>
            </g>

            <!-- Item 3 -->
            <g transform="translate(0, 108)">
              <rect x="0" y="0" width="415" height="46" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="12" y="18" class="text-mono-purple" font-size="11">3. SECURITY &amp; PII BOUNDARIES</text>
              <text x="12" y="36" class="text-p">De-identification filters and customer-managed KMS keys.</text>
            </g>

            <!-- Item 4 -->
            <g transform="translate(0, 162)">
              <rect x="0" y="0" width="415" height="46" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="12" y="18" class="text-mono-amber" font-size="11">4. EVALUATION &amp; REGRESSION TEST SETS</text>
              <text x="12" y="36" class="text-p">Golden test sets for code extraction accuracy &amp; false claims.</text>
            </g>

            <!-- Item 5 -->
            <g transform="translate(0, 216)">
              <rect x="0" y="0" width="415" height="52" rx="4" fill="#24191d" stroke="#d98585" stroke-width="1.2"/>
              <text x="12" y="18" class="text-mono-coral" font-size="11">5. MANDATORY DISQUALIFIED ALTERNATIVE</text>
              <text x="12" y="38" class="text-p">Explicit technical rationale why another cloud was disqualified.</text>
            </g>

            <g transform="translate(0, 278)">
              <rect x="0" y="0" width="415" height="42" rx="4" fill="#172233" stroke="#3b82f6"/>
              <text x="207" y="26" text-anchor="middle" class="text-mono">Session: 12 min build &bull; 3 min defense</text>
            </g>
          </g>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Set up the student workshop. Have students design a multimodal medical claims assistant and defend it under enterprise constraints.",
        "talkTrack": "Set up the workshop. Students design a claims-processing assistant with PDF/image input, extracted fields, anomaly explanation, and human review. They have 12 minutes to build and 3 minutes to defend. Remind students that omitting security boundaries or failing to explain why an alternative cloud was disqualified will result in deductions: an executive recommendation requires trade-offs, boundaries, and explicit disqualifications.",
        "timing": "120:00 - 135:00 (15 min)"
    }
}
