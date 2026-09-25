# -*- coding: utf-8 -*-
slide_data = {
    "index": 12,
    "badge": "RETRIEVAL PARADIGMS",
    "title": "Lexical vs Dense Retrieval: Why Neither Alone is Enough",
    "subtitle": "BM25 keyword precision vs bi-encoder semantic abstraction: complimentary strengths.",
    "takeaway_tag": "HYBRID REASONING",
    "takeaway": "Dense embeddings blur exact codes and part numbers: lexical BM25 guarantees keyword precision.",
    "notes": """
      <h4>Complementary Strengths</h4>
      <p>Demonstrate why pure dense vector search fails on alphanumeric codes (Room B12, POL-SEC-402, 0x80070005). BM25 handles exact tokens; Dense handles semantic synonyms.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: Sparse BM25 -->
      <g transform="translate(40, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#60a5fa">SPARSE LEXICAL (BM25 INVERTED INDEX)</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10" fill="#6ee7b7">Unbeatable On Exact Matches:</text>
          <text x="12" y="38" class="text-p" font-size="9.5">- Alphanumeric codes: 'POL-IT-101', 'Room B12'</text>
          <text x="12" y="52" class="text-p" font-size="9.5">- Technical error codes: '0x80070005', 'CVE-2026-118'</text>

          <rect y="70" width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10" fill="#6ee7b7">Vocabulary Specifics:</text>
          <text x="12" y="38" class="text-p" font-size="9.5">- Product SKUs, person names, and acronyms</text>
          <text x="12" y="52" class="text-p" font-size="9.5">- Zero embedding model inference needed</text>

          <rect y="140" width="320" height="75" rx="4" fill="#1b2434" stroke="#d98585"/>
          <text x="12" y="162" class="text-mono-bold" font-size="10.5" fill="#d98585">Critical Failure Mode: Vocabulary Mismatch</text>
          <text x="12" y="180" class="text-p" font-size="9">- Searching 'laptop loan' fails if doc says 'hardware borrow'</text>
          <text x="12" y="196" class="text-dim" font-size="8.5">- Zero conceptual generalization or multilingual bridging</text>
        </g>
      </g>

      <!-- Right: Dense Bi-Encoder -->
      <g transform="translate(460, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#b4a4e5">DENSE VECTOR (BI-ENCODER EMBEDDINGS)</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10" fill="#6ee7b7">Unbeatable On Conceptual Intent:</text>
          <text x="12" y="38" class="text-p" font-size="9.5">- Synonyms: 'take laptop' ≈ 'equipment loan'</text>
          <text x="12" y="52" class="text-p" font-size="9.5">- Multilingual alignment: cross-lingual retrieval</text>

          <rect y="70" width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10" fill="#6ee7b7">Paraphrase Robustness:</text>
          <text x="12" y="38" class="text-p" font-size="9.5">- Robust to typos and conversational framing</text>
          <text x="12" y="52" class="text-p" font-size="9.5">- Captures latent domain concepts</text>

          <rect y="140" width="320" height="75" rx="4" fill="#1b2434" stroke="#d98585"/>
          <text x="12" y="162" class="text-mono-bold" font-size="10.5" fill="#d98585">Critical Failure Mode: Keyword Blindness</text>
          <text x="12" y="180" class="text-p" font-size="9">- Blurs 'Room B12' into generic office location vectors</text>
          <text x="12" y="196" class="text-dim" font-size="8.5">- Confuses similar product model numbers (V100 vs H100)</text>
        </g>
      </g>
    </svg>"""
}
