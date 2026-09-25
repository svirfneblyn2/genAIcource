# Slide 04: The Proven Enterprise Learning Pattern
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 4,
    "kicker": "PEDAGOGICAL METHOD",
    "title": "The 4-Phase System Design Flow",
    "lead": "Reusing official cloud architecture training methodology: Concept to Decision.",
    "section": "Learning Methodology",
    "takeaway": "Avoid loose catalog tours: anchor every service in a concrete system responsibility.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 35)">
        <!-- Step 1: Concept -->
        <rect x="0" y="0" width="240" height="380" rx="8" class="node-box"/>
        <rect x="0" y="0" width="240" height="46" rx="8" fill="#1b2434"/>
        <text x="24" y="29" class="text-mono" font-size="14" fill="#60a5fa">PHASE 01</text>
        <text x="120" y="29" class="text-h1">Concept</text>
        
        <g transform="translate(18, 65)">
          {render_icon("brain_model", 0, 0, size=24, color="#60a5fa")}
          <text x="34" y="18" class="text-h2">Mental Model</text>
          <text x="0" y="45" class="text-p">Define the workload contract</text>
          <text x="0" y="68" class="text-p">Establish security perimeter</text>
          <text x="0" y="91" class="text-p">Separate ingestion &amp; inference</text>
          <text x="0" y="114" class="text-p">Human in the loop gates</text>
          
          <g transform="translate(0, 135)">
            <rect x="0" y="0" width="204" height="150" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="12" y="26" class="text-mono" font-size="11">KEY DELIVERABLE</text>
            <text x="12" y="52" class="text-p">Two-lane architecture</text>
            <text x="12" y="74" class="text-p">Grounded SLA definition</text>
            <text x="12" y="96" class="text-p">Strict permission policy</text>
            <text x="12" y="128" class="text-dim">Neutral foundation</text>
          </g>
        </g>
      </g>

      <path d="M 295 210 L 325 210" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

      <g transform="translate(335, 35)">
        <!-- Step 2: Capability Map -->
        <rect x="0" y="0" width="240" height="380" rx="8" class="node-box"/>
        <rect x="0" y="0" width="240" height="46" rx="8" fill="#1b2434"/>
        <text x="24" y="29" class="text-mono" font-size="14" fill="#6ee7b7">PHASE 02</text>
        <text x="120" y="29" class="text-h1">Capability Map</text>
        
        <g transform="translate(18, 65)">
          {render_icon("search", 0, 0, size=24, color="#6ee7b7")}
          <text x="34" y="18" class="text-h2">The 6 Pillars</text>
          <text x="0" y="45" class="text-p">Group vendor services</text>
          <text x="0" y="68" class="text-p">Models &amp; Model Garden</text>
          <text x="0" y="91" class="text-p">Knowledge &amp; Hybrid Search</text>
          <text x="0" y="114" class="text-p">Agents, Evals &amp; Observability</text>
          
          <g transform="translate(0, 135)">
            <rect x="0" y="0" width="204" height="150" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="12" y="26" class="text-mono-green" font-size="11">STANDARDIZATION</text>
            <text x="12" y="52" class="text-p">Platform capability matrix</text>
            <text x="12" y="74" class="text-p">Service classification</text>
            <text x="12" y="96" class="text-p">Bypass marketing hype</text>
            <text x="12" y="128" class="text-dim">Universal language</text>
          </g>
        </g>
      </g>

      <path d="M 590 210 L 620 210" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>

      <g transform="translate(630, 35)">
        <!-- Step 3: Guided Build -->
        <rect x="0" y="0" width="240" height="380" rx="8" class="node-box"/>
        <rect x="0" y="0" width="240" height="46" rx="8" fill="#1b2434"/>
        <text x="24" y="29" class="text-mono" font-size="14" fill="#b4a4e5">PHASE 03</text>
        <text x="120" y="29" class="text-h1">Guided Build</text>
        
        <g transform="translate(18, 65)">
          {render_icon("tool", 0, 0, size=24, color="#b4a4e5")}
          <text x="34" y="18" class="text-h2">1 Workload &times; 3 Clouds</text>
          <text x="0" y="45" class="text-p">AWS Bedrock implementation</text>
          <text x="0" y="68" class="text-p">Azure Foundry implementation</text>
          <text x="0" y="91" class="text-p">Google Cloud implementation</text>
          <text x="0" y="114" class="text-p">Map concrete endpoints</text>
          
          <g transform="translate(0, 135)">
            <rect x="0" y="0" width="204" height="150" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="12" y="26" class="text-mono-purple" font-size="11">SYSTEM VERIFICATION</text>
            <text x="12" y="52" class="text-p">Console topology translation</text>
            <text x="12" y="74" class="text-p">VPC &amp; IAM boundaries</text>
            <text x="12" y="96" class="text-p">Action gate wiring</text>
            <text x="12" y="128" class="text-dim">Equal business contract</text>
          </g>
        </g>
      </g>

      <path d="M 885 210 L 915 210" stroke="#b4a4e5" stroke-width="2" fill="none" marker-end="url(#arr-purple)"/>

      <g transform="translate(925, 35)">
        <!-- Step 4: Decision -->
        <rect x="0" y="0" width="240" height="380" rx="8" class="node-box-active" stroke="#e0c58e"/>
        <rect x="0" y="0" width="240" height="46" rx="8" fill="#2d2516"/>
        <text x="24" y="29" class="text-mono" font-size="14" fill="#e0c58e">PHASE 04</text>
        <text x="120" y="29" class="text-h1">Decision</text>
        
        <g transform="translate(18, 65)">
          {render_icon("approval", 0, 0, size=24, color="#e0c58e")}
          <text x="34" y="18" class="text-h2">Defense Framework</text>
          <text x="0" y="45" class="text-p">5-question rubric</text>
          <text x="0" y="68" class="text-p">Full bill monthly TCO</text>
          <text x="0" y="91" class="text-p">Operational team profile</text>
          <text x="0" y="114" class="text-p">Rejected alternative defense</text>
          
          <g transform="translate(0, 135)">
            <rect x="0" y="0" width="204" height="150" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="12" y="26" class="text-mono-amber" font-size="11">EXECUTIVE OUTPUT</text>
            <text x="12" y="52" class="text-p">Defensible recommendation</text>
            <text x="12" y="74" class="text-p">Documented trade-offs</text>
            <text x="12" y="96" class="text-p">Disqualified vendor proof</text>
            <text x="12" y="128" class="text-dim">Boardroom ready</text>
          </g>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Explain the 4-phase learning pattern used in rigorous cloud architecture training: Concept, Capability Map, Guided Build, Decision.",
        "talkTrack": "Explain the training pattern used in strong cloud learning material: first concept, then capability map, then guided build, then decision. Say that this is the structure of the lecture. By avoiding a catalog tour, we anchor every service in a real architectural responsibility and give you the skills to defend your choice under scrutiny.",
        "timing": "15:00 - 20:00 (5 min)"
    }
}
