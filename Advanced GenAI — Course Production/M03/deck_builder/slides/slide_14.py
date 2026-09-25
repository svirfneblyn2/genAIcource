# -*- coding: utf-8 -*-
slide_data = {
    "index": 14,
    "badge": "TWO-STAGE RETRIEVAL",
    "title": "Cross-Encoder Reranking: Two-Stage Pipeline Precision",
    "subtitle": "Combining ultra-fast bi-encoder candidate retrieval with full cross-attention scoring.",
    "takeaway_tag": "RERANKING GAINS",
    "takeaway": "Bi-encoders fetch top-50 candidates in 15ms: a cross-encoder scores full joint attention to pick top-5.",
    "notes": """
      <h4>Two-Stage Retrieval</h4>
      <p>Bi-encoders encode query and document independently (fast, vector dot-product). Cross-encoders concatenate query + document into a single transformer with full cross-attention (slow, but captures deep token interactions).</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr-green" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
          <polygon points="0 0, 8 3, 0 6" fill="#6ee7b7"/>
        </marker>
      </defs>

      <!-- Stage 1 Box: Bi-Encoder Candidate Retrieval -->
      <g transform="translate(40, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#60a5fa">STAGE 1: BI-ENCODER (HIGH RECALL)</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="50" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono" font-size="10" fill="#60a5fa">Architecture: Dual Independent Towers</text>
          <text x="12" y="36" class="text-p" font-size="9.5">Vector(Query) · Vector(Document)</text>

          <rect y="60" width="320" height="55" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="22" class="text-mono" font-size="10" fill="#f8fafc">Latency &amp; Throughput:</text>
          <text x="12" y="42" class="text-mono" font-size="10" fill="#6ee7b7">Latency: ~10ms - 20ms | Scans Millions</text>

          <rect y="125" width="320" height="70" rx="4" fill="#1b2434" stroke="#60a5fa"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10.5" fill="#60a5fa">First-Stage Output:</text>
          <text x="12" y="38" class="text-p" font-size="9.5">Retrieves Top-50 candidates with high recall</text>
          <text x="12" y="54" class="text-dim" font-size="8.5">Misses subtle multi-sentence syntactic nuances</text>
        </g>
      </g>

      <!-- Center Transition Arrow -->
      <path d="M 405 175 L 450 175" stroke="#6ee7b7" stroke-width="2" marker-end="url(#arr-green)"/>
      <text x="428" y="165" text-anchor="middle" class="text-mono" font-size="9" fill="#6ee7b7">Top-50</text>

      <!-- Stage 2 Box: Cross-Encoder Precision Reranker -->
      <g transform="translate(460, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#6ee7b7">STAGE 2: CROSS-ENCODER (HIGH PRECISION)</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="50" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono" font-size="10" fill="#6ee7b7">Architecture: Joint Transformer Attention</text>
          <text x="12" y="36" class="text-p" font-size="9.5">Softmax( [Query ; Document] )</text>

          <rect y="60" width="320" height="55" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="22" class="text-mono" font-size="10" fill="#f8fafc">Latency &amp; Throughput:</text>
          <text x="12" y="42" class="text-mono" font-size="10" fill="#e0c58e">Latency: ~30ms - 50ms | Top-50 Pairs Only</text>

          <rect y="125" width="320" height="70" rx="4" fill="#1b2434" stroke="#6ee7b7"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">Final High-Precision Output:</text>
          <text x="12" y="38" class="text-p" font-size="9.5">Selects Top-5 highest confidence chunks</text>
          <text x="12" y="54" class="text-dim" font-size="8.5">NDCG@5 improves by +18% to +34% across benchmarks</text>
        </g>
      </g>
    </svg>"""
}
