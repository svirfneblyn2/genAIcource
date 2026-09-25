# -*- coding: utf-8 -*-
slide_data = {
    "index": 13,
    "badge": "RANKING MECHANICS",
    "title": "Hybrid Fusion: Reciprocal Rank Fusion (RRF)",
    "subtitle": "Combining disparate score distributions into a single mathematically calibrated ranking.",
    "takeaway_tag": "FUSION FORMULA",
    "takeaway": "Reciprocal Rank Fusion (k=60) merges sparse and dense rankings without score normalization.",
    "notes": """
      <h4>RRF Mathematics</h4>
      <p>Explain why we cannot simply add BM25 scores (0 to inf) and Cosine scores (-1 to 1). RRF uses ordinal rank positions with smoothing constant k=60, making it immune to scale calibration issues.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
          <polygon points="0 0, 8 3, 0 6" fill="#60a5fa"/>
        </marker>
      </defs>

      <!-- Left: Two Streams -->
      <g transform="translate(30, 30)">
        <!-- Stream 1: Dense -->
        <rect width="260" height="135" rx="6" fill="#141c28" stroke="#b4a4e5" stroke-width="1.2"/>
        <rect width="260" height="28" rx="6" fill="#1b2434"/>
        <text x="130" y="19" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#b4a4e5">Stream A: Dense Vector Search</text>
        <g transform="translate(15, 38)">
          <text x="0" y="18" class="text-mono" font-size="10">Rank #1: Chunk 004 (Cosine: 0.88)</text>
          <text x="0" y="36" class="text-mono" font-size="10">Rank #2: Chunk 002 (Cosine: 0.84)</text>
          <text x="0" y="54" class="text-mono" font-size="10">Rank #3: Chunk 009 (Cosine: 0.79)</text>
          <text x="0" y="72" class="text-dim" font-size="9">Cosine range: [-1.0, 1.0]</text>
        </g>

        <!-- Stream 2: Sparse BM25 -->
        <g transform="translate(0, 155)">
          <rect width="260" height="135" rx="6" fill="#141c28" stroke="#60a5fa" stroke-width="1.2"/>
          <rect width="260" height="28" rx="6" fill="#1b2434"/>
          <text x="130" y="19" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#60a5fa">Stream B: Sparse BM25 Search</text>
          <g transform="translate(15, 38)">
            <text x="0" y="18" class="text-mono" font-size="10">Rank #1: Chunk 002 (BM25: 14.8)</text>
            <text x="0" y="36" class="text-mono" font-size="10">Rank #2: Chunk 008 (BM25: 11.2)</text>
            <text x="0" y="54" class="text-mono" font-size="10">Rank #3: Chunk 004 (BM25: 6.4)</text>
            <text x="0" y="72" class="text-dim" font-size="9">BM25 range: [0.0, ∞)</text>
          </g>
        </g>
      </g>

      <!-- Center Arrows -->
      <path d="M 300 95 L 350 160" stroke="#b4a4e5" stroke-width="1.5" marker-end="url(#arr)"/>
      <path d="M 300 220 L 350 180" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#arr)"/>

      <!-- Right: Fusion Engine -->
      <g transform="translate(360, 30)">
        <rect width="470" height="290" rx="8" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
        <rect width="470" height="34" rx="8" fill="#1b2434"/>
        <text x="235" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#6ee7b7">RECIPROCAL RANK FUSION (RRF) ENGINE</text>

        <g transform="translate(20, 50)">
          <!-- Formula Box -->
          <rect width="430" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="15" y="22" class="text-mono" font-size="10.5" fill="#94a3b8">The Universal RRF Equation (k = 60):</text>
          <text x="15" y="46" class="text-mono-bold" font-size="13" fill="#6ee7b7">RRF_Score(d) = Σ [ 1 / (60 + Rank_m(d)) ]</text>

          <!-- Calculated Example -->
          <rect y="72" width="430" height="150" rx="4" fill="#1b2434" stroke="#6ee7b7" stroke-width="1.2"/>
          <text x="15" y="94" class="text-mono-bold" font-size="11" fill="#6ee7b7">Computed Results for Query "Room B12 Loan":</text>

          <text x="15" y="118" class="text-mono" font-size="10.5" fill="#f8fafc">1. Chunk 002 (Ranked #2 Dense, #1 BM25):</text>
          <text x="35" y="134" class="text-mono" font-size="9.5" fill="#6ee7b7">Score = 1/(60+2) + 1/(60+1) = 0.0161 + 0.0164 = 0.0325 → RANK #1</text>

          <text x="15" y="156" class="text-mono" font-size="10.5" fill="#f8fafc">2. Chunk 004 (Ranked #1 Dense, #3 BM25):</text>
          <text x="35" y="172" class="text-mono" font-size="9.5" fill="#94a3b8">Score = 1/(60+1) + 1/(60+3) = 0.0164 + 0.0158 = 0.0322 → RANK #2</text>

          <text x="15" y="196" class="text-p" font-size="9.5" fill="#cbd5e1">Outcome: Documents verified by BOTH semantic and lexical signals win.</text>
        </g>
      </g>
    </svg>"""
}
