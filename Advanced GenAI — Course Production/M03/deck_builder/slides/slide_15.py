# -*- coding: utf-8 -*-
slide_data = {
    "index": 15,
    "badge": "CONTEXT ARCHITECTURE",
    "title": "Context Window Assembly: The 'Lost in the Middle' Phenomenon",
    "subtitle": "How transformer attention decay shapes evidence positioning within prompt budgets.",
    "takeaway_tag": "BOUNDARY RULES",
    "takeaway": "Position critical evidence at prompt boundaries: anchor output schemas at the absolute end.",
    "notes": """
      <h4>Attention U-Curve</h4>
      <p>Explain the Stanford empirical finding: facts in the center of long prompts suffer 30-50% retrieval drop. Mitigate by pinning high-scoring chunks to the top (Primacy) and schema rules to the bottom (Recency).</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: Stanford Attention Curve -->
      <g transform="translate(30, 30)">
        <rect width="380" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="380" height="34" rx="8" fill="#1b2434"/>
        <text x="190" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#60a5fa">EMPIRICAL RETRIEVAL ACCURACY VS POSITION</text>

        <!-- The U Curve Graph -->
        <g transform="translate(45, 230)">
          <line x1="0" y1="0" x2="300" y2="0" stroke="#364761" stroke-width="1.5"/>
          <line x1="0" y1="0" x2="0" y2="-150" stroke="#364761" stroke-width="1.5"/>
          <line x1="0" y1="-120" x2="300" y2="-120" stroke="#253245" stroke-dasharray="2,2"/>
          <line x1="0" y1="-60" x2="300" y2="-60" stroke="#253245" stroke-dasharray="2,2"/>

          <text x="-10" y="-115" text-anchor="end" class="text-mono" font-size="8.5" fill="#64748b">80%</text>
          <text x="-10" y="-55" text-anchor="end" class="text-mono" font-size="8.5" fill="#64748b">40%</text>

          <path d="M 0 -130 C 60 -125, 90 -40, 150 -40 C 210 -40, 240 -120, 300 -125" fill="none" stroke="#60a5fa" stroke-width="3"/>

          <circle cx="15" cy="-128" r="5" fill="#6ee7b7"/>
          <text x="15" y="-140" text-anchor="middle" class="text-mono-bold" font-size="9" fill="#6ee7b7">Primacy: 92%</text>

          <circle cx="150" cy="-40" r="5" fill="#d98585"/>
          <text x="150" y="-20" text-anchor="middle" class="text-mono-bold" font-size="9" fill="#d98585">Middle Trough: ~38%</text>

          <circle cx="285" cy="-124" r="5" fill="#6ee7b7"/>
          <text x="285" y="-136" text-anchor="middle" class="text-mono-bold" font-size="9" fill="#6ee7b7">Recency: 89%</text>

          <text x="15" y="16" class="text-dim" font-size="8.5">0% (Prompt Start)</text>
          <text x="150" y="16" text-anchor="middle" class="text-dim" font-size="8.5">50% (Center)</text>
          <text x="285" y="16" text-anchor="end" class="text-dim" font-size="8.5">100% (End)</text>
        </g>
      </g>

      <!-- Right: Boundary Assembly Strategy -->
      <g transform="translate(430, 30)">
        <rect width="400" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="400" height="34" rx="8" fill="#1b2434"/>
        <text x="200" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#6ee7b7">BOUNDARY ENGINEERING RULES</text>

        <g transform="translate(20, 50)">
          <rect width="360" height="58" rx="4" fill="#1b2434" stroke="#6ee7b7" stroke-width="1.2"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">1. Pin Primary Evidence to Start (Primacy)</text>
          <text x="12" y="36" class="text-p" font-size="9.5">Put highest-scoring Reranker chunks (#1, #2) at the top</text>
          <text x="12" y="50" class="text-dim" font-size="8.5">Benefits from maximum initial attention allocation</text>

          <rect y="68" width="360" height="58" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10.5" fill="#e0c58e">2. Neutral Middle Chunk Space</text>
          <text x="12" y="36" class="text-p" font-size="9.5">Auxiliary background or secondary reference context</text>
          <text x="12" y="50" class="text-dim" font-size="8.5">Avoid placing critical security/action rules here</text>

          <rect y="136" width="360" height="58" rx="4" fill="#1b2434" stroke="#60a5fa" stroke-width="1.2"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10.5" fill="#60a5fa">3. Pin Task &amp; Citations to End (Recency)</text>
          <text x="12" y="36" class="text-p" font-size="9.5">Re-state prompt instructions, output schema, and query</text>
          <text x="12" y="50" class="text-dim" font-size="8.5">Direct proximity to the first autoregressive generation token</text>
        </g>
      </g>
    </svg>"""
}
