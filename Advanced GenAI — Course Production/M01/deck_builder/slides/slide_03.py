# Slide 03: Why Cloud AI Platforms Matter: The Iceberg Problem
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 3,
    "kicker": "PRODUCTION REALITY",
    "title": "Moving Beyond the Prototype: The Iceberg Problem",
    "lead": "A raw model endpoint is only 15% of a production GenAI system.",
    "section": "Production Context",
    "takeaway": "Managed cloud platforms package the boring 85% so teams avoid building custom infrastructure from scratch.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Left side: The Iceberg visual -->
        <g transform="translate(0, 0)">
          <!-- Sky & Water boundary -->
          <rect x="0" y="0" width="500" height="395" rx="8" fill="#121824" stroke="#253245"/>
          
          <!-- Waterline -->
          <line x1="0" y1="120" x2="500" y2="120" stroke="#3b82f6" stroke-width="2" stroke-dasharray="6 4"/>
          <text x="480" y="112" text-anchor="end" class="text-mono" font-size="11">WATERLINE: PROTOTYPE VS PRODUCTION</text>

          <!-- Tip of Iceberg (15%) -->
          <polygon points="250,30 360,115 140,115" fill="#1e2c42" stroke="#60a5fa" stroke-width="2"/>
          <text x="250" y="65" text-anchor="middle" class="text-mono" fill="#ffffff" font-weight="700">VISIBLE TIP: 15%</text>
          <text x="250" y="85" text-anchor="middle" class="text-p">Prompt &rarr; Model API &rarr; Output</text>
          <text x="250" y="103" text-anchor="middle" class="text-dim">What developer tutorials show</text>

          <!-- Submerged Body of Iceberg (85%) -->
          <polygon points="140,125 360,125 460,370 40,370" fill="#151d2a" stroke="#364761" stroke-width="1.8"/>
          
          <text x="250" y="155" text-anchor="middle" class="text-mono-coral" font-weight="700" font-size="13">SUBMERGED FOUNDATION: 85%</text>
          <text x="250" y="175" text-anchor="middle" class="text-p">The mandatory enterprise plumbing</text>

          <!-- Submerged items -->
          <g transform="translate(70, 195)">
            <rect x="0" y="0" width="360" height="32" rx="4" fill="#1a2434" stroke="#253245"/>
            {render_icon("lock", 10, 4, size=20, color="#60a5fa")}
            <text x="38" y="21" class="text-p">Enterprise Identity: SSO, IAM Roles &amp; JWT Validation</text>

            <rect x="0" y="40" width="360" height="32" rx="4" fill="#1a2434" stroke="#253245"/>
            {render_icon("shield", 10, 44, size=20, color="#6ee7b7")}
            <text x="38" y="61" class="text-p">Document Permissions: Fine-grained ACL Trimming</text>

            <rect x="0" y="80" width="360" height="32" rx="4" fill="#1a2434" stroke="#253245"/>
            {render_icon("search", 10, 84, size=20, color="#e0c58e")}
            <text x="38" y="101" class="text-p">Hybrid Retrieval: BM25, Dense Vector, Reranking</text>

            <rect x="0" y="120" width="360" height="32" rx="4" fill="#1a2434" stroke="#253245"/>
            {render_icon("monitoring", 10, 124, size=20, color="#b4a4e5")}
            <text x="38" y="141" class="text-p">Distributed Tracing: OpenTelemetry &amp; Audit Logs</text>
          </g>
        </g>

        <!-- Right side: Systems Comparison Table & Rationale -->
        <g transform="translate(535, 0)">
          <rect x="0" y="0" width="505" height="395" rx="8" class="node-box"/>
          <rect x="0" y="0" width="505" height="42" rx="8" fill="#1b2434"/>
          <text x="252" y="27" text-anchor="middle" class="text-h1">Prototype Failures vs Production Reality</text>

          <!-- Row 1 -->
          <g transform="translate(20, 52)">
            <rect x="0" y="0" width="465" height="68" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="14" y="20" class="text-mono-coral">Failure Mode 1: Data Leaks &amp; ACL Bypasses</text>
            <text x="14" y="40" class="text-p">Naive RAG indexes all corporate documents into a flat vector store.</text>
            <text x="14" y="58" class="text-dim">Result: Standard users retrieve restricted executive payroll records.</text>
          </g>

          <!-- Row 2 -->
          <g transform="translate(20, 128)">
            <rect x="0" y="0" width="465" height="68" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="14" y="20" class="text-mono-coral">Failure Mode 2: Unbounded Latency &amp; Cost</text>
            <text x="14" y="40" class="text-p">Zero semantic caching, uncompressed system prompts, and loops</text>
            <text x="14" y="58" class="text-dim">spinning autonomously on ambiguous questions inflate bills 10x.</text>
          </g>

          <!-- Row 3 -->
          <g transform="translate(20, 204)">
            <rect x="0" y="0" width="465" height="68" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="14" y="20" class="text-mono-coral">Failure Mode 3: Silent Quality Degradation</text>
            <text x="14" y="40" class="text-p">Document updates break table chunking: retrieval precision drops</text>
            <text x="14" y="58" class="text-dim">30% with zero regression alerts or CI/CD test gates.</text>
          </g>

          <!-- Managed Platform Promise -->
          <g transform="translate(20, 280)">
            <rect x="0" y="0" width="465" height="102" rx="6" fill="#152232" stroke="#3b82f6" stroke-width="1.2"/>
            {render_icon("cloud", 14, 12, size=24, color="#60a5fa")}
            <text x="46" y="28" class="text-h2" fill="#60a5fa">The Managed Cloud Advantage</text>
            <text x="14" y="52" class="text-p">Cloud platforms package IAM connectors, VPC isolation, vector indices,</text>
            <text x="14" y="70" class="text-p">and automated evaluation so teams deploy securely in days, not quarters.</text>
            <text x="14" y="90" class="text-mono" font-size="11">Focus engineering on business logic, approval gates &amp; golden evals.</text>
          </g>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Contrast a prototype with a production system. Explain that prompt -> model -> text is only 15% of the real architecture.",
        "talkTrack": "Contrast a prototype with a production system. Say that prompt -> model -> text is useful, but not enough for an enterprise workload. Production systems require the boring parts that prevent expensive incidents: identity, data access, retrieval quality, action approvals, evaluation, monitoring, and cost control. Managed cloud platforms package this submerged 85% so teams do not build fragile custom infrastructure from scratch.",
        "timing": "10:00 - 15:00 (5 min)"
    }
}
