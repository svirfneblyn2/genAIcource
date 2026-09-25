# -*- coding: utf-8 -*-
slide_data = {
    "index": 20,
    "badge": "INCIDENT TRIAGE",
    "title": "RAG Failure Taxonomy: Root-Cause Analysis (Part 1)",
    "subtitle": "Pinpointing defects across the first 4 ingestion, chunking, and retrieval stages.",
    "takeaway_tag": "FAILURE TRIAGE 1",
    "takeaway": "Diagnose the stage, not the symptom: 'the answer is wrong' is an unhelpful bug report.",
    "notes": """
      <h4>Failure Modes 1-4</h4>
      <p>Break down the first 4 stages: Ingestion Gap (OCR error), Chunking Fracture (split tables), Retrieval Miss (vocabulary gap), and Security Filter Drop (over-restrictive ACL).</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 30)">
        <!-- Stage 1 -->
        <g transform="translate(0, 0)">
          <rect width="185" height="280" rx="6" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
          <rect width="185" height="32" rx="6" fill="#1b2434"/>
          <text x="92" y="20" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#d98585">1. INGESTION GAP</text>

          <g transform="translate(12, 45)">
            <text x="0" y="16" class="text-mono" font-size="9.5" fill="#f8fafc">Root Cause:</text>
            <text x="0" y="32" class="text-p" font-size="9">OCR failure on scanned</text>
            <text x="0" y="46" class="text-p" font-size="9">PDF or crawler skipped</text>
            <text x="0" y="60" class="text-p" font-size="9">dynamic JS page.</text>

            <rect y="75" width="160" height="50" rx="4" fill="#0e131b"/>
            <text x="10" y="96" class="text-dim" font-size="8.5">Content never entered</text>
            <text x="10" y="112" class="text-dim" font-size="8.5">the search index.</text>

            <text x="0" y="148" class="text-mono-bold" font-size="9.5" fill="#6ee7b7">Fix:</text>
            <text x="0" y="165" class="text-p" font-size="8.5">Layout-aware parsers</text>
            <text x="0" y="180" class="text-p" font-size="8.5">&amp; ingestion telemetry.</text>
          </g>
        </g>

        <!-- Stage 2 -->
        <g transform="translate(205, 0)">
          <rect width="185" height="280" rx="6" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
          <rect width="185" height="32" rx="6" fill="#1b2434"/>
          <text x="92" y="20" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#d98585">2. CHUNKING FRACTURE</text>

          <g transform="translate(12, 45)">
            <text x="0" y="16" class="text-mono" font-size="9.5" fill="#f8fafc">Root Cause:</text>
            <text x="0" y="32" class="text-p" font-size="9">Blind character split</text>
            <text x="0" y="46" class="text-p" font-size="9">severed condition from</text>
            <text x="0" y="60" class="text-p" font-size="9">the policy clause.</text>

            <rect y="75" width="160" height="50" rx="4" fill="#0e131b"/>
            <text x="10" y="96" class="text-dim" font-size="8.5">Table column headers</text>
            <text x="10" y="112" class="text-dim" font-size="8.5">separated from values.</text>

            <text x="0" y="148" class="text-mono-bold" font-size="9.5" fill="#6ee7b7">Fix:</text>
            <text x="0" y="165" class="text-p" font-size="8.5">Heading hierarchy</text>
            <text x="0" y="180" class="text-p" font-size="8.5">prepended to chunks.</text>
          </g>
        </g>

        <!-- Stage 3 -->
        <g transform="translate(410, 0)">
          <rect width="185" height="280" rx="6" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
          <rect width="185" height="32" rx="6" fill="#1b2434"/>
          <text x="92" y="20" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#d98585">3. RETRIEVAL MISS</text>

          <g transform="translate(12, 45)">
            <text x="0" y="16" class="text-mono" font-size="9.5" fill="#f8fafc">Root Cause:</text>
            <text x="0" y="32" class="text-p" font-size="9">Vocabulary mismatch</text>
            <text x="0" y="46" class="text-p" font-size="9">or alphanumeric blur</text>
            <text x="0" y="60" class="text-p" font-size="9">in dense embedding.</text>

            <rect y="75" width="160" height="50" rx="4" fill="#0e131b"/>
            <text x="10" y="96" class="text-dim" font-size="8.5">Correct chunk scored</text>
            <text x="10" y="112" class="text-dim" font-size="8.5">below top-k boundary.</text>

            <text x="0" y="148" class="text-mono-bold" font-size="9.5" fill="#6ee7b7">Fix:</text>
            <text x="0" y="165" class="text-p" font-size="8.5">Hybrid BM25 + Dense</text>
            <text x="0" y="180" class="text-p" font-size="8.5">with RRF fusion.</text>
          </g>
        </g>

        <!-- Stage 4 -->
        <g transform="translate(615, 0)">
          <rect width="185" height="280" rx="6" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
          <rect width="185" height="32" rx="6" fill="#1b2434"/>
          <text x="92" y="20" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#d98585">4. FILTER EXCLUSION</text>

          <g transform="translate(12, 45)">
            <text x="0" y="16" class="text-mono" font-size="9.5" fill="#f8fafc">Root Cause:</text>
            <text x="0" y="32" class="text-p" font-size="9">Erroneous or overly</text>
            <text x="0" y="46" class="text-p" font-size="9">restrictive metadata</text>
            <text x="0" y="60" class="text-p" font-size="9">predicate on index.</text>

            <rect y="75" width="160" height="50" rx="4" fill="#0e131b"/>
            <text x="10" y="96" class="text-dim" font-size="8.5">Valid document dropped</text>
            <text x="10" y="112" class="text-dim" font-size="8.5">before search started.</text>

            <text x="0" y="148" class="text-mono-bold" font-size="9.5" fill="#6ee7b7">Fix:</text>
            <text x="0" y="165" class="text-p" font-size="8.5">Audited role hierarchy</text>
            <text x="0" y="180" class="text-p" font-size="8.5">&amp; tenant tag validation.</text>
          </g>
        </g>
      </g>
    </svg>"""
}
