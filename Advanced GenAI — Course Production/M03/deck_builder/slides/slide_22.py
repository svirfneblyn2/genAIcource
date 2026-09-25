# -*- coding: utf-8 -*-
slide_data = {
    "index": 22,
    "badge": "EVALUATION METRICS",
    "title": "Retrieval Evaluation: Hit Rate, Recall@k, MRR & NDCG",
    "subtitle": "Quantitative statistical benchmarks for measuring retrieval quality before model generation.",
    "takeaway_tag": "RETRIEVAL BENCHMARKS",
    "takeaway": "Test retrieval independently: Hit Rate, MRR, and NDCG verify your index before touching prompts.",
    "notes": """
      <h4>Retrieval Metrics</h4>
      <p>Explain Hit Rate (binary presence), Recall@k (fraction of all relevant chunks), MRR (position penalty for rank #1), and NDCG@k (graded relevance across ranked candidates).</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 30)">
        <!-- Metric 1: Hit Rate -->
        <g transform="translate(0, 0)">
          <rect width="185" height="280" rx="6" fill="#141c28" stroke="#60a5fa" stroke-width="1.2"/>
          <rect width="185" height="32" rx="6" fill="#1b2434"/>
          <text x="92" y="20" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#60a5fa">HIT RATE @ k</text>

          <g transform="translate(12, 45)">
            <rect width="160" height="48" rx="4" fill="#0e131b"/>
            <text x="10" y="20" class="text-mono" font-size="9.5" fill="#94a3b8">Formula:</text>
            <text x="10" y="38" class="text-mono-bold" font-size="10.5" fill="#f8fafc">Hits / Total Queries</text>

            <text x="0" y="112" class="text-mono-bold" font-size="10" fill="#6ee7b7">What it measures:</text>
            <text x="0" y="130" class="text-p" font-size="9">Percentage of queries</text>
            <text x="0" y="144" class="text-p" font-size="9">where AT LEAST ONE</text>
            <text x="0" y="158" class="text-p" font-size="9">true relevant chunk is</text>
            <text x="0" y="172" class="text-p" font-size="9">present in top-k.</text>

            <rect y="190" width="160" height="36" rx="4" fill="#1b2434"/>
            <text x="80" y="212" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#60a5fa">Target: &gt; 92%</text>
          </g>
        </g>

        <!-- Metric 2: Recall@k -->
        <g transform="translate(205, 0)">
          <rect width="185" height="280" rx="6" fill="#141c28" stroke="#b4a4e5" stroke-width="1.2"/>
          <rect width="185" height="32" rx="6" fill="#1b2434"/>
          <text x="92" y="20" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#b4a4e5">RECALL @ k</text>

          <g transform="translate(12, 45)">
            <rect width="160" height="48" rx="4" fill="#0e131b"/>
            <text x="10" y="20" class="text-mono" font-size="9.5" fill="#94a3b8">Formula:</text>
            <text x="10" y="38" class="text-mono-bold" font-size="10.5" fill="#f8fafc">Retrieved_Rel / Total_Rel</text>

            <text x="0" y="112" class="text-mono-bold" font-size="10" fill="#6ee7b7">What it measures:</text>
            <text x="0" y="130" class="text-p" font-size="9">Fraction of all relevant</text>
            <text x="0" y="144" class="text-p" font-size="9">ground-truth chunks</text>
            <text x="0" y="158" class="text-p" font-size="9">successfully found</text>
            <text x="0" y="172" class="text-p" font-size="9">in the top-k window.</text>

            <rect y="190" width="160" height="36" rx="4" fill="#1b2434"/>
            <text x="80" y="212" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#b4a4e5">Target: &gt; 85%</text>
          </g>
        </g>

        <!-- Metric 3: MRR -->
        <g transform="translate(410, 0)">
          <rect width="185" height="280" rx="6" fill="#141c28" stroke="#e0c58e" stroke-width="1.2"/>
          <rect width="185" height="32" rx="6" fill="#1b2434"/>
          <text x="92" y="20" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#e0c58e">MRR (RECIPROCAL)</text>

          <g transform="translate(12, 45)">
            <rect width="160" height="48" rx="4" fill="#0e131b"/>
            <text x="10" y="20" class="text-mono" font-size="9.5" fill="#94a3b8">Formula:</text>
            <text x="10" y="38" class="text-mono-bold" font-size="10.5" fill="#f8fafc">(1 / Q) Σ (1 / rank_i)</text>

            <text x="0" y="112" class="text-mono-bold" font-size="10" fill="#6ee7b7">What it measures:</text>
            <text x="0" y="130" class="text-p" font-size="9">How close to the TOP</text>
            <text x="0" y="144" class="text-p" font-size="9">the primary correct</text>
            <text x="0" y="158" class="text-p" font-size="9">chunk is placed.</text>
            <text x="0" y="172" class="text-p" font-size="9">(Rank 1 = 1.0, Rank 2 = 0.5)</text>

            <rect y="190" width="160" height="36" rx="4" fill="#1b2434"/>
            <text x="80" y="212" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#e0c58e">Target: &gt; 0.80</text>
          </g>
        </g>

        <!-- Metric 4: NDCG -->
        <g transform="translate(615, 0)">
          <rect width="185" height="280" rx="6" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
          <rect width="185" height="32" rx="6" fill="#1b2434"/>
          <text x="92" y="20" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">NDCG @ k</text>

          <g transform="translate(12, 45)">
            <rect width="160" height="48" rx="4" fill="#0e131b"/>
            <text x="10" y="20" class="text-mono" font-size="9.5" fill="#94a3b8">Formula:</text>
            <text x="10" y="38" class="text-mono-bold" font-size="10.5" fill="#f8fafc">DCG@k / IDCG@k</text>

            <text x="0" y="112" class="text-mono-bold" font-size="10" fill="#6ee7b7">What it measures:</text>
            <text x="0" y="130" class="text-p" font-size="9">Graded relevance quality.</text>
            <text x="0" y="144" class="text-p" font-size="9">Heavily penalizes highly</text>
            <text x="0" y="158" class="text-p" font-size="9">relevant items placed</text>
            <text x="0" y="172" class="text-p" font-size="9">low in the result list.</text>

            <rect y="190" width="160" height="36" rx="4" fill="#1b2434"/>
            <text x="80" y="212" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#6ee7b7">Target: &gt; 0.85</text>
          </g>
        </g>
      </g>
    </svg>"""
}
