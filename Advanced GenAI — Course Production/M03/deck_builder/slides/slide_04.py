# -*- coding: utf-8 -*-
slide_data = {
    "index": 4,
    "badge": "SYSTEM TOPOLOGY",
    "title": "Dual-Lane Architecture: Ingestion vs Real-Time Query",
    "subtitle": "Decoupling high-latency batch preparation from sub-second client request inference.",
    "takeaway_tag": "LANE ISOLATION",
    "takeaway": "Never parse or chunk documents synchronously inside a user query request.",
    "notes": """
      <h4>Architectural Separation</h4>
      <p>Top lane is asynchronous document indexing (hours/minutes). Bottom lane is synchronous user query response (sub-500ms). Both share storage and observability.</p>
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

      <!-- Lane 1: Offline Ingestion -->
      <g transform="translate(30, 25)">
        <rect width="800" height="120" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="180" height="24" rx="4" fill="#1b2434"/>
        <text x="12" y="16" class="text-mono" font-size="10.5" fill="#60a5fa">LANE 1: OFFLINE INGESTION</text>

        <!-- Pipeline Steps -->
        <g transform="translate(20, 36)">
          <rect width="120" height="65" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="60" y="24" text-anchor="middle" class="text-h1" font-size="11">Sources</text>
          <text x="60" y="42" text-anchor="middle" class="text-dim" font-size="9">PDF, Markdown</text>
          <text x="60" y="55" text-anchor="middle" class="text-dim" font-size="8.5">SharePoint, S3</text>

          <path d="M 125 32 L 155 32" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>

          <rect x="160" width="125" height="65" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="222" y="24" text-anchor="middle" class="text-h1" font-size="11">Structure Parser</text>
          <text x="222" y="42" text-anchor="middle" class="text-dim" font-size="9">Heading Extraction</text>
          <text x="222" y="55" text-anchor="middle" class="text-dim" font-size="8.5">Tables &amp; Sections</text>

          <path d="M 290 32 L 320 32" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>

          <rect x="325" width="125" height="65" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="387" y="24" text-anchor="middle" class="text-h1" font-size="11">Embedder</text>
          <text x="387" y="42" text-anchor="middle" class="text-dim" font-size="9">Dense: 1536-dim</text>
          <text x="387" y="55" text-anchor="middle" class="text-dim" font-size="8.5">Sparse: BM25 terms</text>

          <path d="M 455 32 L 485 32" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>

          <rect x="490" width="125" height="65" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="552" y="24" text-anchor="middle" class="text-h1" font-size="11">Metadata Tagger</text>
          <text x="552" y="42" text-anchor="middle" class="text-dim" font-size="9">tenant_id, role</text>
          <text x="552" y="55" text-anchor="middle" class="text-dim" font-size="8.5">version, doc_id</text>

          <path d="M 620 32 L 650 32" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>

          <rect x="655" width="105" height="65" rx="4" fill="#1b2434" stroke="#60a5fa" stroke-width="1.2"/>
          <text x="707" y="25" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#60a5fa">Vector Store</text>
          <text x="707" y="42" text-anchor="middle" class="text-p" font-size="9">HNSW Index</text>
          <text x="707" y="55" text-anchor="middle" class="text-dim" font-size="8.5">+ Inverted Index</text>
        </g>
      </g>

      <!-- Center Connector -->
      <path d="M 737 148 L 737 175" stroke="#6ee7b7" stroke-width="1.5" stroke-dasharray="3,3"/>
      <circle cx="737" cy="162" r="8" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>

      <!-- Lane 2: Online Request -->
      <g transform="translate(30, 180)">
        <rect width="800" height="145" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="180" height="24" rx="4" fill="#1b2434"/>
        <text x="12" y="16" class="text-mono" font-size="10.5" fill="#6ee7b7">LANE 2: ONLINE REQUEST</text>

        <!-- Pipeline Steps -->
        <g transform="translate(20, 36)">
          <rect width="115" height="85" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="57" y="24" text-anchor="middle" class="text-h1" font-size="11">User Query</text>
          <text x="57" y="42" text-anchor="middle" class="text-dim" font-size="9">Web / API Client</text>
          <text x="57" y="60" text-anchor="middle" class="text-mono" font-size="8.5" fill="#60a5fa">Auth: JWT / Role</text>

          <path d="M 120 42 L 145 42" stroke="#6ee7b7" stroke-width="1.2" marker-end="url(#arr-green)"/>

          <rect x="150" width="125" height="85" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="212" y="24" text-anchor="middle" class="text-h1" font-size="11">Pre-Filter Gate</text>
          <text x="212" y="42" text-anchor="middle" class="text-dim" font-size="9">Prunes search space</text>
          <text x="212" y="60" text-anchor="middle" class="text-mono" font-size="8.5" fill="#e0c58e">ACL Enforced</text>

          <path d="M 280 42 L 305 42" stroke="#6ee7b7" stroke-width="1.2" marker-end="url(#arr-green)"/>

          <rect x="310" width="130" height="85" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="375" y="24" text-anchor="middle" class="text-h1" font-size="11">Hybrid Retrieval</text>
          <text x="375" y="42" text-anchor="middle" class="text-dim" font-size="9">Dense + BM25</text>
          <text x="375" y="60" text-anchor="middle" class="text-mono" font-size="8.5" fill="#b4a4e5">RRF (k=60)</text>

          <path d="M 445 42 L 470 42" stroke="#6ee7b7" stroke-width="1.2" marker-end="url(#arr-green)"/>

          <rect x="475" width="130" height="85" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="540" y="24" text-anchor="middle" class="text-h1" font-size="11">Context Assembly</text>
          <text x="540" y="42" text-anchor="middle" class="text-dim" font-size="9">Lost-in-Middle fix</text>
          <text x="540" y="60" text-anchor="middle" class="text-mono" font-size="8.5" fill="#e0c58e">Citation Hooks</text>

          <path d="M 610 42 L 635 42" stroke="#6ee7b7" stroke-width="1.2" marker-end="url(#arr-green)"/>

          <rect x="640" width="120" height="85" rx="4" fill="#1b2434" stroke="#6ee7b7" stroke-width="1.2"/>
          <text x="700" y="25" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#6ee7b7">Grounded LLM</text>
          <text x="700" y="44" text-anchor="middle" class="text-p" font-size="9.5">Inline Citations</text>
          <text x="700" y="62" text-anchor="middle" class="text-dim" font-size="8.5">Deterministic Guard</text>
        </g>
      </g>
    </svg>"""
}
