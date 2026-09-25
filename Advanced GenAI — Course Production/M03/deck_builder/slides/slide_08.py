# -*- coding: utf-8 -*-
slide_data = {
    "index": 8,
    "badge": "SEARCH COMPLEXITY",
    "title": "Similarity Search: Exact kNN vs Approximate Nearest Neighbors",
    "subtitle": "Trading 1% recall for orders-of-magnitude reduction in latency and compute complexity.",
    "takeaway_tag": "ANN COMPLEXITY",
    "takeaway": "At scale, exact kNN search O(N·d) is cost-prohibitive: enterprise search requires O(log N) ANN.",
    "notes": """
      <h4>Complexity Comparison</h4>
      <p>Show the math: 10M vectors at 1536 dims burns 15.3 billion FLOPS for a single query in exact search. ANN with HNSW drops latency from seconds to 3-5 milliseconds.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: Exact kNN -->
      <g transform="translate(40, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono" font-size="11" fill="#d98585">EXACT SEARCH (FLAT / BRUTE-FORCE)</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="24" class="text-mono" font-size="10.5" fill="#94a3b8">Computational Complexity:</text>
          <text x="14" y="48" class="text-mono-bold" font-size="14" fill="#d98585">O( N · d )</text>

          <rect y="70" width="320" height="75" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="90" class="text-mono" font-size="10" fill="#60a5fa">Benchmark on 10,000,000 Vectors:</text>
          <text x="14" y="110" class="text-p" font-size="9.5">10,000,000 × 1536 dims = 15.36 Billion Ops</text>
          <text x="14" y="128" class="text-dim" font-size="9">Query Latency: 2,500ms - 8,000ms per call</text>

          <rect y="155" width="320" height="65" rx="4" fill="#1b2434" stroke="#d98585"/>
          <text x="14" y="178" class="text-mono-bold" font-size="10.5" fill="#d98585">Trade-off Profile:</text>
          <text x="14" y="196" class="text-p" font-size="9.5">+ 100% Exact Recall (No false negatives)</text>
          <text x="14" y="210" class="text-dim" font-size="8.5">- Completely unusable for interactive user applications</text>
        </g>
      </g>

      <!-- Right: Approximate Nearest Neighbors (ANN) -->
      <g transform="translate(460, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono" font-size="11" fill="#6ee7b7">APPROXIMATE NEAREST NEIGHBORS (ANN)</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="24" class="text-mono" font-size="10.5" fill="#94a3b8">Search Complexity (HNSW):</text>
          <text x="14" y="48" class="text-mono-bold" font-size="14" fill="#6ee7b7">O( log N )</text>

          <rect y="70" width="320" height="75" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="90" class="text-mono" font-size="10" fill="#6ee7b7">Benchmark on 10,000,000 Vectors:</text>
          <text x="14" y="110" class="text-p" font-size="9.5">Inspects only ~500 to 2,000 candidate nodes</text>
          <text x="14" y="128" class="text-mono" font-size="9" fill="#6ee7b7">Query Latency: 2ms - 8ms per call</text>

          <rect y="155" width="320" height="65" rx="4" fill="#1b2434" stroke="#6ee7b7"/>
          <text x="14" y="178" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">Production Viability:</text>
          <text x="14" y="196" class="text-p" font-size="9.5">+ 98% - 99.5% Empirical Recall</text>
          <text x="14" y="210" class="text-dim" font-size="8.5">+ Enables sub-second interactive RAG pipelines</text>
        </g>
      </g>
    </svg>"""
}
