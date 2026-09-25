# -*- coding: utf-8 -*-
slide_data = {
    "index": 9,
    "badge": "ALGORITHMIC DEEP-DIVE",
    "title": "Vector Indexing: HNSW Multi-Layer Skip Graph",
    "subtitle": "Hierarchical Navigable Small World: Combining probabilistic skip-lists with proximity graphs.",
    "takeaway_tag": "HNSW ARCHITECTURE",
    "takeaway": "HNSW provides sub-5ms search: top sparse layers make long-range jumps, bottom layers route locally.",
    "notes": """
      <h4>HNSW Deep-Dive</h4>
      <p>Explain the multi-layer graph topology. Query starts at top entry point (Layer 2) with wide skips, then drops to Layer 1, and finishes in Layer 0 with fine-grained greedy routing.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Diagram Arena -->
      <g transform="translate(30, 25)">
        <rect width="800" height="300" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>

        <!-- Layer 2 (Top Sparse Layer) -->
        <g transform="translate(40, 25)">
          <rect width="720" height="65" rx="6" fill="#1b2434" stroke="#60a5fa" stroke-width="1"/>
          <text x="15" y="20" class="text-mono-bold" font-size="10.5" fill="#60a5fa">LAYER 2: SPARSE ENTRY HIGHWAY (Long-range jumps)</text>

          <circle cx="120" cy="40" r="8" fill="#60a5fa"/>
          <text x="120" y="44" text-anchor="middle" class="text-mono-bold" font-size="9" fill="#0e131b">EP</text>

          <line x1="128" y1="40" x2="380" y2="40" stroke="#60a5fa" stroke-width="2"/>

          <circle cx="380" cy="40" r="7" fill="#60a5fa"/>
          <circle cx="620" cy="40" r="7" fill="#334155"/>

          <line x1="387" y1="40" x2="613" y2="40" stroke="#334155" stroke-width="1.5" stroke-dasharray="3,3"/>

          <!-- Drop line to Layer 1 -->
          <path d="M 380 47 L 380 95" stroke="#e0c58e" stroke-width="2" stroke-dasharray="3,3"/>
        </g>

        <!-- Layer 1 (Intermediate Layer) -->
        <g transform="translate(40, 105)">
          <rect width="720" height="75" rx="6" fill="#1b2434" stroke="#b4a4e5" stroke-width="1"/>
          <text x="15" y="20" class="text-mono-bold" font-size="10.5" fill="#b4a4e5">LAYER 1: MEDIUM NAVIGATION GRAPH</text>

          <circle cx="100" cy="45" r="6" fill="#334155"/>
          <circle cx="220" cy="45" r="6" fill="#334155"/>
          <circle cx="380" cy="45" r="7" fill="#e0c58e"/>
          <circle cx="480" cy="45" r="7" fill="#b4a4e5"/>
          <circle cx="640" cy="45" r="6" fill="#334155"/>

          <line x1="106" y1="45" x2="214" y2="45" stroke="#334155" stroke-width="1"/>
          <line x1="226" y1="45" x2="373" y2="45" stroke="#334155" stroke-width="1"/>
          <line x1="387" y1="45" x2="473" y2="45" stroke="#b4a4e5" stroke-width="2"/>
          <line x1="487" y1="45" x2="634" y2="45" stroke="#334155" stroke-width="1"/>

          <!-- Drop line to Layer 0 -->
          <path d="M 480 52 L 480 100" stroke="#6ee7b7" stroke-width="2" stroke-dasharray="3,3"/>
        </g>

        <!-- Layer 0 (Bottom Dense All-Nodes Layer) -->
        <g transform="translate(40, 195)">
          <rect width="720" height="90" rx="6" fill="#0e131b" stroke="#6ee7b7" stroke-width="1.2"/>
          <text x="15" y="20" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">LAYER 0: ALL VECTORS (Dense Proximity Graph)</text>

          <!-- Nodes -->
          <circle cx="80" cy="55" r="5" fill="#334155"/>
          <circle cx="160" cy="55" r="5" fill="#334155"/>
          <circle cx="260" cy="55" r="5" fill="#334155"/>
          <circle cx="360" cy="55" r="5" fill="#334155"/>
          <circle cx="480" cy="55" r="7" fill="#6ee7b7"/>
          <circle cx="530" cy="40" r="7" fill="#6ee7b7"/>
          <circle cx="550" cy="65" r="8" fill="#6ee7b7" stroke="#fff" stroke-width="2"/>
          <circle cx="650" cy="55" r="5" fill="#334155"/>

          <!-- Routing Path in Layer 0 -->
          <line x1="487" y1="52" x2="523" y2="42" stroke="#6ee7b7" stroke-width="2"/>
          <line x1="535" y1="45" x2="547" y2="60" stroke="#6ee7b7" stroke-width="2.5"/>

          <text x="565" y="70" class="text-mono-bold" font-size="11" fill="#6ee7b7">Nearest Match (k=1)</text>
        </g>
      </g>
    </svg>"""
}
