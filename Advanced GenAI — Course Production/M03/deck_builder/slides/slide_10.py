# -*- coding: utf-8 -*-
slide_data = {
    "index": 10,
    "badge": "MEMORY OPTIMIZATION",
    "title": "Vector Indexing: IVF Voronoi Cells & Quantization",
    "subtitle": "Compressing vector memory footprints by 75% to 90% for massive 100M+ vector scale.",
    "takeaway_tag": "QUANTIZATION COMPACTION",
    "takeaway": "Scalar Quantization (SQ8) compresses vectors from 4 bytes to 1 byte with under 1% recall loss.",
    "notes": """
      <h4>IVF and Quantization</h4>
      <p>Explain Voronoi cell partitioning (IVF). Explain how Scalar Quantization (float32 to int8) cuts RAM by 75%, and Product Quantization (PQ) cuts RAM by up to 95%.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: IVF Voronoi Partitioning -->
      <g transform="translate(40, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono" font-size="11" fill="#e0c58e">INVERTED FILE (IVF VORONOI CELLS)</text>

        <g transform="translate(30, 50)">
          <!-- Voronoi Cells visualization -->
          <rect width="300" height="135" rx="6" fill="#0e131b" stroke="#253245"/>
          
          <!-- Cell 1 -->
          <polygon points="10,10 120,15 100,75 15,65" fill="#141c28" stroke="#364761"/>
          <circle cx="60" cy="40" r="4" fill="#60a5fa"/>
          <text x="60" y="55" text-anchor="middle" class="text-dim" font-size="8">Centroid C1</text>

          <!-- Cell 2 (Active probe) -->
          <polygon points="120,15 210,10 230,80 100,75" fill="rgba(224, 197, 142, 0.12)" stroke="#e0c58e" stroke-width="1.5"/>
          <circle cx="165" cy="45" r="5" fill="#e0c58e"/>
          <circle cx="180" cy="35" r="3" fill="#cbd5e1"/>
          <circle cx="150" cy="60" r="3" fill="#cbd5e1"/>
          <circle cx="190" cy="55" r="3" fill="#cbd5e1"/>
          <text x="165" y="72" text-anchor="middle" class="text-mono-bold" font-size="8.5" fill="#e0c58e">nprobe Cell</text>

          <!-- Cell 3 -->
          <polygon points="210,10 290,15 285,75 230,80" fill="#141c28" stroke="#364761"/>
          <circle cx="260" cy="45" r="4" fill="#60a5fa"/>

          <!-- Text description -->
          <rect y="145" width="300" height="80" rx="4" fill="#1b2434" stroke="#253245"/>
          <text x="12" y="165" class="text-mono-bold" font-size="10" fill="#e0c58e">IVF Mechanics (k-means):</text>
          <text x="12" y="182" class="text-p" font-size="9">- Partitions vectors into k clusters</text>
          <text x="12" y="198" class="text-p" font-size="9">- Search checks only 'nprobe' nearest centroids</text>
          <text x="12" y="214" class="text-p" font-size="9">- Trades exact boundaries for fast pruning</text>
        </g>
      </g>

      <!-- Right: Quantization Comparison -->
      <g transform="translate(460, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono" font-size="11" fill="#6ee7b7">QUANTIZATION: COMPRESSION TIERS</text>

        <g transform="translate(20, 50)">
          <!-- Tier 1: Full float32 -->
          <rect width="320" height="58" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10.5" fill="#f8fafc">1. Float32 (Uncompressed Baseline)</text>
          <text x="12" y="36" class="text-p" font-size="9.5">4 bytes per dimension | 1536 dims = 6,144 bytes / vector</text>
          <text x="12" y="50" class="text-dim" font-size="9">Maximum precision, highest RAM expenditure</text>

          <!-- Tier 2: SQ8 (int8) -->
          <rect y="68" width="320" height="66" rx="4" fill="#1b2434" stroke="#6ee7b7" stroke-width="1.2"/>
          <text x="12" y="88" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">2. Scalar Quantization: SQ8 (int8)</text>
          <text x="12" y="104" class="text-p" font-size="9.5">1 byte per dimension | 1536 dims = 1,536 bytes / vector</text>
          <text x="12" y="122" class="text-mono" font-size="9.5" fill="#6ee7b7">75% Memory Reduction | Recall drop &lt; 0.8%</text>

          <!-- Tier 3: PQ (Product Quantization) -->
          <rect y="144" width="320" height="68" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="164" class="text-mono-bold" font-size="10.5" fill="#b4a4e5">3. Product Quantization: PQ</text>
          <text x="12" y="180" class="text-p" font-size="9.5">Sub-vector centroid codebooks | 64 - 128 bytes / vector</text>
          <text x="12" y="198" class="text-mono" font-size="9.5" fill="#b4a4e5">Up to 95% Memory Reduction | Best for 100M+ scale</text>
        </g>
      </g>
    </svg>"""
}
