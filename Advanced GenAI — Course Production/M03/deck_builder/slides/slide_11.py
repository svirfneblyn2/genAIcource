# -*- coding: utf-8 -*-
slide_data = {
    "index": 11,
    "badge": "CAPACITY PLANNING",
    "title": "Vector DB Sizing Math: Calculating RAM for 1M Vectors",
    "subtitle": "Step-by-step engineering sizing for memory footprints, index overhead, and payload storage.",
    "takeaway_tag": "MEMORY CAPACITY",
    "takeaway": "Unquantized 1M vectors requires 14-16 GB RAM: SQ8 quantization slashes this to under 4 GB.",
    "notes": """
      <h4>Capacity Sizing Equation</h4>
      <p>Break down the 3 components: raw float32 vectors (6.14 GB), HNSW graph links overhead (1.75x -> 10.75 GB), and payload/metadata storage (3 GB). Total is 14-16 GB RAM.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: Stacked Memory Calculation -->
      <g transform="translate(40, 30)">
        <rect width="400" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="400" height="34" rx="8" fill="#1b2434"/>
        <text x="200" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#60a5fa">PRODUCTION SIZING: 1,000,000 VECTORS (1536-DIM)</text>

        <g transform="translate(20, 50)">
          <!-- Item 1: Raw Vectors -->
          <rect width="360" height="52" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="22" class="text-mono-bold" font-size="10.5" fill="#f8fafc">1. Raw Float32 Vector Storage</text>
          <text x="14" y="40" class="text-mono" font-size="10" fill="#60a5fa">1M × 1536 dims × 4 bytes = 6.14 GB</text>

          <!-- Item 2: HNSW Graph Links -->
          <rect y="60" width="360" height="52" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="82" class="text-mono-bold" font-size="10.5" fill="#f8fafc">2. HNSW Graph Connectivity Links (M=16)</text>
          <text x="14" y="100" class="text-mono" font-size="10" fill="#b4a4e5">Index overhead factor ~1.75x = +4.60 GB</text>

          <!-- Item 3: Metadata & Payloads -->
          <rect y="120" width="360" height="52" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="142" class="text-mono-bold" font-size="10.5" fill="#f8fafc">3. Document Payload &amp; ACL Metadata</text>
          <text x="14" y="160" class="text-mono" font-size="10" fill="#e0c58e">1M chunks × 3 KB text/metadata = 3.00 GB</text>

          <!-- Total Banner -->
          <rect y="180" width="360" height="42" rx="4" fill="#1b2434" stroke="#d98585" stroke-width="1.2"/>
          <text x="14" y="206" class="text-mono-bold" font-size="11.5" fill="#d98585">Total In-Memory RAM Needed: ~14.0 to 16.0 GB</text>
        </g>
      </g>

      <!-- Right: With Quantization Comparison -->
      <g transform="translate(460, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#6ee7b7">WITH SQ8 QUANTIZATION (INT8)</text>

        <g transform="translate(20, 50)">
          <!-- Quantized Vector -->
          <rect width="320" height="52" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="22" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">1. Quantized SQ8 Vectors</text>
          <text x="14" y="40" class="text-mono" font-size="10" fill="#6ee7b7">1M × 1536 dims × 1 byte = 1.54 GB (75% savings)</text>

          <!-- Quantized Graph -->
          <rect y="60" width="320" height="52" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="82" class="text-mono-bold" font-size="10.5" fill="#f8fafc">2. Compressed Graph Links</text>
          <text x="14" y="100" class="text-mono" font-size="10" fill="#6ee7b7">Optimized neighbor list = +1.15 GB</text>

          <!-- Payload in disk / mmap -->
          <rect y="120" width="320" height="52" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="142" class="text-mono-bold" font-size="10.5" fill="#f8fafc">3. Text Payloads on SSD (mmap)</text>
          <text x="14" y="160" class="text-mono" font-size="10" fill="#e0c58e">Memory-mapped disk read: ~0.50 GB RAM cache</text>

          <!-- Quantized Total -->
          <rect y="180" width="320" height="42" rx="4" fill="#1b2434" stroke="#6ee7b7" stroke-width="1.2"/>
          <text x="14" y="206" class="text-mono-bold" font-size="11.5" fill="#6ee7b7">Quantized RAM Footprint: ~3.2 to 3.8 GB</text>
        </g>
      </g>
    </svg>"""
}
