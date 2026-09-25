# Slide 10: Platform Capability Heatmap
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 10,
    "kicker": "COMPARATIVE MATRIX",
    "title": "Qualitative Feature Matrix for the Support Assistant",
    "lead": "Evaluating AWS, Azure, and Google Cloud across 8 enterprise dimensions.",
    "section": "Comparative Evaluation",
    "takeaway": "No single cloud wins every category: the optimal choice is anchored to where enterprise data and identity already live.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 20)">
        <!-- Table Header -->
        <rect x="0" y="0" width="1040" height="38" rx="6" fill="#1b2434" stroke="#253245"/>
        <text x="24" y="24" class="text-mono" font-size="12" fill="#cbd5e1">ARCHITECTURAL DIMENSION</text>
        <text x="360" y="24" class="text-mono" font-size="12" fill="#60a5fa">AWS BEDROCK</text>
        <text x="600" y="24" class="text-mono" font-size="12" fill="#b4a4e5">AZURE AI FOUNDRY</text>
        <text x="830" y="24" class="text-mono" font-size="12" fill="#e0c58e">GOOGLE CLOUD</text>

        <!-- Rows Definition -->
        <!-- Row 1: Model Breadth -->
        <g transform="translate(0, 44)">
          <rect x="0" y="0" width="1040" height="38" rx="4" fill="#141c28" stroke="#1e293b"/>
          <text x="24" y="24" class="text-p" fill="#f8fafc">1. Frontier Model Access</text>
          
          <rect x="335" y="7" width="205" height="24" rx="4" fill="#1e2c42" stroke="#60a5fa"/>
          <text x="437" y="23" text-anchor="middle" class="text-mono" font-size="10.5">Strong (Claude, Nova)</text>
          
          <rect x="565" y="7" width="220" height="24" rx="4" fill="#2d223f" stroke="#b4a4e5"/>
          <text x="675" y="23" text-anchor="middle" class="text-mono-purple" font-size="10.5">Differentiator (OpenAI)</text>

          <rect x="805" y="7" width="215" height="24" rx="4" fill="#2d2516" stroke="#e0c58e"/>
          <text x="912" y="23" text-anchor="middle" class="text-mono-amber" font-size="10.5">Strong (Gemini 2.0)</text>
        </g>

        <!-- Row 2: Managed RAG -->
        <g transform="translate(0, 88)">
          <rect x="0" y="0" width="1040" height="38" rx="4" fill="#121824" stroke="#1e293b"/>
          <text x="24" y="24" class="text-p" fill="#f8fafc">2. Managed RAG &amp; Reranking</text>
          
          <rect x="335" y="7" width="205" height="24" rx="4" fill="#172233" stroke="#253245"/>
          <text x="437" y="23" text-anchor="middle" class="text-dim" font-size="10.5">Baseline (Bedrock KB)</text>
          
          <rect x="565" y="7" width="220" height="24" rx="4" fill="#2d223f" stroke="#b4a4e5"/>
          <text x="675" y="23" text-anchor="middle" class="text-mono-purple" font-size="10.5">Differentiator (AI Search)</text>

          <rect x="805" y="7" width="215" height="24" rx="4" fill="#2d2516" stroke="#e0c58e"/>
          <text x="912" y="23" text-anchor="middle" class="text-mono-amber" font-size="10.5">Strong (Vertex Ground)</text>
        </g>

        <!-- Row 3: Agent Orchestration -->
        <g transform="translate(0, 132)">
          <rect x="0" y="0" width="1040" height="38" rx="4" fill="#141c28" stroke="#1e293b"/>
          <text x="24" y="24" class="text-p" fill="#f8fafc">3. Agent Runtime &amp; Tools</text>
          
          <rect x="335" y="7" width="205" height="24" rx="4" fill="#1e2c42" stroke="#60a5fa"/>
          <text x="437" y="23" text-anchor="middle" class="text-mono" font-size="10.5">Strong (AgentCore)</text>
          
          <rect x="565" y="7" width="220" height="24" rx="4" fill="#221e33" stroke="#253245"/>
          <text x="675" y="23" text-anchor="middle" class="text-dim" font-size="10.5">Baseline (Foundry Agent)</text>

          <rect x="805" y="7" width="215" height="24" rx="4" fill="#2d2516" stroke="#e0c58e"/>
          <text x="912" y="23" text-anchor="middle" class="text-mono-amber" font-size="10.5">Strong (Gemini ADK)</text>
        </g>

        <!-- Row 4: Pre/Post Evaluation -->
        <g transform="translate(0, 176)">
          <rect x="0" y="0" width="1040" height="38" rx="4" fill="#121824" stroke="#1e293b"/>
          <text x="24" y="24" class="text-p" fill="#f8fafc">4. Automated Evaluations</text>
          
          <rect x="335" y="7" width="205" height="24" rx="4" fill="#172233" stroke="#253245"/>
          <text x="437" y="23" text-anchor="middle" class="text-dim" font-size="10.5">Baseline (Bedrock Eval)</text>
          
          <rect x="565" y="7" width="220" height="24" rx="4" fill="#2d223f" stroke="#b4a4e5"/>
          <text x="675" y="23" text-anchor="middle" class="text-mono-purple" font-size="10.5">Strong (Foundry Evals)</text>

          <rect x="805" y="7" width="215" height="24" rx="4" fill="#2d2516" stroke="#e0c58e"/>
          <text x="912" y="23" text-anchor="middle" class="text-mono-amber" font-size="10.5">Strong (Vertex GenAI)</text>
        </g>

        <!-- Row 5: Identity & RBAC -->
        <g transform="translate(0, 220)">
          <rect x="0" y="0" width="1040" height="38" rx="4" fill="#141c28" stroke="#1e293b"/>
          <text x="24" y="24" class="text-p" fill="#f8fafc">5. Enterprise Identity &amp; ACLs</text>
          
          <rect x="335" y="7" width="205" height="24" rx="4" fill="#1e2c42" stroke="#60a5fa"/>
          <text x="437" y="23" text-anchor="middle" class="text-mono" font-size="10.5">Strong (IAM Roles)</text>
          
          <rect x="565" y="7" width="220" height="24" rx="4" fill="#2d223f" stroke="#b4a4e5"/>
          <text x="675" y="23" text-anchor="middle" class="text-mono-purple" font-size="10.5">Differentiator (Entra ID)</text>

          <rect x="805" y="7" width="215" height="24" rx="4" fill="#23201a" stroke="#253245"/>
          <text x="912" y="23" text-anchor="middle" class="text-dim" font-size="10.5">Baseline (Cloud ID)</text>
        </g>

        <!-- Row 6: Data Platform Co-location -->
        <g transform="translate(0, 264)">
          <rect x="0" y="0" width="1040" height="38" rx="4" fill="#121824" stroke="#1e293b"/>
          <text x="24" y="24" class="text-p" fill="#f8fafc">6. Data Platform Co-location</text>
          
          <rect x="335" y="7" width="205" height="24" rx="4" fill="#1e2c42" stroke="#60a5fa"/>
          <text x="437" y="23" text-anchor="middle" class="text-mono" font-size="10.5">Strong (S3 &bull; OpenSearch)</text>
          
          <rect x="565" y="7" width="220" height="24" rx="4" fill="#2d223f" stroke="#b4a4e5"/>
          <text x="675" y="23" text-anchor="middle" class="text-mono-purple" font-size="10.5">Strong (Fabric &bull; Cosmos)</text>

          <rect x="805" y="7" width="215" height="24" rx="4" fill="#2d2516" stroke="#e0c58e"/>
          <text x="912" y="23" text-anchor="middle" class="text-mono-amber" font-size="10.5">Differentiator (BigQuery)</text>
        </g>

        <!-- Row 7: Ecosystem Friction -->
        <g transform="translate(0, 308)">
          <rect x="0" y="0" width="1040" height="38" rx="4" fill="#141c28" stroke="#1e293b"/>
          <text x="24" y="24" class="text-p" fill="#f8fafc">7. Organizational Gravity</text>
          
          <rect x="335" y="7" width="205" height="24" rx="4" fill="#1e2c42" stroke="#60a5fa"/>
          <text x="437" y="23" text-anchor="middle" class="text-mono" font-size="10.5">Native for AWS Estates</text>
          
          <rect x="565" y="7" width="220" height="24" rx="4" fill="#2d223f" stroke="#b4a4e5"/>
          <text x="675" y="23" text-anchor="middle" class="text-mono-purple" font-size="10.5">Native for M365 Shops</text>

          <rect x="805" y="7" width="215" height="24" rx="4" fill="#2d2516" stroke="#e0c58e"/>
          <text x="912" y="23" text-anchor="middle" class="text-mono-amber" font-size="10.5">Native for Data / GCP</text>
        </g>

        <!-- Row 8: Context Caching & Cost -->
        <g transform="translate(0, 352)">
          <rect x="0" y="0" width="1040" height="38" rx="4" fill="#121824" stroke="#1e293b"/>
          <text x="24" y="24" class="text-p" fill="#f8fafc">8. Long-Context &amp; Caching</text>
          
          <rect x="335" y="7" width="205" height="24" rx="4" fill="#1e2c42" stroke="#60a5fa"/>
          <text x="437" y="23" text-anchor="middle" class="text-mono" font-size="10.5">Prompt Cache (Claude)</text>
          
          <rect x="565" y="7" width="220" height="24" rx="4" fill="#221e33" stroke="#253245"/>
          <text x="675" y="23" text-anchor="middle" class="text-dim" font-size="10.5">Prompt Cache (OpenAI)</text>

          <rect x="805" y="7" width="215" height="24" rx="4" fill="#2d2516" stroke="#e0c58e"/>
          <text x="912" y="23" text-anchor="middle" class="text-mono-amber" font-size="10.5">Differentiator (2M Cache)</text>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Use the heatmap as a heuristic framework for the support assistant case, not as an absolute vendor scoreboard.",
        "talkTrack": "Use the heatmap as a heuristic. Do not read it like a benchmark. It tells students what to investigate during selection: model breadth, RAG, agent runtime, evaluation, identity, data integration, ecosystem fit, and cost predictability. Every cloud has clear strong points: Azure leads in corporate identity and M365 grounding; Google leads in long-context analytics and BigQuery co-location; AWS leads in serverless operational rigor and VPC security integration.",
        "timing": "45:00 - 50:00 (5 min)"
    }
}
