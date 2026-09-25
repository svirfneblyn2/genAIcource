# -*- coding: utf-8 -*-
slide_data = {
    "index": 3,
    "badge": "DIAGNOSTIC FOUNDATION",
    "title": "The Hook: The Generative Model Can Be Innocent",
    "subtitle": "Over 75% of production RAG defects originate in data retrieval, not in model weights.",
    "takeaway_tag": "ROOT CAUSE ANALYSIS",
    "takeaway": "Do not tune prompts to fix bad retrieval: fix chunk freshness, parsing, and index filtering.",
    "notes": """
      <h4>Pedagogical Focus</h4>
      <p>Demonstrate that the same model with the same temperature will hallucinate or answer accurately depending strictly on the context fed to it.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-red" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
          <polygon points="0 0, 8 3, 0 6" fill="#d98585"/>
        </marker>
        <marker id="arr-green" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
          <polygon points="0 0, 8 3, 0 6" fill="#6ee7b7"/>
        </marker>
        <marker id="arr-blue" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
          <polygon points="0 0, 8 3, 0 6" fill="#60a5fa"/>
        </marker>
      </defs>

      <!-- Center Query -->
      <g transform="translate(30, 20)">
        <rect width="800" height="42" rx="6" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <text x="20" y="26" class="text-mono" font-size="12" fill="#60a5fa">User Query:</text>
        <text x="115" y="26" class="text-h1" font-size="12.5" fill="#f8fafc">"How many days can an employee borrow an emergency replacement laptop?"</text>
      </g>

      <!-- Scenario A: Stale Context -->
      <g transform="translate(30, 80)">
        <rect width="250" height="235" rx="6" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
        <rect width="250" height="30" rx="6" fill="#1b2434"/>
        <text x="125" y="20" text-anchor="middle" class="text-mono" font-size="11" fill="#d98585">SCENARIO A: STALE RETRIEVAL</text>

        <rect x="15" y="42" width="220" height="52" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="25" y="62" class="text-mono" font-size="10" fill="#d98585">Retrieved Chunk (v1.2):</text>
        <text x="25" y="78" class="text-p" font-size="10">"Hardware loan limit: 7 days"</text>

        <path d="M 125 100 L 125 125" stroke="#d98585" stroke-width="1.2" marker-end="url(#arr-red)"/>

        <rect x="15" y="132" width="220" height="46" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="25" y="152" class="text-mono" font-size="10" fill="#60a5fa">Inference Engine:</text>
        <text x="25" y="166" class="text-dim" font-size="9">Temperature = 0.0</text>

        <path d="M 125 184 L 125 198" stroke="#d98585" stroke-width="1.2" marker-end="url(#arr-red)"/>

        <rect x="15" y="202" width="220" height="24" rx="4" fill="#1b2434"/>
        <text x="125" y="218" text-anchor="middle" class="text-mono" font-size="10.5" fill="#d98585">Output: "7 calendar days" (FALSE)</text>
      </g>

      <!-- Scenario B: Accurate Context -->
      <g transform="translate(305, 80)">
        <rect width="250" height="235" rx="6" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
        <rect width="250" height="30" rx="6" fill="#1b2434"/>
        <text x="125" y="20" text-anchor="middle" class="text-mono" font-size="11" fill="#6ee7b7">SCENARIO B: FRESH RETRIEVAL</text>

        <rect x="15" y="42" width="220" height="52" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="25" y="62" class="text-mono" font-size="10" fill="#6ee7b7">Retrieved Chunk (v2.4):</text>
        <text x="25" y="78" class="text-p" font-size="10">"Hardware loan limit: 14 days"</text>

        <path d="M 125 100 L 125 125" stroke="#6ee7b7" stroke-width="1.2" marker-end="url(#arr-green)"/>

        <rect x="15" y="132" width="220" height="46" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="25" y="152" class="text-mono" font-size="10" fill="#60a5fa">Inference Engine:</text>
        <text x="25" y="166" class="text-dim" font-size="9">Same Model &amp; Prompt</text>

        <path d="M 125 184 L 125 198" stroke="#6ee7b7" stroke-width="1.2" marker-end="url(#arr-green)"/>

        <rect x="15" y="202" width="220" height="24" rx="4" fill="#1b2434"/>
        <text x="125" y="218" text-anchor="middle" class="text-mono" font-size="10.5" fill="#6ee7b7">Output: "14 calendar days" (TRUE)</text>
      </g>

      <!-- Scenario C: Missing Context -->
      <g transform="translate(580, 80)">
        <rect width="250" height="235" rx="6" fill="#141c28" stroke="#60a5fa" stroke-width="1.2"/>
        <rect width="250" height="30" rx="6" fill="#1b2434"/>
        <text x="125" y="20" text-anchor="middle" class="text-mono" font-size="11" fill="#60a5fa">SCENARIO C: SAFE REFUSAL</text>

        <rect x="15" y="42" width="220" height="52" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="25" y="62" class="text-mono" font-size="10" fill="#e0c58e">Retrieval Result:</text>
        <text x="25" y="78" class="text-dim" font-size="10">No matching chunks above threshold</text>

        <path d="M 125 100 L 125 125" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr-blue)"/>

        <rect x="15" y="132" width="220" height="46" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="25" y="152" class="text-mono" font-size="10" fill="#60a5fa">Grounded Guardrail:</text>
        <text x="25" y="166" class="text-dim" font-size="9">Enforces explicit refusal</text>

        <path d="M 125 184 L 125 198" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr-blue)"/>

        <rect x="15" y="202" width="220" height="24" rx="4" fill="#1b2434"/>
        <text x="125" y="218" text-anchor="middle" class="text-mono" font-size="10" fill="#6ee7b7">"Insufficient policy evidence" (SAFE)</text>
      </g>
    </svg>"""
}
