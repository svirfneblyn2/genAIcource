# Slide 27: Final Synthesis & Architectural Takeaways
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 27,
    "kicker": "SYNTHESIS & CONCLUSION",
    "title": "The Cloud AI Golden Rule",
    "lead": "Managed platforms remove infrastructure work: they do not remove architecture decisions.",
    "section": "Course Synthesis",
    "takeaway": "Cloud platforms manage servers and models: you remain fully responsible for system architecture and business trust.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 20)">
        <!-- Center Hub: The Golden Rule Banner -->
        <g transform="translate(295, 140)">
          <rect x="0" y="0" width="450" height="115" rx="10" fill="#1b2434" stroke="#e0c58e" stroke-width="2"/>
          {render_icon("shield", 205, 14, size=38, color="#e0c58e")}
          <text x="225" y="72" text-anchor="middle" class="text-h1" font-size="18" fill="#e0c58e">THE CLOUD AI GOLDEN RULE</text>
          <text x="225" y="96" text-anchor="middle" class="text-p">Cloud platforms manage the models and hardware.</text>
          <text x="225" y="112" text-anchor="middle" class="text-p" fill="#f8fafc">You own the boundaries, trust, and business risk.</text>
        </g>

        <!-- Surrounding Satellite Cards (5 Permanent Questions) -->
        <!-- Q1: Grounding -->
        <g transform="translate(30, 25)">
          <rect x="0" y="0" width="280" height="95" rx="6" class="node-box"/>
          {render_icon("search", 14, 12, size=22, color="#60a5fa")}
          <text x="44" y="28" class="text-h2" fill="#60a5fa">1. Evidence &amp; Grounding</text>
          <text x="14" y="52" class="text-p">Where does the factual evidence live?</text>
          <text x="14" y="72" class="text-dim">Never rely on model memory alone.</text>
          <path d="M 280 60 L 330 140" stroke="#60a5fa" stroke-width="1.5" stroke-dasharray="3 3" fill="none"/>
        </g>

        <!-- Q2: Identity -->
        <g transform="translate(730, 25)">
          <rect x="0" y="0" width="280" height="95" rx="6" class="node-box"/>
          {render_icon("lock", 14, 12, size=22, color="#6ee7b7")}
          <text x="44" y="28" class="text-h2" fill="#6ee7b7">2. Identity &amp; ACLs</text>
          <text x="14" y="52" class="text-p">Who is authorized to see each chunk?</text>
          <text x="14" y="72" class="text-dim">Trim documents before prompt injection.</text>
          <path d="M 730 60 L 710 140" stroke="#6ee7b7" stroke-width="1.5" stroke-dasharray="3 3" fill="none"/>
        </g>

        <!-- Q3: Human Gate -->
        <g transform="translate(0, 280)">
          <rect x="0" y="0" width="295" height="95" rx="6" class="node-box" stroke="#d98585"/>
          {render_icon("approval", 14, 12, size=22, color="#d98585")}
          <text x="44" y="28" class="text-h2" fill="#d98585">3. Human Approval Gates</text>
          <text x="14" y="52" class="text-p">Which actions require human sign-off?</text>
          <text x="14" y="72" class="text-dim">Zero blind ticket/payment execution.</text>
          <path d="M 295 320 L 350 255" stroke="#d98585" stroke-width="1.5" stroke-dasharray="3 3" fill="none"/>
        </g>

        <!-- Q4: Systematic Evaluation -->
        <g transform="translate(370, 280)">
          <rect x="0" y="0" width="300" height="95" rx="6" class="node-box"/>
          {render_icon("evaluation", 14, 12, size=22, color="#b4a4e5")}
          <text x="44" y="28" class="text-h2" fill="#b4a4e5">4. Systematic Evaluation</text>
          <text x="14" y="52" class="text-p">How is quality continuously tested?</text>
          <text x="14" y="72" class="text-dim">Golden sets and automated judges.</text>
          <path d="M 520 280 L 520 255" stroke="#b4a4e5" stroke-width="1.5" stroke-dasharray="3 3" fill="none"/>
        </g>

        <!-- Q5: Observability & TCO -->
        <g transform="translate(745, 280)">
          <rect x="0" y="0" width="295" height="95" rx="6" class="node-box"/>
          {render_icon("monitoring", 14, 12, size=22, color="#e0c58e")}
          <text x="44" y="28" class="text-h2" fill="#e0c58e">5. Observability &amp; TCO</text>
          <text x="14" y="52" class="text-p">How are errors traced and bills tracked?</text>
          <text x="14" y="72" class="text-dim">Vector minimums, OTel spans, tokens.</text>
          <path d="M 745 320 L 690 255" stroke="#e0c58e" stroke-width="1.5" stroke-dasharray="3 3" fill="none"/>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Deliver the final lecture synthesis. Emphasize that managed platforms remove servers, but architecture decisions remain the engineer's responsibility.",
        "talkTrack": "Close with the final statement: managed platforms can remove infrastructure work, but they cannot remove architecture decisions. Read the five closing questions and connect them to the homework. Whether you deploy on AWS Bedrock, Microsoft Azure AI Foundry, or Google Cloud, these five questions will protect your architecture from security vulnerabilities, budget overruns, and quality degradation.",
        "timing": "145:00 - 150:00 (5 min)"
    }
}
