# Slide 06: State Persistence & Checkpointing
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon
from ..logos import render_logo_badge

SLIDE_DATA = {
    "index": 6,
    "kicker": "STATE PERSISTENCE",
    "title": "Checkpointer Architecture: Memory, Postgres, and Redis",
    "lead": "Checkpointing snapshots agent state at every super-step, enabling fault recovery and multi-turn threads.",
    "section": "State & Persistence",
    "takeaway": "PostgresSaver provides ACID thread isolation for multi-tenant SaaS; Redis provides sub-millisecond ephemeral state.",
    "notes": {
        "goal": "Examine the technical mechanics of checkpointers across volatile development stores and production distributed databases.",
        "talkTrack": "In production, an agent does not live in a single server process. What happens when your Kubernetes pod restarts midway through a 5-step workflow? Without a checkpointer, the conversation and state are lost. Checkpointers persist the state delta after every super-step. MemorySaver is strictly for unit testing. For enterprise SaaS, PostgresSaver stores snapshots in JSONB with ACID guarantees. For high-throughput chatbots, RedisSaver gives sub-millisecond writes.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Top Orchestrator to Checkpointer Bus -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="1260" height="90" rx="8" class="node-box-active"/>
          <text x="20" y="24" class="text-mono" font-size="11">ORCHESTRATOR EXECUTION ZONE: SUPER-STEP N</text>
          
          <g transform="translate(20, 36)">
            <rect x="0" y="0" width="180" height="38" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="90" y="24" text-anchor="middle" class="text-mono" font-size="11">Node Output: Delta</text>

            <path d="M 180 19 L 260 19" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>
            
            <rect x="270" y="0" width="340" height="38" rx="4" fill="#1e2c42" stroke="#60a5fa"/>
            <text x="440" y="24" text-anchor="middle" class="text-mono" font-size="11">checkpointer.put(config, checkpoint, metadata)</text>

            <path d="M 610 19 L 690 19" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

            <rect x="700" y="0" width="220" height="38" rx="4" fill="#141c28" stroke="#3b82f6"/>
            <text x="810" y="24" text-anchor="middle" class="text-mono-green" font-size="11">thread_id: 'usr_8921'</text>

            <path d="M 920 19 L 990 19" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>

            <rect x="1000" y="0" width="210" height="38" rx="4" fill="#152420" stroke="#6ee7b7"/>
            <text x="1105" y="24" text-anchor="middle" class="text-mono-green" font-size="11">checkpoint_id: '1ef8...'</text>
          </g>
        </g>

        <!-- Downward Storage Connectors -->
        <path d="M 230 90 L 230 135" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>
        <path d="M 640 90 L 640 135" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>
        <path d="M 1050 90 L 1050 135" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

        <!-- 3 Persistence Tiers -->
        <!-- Tier 1: MemorySaver -->
        <g transform="translate(0, 140)">
          <rect x="0" y="0" width="395" height="260" rx="8" class="node-box"/>
          <rect x="0" y="0" width="395" height="40" rx="8" fill="#1b2434"/>
          {render_icon("memory", 14, 8, size=22, color="#60a5fa")}
          <text x="44" y="26" class="text-h1" fill="#60a5fa">MemorySaver</text>
          
          <g transform="translate(18, 55)">
            <rect x="0" y="0" width="360" height="48" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="12" y="20" class="text-mono" font-size="10.5">STORAGE MECHANISM:</text>
            <text x="12" y="38" class="text-p">In-memory dict: defaultdict(dict)</text>

            <text x="0" y="75" class="text-mono-coral" font-size="10.5">CHARACTERISTICS:</text>
            <text x="0" y="95" class="text-p">&bull; 0ms network latency overhead</text>
            <text x="0" y="115" class="text-p">&bull; Ephemeral: lost immediately on process exit</text>
            <text x="0" y="135" class="text-p">&bull; Single-process only: 0 multi-worker concurrency</text>
            
            <rect x="0" y="152" width="360" height="34" rx="4" fill="#24191d" stroke="#d98585"/>
            <text x="180" y="174" text-anchor="middle" class="text-mono-coral" font-size="10.5">STRICT FIT: Unit Tests &amp; Local CLI Only</text>
          </g>
        </g>

        <!-- Tier 2: PostgresSaver -->
        <g transform="translate(425, 140)">
          <rect x="0" y="0" width="415" height="260" rx="8" class="node-box-active"/>
          <rect x="0" y="0" width="415" height="40" rx="8" fill="#1e2c42"/>
          {render_icon("database", 14, 8, size=22, color="#6ee7b7")}
          <text x="44" y="26" class="text-h1" fill="#6ee7b7">PostgresSaver (Enterprise Default)</text>
          
          <g transform="translate(18, 55)">
            <rect x="0" y="0" width="380" height="48" rx="4" fill="#141c28" stroke="#3b82f6"/>
            <text x="12" y="20" class="text-mono-green" font-size="10.5">TABLES: checkpoints &amp; checkpoint_writes</text>
            <text x="12" y="38" class="text-p">JSONB state blobs + version sequence numbers</text>

            <text x="0" y="75" class="text-mono-green" font-size="10.5">CHARACTERISTICS:</text>
            <text x="0" y="95" class="text-p">&bull; Full ACID transactions &amp; thread isolation</text>
            <text x="0" y="115" class="text-p">&bull; Multi-pod Kubernetes safe (read-after-write)</text>
            <text x="0" y="135" class="text-p">&bull; Permanent audit log for regulatory compliance</text>
            
            <rect x="0" y="152" width="380" height="34" rx="4" fill="#152420" stroke="#6ee7b7"/>
            <text x="190" y="174" text-anchor="middle" class="text-mono-green" font-size="10.5">STRICT FIT: Enterprise SaaS &amp; HITL Workflows</text>
          </g>
        </g>

        <!-- Tier 3: RedisSaver -->
        <g transform="translate(865, 140)">
          <rect x="0" y="0" width="395" height="260" rx="8" class="node-box"/>
          <rect x="0" y="0" width="395" height="40" rx="8" fill="#1b2434"/>
          {render_icon("checkpoint", 14, 8, size=22, color="#e0c58e")}
          <text x="44" y="26" class="text-h1" fill="#e0c58e">RedisSaver</text>
          
          <g transform="translate(18, 55)">
            <rect x="0" y="0" width="360" height="48" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="12" y="20" class="text-mono-amber" font-size="10.5">STORAGE MECHANISM:</text>
            <text x="12" y="38" class="text-p">Redis Hashes / Strings with thread key prefixes</text>

            <text x="0" y="75" class="text-mono-amber" font-size="10.5">CHARACTERISTICS:</text>
            <text x="0" y="95" class="text-p">&bull; Sub-millisecond write performance (&lt;2ms)</text>
            <text x="0" y="115" class="text-p">&bull; Built-in TTL expiration for ephemeral sessions</text>
            <text x="0" y="135" class="text-p">&bull; Redis Cluster support for multi-region scale</text>
            
            <rect x="0" y="152" width="360" height="34" rx="4" fill="#2d2516" stroke="#e0c58e"/>
            <text x="180" y="174" text-anchor="middle" class="text-mono-amber" font-size="10.5">STRICT FIT: Real-Time High-RPS Chatbots</text>
          </g>
        </g>
      </g>
    """)
}
