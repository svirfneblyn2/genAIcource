# -*- coding: utf-8 -*-
slide_data = {
    "index": 7,
    "badge": "ENTERPRISE SECURITY",
    "title": "Metadata Filtering & The Security Boundary",
    "subtitle": "Why similarity search alone cannot enforce authorization: pre-filtering vs post-filtering.",
    "takeaway_tag": "SECURITY BOUNDARY",
    "takeaway": "Always pre-filter by user ACLs: post-filtering risks leaking data or returning zero results.",
    "notes": """
      <h4>Security Flaw in RAG</h4>
      <p>Vector similarity is blind to permissions. Explain why pre-filtering (filtering before ANN search) is mandatory in enterprise multi-tenant systems.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: Pre-Filtering (Approved) -->
      <g transform="translate(40, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="12" fill="#6ee7b7">PRE-FILTERING (ENTERPRISE STANDARD)</text>

        <g transform="translate(20, 50)">
          <!-- Step 1: User Request -->
          <rect width="320" height="42" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono" font-size="10" fill="#60a5fa">1. Query + User Identity</text>
          <text x="12" y="34" class="text-dim" font-size="9">User: Alice | Role: 'engineer' | Tenant: 'Acme'</text>

          <!-- Step 2: Index Pruning -->
          <rect y="50" width="320" height="48" rx="4" fill="#1b2434" stroke="#6ee7b7" stroke-width="1.2"/>
          <text x="12" y="70" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">2. Hard Metadata Filter BEFORE Search</text>
          <text x="12" y="86" class="text-p" font-size="9.5">WHERE tenant == 'Acme' AND role IN ('all', 'engineer')</text>

          <!-- Step 3: Vector Search on Subset -->
          <rect y="106" width="320" height="42" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="126" class="text-mono" font-size="10" fill="#f8fafc">3. Approximate Nearest Neighbor Search</text>
          <text x="12" y="140" class="text-dim" font-size="9">Vector traversal runs ONLY on authorized subset</text>

          <!-- Outcome -->
          <rect y="156" width="320" height="65" rx="4" fill="#0e131b" stroke="#6ee7b7"/>
          <text x="12" y="178" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">Zero Leakage Guarantee:</text>
          <text x="12" y="196" class="text-p" font-size="9">+ Confidential C-suite chunks cannot enter top-k</text>
          <text x="12" y="210" class="text-p" font-size="9">+ Full top-k slots populated with valid evidence</text>
        </g>
      </g>

      <!-- Right: Post-Filtering (Flawed) -->
      <g transform="translate(460, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="12" fill="#d98585">POST-FILTERING (FLAWED ARCHITECTURE)</text>

        <g transform="translate(20, 50)">
          <!-- Step 1: Blind Vector Search -->
          <rect width="320" height="42" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono" font-size="10" fill="#d98585">1. Blind Global Vector Search</text>
          <text x="12" y="34" class="text-dim" font-size="9">Searches across ALL tenants and confidential documents</text>

          <!-- Step 2: Unfiltered Candidates -->
          <rect y="50" width="320" height="48" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="70" class="text-mono" font-size="10.5" fill="#f8fafc">2. Retrieves Global Top-10 Chunks</text>
          <text x="12" y="86" class="text-dim" font-size="9.5">Top 8 matches happen to be Executive Compensation</text>

          <!-- Step 3: Dropping Chunks -->
          <rect y="106" width="320" height="42" rx="4" fill="#1b2434" stroke="#d98585" stroke-width="1.2"/>
          <text x="12" y="126" class="text-mono-bold" font-size="10" fill="#d98585">3. Drop Unauthorized Chunks Afterwards</text>
          <text x="12" y="140" class="text-p" font-size="9">Drops 8 out of 10 chunks from context</text>

          <!-- Failure Outcome -->
          <rect y="156" width="320" height="65" rx="4" fill="#0e131b" stroke="#d98585"/>
          <text x="12" y="178" class="text-mono-bold" font-size="10.5" fill="#d98585">Recall Starvation Failure:</text>
          <text x="12" y="196" class="text-p" font-size="9">- Only 2 chunks reach the LLM (Recall Collapse)</text>
          <text x="12" y="210" class="text-p" font-size="9">- If top-10 are unauthorized, user gets 0 chunks</text>
        </g>
      </g>
    </svg>"""
}
