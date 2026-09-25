# -*- coding: utf-8 -*-
slide_data = {
    "index": 6,
    "badge": "INGESTION ENGINEERING",
    "title": "Chunking Strategies: Naive Character vs Structure-Aware",
    "subtitle": "How document segmentation determines the atomic boundary of retrieval accuracy.",
    "takeaway_tag": "CHUNK QUALITY",
    "takeaway": "Blind character splits destroy context: prepend heading hierarchy to every chunk.",
    "notes": """
      <h4>Chunking Trade-offs</h4>
      <p>Explain that naive character splits cut sentences and drop table rows. Structure-aware chunking preserves section paths and enables contextualized embeddings.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Strategy 1: Naive Fixed Size -->
      <g transform="translate(30, 30)">
        <rect width="250" height="290" rx="8" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
        <rect width="250" height="32" rx="8" fill="#1b2434"/>
        <text x="125" y="21" text-anchor="middle" class="text-mono" font-size="11" fill="#d98585">1. NAIVE FIXED-SIZE</text>

        <g transform="translate(15, 45)">
          <rect width="220" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="22" class="text-mono" font-size="10" fill="#d98585">Chunk #1 (chars 0-400)</text>
          <text x="12" y="42" class="text-p" font-size="9.5">"...standard issue includes one"</text>
          <text x="12" y="54" class="text-dim" font-size="8.5">[Cut mid-sentence!]</text>

          <rect y="70" width="220" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="92" class="text-mono" font-size="10" fill="#d98585">Chunk #2 (chars 350-750)</text>
          <text x="12" y="112" class="text-p" font-size="9.5">"laptop workstation. ## Sec 2..."</text>
          <text x="12" y="124" class="text-dim" font-size="8.5">[Separated from heading]</text>

          <rect y="140" width="220" height="90" rx="4" fill="#1b2434" stroke="#d98585"/>
          <text x="12" y="160" class="text-mono-bold" font-size="10" fill="#d98585">Critical Pitfalls:</text>
          <text x="12" y="178" class="text-p" font-size="9">- Separates tables from headers</text>
          <text x="12" y="194" class="text-p" font-size="9">- Splits sentences across chunks</text>
          <text x="12" y="210" class="text-p" font-size="9">- Zero semantic awareness</text>
        </g>
      </g>

      <!-- Strategy 2: Structure-Aware Markdown -->
      <g transform="translate(305, 30)">
        <rect width="250" height="290" rx="8" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
        <rect width="250" height="32" rx="8" fill="#1b2434"/>
        <text x="125" y="21" text-anchor="middle" class="text-mono" font-size="11" fill="#6ee7b7">2. STRUCTURE-AWARE</text>

        <g transform="translate(15, 45)">
          <rect width="220" height="75" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono" font-size="9.5" fill="#60a5fa">Breadcrumb Context:</text>
          <text x="12" y="36" class="text-dim" font-size="9">Doc: Hardware Policy</text>
          <text x="12" y="50" class="text-dim" font-size="9">Sec: 2. Temporary Loans</text>
          <text x="12" y="66" class="text-p" font-size="9.5">Content: 14 days, Room B12...</text>

          <rect y="85" width="220" height="50" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="105" class="text-mono" font-size="9.5" fill="#6ee7b7">Preserved Table Unit:</text>
          <text x="12" y="122" class="text-p" font-size="9">All columns and headers intact</text>

          <rect y="145" width="220" height="85" rx="4" fill="#1b2434" stroke="#6ee7b7"/>
          <text x="12" y="165" class="text-mono-bold" font-size="10" fill="#6ee7b7">Production Benefits:</text>
          <text x="12" y="182" class="text-p" font-size="9">+ Clean logical boundary</text>
          <text x="12" y="198" class="text-p" font-size="9">+ Breadcrumbs enrich semantics</text>
          <text x="12" y="214" class="text-p" font-size="9">+ Ideal for technical policies</text>
        </g>
      </g>

      <!-- Strategy 3: Semantic Windowing -->
      <g transform="translate(580, 30)">
        <rect width="250" height="290" rx="8" fill="#141c28" stroke="#60a5fa" stroke-width="1.2"/>
        <rect width="250" height="32" rx="8" fill="#1b2434"/>
        <text x="125" y="21" text-anchor="middle" class="text-mono" font-size="11" fill="#60a5fa">3. SEMANTIC WINDOWING</text>

        <g transform="translate(15, 45)">
          <rect width="220" height="65" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono" font-size="9.5" fill="#e0c58e">Rolling Embeddings:</text>
          <text x="12" y="36" class="text-dim" font-size="9">Computes adjacent sentence</text>
          <text x="12" y="52" class="text-dim" font-size="9">cosine similarity distance</text>

          <rect y="75" width="220" height="55" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="95" class="text-mono" font-size="9.5" fill="#60a5fa">Adaptive Split Barrier:</text>
          <text x="12" y="112" class="text-p" font-size="9">Splits when similarity drops</text>

          <rect y="140" width="220" height="90" rx="4" fill="#1b2434" stroke="#60a5fa"/>
          <text x="12" y="160" class="text-mono-bold" font-size="10" fill="#60a5fa">Best Used For:</text>
          <text x="12" y="178" class="text-p" font-size="9">- Narrative text without headers</text>
          <text x="12" y="194" class="text-p" font-size="9">- Transcripts and conversation logs</text>
          <text x="12" y="210" class="text-p" font-size="9">- Higher offline compute cost</text>
        </g>
      </g>
    </svg>"""
}
