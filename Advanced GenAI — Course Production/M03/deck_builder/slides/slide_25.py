# -*- coding: utf-8 -*-
slide_data = {
    "index": 25,
    "badge": "PRACTICAL WORKSHOP",
    "title": "Hands-On Workshop: Enterprise Policy Assistant",
    "subtitle": "Building and defending a grounded retrieval system under strict enterprise constraints.",
    "takeaway_tag": "WORKSHOP BRIEF",
    "takeaway": "Design under real constraints: role-based access filtering, hybrid search, and citation grounding.",
    "notes": """
      <h4>Workshop Instructions</h4>
      <p>Students have 15 minutes to design or implement the policy assistant. Two tracks available: Track A (Architecture & Evaluation Plan) and Track B (Python Code Prototype with zero-cost guarantee).</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: Scenario Description -->
      <g transform="translate(40, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#60a5fa">WORKSHOP SCENARIO: APEX GLOBAL</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="65" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10" fill="#e0c58e">Enterprise Workload:</text>
          <text x="12" y="38" class="text-p" font-size="9.5">Corporate IT &amp; HR Policy Knowledge Base</text>
          <text x="12" y="52" class="text-dim" font-size="9">18,000 employees across 14 global offices</text>

          <rect y="75" width="320" height="135" rx="4" fill="#1b2434" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10" fill="#f8fafc">4 Core Engineering Constraints:</text>
          <text x="12" y="40" class="text-p" font-size="9">1. Zero Role Leakage: Interns cannot read executive perks</text>
          <text x="12" y="58" class="text-p" font-size="9">2. Alphanumeric Search: Matches exact room 'B12' and codes</text>
          <text x="12" y="76" class="text-p" font-size="9">3. Mandatory Grounding: Inline [Source: ID § Sec] tags</text>
          <text x="12" y="94" class="text-p" font-size="9">4. Explicit Refusal: Refuse out-of-domain questions cleanly</text>
          <text x="12" y="116" class="text-mono" font-size="8.5" fill="#6ee7b7">Evaluation: Tested against 10 golden queries</text>
        </g>
      </g>

      <!-- Right: Deliverables -->
      <g transform="translate(460, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#6ee7b7">CHOOSE YOUR TRACK (100-POINT RUBRIC)</text>

        <g transform="translate(20, 50)">
          <!-- Track A -->
          <rect width="320" height="95" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10.5" fill="#60a5fa">Track A: Architecture &amp; Evaluation</text>
          <text x="12" y="40" class="text-p" font-size="9">- Complete Mermaid.js topology diagram</text>
          <text x="12" y="56" class="text-p" font-size="9">- Chunking &amp; metadata pre-filtering schema</text>
          <text x="12" y="72" class="text-p" font-size="9">- Ragas automated evaluation specification</text>
          <text x="12" y="86" class="text-dim" font-size="8.5">Ideal for System Architects &amp; Tech Leads (No coding)</text>

          <!-- Track B -->
          <rect y="105" width="320" height="95" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">Track B: Working Python Prototype</text>
          <text x="12" y="40" class="text-p" font-size="9">- Working local script (NumPy or ChromaDB)</text>
          <text x="12" y="56" class="text-p" font-size="9">- Role-based ACL pre-filter + BM25 hybrid fusion</text>
          <text x="12" y="72" class="text-p" font-size="9">- Grounded prompt synthesis &amp; refusal path</text>
          <text x="12" y="86" class="text-mono" font-size="8.5" fill="#6ee7b7">100% Zero-cost guarantee (local execution)</text>
        </g>
      </g>
    </svg>"""
}
