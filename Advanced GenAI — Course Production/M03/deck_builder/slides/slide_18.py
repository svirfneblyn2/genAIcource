# -*- coding: utf-8 -*-
slide_data = {
    "index": 18,
    "badge": "DATABASE SELECTION",
    "title": "Vector Database Landscape: Managed Cloud vs Self-Hosted",
    "subtitle": "Architectural trade-offs across data privacy, operations overhead, and latency tiers.",
    "takeaway_tag": "ENGINEERING CHOICE",
    "takeaway": "Managed cloud vector DBs accelerate time to market: self-hosted (Qdrant/pgvector) guarantees data sovereignty.",
    "notes": """
      <h4>Database Comparison</h4>
      <p>Evaluate managed SaaS (Pinecone, Azure AI Search, Bedrock KB) vs self-hosted (Qdrant, Milvus, pgvector). Focus on operational burden, security boundaries, and scaling limits.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: Managed Cloud SaaS -->
      <g transform="translate(40, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#60a5fa">MANAGED CLOUD SAAS (Pinecone, Azure Search, Bedrock KB)</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10" fill="#6ee7b7">Key Advantages:</text>
          <text x="12" y="38" class="text-p" font-size="9.5">+ Zero infrastructure maintenance or GPU cluster ops</text>
          <text x="12" y="52" class="text-p" font-size="9.5">+ Automated serverless scaling, backups, and high availability</text>

          <rect y="70" width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10" fill="#60a5fa">Ecosystem Integration:</text>
          <text x="12" y="38" class="text-p" font-size="9.5">+ Native IAM / Entra ID role mapping</text>
          <text x="12" y="52" class="text-p" font-size="9.5">+ Pre-built connectors for S3, SharePoint, Blob</text>

          <rect y="140" width="320" height="75" rx="4" fill="#1b2434" stroke="#d98585"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10.5" fill="#d98585">Trade-offs &amp; Constraints:</text>
          <text x="12" y="38" class="text-p" font-size="9">- Higher unit compute pricing and minimum spend floors</text>
          <text x="12" y="52" class="text-p" font-size="9">- Vendor lock-in across proprietary search APIs</text>
          <text x="12" y="66" class="text-dim" font-size="8.5">Data egress outside private corporate VPC boundary</text>
        </g>
      </g>

      <!-- Right: Self-Hosted / Bare Metal -->
      <g transform="translate(460, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#b4a4e5">SELF-HOSTED / EMBEDDED (Qdrant, Milvus, pgvector)</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10" fill="#6ee7b7">Key Advantages:</text>
          <text x="12" y="38" class="text-p" font-size="9.5">+ Complete data sovereignty: air-gapped on-prem or VPC</text>
          <text x="12" y="52" class="text-p" font-size="9.5">+ Predictable flat bare-metal hardware cost</text>

          <rect y="70" width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10" fill="#b4a4e5">Flexibility &amp; Control:</text>
          <text x="12" y="38" class="text-p" font-size="9.5">+ Custom index tuning (M, efSearch, PQ centroids)</text>
          <text x="12" y="52" class="text-p" font-size="9.5">+ Direct integration with existing PostgreSQL (pgvector)</text>

          <rect y="140" width="320" height="75" rx="4" fill="#1b2434" stroke="#d98585"/>
          <text x="12" y="20" class="text-mono-bold" font-size="10.5" fill="#d98585">Trade-offs &amp; Constraints:</text>
          <text x="12" y="38" class="text-p" font-size="9">- Requires dedicated 24/7 database operations team</text>
          <text x="12" y="52" class="text-p" font-size="9">- Complex sharding, snapshotting, and memory tuning</text>
          <text x="12" y="66" class="text-dim" font-size="8.5">Scaling requires manual Kubernetes cluster management</text>
        </g>
      </g>
    </svg>"""
}
