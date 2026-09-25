# -*- coding: utf-8 -*-
slide_data = {
    "index": 17,
    "badge": "COST & LATENCY ANALYSIS",
    "title": "RAG vs Million-Token Context Windows: Economic Reality",
    "subtitle": "Why 1M+ context windows do not replace RAG for enterprise knowledge repositories.",
    "takeaway_tag": "ECONOMIC CURVE",
    "takeaway": "RAG is 700x cheaper and 25x faster than stuffing 1M tokens into frontier models for every query.",
    "notes": """
      <h4>Economic & Performance Realities</h4>
      <p>Compare costs: 1M tokens costs $3.50-$7.00 per query with 20s latency. RAG costs $0.005 with 800ms latency. Long context is for single large files; RAG is for enterprise scale.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: Long Context Brute Force -->
      <g transform="translate(40, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#d98585">STUFFING 1,000,000 TOKENS (BRUTE FORCE)</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10.5" fill="#d98585">Cost Per Single User Query:</text>
          <text x="12" y="44" class="text-mono-bold" font-size="13" fill="#d98585">$3.50 - $7.00 per query</text>

          <rect y="70" width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10.5" fill="#d98585">Time to First Token (TTFT):</text>
          <text x="12" y="44" class="text-mono-bold" font-size="13" fill="#d98585">15,000ms - 30,000ms (15-30s latency)</text>

          <rect y="140" width="320" height="75" rx="4" fill="#1b2434" stroke="#d98585"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10" fill="#d98585">Attention Quality:</text>
          <text x="12" y="40" class="text-p" font-size="9">- Severe needle-in-haystack degradation</text>
          <text x="12" y="54" class="text-p" font-size="9">- Confuses outdated policy versions in text</text>
          <text x="12" y="68" class="text-dim" font-size="8.5">10,000 daily queries = $35,000 - $70,000 / day</text>
        </g>
      </g>

      <!-- Right: Hybrid RAG Architecture -->
      <g transform="translate(460, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#6ee7b7">HYBRID ENTERPRISE RAG ARCHITECTURE</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">Cost Per Single User Query:</text>
          <text x="12" y="44" class="text-mono-bold" font-size="13" fill="#6ee7b7">$0.003 - $0.008 per query</text>

          <rect y="70" width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">Time to First Token (TTFT):</text>
          <text x="12" y="44" class="text-mono-bold" font-size="13" fill="#6ee7b7">400ms - 850ms (Sub-second streaming)</text>

          <rect y="140" width="320" height="75" rx="4" fill="#1b2434" stroke="#6ee7b7"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10" fill="#6ee7b7">Attention Quality:</text>
          <text x="12" y="40" class="text-p" font-size="9">+ Precise top-5 chunks focus model reasoning</text>
          <text x="12" y="54" class="text-p" font-size="9">+ Pre-filtered for current version and user ACL</text>
          <text x="12" y="68" class="text-mono" font-size="8.5" fill="#6ee7b7">10,000 daily queries = ~$50 / day (700x cheaper)</text>
        </g>
      </g>
    </svg>"""
}
