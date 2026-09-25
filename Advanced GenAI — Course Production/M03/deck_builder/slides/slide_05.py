# -*- coding: utf-8 -*-
slide_data = {
    "index": 5,
    "badge": "MATHEMATICAL FOUNDATION",
    "title": "Text Embeddings & Geometric Metric Spaces",
    "subtitle": "How natural language is projected into continuous high-dimensional vector representations.",
    "takeaway_tag": "VECTOR GEOMETRY",
    "takeaway": "Unit L2 normalization simplifies cosine similarity to a single hardware-accelerated dot product.",
    "notes": """
      <h4>Mathematical Details</h4>
      <p>Show that when vectors are L2-normalized, ||u|| = 1 and ||v|| = 1. The denominator of cosine similarity disappears, reducing search to matrix multiplication (GEMV) on tensor cores.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: Geometry Graph -->
      <g transform="translate(40, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="32" rx="8" fill="#1b2434"/>
        <text x="180" y="21" text-anchor="middle" class="text-mono" font-size="11" fill="#60a5fa">Vector Angle &amp; Cosine Metric</text>

        <!-- Coordinate axes -->
        <g transform="translate(60, 240)">
          <line x1="0" y1="0" x2="240" y2="0" stroke="#364761" stroke-width="1.5"/>
          <line x1="0" y1="0" x2="0" y2="-170" stroke="#364761" stroke-width="1.5"/>
          
          <!-- Vector u (Query) -->
          <line x1="0" y1="0" x2="160" y2="-120" stroke="#60a5fa" stroke-width="2.5"/>
          <circle cx="160" cy="-120" r="5" fill="#60a5fa"/>
          <text x="175" y="-120" class="text-mono-bold" font-size="11" fill="#60a5fa">q (Query)</text>
          
          <!-- Vector v (Target chunk) -->
          <line x1="0" y1="0" x2="190" y2="-80" stroke="#6ee7b7" stroke-width="2.5"/>
          <circle cx="190" cy="-80" r="5" fill="#6ee7b7"/>
          <text x="205" y="-80" class="text-mono-bold" font-size="11" fill="#6ee7b7">d1 (Match)</text>

          <!-- Vector w (Unrelated chunk) -->
          <line x1="0" y1="0" x2="40" y2="-150" stroke="#d98585" stroke-width="1.8"/>
          <circle cx="40" cy="-150" r="4" fill="#d98585"/>
          <text x="50" y="-155" class="text-mono" font-size="10" fill="#d98585">d2 (Unrelated)</text>

          <!-- Angle theta -->
          <path d="M 60 -45 A 75 75 0 0 1 70 -30" fill="none" stroke="#e0c58e" stroke-width="1.5"/>
          <text x="85" y="-40" class="text-mono" font-size="11" fill="#e0c58e">θ ≈ 18°</text>
        </g>
      </g>

      <!-- Right: Formulas & Hardware Optimization -->
      <g transform="translate(430, 30)">
        <rect width="390" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="390" height="32" rx="8" fill="#1b2434"/>
        <text x="195" y="21" text-anchor="middle" class="text-mono" font-size="11" fill="#e0c58e">Formula &amp; Tensor Core Optimization</text>

        <g transform="translate(20, 50)">
          <!-- General Cosine Formula -->
          <rect width="350" height="65" rx="6" fill="#0e131b" stroke="#253245"/>
          <text x="15" y="22" class="text-mono" font-size="10.5" fill="#94a3b8">Standard Cosine Metric:</text>
          <text x="15" y="46" class="text-mono-bold" font-size="12" fill="#f8fafc">Cosine(q, d) = (q · d) / ( ||q|| · ||d|| )</text>

          <!-- L2 Normalization Benefit -->
          <rect y="78" width="350" height="75" rx="6" fill="#1b2434" stroke="#6ee7b7" stroke-width="1.2"/>
          <text x="15" y="98" class="text-mono-bold" font-size="11" fill="#6ee7b7">Production Optimization: Unit L2 Norm</text>
          <text x="15" y="118" class="text-p" font-size="10.5">If ||q|| = 1.0 and ||d|| = 1.0, denominator = 1.0:</text>
          <text x="15" y="138" class="text-mono-bold" font-size="12.5" fill="#6ee7b7">Cosine(q, d) ≡ q · d = Σ (q_i × d_i)</text>

          <!-- Tensor Core Note -->
          <rect y="165" width="350" height="55" rx="6" fill="#0e131b" stroke="#253245"/>
          <text x="15" y="185" class="text-mono" font-size="10" fill="#60a5fa">Hardware Execution: Pure GEMV</text>
          <text x="15" y="202" class="text-dim" font-size="9">Eliminates sqrt() and div() across millions of vector checks</text>
        </g>
      </g>
    </svg>"""
}
