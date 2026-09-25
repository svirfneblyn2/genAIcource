# Slide 18: RAG Architecture: Managed SaaS vs Custom Pipeline
from ..common_svg import svg_frame
from ..icons import render_icon
from ..logos import render_logo, render_logo_badge

SLIDE_DATA = {
    "index": 18,
    "kicker": "RETRIEVAL ENGINEERING",
    "title": "Enterprise Knowledge: Managed RAG vs Custom Hybrid Pipeline",
    "lead": "Balancing development velocity against parsing quality and retrieval precision.",
    "section": "Retrieval Engineering",
    "takeaway": "Start with managed cloud RAG for validation; transition to custom chunking and reranking only when retrieval failure rates exceed business tolerance.",
    "svg": svg_frame(f"""<g transform="translate(40, 20)">
        <!-- Top Pipeline: Path A Managed Cloud RAG -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="1040" height="155" rx="8" class="node-box-active"/>
          <rect x="0" y="0" width="1040" height="36" rx="8" fill="#1b2434"/>
          {render_icon("cloud", 14, 8, size=20, color="#60a5fa")}
          <text x="42" y="24" class="text-h1" fill="#60a5fa">Path A: Turnkey Managed Cloud RAG (Black-Box Conveyor)</text>
          <rect x="740" y="6" width="285" height="24" rx="4" fill="#162924"/>
          <text x="882" y="22" text-anchor="middle" class="text-mono-green" font-size="10.5">SPEED: 2 TO 5 DAYS TO DEPLOY</text>

          <!-- Stage 1: Cloud Storage -->
          <g transform="translate(18, 48)">
            <rect x="0" y="0" width="155" height="68" rx="5" class="node-box"/>
            {render_icon("bucket", 10, 10, size=18, color="#60a5fa")}
            <text x="34" y="24" class="text-h2" font-size="12">Cloud Storage</text>
            <text x="12" y="44" class="text-dim">S3 &bull; Blob &bull; Drive</text>
            <text x="12" y="60" class="text-mono" font-size="9.5">Auto-Sync Connector</text>
          </g>

          <path d="M 183 82 L 213 82" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>

          <!-- Stage 2: Managed Ingestion Engine -->
          <g transform="translate(223, 48)">
            <rect x="0" y="0" width="235" height="68" rx="5" class="node-box"/>
            {render_icon("tool", 10, 10, size=18, color="#cbd5e1")}
            <text x="34" y="24" class="text-h2" font-size="12">Managed Ingestion Engine</text>
            <text x="12" y="44" class="text-dim">Bedrock KB &bull; AI Search &bull; Vertex</text>
            <text x="12" y="60" class="text-mono-coral" font-size="9.5">Fixed-token (512/1000) chunking</text>
          </g>

          <path d="M 468 82 L 498 82" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>

          <!-- Stage 3: Managed Vector DB -->
          <g transform="translate(508, 48)">
            <rect x="0" y="0" width="225" height="68" rx="5" class="node-box"/>
            {render_icon("database", 10, 10, size=18, color="#6ee7b7")}
            <text x="34" y="24" class="text-h2" font-size="12">Managed Vector Index</text>
            <text x="12" y="44" class="text-dim">OpenSearch &bull; ScaNN &bull; AI Search</text>
            <text x="12" y="60" class="text-mono-green" font-size="9.5">Zero Index Ops &bull; Auto-scaled</text>
          </g>

          <path d="M 743 82 L 773 82" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Stage 4: Cloud Query API -->
          <g transform="translate(783, 48)">
            <rect x="0" y="0" width="240" height="68" rx="5" class="node-box-active"/>
            {render_icon("api", 10, 10, size=18, color="#60a5fa")}
            <text x="34" y="24" class="text-h2" font-size="12" fill="#60a5fa">RetrieveAndGenerate API</text>
            <text x="12" y="44" class="text-dim">Single SDK call &rarr; Grounded response</text>
            <text x="12" y="60" class="text-mono" font-size="9.5">Opaque relevance scoring</text>
          </g>

          <!-- Bottom Warning Pill -->
          <rect x="18" y="124" width="1004" height="22" rx="3" fill="#141c28"/>
          <text x="28" y="139" class="text-mono-coral" font-size="9.5">TRADEOFF:</text>
          <text x="100" y="139" class="text-dim" font-size="9.5">Standard fixed-token chunking cuts complex multi-row PDF tables and splits footnotes from headers.</text>
        </g>

        <!-- Bottom Pipeline: Path B Custom Modular Pipeline -->
        <g transform="translate(0, 165)">
          <rect x="0" y="0" width="1040" height="195" rx="8" class="node-box"/>
          <rect x="0" y="0" width="1040" height="36" rx="8" fill="#162924"/>
          {render_icon("pipeline", 14, 8, size=20, color="#6ee7b7")}
          <text x="42" y="24" class="text-h1" fill="#6ee7b7">Path B: Custom Modular Hybrid Pipeline (Production Precision)</text>
          <rect x="740" y="6" width="285" height="24" rx="4" fill="#2d2218"/>
          <text x="882" y="22" text-anchor="middle" class="text-mono-amber" font-size="10.5">VELOCITY: 4 TO 8 WEEKS BUILD</text>

          <!-- Step 1: Document Layout Parser -->
          <g transform="translate(18, 48)">
            <rect x="0" y="0" width="175" height="85" rx="5" class="node-box"/>
            {render_icon("document", 10, 10, size=18, color="#e0c58e")}
            <text x="34" y="24" class="text-h2" font-size="11.5">1. Layout &amp; OCR</text>
            <text x="12" y="44" class="text-mono-amber" font-size="9.5">Docling &bull; LlamaParse</text>
            <text x="12" y="62" class="text-dim" font-size="8.5">Extracts tables to</text>
            <text x="12" y="76" class="text-mono-green" font-size="8.5">clean Markdown tables</text>
          </g>

          <path d="M 200 90 L 220 90" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Step 2: Semantic Chunker -->
          <g transform="translate(225, 48)">
            <rect x="0" y="0" width="175" height="85" rx="5" class="node-box"/>
            {render_icon("tool", 10, 10, size=18, color="#6ee7b7")}
            <text x="34" y="24" class="text-h2" font-size="11.5">2. Table Chunker</text>
            <text x="12" y="44" class="text-mono-green" font-size="9.5">Hierarchy &bull; Headings</text>
            <text x="12" y="62" class="text-dim" font-size="8.5">Keeps tables intact;</text>
            <text x="12" y="76" class="text-mono" font-size="8.5">prepends breadcrumbs</text>
          </g>

          <path d="M 407 90 L 427 90" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Step 3: Hybrid Index (Pinecone / Qdrant) -->
          <g transform="translate(432, 48)">
            <rect x="0" y="0" width="195" height="85" rx="5" class="node-box"/>
            {render_logo("pinecone", 10, 10, size=18, color="#6ee7b7")}
            <text x="34" y="24" class="text-h2" font-size="11.5">3. Hybrid Store</text>
            <text x="12" y="44" class="text-mono" font-size="9.5">Pinecone &bull; Qdrant &bull; Milvus</text>
            <text x="12" y="62" class="text-dim" font-size="8.5">Dense Vector + Sparse BM25</text>
            <text x="12" y="76" class="text-mono-purple" font-size="8.5">Retrieves Top-50 candidates</text>
          </g>

          <path d="M 634 90 L 654 90" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Step 4: Cohere Neural Reranker -->
          <g transform="translate(659, 48)">
            <rect x="0" y="0" width="185" height="85" rx="5" class="node-box"/>
            {render_logo("cohere", 10, 10, size=18, color="#b4a4e5")}
            <text x="34" y="24" class="text-h2" font-size="11.5">4. Neural Rerank</text>
            <text x="12" y="44" class="text-mono-purple" font-size="9.5">Cohere Rerank v3.5</text>
            <text x="12" y="62" class="text-dim" font-size="8.5">Cross-encoder reranking</text>
            <text x="12" y="76" class="text-mono-green" font-size="8.5">Top-3 precision chunks</text>
          </g>

          <path d="M 851 90 L 871 90" stroke="#b4a4e5" stroke-width="1.8" fill="none" marker-end="url(#arr-purple)"/>

          <!-- Step 5: LLM Context Window -->
          <g transform="translate(876, 48)">
            <rect x="0" y="0" width="145" height="85" rx="5" class="node-box-active" stroke="#b4a4e5"/>
            {render_icon("brain_model", 10, 10, size=18, color="#b4a4e5")}
            <text x="34" y="24" class="text-h2" font-size="11.5" fill="#b4a4e5">5. Synthesis</text>
            <text x="12" y="44" class="text-mono" font-size="9">Target LLM</text>
            <text x="12" y="62" class="text-dim" font-size="8.5">Accurate table</text>
            <text x="12" y="76" class="text-dim" font-size="8.5">reasoning</text>
          </g>

          <!-- Bottom Summary Pill -->
          <rect x="18" y="146" width="1004" height="38" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="30" y="162" class="text-mono-green" font-size="10">PRODUCTION ARCHITECTURAL RULE:</text>
          <text x="248" y="162" class="text-p">Start with Managed Cloud RAG to validate demand. Upgrade to Custom Pipeline when</text>
          <text x="30" y="176" class="text-p">automated evaluations prove that retrieval failures (table extraction or cross-page correlation) violate business SLAs.</text>
        </g>
      </g>"""),
    "notes": {
        "goal": "Compare managed cloud RAG services with a custom-engineered retrieval pipeline. Provide explicit criteria for when to transition from managed to custom.",
        "talkTrack": "Compare managed RAG and custom RAG. Managed RAG is faster and easier to operate. Custom RAG gives more control over chunking, ranking, permissions, and optimization. The dirty secret of enterprise RAG is that PDF tables and multi-column layouts frequently break standard managed chunkers. Start with managed RAG to validate the application; move to custom parsers only when your evaluation sets prove that retrieval failures are impacting production accuracy.",
        "timing": "85:00 - 90:00 (5 min)"
    }
}
