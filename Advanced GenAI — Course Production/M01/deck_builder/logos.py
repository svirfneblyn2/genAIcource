# Vector SVG Logos for AI Providers and Enterprise SaaS Platforms
# Clean, pixel-perfect, scalable inline SVG paths for 24x24 viewBox

LOGOS = {
    # OpenAI: Canonical 6-fold spiral rosette
    'openai': (
        '<g fill="currentColor">'
        '<path d="M20.5 10.2a5.4 5.4 0 0 0-.4-4.2 5.5 5.5 0 0 0-4.7-2.7 5.4 5.4 0 0 0-3.3 1.1A5.4 5.4 0 0 0 7.8 3a5.5 5.5 0 0 0-5.3 4 5.4 5.4 0 0 0 .8 5.4 5.4 5.4 0 0 0-.4 4.2 5.5 5.5 0 0 0 4.7 2.7 5.4 5.4 0 0 0 3.3-1.1A5.4 5.4 0 0 0 15.2 21a5.5 5.5 0 0 0 5.3-4 5.4 5.4 0 0 0-.8-5.4l.8-1.4zm-7.6 9.4c-1.3 0-2.5-.5-3.4-1.4l.8-.5 3.3-1.9a.8.8 0 0 0 .4-.7v-4.5l1.4.8v3.9a3.7 3.7 0 0 1-2.5 4.3zm-7.6-3.2a3.7 3.7 0 0 1-.4-4.9l.8.5 3.3 1.9c.2.1.5.1.7 0l3.9-2.3v1.6l-3.4 2a3.7 3.7 0 0 1-4.9 1.2zm-1.1-7.7a3.7 3.7 0 0 1 2.1-3.6v6.2l3.9-2.3v-1.6l-3.4-2a3.7 3.7 0 0 1-2.6 3.3zm12.3-1.3l-3.9 2.3v-1.6l3.4-2a3.7 3.7 0 0 1 4.5 1.5 3.7 3.7 0 0 1-.4 4.9l-.8-.5-3.3-1.9a.8.8 0 0 0-.7 0l.2-.7zm2.8 5.6a3.7 3.7 0 0 1-2.1 3.6v-6.2l-3.9 2.3v1.6l3.4 2a3.7 3.7 0 0 1 2.6-3.3zm-6.9-1.9l-1.9-1.1 1.9-1.1 1.9 1.1-1.9 1.1z"/>'
        '</g>'
    ),

    # Anthropic: Minimalist geometric abstract A
    'anthropic': (
        '<g fill="currentColor">'
        '<polygon points="14.3,3.5 9.7,19.5 12.8,19.5 14.1,14.8 19.3,14.8 20.6,19.5 23.7,19.5 19.1,3.5"/>'
        '<polygon points="16.7,6.8 18.4,12.5 15,12.5"/>'
        '<polygon points="0.3,19.5 4.3,19.5 8.9,3.5 5.8,3.5"/>'
        '</g>'
    ),

    # Google Gemini: 4-pointed curvature star spark
    'gemini': (
        '<g fill="currentColor">'
        '<path d="M12 2C12 7.52 7.52 12 2 12C7.52 12 12 16.48 12 22C12 16.48 16.48 12 22 12C16.48 12 12 7.52 12 2Z"/>'
        '</g>'
    ),

    # Meta: The iconic infinity loop ribbon
    'meta': (
        '<g fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M16.5 7.5c2.5-2.5 5.5-1 5.5 2.5 0 4-3.5 7.5-6.5 9.5-3 2-7 2-10 0-3-2-6.5-5.5-6.5-9.5 0-3.5 3-5 5.5-2.5 2.5 2.5 4.5 5.5 7 5.5s4.5-3 7-5.5z"/>'
        '</g>'
    ),

    # Mistral AI: The stepped pixel cascades (M shape)
    'mistral': (
        '<g fill="currentColor">'
        '<rect x="2" y="5" width="3.5" height="14" rx="0.5"/>'
        '<rect x="6.5" y="8" width="3.5" height="11" rx="0.5"/>'
        '<rect x="10.25" y="11" width="3.5" height="8" rx="0.5"/>'
        '<rect x="14" y="8" width="3.5" height="11" rx="0.5"/>'
        '<rect x="18.5" y="5" width="3.5" height="14" rx="0.5"/>'
        '</g>'
    ),

    # Hugging Face: Smiley mascot silhouette
    'huggingface': (
        '<g stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">'
        '<circle cx="12" cy="12" r="9"/>'
        '<circle cx="9" cy="10" r="1" fill="currentColor"/>'
        '<circle cx="15" cy="10" r="1" fill="currentColor"/>'
        '<path d="M8.5 14.5c1 1.5 2.5 2 3.5 2s2.5-.5 3.5-2"/>'
        '<path d="M3 13c1 1 2.5 0 2.5 0M21 13c-1 1-2.5 0-2.5 0"/>'
        '</g>'
    ),

    # Cohere: Cell nucleus / organic data cluster
    'cohere': (
        '<g fill="currentColor">'
        '<circle cx="8" cy="9" r="4.5" opacity="0.9"/>'
        '<circle cx="15" cy="8" r="3.5" opacity="0.75"/>'
        '<circle cx="13" cy="15" r="5" opacity="0.85"/>'
        '<circle cx="7" cy="16" r="3" opacity="0.6"/>'
        '</g>'
    ),

    # Pinecone: Stylized geometric pinecone prism
    'pinecone': (
        '<g fill="currentColor">'
        '<path d="M12 2l3 4.5h-6zM8 7.5l4 6 4-6h-8zM6.5 14.5l5.5 7.5 5.5-7.5h-11z"/>'
        '</g>'
    ),

    # vLLM: Ultra-fast inference engine / High-speed V
    'vllm': (
        '<g stroke="currentColor" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M4 4l8 16L20 4"/>'
        '<path d="M8 4l4 8 4-8" opacity="0.6"/>'
        '</g>'
    ),

    # AWS: Cloud smile arrow
    'aws': (
        '<g stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M4 15c4 4 12 4 16 0"/>'
        '<path d="M17 17l3-2-1-3"/>'
        '<path d="M6 7l2 6 2-6M12 7v6M16 7l2 6 2-6"/>'
        '</g>'
    ),

    # Azure: Angular enterprise cloud / Microsoft 4-square
    'azure': (
        '<g fill="currentColor">'
        '<rect x="3" y="3" width="8" height="8" rx="1"/>'
        '<rect x="13" y="3" width="8" height="8" rx="1"/>'
        '<rect x="3" y="13" width="8" height="8" rx="1"/>'
        '<rect x="13" y="13" width="8" height="8" rx="1"/>'
        '</g>'
    ),

    # Google Cloud: Cloud node outline
    'gcp': (
        '<g stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M7 18h10a4 4 0 0 0 .4-8 5.5 5.5 0 0 0-10.5-1.6A4.2 4.2 0 0 0 7 18z"/>'
        '<circle cx="12" cy="12" r="2" fill="currentColor"/>'
        '</g>'
    ),

    # Microsoft Teams: Collaborative T badge
    'teams': (
        '<g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
        '<rect x="3" y="4" width="18" height="16" rx="3"/>'
        '<path d="M7 9h10M12 9v7"/>'
        '</g>'
    ),

    # ServiceNow / Enterprise IT Ticketing
    'servicenow': (
        '<g stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">'
        '<circle cx="12" cy="12" r="8"/>'
        '<path d="M12 7v5l3 3"/>'
        '</g>'
    ),

    # Qdrant / Vector Engine
    'qdrant': (
        '<g stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">'
        '<circle cx="11" cy="11" r="7"/>'
        '<path d="M16 16l5 5"/>'
        '<circle cx="11" cy="11" r="2.5" fill="currentColor"/>'
        '</g>'
    ),

    # Kubernetes: K8s Helm wheel
    'k8s': (
        '<g stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">'
        '<circle cx="12" cy="12" r="8"/>'
        '<path d="M12 4v16M4 12h16M6.3 6.3l11.4 11.4M6.3 17.7l11.4-11.4"/>'
        '</g>'
    ),

    # NVIDIA / GPU Acceleration
    'nvidia': (
        '<g fill="currentColor">'
        '<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/>'
        '<rect x="6" y="8" width="4" height="8" rx="1"/>'
        '<rect x="12" y="8" width="6" height="8" rx="1"/>'
        '</g>'
    )
}

def render_logo(name, x, y, size=24, color="#60a5fa"):
    inner = LOGOS.get(name, "")
    if not inner:
        return ""
    scale = size / 24.0
    return f'<g transform="translate({x}, {y}) scale({scale})" color="{color}">{inner}</g>'

def render_logo_badge(name, x, y, label, width=120, height=30, color="#60a5fa", bg="#141c28", border="#253245", text_color="#cbd5e1"):
    logo_svg = render_logo(name, 8, int((height - 18) / 2), size=18, color=color)
    return f'''<g transform="translate({x}, {y})">
      <rect x="0" y="0" width="{width}" height="{height}" rx="5" fill="{bg}" stroke="{border}" stroke-width="1.2"/>
      {logo_svg}
      <text x="32" y="{int(height / 2 + 4)}" class="text-mono" font-size="11" fill="{text_color}">{label}</text>
    </g>'''
