# Slide 09: Sandboxing & Execution Isolation
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon
from ..logos import render_logo_badge

SLIDE_DATA = {
    "index": 9,
    "kicker": "SECURITY & ISOLATION",
    "title": "Execution Sandboxing: In-Process vs. Docker vs. MicroVMs",
    "lead": "Isolating untrusted model code generation and external tools from the production host environment.",
    "section": "Tools & Sandboxing",
    "takeaway": "Never execute LLM-generated code in the host process; enforce ephemeral microVM isolation with strict network egress controls.",
    "notes": {
        "goal": "Evaluate the 3 tiers of code sandboxing security, contrasting in-process execution with containers and Firecracker microVMs.",
        "talkTrack": "When an agent generates Python code or executes shell scripts, running that code inside your orchestrator process is catastrophic. A prompt injection can read os.environ, exfiltrate AWS credentials, or run a fork bomb. In enterprise production, we mandate hardware-isolated sandboxes. While Docker provides namespace isolation, Firecracker microVMs (used by E2B and AWS Lambda) give full hardware virtualization with 150ms boot times.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- 3 Isolation Tiers -->
        <!-- Tier 1: In-Process -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="395" height="400" rx="8" class="node-box"/>
          <rect x="0" y="0" width="395" height="44" rx="8" fill="#24191d"/>
          {render_icon("alert", 14, 10, size=24, color="#d98585")}
          <text x="44" y="28" class="text-h1" fill="#d98585">1. In-Process (Dangerous)</text>
          
          <g transform="translate(18, 58)">
            <rect x="0" y="0" width="360" height="95" rx="6" fill="#141c28" stroke="#d98585" stroke-width="1.5"/>
            <text x="14" y="24" class="text-mono-coral" font-size="11">EXECUTION ENVIRONMENT:</text>
            <text x="14" y="46" class="text-p">exec(code) or subprocess.run() in host container</text>
            <text x="14" y="66" class="text-dim">Shares memory, file descriptors, and environment</text>
            <text x="14" y="86" class="text-mono-coral" font-size="10.5">ISOLATION LEVEL: ZERO (0)</text>

            <g transform="translate(0, 110)">
              <rect x="0" y="0" width="360" height="135" rx="6" fill="#111722" stroke="#253245"/>
              <text x="14" y="24" class="text-mono-coral" font-size="10.5">CRITICAL ATTACK VECTORS:</text>
              <text x="14" y="48" class="text-p">&bull; Env exfiltration: os.environ['DB_PASS']</text>
              <text x="14" y="70" class="text-p">&bull; Filesystem wipe: shutil.rmtree('/')</text>
              <text x="14" y="92" class="text-p">&bull; Host resource exhaustion / fork bombs</text>
              <text x="14" y="114" class="text-p">&bull; SSRF to cloud metadata (169.254.169.254)</text>
            </g>

            <rect x="0" y="260" width="360" height="60" rx="4" fill="#24191d" stroke="#d98585"/>
            <text x="180" y="285" text-anchor="middle" class="text-mono-coral" font-size="11">PROHIBITED IN PRODUCTION</text>
            <text x="180" y="305" text-anchor="middle" class="text-dim">Acceptable only for pure math tools</text>
          </g>
        </g>

        <!-- Tier 2: Docker Containers -->
        <g transform="translate(425, 0)">
          <rect x="0" y="0" width="415" height="400" rx="8" class="node-box"/>
          <rect x="0" y="0" width="415" height="44" rx="8" fill="#1b2434"/>
          {render_icon("sandbox", 14, 10, size=24, color="#60a5fa")}
          <text x="44" y="28" class="text-h1" fill="#60a5fa">2. Container Sandbox (Docker)</text>

          <g transform="translate(18, 58)">
            <rect x="0" y="0" width="380" height="95" rx="6" fill="#141c28" stroke="#3b82f6"/>
            <text x="14" y="24" class="text-mono" font-size="11">EXECUTION ENVIRONMENT:</text>
            <text x="14" y="46" class="text-p">Ephemeral Docker container with cgroups &amp; namespaces</text>
            <text x="14" y="66" class="text-dim">Volume mounted with read-only root filesystem</text>
            <text x="14" y="86" class="text-mono-blue" font-size="10.5">ISOLATION LEVEL: OS NAMESPACE</text>

            <g transform="translate(0, 110)">
              <rect x="0" y="0" width="380" height="135" rx="6" fill="#111722" stroke="#253245"/>
              <text x="14" y="24" class="text-mono" font-size="10.5">ENGINEERING SPECS:</text>
              <text x="14" y="48" class="text-p">&bull; Startup latency: 800ms - 2,500ms (container spin)</text>
              <text x="14" y="70" class="text-p">&bull; Shared Linux host kernel (kernel exploit risk)</text>
              <text x="14" y="92" class="text-p">&bull; Requires pre-warmed container pools</text>
              <text x="14" y="114" class="text-p">&bull; Requires --cap-drop=ALL and no-new-privileges</text>
            </g>

            <rect x="0" y="260" width="380" height="60" rx="4" fill="#172233" stroke="#3b82f6"/>
            <text x="190" y="285" text-anchor="middle" class="text-mono" font-size="11">ACCEPTABLE WITH HARDENED CGROUPS</text>
            <text x="190" y="305" text-anchor="middle" class="text-dim">Good for predictable internal batch jobs</text>
          </g>
        </g>

        <!-- Tier 3: MicroVMs (E2B / Firecracker) -->
        <g transform="translate(865, 0)">
          <rect x="0" y="0" width="395" height="400" rx="8" class="node-box-active"/>
          <rect x="0" y="0" width="395" height="44" rx="8" fill="#1e2c42"/>
          {render_icon("shield", 14, 10, size=24, color="#6ee7b7")}
          <text x="44" y="28" class="text-h1" fill="#6ee7b7">3. MicroVMs (E2B / Firecracker)</text>

          <g transform="translate(18, 58)">
            <rect x="0" y="0" width="360" height="95" rx="6" fill="#152420" stroke="#6ee7b7"/>
            <text x="14" y="24" class="text-mono-green" font-size="11">EXECUTION ENVIRONMENT:</text>
            <text x="14" y="46" class="text-p">Hardware-virtualized guest kernel (KVM)</text>
            <text x="14" y="66" class="text-dim">Ephemeral guest OS per model execution</text>
            <text x="14" y="86" class="text-mono-green" font-size="10.5">ISOLATION LEVEL: HARDWARE VIRTUALIZATION</text>

            <g transform="translate(0, 110)">
              <rect x="0" y="0" width="360" height="135" rx="6" fill="#111722" stroke="#253245"/>
              <text x="14" y="24" class="text-mono-green" font-size="10.5">ENTERPRISE GOLD STANDARD:</text>
              <text x="14" y="48" class="text-p">&bull; Ultra-fast cold start: ~150ms boot</text>
              <text x="14" y="70" class="text-p">&bull; Zero host kernel sharing (KVM boundary)</text>
              <text x="14" y="92" class="text-p">&bull; Strict network egress allowlist by domain</text>
              <text x="14" y="114" class="text-p">&bull; Automatic teardown upon completion</text>
            </g>

            <rect x="0" y="260" width="360" height="60" rx="4" fill="#152420" stroke="#6ee7b7"/>
            <text x="180" y="285" text-anchor="middle" class="text-mono-green" font-size="11">RECOMMENDED PRODUCTION STANDARD</text>
            <text x="180" y="305" text-anchor="middle" class="text-dim">E2B Sandboxes / AWS Firecracker</text>
          </g>
        </g>
      </g>
    """)
}
