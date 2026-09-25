# Slide 12: AWS: Selection Rationale & Watch-Outs
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 12,
    "kicker": "DECISION LOGIC: AWS",
    "title": "When AWS Bedrock is the Strongest Choice",
    "lead": "Strategic alignment, architectural advantages, and operational gotchas.",
    "section": "Decision Logic: AWS",
    "takeaway": "Choose AWS when your organizational gravity, data lakes, and security controls are already AWS-native.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Left Card: Architectural Alignment & Strengths -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="505" height="395" rx="8" class="node-box-active"/>
          <rect x="0" y="0" width="505" height="46" rx="8" fill="#1b2434"/>
          {render_icon("approval", 16, 11, size=24, color="#60a5fa")}
          <text x="48" y="30" class="text-h1" fill="#60a5fa">Why Choose Amazon Bedrock?</text>
          
          <g transform="translate(20, 60)">
            <!-- Point 1 -->
            <g transform="translate(0, 0)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#6ee7b7">1. Existing AWS Data Gravity</text>
              <text x="14" y="42" class="text-p">Enterprise policy documents, wikis, and databases already</text>
              <text x="14" y="60" class="text-dim">reside inside S3, RDS, or DynamoDB with mature IAM policies.</text>
            </g>

            <!-- Point 2 -->
            <g transform="translate(0, 80)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#6ee7b7">2. Enterprise Claude via Private VPC</text>
              <text x="14" y="42" class="text-p">Direct access to Anthropic Claude 3.5 Sonnet without public</text>
              <text x="14" y="60" class="text-dim">internet egress, routed through private AWS VPC endpoints.</text>
            </g>

            <!-- Point 3 -->
            <g transform="translate(0, 160)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#6ee7b7">3. Serverless Operational Model</text>
              <text x="14" y="42" class="text-p">Zero container clusters or server provisioning: Bedrock handles</text>
              <text x="14" y="60" class="text-dim">auto-scaling, cold-starts, and multi-AZ operational redundancy.</text>
            </g>

            <!-- Bottom summary box -->
            <g transform="translate(0, 240)">
              <rect x="0" y="0" width="465" height="78" rx="6" fill="#172233" stroke="#3b82f6" stroke-width="1.2"/>
              <text x="14" y="24" class="text-mono" font-size="11">ORGANIZATIONAL ALIGNMENT</text>
              <text x="14" y="46" class="text-p">Strongest when the company is already an AWS shop: security,</text>
              <text x="14" y="64" class="text-dim">DevOps, IAM roles, and procurement pipelines are already in place.</text>
            </g>
          </g>
        </g>

        <!-- Right Card: Watch-outs & Architectural Constraints -->
        <g transform="translate(535, 0)">
          <rect x="0" y="0" width="505" height="395" rx="8" class="node-box" stroke="#d98585"/>
          <rect x="0" y="0" width="505" height="46" rx="8" fill="#2d1c22"/>
          {render_icon("alert", 16, 11, size=24, color="#d98585")}
          <text x="48" y="30" class="text-h1" fill="#d98585">Watch-Outs &amp; Operational Gotchas</text>
          
          <g transform="translate(20, 60)">
            <!-- Watch-out 1 -->
            <g transform="translate(0, 0)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#d98585">1. OpenSearch Serverless Cost Floor</text>
              <text x="14" y="42" class="text-p">Requires a minimum of 4 OCUs (2 search + 2 indexing),</text>
              <text x="14" y="60" class="text-dim">creating a fixed cost floor of ~$700/mo even for low-traffic PoCs.</text>
            </g>

            <!-- Watch-out 2 -->
            <g transform="translate(0, 80)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#d98585">2. Knowledge Bases Chunking Rigidity</text>
              <text x="14" y="42" class="text-p">Standard chunking splits complex PDF tables poorly; custom</text>
              <text x="14" y="60" class="text-dim">chunking requires building an external Lambda preprocessing step.</text>
            </g>

            <!-- Watch-out 3 -->
            <g transform="translate(0, 160)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#d98585">3. Cross-Region Routing &amp; Quotas</text>
              <text x="14" y="42" class="text-p">Claude 3.5 capacity in US-East-1 requires setting up</text>
              <text x="14" y="60" class="text-dim">cross-region inference profiles to avoid 429 Throttling exceptions.</text>
            </g>

            <!-- Bottom mitigation box -->
            <g transform="translate(0, 240)">
              <rect x="0" y="0" width="465" height="78" rx="6" fill="#24191d" stroke="#d98585" stroke-width="1.2"/>
              <text x="14" y="24" class="text-mono-coral" font-size="11">ARCHITECTURAL MITIGATION</text>
              <text x="14" y="46" class="text-p">For pilot workloads under 10k queries/month, use Amazon Aurora</text>
              <text x="14" y="64" class="text-dim">PostgreSQL with pgvector instead of OpenSearch Serverless.</text>
            </g>
          </g>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Translate AWS capabilities into real selection logic. Explain organizational gravity and warn students about the OpenSearch Serverless OCU cost floor.",
        "talkTrack": "Translate AWS into selection logic. AWS is a strong choice when the organization is already AWS-heavy, when data and applications live there, and when the team wants GenAI close to existing IAM, networking, logging, and platform operations. But watch out: OpenSearch Serverless has a minimum 4 OCU allocation (2 for indexing, 2 for search), which means your vector database costs ~$700/month before you ever process a single query! If you are building a small PoC, consider Aurora PostgreSQL with pgvector instead.",
        "timing": "55:00 - 60:00 (5 min)"
    }
}
