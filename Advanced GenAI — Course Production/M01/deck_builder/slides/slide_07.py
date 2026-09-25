# Slide 07: End-to-End Architecture: Two-Lane Topology
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 7,
    "kicker": "REFERENCE TOPOLOGY",
    "title": "Dual-Lane Architecture: Offline Ingestion vs Online Request",
    "lead": "Decoupling continuous document indexing from real-time low-latency inference.",
    "section": "Reference Topology",
    "takeaway": "Never mix document indexing pipelines with synchronous user inference paths.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 20)">
        <!-- Lane 1: Offline Ingestion Swimlane -->
        <rect x="0" y="0" width="1040" height="150" rx="8" class="swimlane-bg"/>
        <rect x="12" y="12" width="220" height="26" rx="4" fill="#1b2434"/>
        <text x="22" y="29" class="text-mono" font-size="12">LANE 1: OFFLINE INGESTION PIPELINE</text>

        <!-- Node 1: Doc Store -->
        <g transform="translate(20, 50)">
          <rect x="0" y="0" width="165" height="85" rx="6" class="node-box"/>
          {render_icon("documents", 12, 10, size=20, color="#60a5fa")}
          <text x="38" y="25" class="text-h2">Policy Docs</text>
          <text x="12" y="50" class="text-dim">PDF, Word, Markdown</text>
          <text x="12" y="70" class="text-mono" font-size="11">S3 / Blob / GCS</text>
        </g>

        <path d="M 195 92 L 225 92" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>

        <!-- Node 2: Chunker -->
        <g transform="translate(235, 50)">
          <rect x="0" y="0" width="175" height="85" rx="6" class="node-box"/>
          {render_icon("tool", 12, 10, size=20, color="#6ee7b7")}
          <text x="38" y="25" class="text-h2">Chunk &amp; Parse</text>
          <text x="12" y="50" class="text-dim">Table-aware layout OCR</text>
          <text x="12" y="70" class="text-mono-green" font-size="11">512 token + overlap</text>
        </g>

        <path d="M 420 92 L 450 92" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

        <!-- Node 3: Embed & ACL -->
        <g transform="translate(460, 50)">
          <rect x="0" y="0" width="180" height="85" rx="6" class="node-box"/>
          {render_icon("lock", 12, 10, size=20, color="#e0c58e")}
          <text x="38" y="25" class="text-h2">Embedding &amp; ACL</text>
          <text x="12" y="50" class="text-dim">Attach Entra/IAM tags</text>
          <text x="12" y="70" class="text-mono-amber" font-size="11">Dense Vector Gen</text>
        </g>

        <path d="M 650 92 L 675 92" stroke="#e0c58e" stroke-width="1.8" fill="none" marker-end="url(#arr-amber)"/>

        <!-- Node 4: Vector Index Store -->
        <g transform="translate(685, 50)">
          <rect x="0" y="0" width="335" height="85" rx="6" class="node-box-active"/>
          {render_icon("database", 14, 10, size=20, color="#60a5fa")}
          <text x="40" y="25" class="text-h2" fill="#60a5fa">Enterprise Vector &amp; Lexical Index</text>
          <text x="14" y="50" class="text-dim">Hybrid BM25 + Dense Vectors + Metadata filters</text>
          <text x="14" y="70" class="text-mono" font-size="10.5">OpenSearch Serverless &bull; AI Search &bull; Vertex</text>
        </g>

        <!-- Lane 2: Online Request Swimlane -->
        <g transform="translate(0, 165)">
          <rect x="0" y="0" width="1040" height="175" rx="8" class="swimlane-bg"/>
          <rect x="12" y="12" width="220" height="26" rx="4" fill="#1b2434"/>
          <text x="22" y="29" class="text-mono-purple" font-size="12">LANE 2: ONLINE QUERY SERVING</text>

          <!-- Client -->
          <g transform="translate(20, 50)">
            <rect x="0" y="0" width="140" height="105" rx="6" class="node-box"/>
            {render_icon("user", 12, 10, size=20, color="#60a5fa")}
            <text x="36" y="25" class="text-h2">User App</text>
            <text x="12" y="50" class="text-dim">Teams / Web UI</text>
            <text x="12" y="70" class="text-dim">JWT Bearer Token</text>
            <text x="12" y="92" class="text-mono" font-size="11">AuthZ Context</text>
          </g>

          <path d="M 170 102 L 195 102" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>

          <!-- Filtered Retrieval -->
          <g transform="translate(205, 50)">
            <rect x="0" y="0" width="165" height="105" rx="6" class="node-box"/>
            {render_icon("search", 12, 10, size=20, color="#6ee7b7")}
            <text x="36" y="25" class="text-h2">ACL Retrieval</text>
            <text x="12" y="50" class="text-dim">Filter: User in doc.acl</text>
            <text x="12" y="70" class="text-dim">Semantic Reranker</text>
            <text x="12" y="92" class="text-mono-green" font-size="11">Top-3 Chunks Only</text>
          </g>

          <!-- Bi-directional link to Index -->
          <path d="M 285 50 L 285 0 L 750 0 L 750 -30" stroke="#6ee7b7" stroke-width="1.5" stroke-dasharray="4 3" fill="none"/>

          <path d="M 380 102 L 405 102" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- LLM Runtime -->
          <g transform="translate(415, 50)">
            <rect x="0" y="0" width="180" height="105" rx="6" class="node-box-active" stroke="#b4a4e5"/>
            {render_icon("brain_model", 12, 10, size=20, color="#b4a4e5")}
            <text x="36" y="25" class="text-h2" fill="#b4a4e5">Model Inference</text>
            <text x="12" y="50" class="text-dim">Prompt + Evidence</text>
            <text x="12" y="70" class="text-dim">Claude / GPT-4o / Gemini</text>
            <text x="12" y="92" class="text-mono-purple" font-size="11">Prompt Cache Hit: 80%</text>
          </g>

          <path d="M 605 102 L 630 102" stroke="#b4a4e5" stroke-width="1.8" fill="none" marker-end="url(#arr-purple)"/>

          <!-- Guardrails & Action Gate -->
          <g transform="translate(640, 50)">
            <rect x="0" y="0" width="190" height="105" rx="6" class="node-box" stroke="#d98585"/>
            {render_icon("approval", 12, 10, size=20, color="#d98585")}
            <text x="36" y="25" class="text-h2" fill="#d98585">Action Gate &amp; Safety</text>
            <text x="12" y="50" class="text-dim">PII / Hallucination check</text>
            <text x="12" y="70" class="text-dim">Confirm Ticket Create?</text>
            <text x="12" y="92" class="text-mono-coral" font-size="11">Human-in-the-Loop</text>
          </g>

          <path d="M 840 102 L 865 102" stroke="#e0c58e" stroke-width="1.8" fill="none" marker-end="url(#arr-amber)"/>

          <!-- Ticket API -->
          <g transform="translate(875, 50)">
            <rect x="0" y="0" width="145" height="105" rx="6" class="node-box"/>
            {render_icon("ticket", 12, 10, size=20, color="#e0c58e")}
            <text x="36" y="25" class="text-h2">IT Service</text>
            <text x="12" y="50" class="text-dim">Jira / ServiceNow</text>
            <text x="12" y="70" class="text-dim">POST /api/v2/tickets</text>
            <text x="12" y="92" class="text-mono-amber" font-size="11">Draft &rarr; Commit</text>
          </g>
        </g>

        <!-- Bottom: Shared Observability & Telemetry Bus -->
        <g transform="translate(0, 355)">
          <rect x="0" y="0" width="1040" height="42" rx="6" fill="#141c28" stroke="#253245"/>
          <text x="20" y="26" class="text-mono" font-size="11">SHARED OBSERVABILITY BUS:</text>
          <text x="220" y="26" class="text-p">OpenTelemetry Distributed Traces &bull; Audit Trail &bull; Evaluation Golden Sets &bull; Token &amp; OCU Cost Metrics</text>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Separate the offline ingestion lane from the online request serving lane. Emphasize why permission tags must be attached during ingestion.",
        "talkTrack": "Separate the offline lane from the online lane. Offline: documents are prepared, permission labels are attached, and the index is built. Online: a user request goes through the app, retrieval, the model, answer generation, and maybe an approved action. Never mix document indexing pipelines with synchronous user inference paths: permission tags must be attached during Lane 1 so that Lane 2 can enforce identity filtering prior to LLM generation.",
        "timing": "30:00 - 35:00 (5 min)"
    }
}
