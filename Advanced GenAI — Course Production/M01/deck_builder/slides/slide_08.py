# Slide 08: Cloud, Local, or Hybrid Deployment Spectrum
from ..common_svg import svg_frame
from ..icons import render_icon
from ..logos import render_logo, render_logo_badge

SLIDE_DATA = {
    "index": 8,
    "kicker": "DEPLOYMENT STRATEGY",
    "title": "The Tri-Model Deployment Spectrum",
    "lead": "Selecting the operational model based on data classification, volume, and team maturity.",
    "section": "Deployment Strategy",
    "takeaway": "Cloud is an engineering trade-off: adopt self-hosting only when data sovereignty or massive steady-state volume justifies GPU operational overhead.",
    "svg": svg_frame(f"""<g transform="translate(40, 25)">
        <!-- Option 1: Managed Cloud AI -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="330" height="395" rx="8" class="node-box-active"/>
          <rect x="0" y="0" width="330" height="46" rx="8" fill="#1b2434"/>
          {render_icon("cloud", 14, 10, size=24, color="#60a5fa")}
          <text x="46" y="29" class="text-h1" fill="#60a5fa">Managed Cloud AI</text>
          
          <g transform="translate(15, 58)">
            <!-- Mini-Topology Diagram -->
            <rect x="0" y="0" width="300" height="135" rx="6" fill="#111824" stroke="#253245" stroke-width="1.2"/>
            <text x="12" y="18" class="text-mono" font-size="9.5" fill="#64748b">TOPOLOGY: MANAGED VPC ENDPOINT</text>
            
            <!-- App Client Node -->
            <rect x="12" y="30" width="76" height="42" rx="4" fill="#172233" stroke="#3b82f6" stroke-width="1.2"/>
            <text x="50" y="48" text-anchor="middle" class="text-mono" font-size="9.5" fill="#93c5fd">App Client</text>
            <text x="50" y="62" text-anchor="middle" class="text-dim" font-size="8.5">Web / API</text>
            
            <!-- Arrow -->
            <path d="M 88 51 L 114 51" stroke="#60a5fa" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>
            
            <!-- PrivateLink / Gateway -->
            <rect x="120" y="30" width="76" height="42" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="158" y="48" text-anchor="middle" class="text-mono" font-size="9" fill="#cbd5e1">PrivateLink</text>
            <text x="158" y="62" text-anchor="middle" class="text-dim" font-size="8">TLS / IAM</text>
            
            <!-- Arrow -->
            <path d="M 196 51 L 218 51" stroke="#60a5fa" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>
            
            <!-- Managed Cloud Model -->
            <rect x="224" y="24" width="64" height="54" rx="4" fill="#1e2c42" stroke="#60a5fa" stroke-width="1.2"/>
            {render_logo("aws", 246, 28, size=20, color="#60a5fa")}
            <text x="256" y="66" text-anchor="middle" class="text-mono" font-size="8.5" fill="#93c5fd">Bedrock/AI</text>
            
            <!-- Sub-lane: Managed Vector DB -->
            <path d="M 256 78 L 256 88" stroke="#60a5fa" stroke-width="1.2" stroke-dasharray="2 2" fill="none"/>
            <rect x="12" y="88" width="276" height="36" rx="4" fill="#141c28" stroke="#1e293b"/>
            {render_icon("database", 18, 94, size=18, color="#6ee7b7")}
            <text x="42" y="105" class="text-mono" font-size="9" fill="#cbd5e1">Serverless Vector RAG + Guardrails</text>
            <text x="42" y="117" class="text-dim" font-size="8">Zero GPU provisioning &bull; Variable per-token</text>
            
            <!-- Architectural Specs -->
            <g transform="translate(0, 146)">
              <rect x="0" y="0" width="300" height="68" rx="5" fill="#141c28" stroke="#253245"/>
              <text x="12" y="20" class="text-mono-green" font-size="10.5">ENGINEERING METRICS</text>
              <text x="12" y="38" class="text-p">&bull; Ops Overhead: 0 GPU ops or driver patching</text>
              <text x="12" y="56" class="text-p">&bull; Time to Market: Days (instant serverless APIs)</text>
            </g>

            <g transform="translate(0, 222)">
              <rect x="0" y="0" width="300" height="105" rx="6" fill="#172233" stroke="#3b82f6" stroke-width="1.2"/>
              <text x="12" y="22" class="text-mono" font-size="10.5">OPTIMAL PRODUCTION FIT</text>
              <text x="12" y="44" class="text-p">Enterprise apps with variable traffic,</text>
              <text x="12" y="64" class="text-p">strict enterprise SSO/IAM needs, and</text>
              <text x="12" y="84" class="text-p">lean platform engineering teams.</text>
            </g>
          </g>
        </g>

        <!-- Option 2: Local / Self-Hosted -->
        <g transform="translate(355, 0)">
          <rect x="0" y="0" width="330" height="395" rx="8" class="node-box"/>
          <rect x="0" y="0" width="330" height="46" rx="8" fill="#1b2434"/>
          {render_icon("database", 14, 10, size=24, color="#6ee7b7")}
          <text x="46" y="29" class="text-h1" fill="#6ee7b7">Local / Self-Hosted</text>
          
          <g transform="translate(15, 58)">
            <!-- Mini-Topology Diagram -->
            <rect x="0" y="0" width="300" height="135" rx="6" fill="#111824" stroke="#253245" stroke-width="1.2"/>
            <text x="12" y="18" class="text-mono-green" font-size="9.5">TOPOLOGY: AIR-GAPPED GPU CLUSTER</text>
            
            <!-- K8s Pod Node -->
            <rect x="12" y="30" width="76" height="42" rx="4" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
            {render_logo("k8s", 16, 38, size=15, color="#6ee7b7")}
            <text x="36" y="48" class="text-mono" font-size="9.5" fill="#a7f3d0">K8s Pod</text>
            <text x="36" y="62" class="text-dim" font-size="8.5">Slurm Job</text>
            
            <!-- Arrow -->
            <path d="M 88 51 L 114 51" stroke="#6ee7b7" stroke-width="1.5" fill="none" marker-end="url(#arr-green)"/>
            
            <!-- vLLM Engine -->
            <rect x="120" y="30" width="76" height="42" rx="4" fill="#13271f" stroke="#6ee7b7" stroke-width="1.2"/>
            {render_logo("vllm", 126, 38, size=15, color="#6ee7b7")}
            <text x="146" y="48" class="text-mono" font-size="9.5" fill="#6ee7b7">vLLM</text>
            <text x="146" y="62" class="text-dim" font-size="8">PagedAttn</text>
            
            <!-- Arrow -->
            <path d="M 196 51 L 218 51" stroke="#6ee7b7" stroke-width="1.5" fill="none" marker-end="url(#arr-green)"/>
            
            <!-- NVIDIA H100 Hardware -->
            <rect x="224" y="24" width="64" height="54" rx="4" fill="#141c28" stroke="#253245"/>
            {render_logo("nvidia", 230, 30, size=18, color="#a7f3d0")}
            <text x="256" y="66" text-anchor="middle" class="text-mono" font-size="8" fill="#cbd5e1">H100 SXM</text>
            
            <!-- Sub-lane: Local Storage / Weights -->
            <path d="M 158 72 L 158 88" stroke="#6ee7b7" stroke-width="1.2" stroke-dasharray="2 2" fill="none"/>
            <rect x="12" y="88" width="276" height="36" rx="4" fill="#141c28" stroke="#1e293b"/>
            {render_logo("huggingface", 18, 95, size=18, color="#e0c58e")}
            <text x="42" y="105" class="text-mono" font-size="9" fill="#cbd5e1">HF Local Weights + Private Vector DB</text>
            <text x="42" y="117" class="text-dim" font-size="8">100% air-gap data sovereignty &bull; 0 egress</text>
            
            <!-- Architectural Specs -->
            <g transform="translate(0, 146)">
              <rect x="0" y="0" width="300" height="68" rx="5" fill="#141c28" stroke="#253245"/>
              <text x="12" y="20" class="text-mono-coral" font-size="10.5">ENGINEERING METRICS</text>
              <text x="12" y="38" class="text-p">&bull; Ops Overhead: 24/7 CUDA drivers &amp; KV cache ops</text>
              <text x="12" y="56" class="text-p">&bull; Economics: Fixed CapEx at &gt;50M tok/day scale</text>
            </g>

            <g transform="translate(0, 222)">
              <rect x="0" y="0" width="300" height="105" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="12" y="22" class="text-mono-green" font-size="10.5">OPTIMAL PRODUCTION FIT</text>
              <text x="12" y="44" class="text-p">Regulated defense or banking air-gaps, or</text>
              <text x="12" y="64" class="text-p">steady ultra-high volume workloads with</text>
              <text x="12" y="84" class="text-p">dedicated GPU infrastructure teams.</text>
            </g>
          </g>
        </g>

        <!-- Option 3: Hybrid Architecture -->
        <g transform="translate(710, 0)">
          <rect x="0" y="0" width="330" height="395" rx="8" class="node-box"/>
          <rect x="0" y="0" width="330" height="46" rx="8" fill="#1b2434"/>
          {render_icon("network", 14, 10, size=24, color="#e0c58e")}
          <text x="46" y="29" class="text-h1" fill="#e0c58e">Hybrid Architecture</text>
          
          <g transform="translate(15, 58)">
            <!-- Mini-Topology Diagram -->
            <rect x="0" y="0" width="300" height="135" rx="6" fill="#111824" stroke="#253245" stroke-width="1.2"/>
            <text x="12" y="18" class="text-mono-amber" font-size="9.5">TOPOLOGY: SPLIT-PLANE ORCHESTRATION</text>
            
            <!-- Cloud Plane Node -->
            <rect x="12" y="30" width="120" height="42" rx="4" fill="#172233" stroke="#e0c58e" stroke-width="1.2"/>
            {render_icon("cloud", 16, 38, size=16, color="#e0c58e")}
            <text x="36" y="48" class="text-mono" font-size="9" fill="#fde68a">Cloud Control</text>
            <text x="36" y="62" class="text-dim" font-size="8">Prompts &amp; Evals</text>
            
            <!-- DirectConnect Pipe -->
            <g transform="translate(136, 38)">
              <line x1="0" y1="12" x2="24" y2="12" stroke="#e0c58e" stroke-width="2"/>
              <text x="12" y="8" text-anchor="middle" class="text-mono" font-size="7.5" fill="#e0c58e">TLS</text>
            </g>
            
            <!-- On-Prem Boundary Node -->
            <rect x="164" y="30" width="124" height="42" rx="4" fill="#141c28" stroke="#253245"/>
            {render_icon("lock", 170, 38, size=16, color="#6ee7b7")}
            <text x="190" y="48" class="text-mono" font-size="9" fill="#cbd5e1">On-Prem DB</text>
            <text x="190" y="62" class="text-dim" font-size="8">Firewall Boundary</text>
            
            <!-- Sub-lane: Split execution -->
            <path d="M 72 72 L 72 88" stroke="#e0c58e" stroke-width="1.2" stroke-dasharray="2 2" fill="none"/>
            <rect x="12" y="88" width="276" height="36" rx="4" fill="#141c28" stroke="#1e293b"/>
            {render_icon("shield", 18, 94, size=18, color="#e0c58e")}
            <text x="42" y="105" class="text-mono" font-size="9" fill="#cbd5e1">Local Embeddings + Sanitized Cloud LLM</text>
            <text x="42" y="117" class="text-dim" font-size="8">PII stripped before transit &bull; Data stays local</text>
            
            <!-- Architectural Specs -->
            <g transform="translate(0, 146)">
              <rect x="0" y="0" width="300" height="68" rx="5" fill="#141c28" stroke="#253245"/>
              <text x="12" y="20" class="text-mono-amber" font-size="10.5">ENGINEERING METRICS</text>
              <text x="12" y="38" class="text-p">&bull; Security: Core records stay on-premise</text>
              <text x="12" y="56" class="text-p">&bull; Network: Dedicated DirectConnect / ExpressRoute</text>
            </g>

            <g transform="translate(0, 222)">
              <rect x="0" y="0" width="300" height="105" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="12" y="22" class="text-mono-amber" font-size="10.5">OPTIMAL PRODUCTION FIT</text>
              <text x="12" y="44" class="text-p">Enterprises with heavy database gravity</text>
              <text x="12" y="64" class="text-p">on-premise wanting rapid cloud GenAI rollout</text>
              <text x="12" y="84" class="text-p">without migrating petabytes of core storage.</text>
            </g>
          </g>
        </g>
      </g>"""),
    "notes": {
        "goal": "Explain why cloud is an engineering trade-off rather than an ideology, and detail when local self-hosting or hybrid architectures are justified.",
        "talkTrack": "Explain that cloud is not ideology. Managed cloud is attractive when speed, governance, identity, monitoring, evaluation, and procurement path matter. Local or self-hosted becomes attractive when data isolation or predictable high-volume economics dominate. Hybrid exists because enterprises usually want both control and acceleration. Caution students against premature self-hosting: managing GPU clusters, driver updates, and KV cache scaling is a significant engineering burden.",
        "timing": "35:00 - 40:00 (5 min)"
    }
}
