# -*- coding: utf-8 -*-
slide_data = {
    "index": 1,
    "badge": "ADVANCED GENAI | MODULE 03",
    "title": "Vector Stores and Enterprise RAG: Architectural Blueprint",
    "subtitle": "Decoupling probabilistic reasoning from deterministic memory across the complete retrieval lifecycle.",
    "takeaway_tag": "SYSTEMS BLUEPRINT",
    "takeaway": "RAG is a distributed systems pattern: externalize factual memory so models focus on synthesis.",
    "notes": """
      <h4>Pedagogical Objective</h4>
      <p>Open the lecture by clarifying the engineering thesis: RAG is not a prompt hack; it is a decoupled distributed memory architecture.</p>
      <h4>What to Highlight</h4>
      <p>Point to the 5 connected stages: Document Ingestion, Vector Indexing, Hybrid Query, Precision Reranking, and Grounded Generation.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
          <polygon points="0 0, 8 3, 0 6" fill="#60a5fa"/>
        </marker>
        <marker id="arr-green" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
          <polygon points="0 0, 8 3, 0 6" fill="#6ee7b7"/>
        </marker>
      </defs>

      <!-- Stage 1: Ingestion -->
      <g transform="translate(15, 40)">
        <rect width="145" height="260" rx="6" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="145" height="32" rx="6" fill="#1b2434"/>
        <text x="72" y="21" text-anchor="middle" class="text-mono" font-size="11" fill="#60a5fa">1. INGESTION</text>
        
        <rect x="12" y="48" width="121" height="55" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="72" y="68" text-anchor="middle" class="text-h1" font-size="11.5">Raw Documents</text>
        <text x="72" y="86" text-anchor="middle" class="text-dim" font-size="9.5">PDFs, Markdown, SQL</text>

        <path d="M 72 103 L 72 120" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>

        <rect x="12" y="125" width="121" height="55" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="72" y="145" text-anchor="middle" class="text-h1" font-size="11.5">Structure Parser</text>
        <text x="72" y="163" text-anchor="middle" class="text-dim" font-size="9.5">Headings &amp; Tables</text>

        <path d="M 72 180 L 72 197" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>

        <rect x="12" y="202" width="121" height="46" rx="4" fill="#0e131b" stroke="#3b82f6" stroke-width="1.2"/>
        <text x="72" y="222" text-anchor="middle" class="text-mono" font-size="10.5" fill="#60a5fa">ACL Metadata</text>
        <text x="72" y="238" text-anchor="middle" class="text-dim" font-size="9">Tenant &amp; Role Tags</text>
      </g>

      <path d="M 160 170 L 185 170" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#arr)"/>

      <!-- Stage 2: Representation & Indexing -->
      <g transform="translate(190, 40)">
        <rect width="150" height="260" rx="6" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="150" height="32" rx="6" fill="#1b2434"/>
        <text x="75" y="21" text-anchor="middle" class="text-mono" font-size="11" fill="#b4a4e5">2. INDEXING</text>

        <rect x="12" y="48" width="126" height="55" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="75" y="68" text-anchor="middle" class="text-h1" font-size="11">Dense Vectors</text>
        <text x="75" y="86" text-anchor="middle" class="text-dim" font-size="9.5">1536-dim Embeddings</text>

        <rect x="12" y="115" width="126" height="55" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="75" y="135" text-anchor="middle" class="text-h1" font-size="11">Sparse Tokens</text>
        <text x="75" y="153" text-anchor="middle" class="text-dim" font-size="9.5">BM25 Inverted Index</text>

        <rect x="12" y="182" width="126" height="66" rx="4" fill="#1b2434" stroke="#b4a4e5" stroke-width="1.2"/>
        <text x="75" y="204" text-anchor="middle" class="text-mono" font-size="10.5" fill="#b4a4e5">Vector DB</text>
        <text x="75" y="222" text-anchor="middle" class="text-p" font-size="9.5">HNSW + IVF-PQ</text>
        <text x="75" y="238" text-anchor="middle" class="text-dim" font-size="8.5">Sub-5ms Graph Routing</text>
      </g>

      <path d="M 340 170 L 365 170" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#arr)"/>

      <!-- Stage 3: Retrieval & Filter -->
      <g transform="translate(370, 40)">
        <rect width="150" height="260" rx="6" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="150" height="32" rx="6" fill="#1b2434"/>
        <text x="75" y="21" text-anchor="middle" class="text-mono" font-size="11" fill="#e0c58e">3. RETRIEVAL</text>

        <rect x="12" y="48" width="126" height="55" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="75" y="68" text-anchor="middle" class="text-h1" font-size="11">Pre-Filtering</text>
        <text x="75" y="86" text-anchor="middle" class="text-dim" font-size="9.5">Role &amp; ACL Check</text>

        <rect x="12" y="115" width="126" height="55" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="75" y="135" text-anchor="middle" class="text-h1" font-size="11">Hybrid Fusion</text>
        <text x="75" y="153" text-anchor="middle" class="text-dim" font-size="9.5">RRF (k=60) Scoring</text>

        <rect x="12" y="182" width="126" height="66" rx="4" fill="#0e131b" stroke="#e0c58e" stroke-width="1.2"/>
        <text x="75" y="204" text-anchor="middle" class="text-mono" font-size="10.5" fill="#e0c58e">Cross-Encoder</text>
        <text x="75" y="222" text-anchor="middle" class="text-p" font-size="9.5">Rerank Top-50</text>
        <text x="75" y="238" text-anchor="middle" class="text-dim" font-size="8.5">Selects Top-5 Clustered</text>
      </g>

      <path d="M 520 170 L 545 170" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#arr)"/>

      <!-- Stage 4: Synthesis & Grounding -->
      <g transform="translate(550, 40)">
        <rect width="150" height="260" rx="6" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="150" height="32" rx="6" fill="#1b2434"/>
        <text x="75" y="21" text-anchor="middle" class="text-mono" font-size="11" fill="#6ee7b7">4. SYNTHESIS</text>

        <rect x="12" y="48" width="126" height="55" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="75" y="68" text-anchor="middle" class="text-h1" font-size="11">Context Assembly</text>
        <text x="75" y="86" text-anchor="middle" class="text-dim" font-size="9.5">Primacy &amp; Recency</text>

        <rect x="12" y="115" width="126" height="55" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="75" y="135" text-anchor="middle" class="text-h1" font-size="11">LLM Inference</text>
        <text x="75" y="153" text-anchor="middle" class="text-dim" font-size="9.5">Grounded Generation</text>

        <rect x="12" y="182" width="126" height="66" rx="4" fill="#0e131b" stroke="#6ee7b7" stroke-width="1.2"/>
        <text x="75" y="204" text-anchor="middle" class="text-mono" font-size="10.5" fill="#6ee7b7">Inline Citations</text>
        <text x="75" y="222" text-anchor="middle" class="text-p" font-size="9.5">[Source: ID § Sec]</text>
        <text x="75" y="238" text-anchor="middle" class="text-dim" font-size="8.5">Verified Evidence Span</text>
      </g>

      <path d="M 700 170 L 725 170" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#arr)"/>

      <!-- Stage 5: Evaluation -->
      <g transform="translate(730, 40)">
        <rect width="115" height="260" rx="6" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="115" height="32" rx="6" fill="#1b2434"/>
        <text x="57" y="21" text-anchor="middle" class="text-mono" font-size="10" fill="#d98585">5. EVALUATION</text>

        <rect x="10" y="55" width="95" height="75" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="57" y="76" text-anchor="middle" class="text-mono" font-size="9.5" fill="#60a5fa">Retrieval</text>
        <text x="57" y="96" text-anchor="middle" class="text-p" font-size="9">Hit Rate</text>
        <text x="57" y="112" text-anchor="middle" class="text-p" font-size="9">MRR, NDCG</text>

        <rect x="10" y="150" width="95" height="85" rx="4" fill="#0e131b" stroke="#253245"/>
        <text x="57" y="172" text-anchor="middle" class="text-mono" font-size="9.5" fill="#6ee7b7">Generation</text>
        <text x="57" y="192" text-anchor="middle" class="text-p" font-size="9">Faithfulness</text>
        <text x="57" y="208" text-anchor="middle" class="text-p" font-size="9">Relevance</text>
        <text x="57" y="224" text-anchor="middle" class="text-dim" font-size="8">Ragas Triad</text>
      </g>
    </svg>"""
}
