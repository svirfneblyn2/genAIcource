# Slide 06: Running Case: Internal IT Support Assistant
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 6,
    "kicker": "REFERENCE WORKLOAD",
    "title": "The Benchmark Case: Grounded Policy Assistant",
    "lead": "A single real-world workload that exposes every critical enterprise boundary.",
    "section": "Reference Workload",
    "takeaway": "Even a simple policy FAQ triggers RAG, IAM, action approval gates, tracing, and billing.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 20)">
        <!-- Top: User interaction box -->
        <rect x="0" y="0" width="1040" height="110" rx="8" class="node-box-active"/>
        <rect x="15" y="14" width="490" height="82" rx="6" fill="#141c28" stroke="#253245"/>
        {render_icon("user", 25, 24, size=22, color="#60a5fa")}
        <text x="56" y="38" class="text-mono">USER QUERY (Sarah, Engineering):</text>
        <text x="56" y="66" class="text-h1" font-size="15">"How long can I borrow a laptop, and where do I collect it?"</text>
        <text x="56" y="86" class="text-dim">Context: Needs loaner equipment for client deployment</text>

        <path d="M 515 55 L 540 55" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

        <rect x="550" y="14" width="475" height="82" rx="6" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
        {render_icon("chat", 560, 24, size=22, color="#6ee7b7")}
        <text x="590" y="38" class="text-mono-green">GROUNDED ASSISTANT RESPONSE:</text>
        <text x="590" y="64" class="text-p">"Standard loans are up to 14 days. Collect at IT Helpdesk B2."</text>
        <text x="590" y="86" class="text-mono-amber" font-size="11">Citation: Equipment Loan Policy (2025 rev), Section 2.1</text>
      </g>

      <!-- Bottom: The 4 Enterprise Boundary Gates -->
      <g transform="translate(40, 150)">
        <!-- Gate 1: Grounding & Citation -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="245" height="245" rx="8" class="node-box"/>
          <rect x="0" y="0" width="245" height="40" rx="8" fill="#1b2434"/>
          {render_icon("document", 12, 10, size=20, color="#60a5fa")}
          <text x="40" y="26" class="text-h2" fill="#60a5fa">Rule 1: Grounded Citation</text>
          
          <text x="16" y="65" class="text-h2">No Evidence = No Answer</text>
          <text x="16" y="90" class="text-p">Must cite exact document name, section number, and revision date.</text>
          <text x="16" y="130" class="text-p">Pure parametric model knowledge is explicitly forbidden.</text>
          
          <rect x="14" y="185" width="217" height="45" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="24" y="205" class="text-mono" font-size="11">FAIL CONDITION</text>
          <text x="24" y="221" class="text-dim">Hallucinated collection hours</text>
        </g>

        <!-- Gate 2: Access Control -->
        <g transform="translate(265, 0)">
          <rect x="0" y="0" width="245" height="245" rx="8" class="node-box"/>
          <rect x="0" y="0" width="245" height="40" rx="8" fill="#1b2434"/>
          {render_icon("shield", 12, 10, size=20, color="#6ee7b7")}
          <text x="40" y="26" class="text-h2" fill="#6ee7b7">Rule 2: Identity &amp; ACLs</text>
          
          <text x="16" y="65" class="text-h2">Role-Based Trimming</text>
          <text x="16" y="90" class="text-p">Assistant can only search documents user has permission to read.</text>
          <text x="16" y="130" class="text-p">Enforces Entra ID / IAM groups prior to LLM prompt injection.</text>
          
          <rect x="14" y="185" width="217" height="45" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="24" y="205" class="text-mono-green" font-size="11">SECURITY CHECK</text>
          <text x="24" y="221" class="text-dim">Pass JWT claims to vector filter</text>
        </g>

        <!-- Gate 3: Ticket Approval Gate -->
        <g transform="translate(530, 0)">
          <rect x="0" y="0" width="245" height="245" rx="8" class="node-box"/>
          <rect x="0" y="0" width="245" height="40" rx="8" fill="#1b2434"/>
          {render_icon("ticket", 12, 10, size=20, color="#e0c58e")}
          <text x="40" y="26" class="text-h2" fill="#e0c58e">Rule 3: Action Approval</text>
          
          <text x="16" y="65" class="text-h2">Human Confirmation</text>
          <text x="16" y="90" class="text-p">Can draft a ServiceNow ticket, but cannot submit autonomously.</text>
          <text x="16" y="130" class="text-p">Requires explicit user UI confirmation before API POST execution.</text>
          
          <rect x="14" y="185" width="217" height="45" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="24" y="205" class="text-mono-amber" font-size="11">APPROVAL GATE</text>
          <text x="24" y="221" class="text-dim">Prevents unintended actions</text>
        </g>

        <!-- Gate 4: Audit & Tracing -->
        <g transform="translate(795, 0)">
          <rect x="0" y="0" width="245" height="245" rx="8" class="node-box"/>
          <rect x="0" y="0" width="245" height="40" rx="8" fill="#1b2434"/>
          {render_icon("monitoring", 12, 10, size=20, color="#b4a4e5")}
          <text x="40" y="26" class="text-h2" fill="#b4a4e5">Rule 4: Audit &amp; Trace</text>
          
          <text x="16" y="65" class="text-h2">Zero Black-Box Runs</text>
          <text x="16" y="90" class="text-p">Full trace captured: prompt, retrieved chunks, token count, latency.</text>
          <text x="16" y="130" class="text-p">Logged to centralized observability for compliance and regression evals.</text>
          
          <rect x="14" y="185" width="217" height="45" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="24" y="205" class="text-mono-purple" font-size="11">OTEL AUDIT LOG</text>
          <text x="24" y="221" class="text-dim">Immutable compliance store</text>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Read the support question aloud. Walk through expected assistant behavior and demonstrate how this simple case forces the hard enterprise questions.",
        "talkTrack": "Read the support question aloud. Then walk through the expected assistant behavior. Emphasize that the same simple case already contains the hard questions: citation, permissions, action approval, traceability, evaluation, and cost. By sticking to this single concrete case across all three cloud platforms, we eliminate marketing hand-waving and focus strictly on system architecture.",
        "timing": "25:00 - 30:00 (5 min)"
    }
}
