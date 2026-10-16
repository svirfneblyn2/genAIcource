# L14 Source Notes: Streamlit and Rapid AI Prototyping (research 2026-10-16)

Primary sources checked on 2026-10-16 for the v2 rebuild. Replaces the September 2026 Drive package source notes.

## Images used in the deck (own captures, 2026-10-16)

| File | What |
|---|---|
| `assets/v2/img/streamlit_chatbot_crop.png` (slide 3) | excerpt of `streamlit_chatbot.png` (kept as the source capture): official Streamlit demo app llm-examples.streamlit.app, Chatbot page (source github.com/streamlit/llm-examples/Chatbot.py). The crop joins the API-key field and the chat column and shortens the empty middle of the input bar, so the text can be shown larger |
| `assets/v2/img/aistudio_build_crop.png` (slide 10) | crop of `aistudio_build.png` (kept as the source capture): aistudio.google.com/apps — Build |

The cover chat window (slide 1), the idea → prototype → feedback → product path (slide 2) and the rerun loop (slide 5) are drawn in HTML/SVG in `deck_v2/build.py` with RU/EN labels; the earlier English-only generated images (`cover_right.png`, `prototype_path*.png`, `rerun_loop.png`) were removed on 2026-10-16.

Streamlit was not installed on the build machine. The slide 4 code (14 non-blank lines, with an `ask_llm` stub so it runs as is) follows the official chat tutorial structure; both RU and EN versions pass `python -m py_compile`, but were not run under `streamlit run`.

---


All items checked 2026-10-16 unless noted. "UNVERIFIED" = no primary source confirmed it today.
Model names and the Gemini Interactions API match L11 source notes (`L11/L11_08_Source_Notes_Research_2026-10.md`, checked 2026-10-16).

## 0. What is out of date in the old package (deck.txt / docx text)

| Old claim | Status today | Fix |
|---|---|---|
| "Install Python 3.10+" (runbook) | **Wrong.** Streamlit 1.66.0 needs Python >= 3.11 (1.66 dropped 3.10, added 3.15) | Say Python 3.11+ |
| OpenAI Responses API only as a target, chat tutorial pattern | `st.write_stream` now natively parses **OpenAI Responses API streams** (since 1.59.0, Jul 2026) as well as Chat Completions and LangChain | Use Responses example below |
| Official tutorial code | Still uses `gpt-3.5-turbo` + Chat Completions; that model name is stale for class use | Don't copy the model name from the tutorial |
| Source notes checked 2026-09-08 | Three releases since (1.64, 1.65, 1.66) | Replace with dates below |
| No mention of AI coding agents | Streamlit now ships official **agent skills** (`streamlit skills` CLI) for Claude Code / Codex / Cursor etc. | New section 4 |
| Deploy section only says "deployment settings" | Community Cloud is free but **public by default; 1 private app**; HF Spaces now **paid** for Gradio/Docker and Streamlit is no longer in the New Space SDK list | Section 2 |
| `st.chat_input` "file/audio options, submit_mode, width, height" | Still correct (1.66.0) | keep |
| Cache decision: cache_data for data, cache_resource for clients | Still correct | keep |
| Text says 90-120 min, 26 slides | n/a (format decision) | — |

## 1. Streamlit itself

| Fact | Value | Source |
|---|---|---|
| Current version | **1.66.0**, released **2026-10-14** | https://pypi.org/project/streamlit/ ; https://docs.streamlit.io/develop/quick-reference/release-notes |
| Licence | **Apache-2.0** (open source, free) | https://pypi.org/pypi/streamlit/json |
| Python | **>= 3.11** (1.66.0 drops 3.10, adds 3.15) | release notes 1.66.0 |
| Owner | Streamlit is part of Snowflake (Snowflake = "Pro" option on streamlit.io/cloud) | https://streamlit.io/cloud |
| Install / run | `pip install streamlit` → `streamlit run app.py` → opens http://localhost:8501 | https://docs.streamlit.io (8501 also in Snowflake guide and HF docs) |

Recent releases (useful "it moves fast" slide), from https://docs.streamlit.io/develop/quick-reference/release-notes/2026 :
- 1.66.0 (2026-10-14): theme padding, Python 3.15 in / 3.10 out; startup error if `secrets.toml` can't be parsed.
- 1.65.0 (2026-10-02): side drawers for `st.dialog`.
- 1.64.0 (2026-09-15): `st.echarts_chart`, async/await in app code.
- 1.63.0 (2026-09-01): `type="step"` for `st.status`/`st.expander` (agent/pipeline progress).
- 1.59.0 (2026-07-06): `submit_mode` + file pasting in `st.chat_input`; **Responses API streams in `st.write_stream`**; app recommends installing AI coding skills on startup.
- 1.58.0 (2026-05-28): **`streamlit skills`** CLI; LangChain callback handler **removed**.
- 1.57.0 (2026-04-29): **`st.bottom`** (pinned container for chat input); agent skills bundled in pip package.

### Mental model (unchanged, still the core idea)
Every widget interaction **reruns the whole script top to bottom**. Things that must survive a rerun go to `st.session_state`; slow repeatable work goes behind `@st.cache_data` / `@st.cache_resource`; keys go to `st.secrets`.

### Chat elements (https://docs.streamlit.io/develop/api-reference/chat, v1.66.0)
- `st.chat_message(name)` — container for one message bubble ("user", "assistant", or custom).
- `st.chat_input(...)` — the input box at the bottom. Exact signature (v1.66.0, https://docs.streamlit.io/develop/api-reference/chat/st.chat_input):
  `st.chat_input(placeholder="Your message", *, key=None, max_chars=None, max_upload_size=None, accept_file=False, file_type=None, accept_audio=False, audio_sample_rate=16000, disabled=False, submit_mode="submit", on_submit=None, args=None, kwargs=None, width="stretch", height="content")`
  Returns `None` (nothing sent), `str` (plain text), or a dict-like `ChatInputValue` (`.text`, `.files`, `.audio`) when files/audio are enabled.
- `st.status(label)` — container for long-running steps.
- `st.write_stream(stream, *, cursor=None)` — typewriter effect; accepts generators, iterables, async generators, **natively parses OpenAI Chat Completions, OpenAI Responses API and LangChain streams**; other SDKs (e.g. Gemini) must be wrapped in a generator. Returns the full text (str). https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream

### Session state
`st.session_state` — per-browser-session dict that survives reruns. Idiom: `if "messages" not in st.session_state: st.session_state.messages = []` (agent skills prefer `st.session_state.setdefault("messages", [])`, per Snowflake guide). https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state

### Caching (https://docs.streamlit.io/develop/concepts/architecture/caching)
- `@st.cache_data` — for data (DataFrames, API responses, strings). Returns a fresh **copy** each call. Docs: "start with st.cache_data and see if it works!"
- `@st.cache_resource` — for global objects (ML model, DB connection, API client). **One shared object across all users/sessions**; must be thread-safe.
- Both take `ttl=` and `max_entries=`. `cache_data` uses pickle → only cache trusted data.
- Teaching note (our rule, not docs): never put per-user private data or keys into `cache_resource` objects — they're shared across users.

### Secrets (https://docs.streamlit.io/develop/concepts/connections/secrets-management)
- Project file: `.streamlit/secrets.toml` in the folder you run Streamlit from; global: `%userprofile%/.streamlit/secrets.toml` (Windows) / `~/.streamlit/secrets.toml`. Project overrides global.
- Format: TOML, e.g. `OPENAI_API_KEY = "sk-..."`.
- Access: `st.secrets["OPENAI_API_KEY"]` or `st.secrets.OPENAI_API_KEY`. Root-level keys are **also exported as environment variables** (`os.environ[...]`), so SDKs that read `OPENAI_API_KEY` / `GEMINI_API_KEY` from env work automatically.
- Docs quote: "Add this file to your `.gitignore` so you don't commit your secrets!"
- 1.66.0: startup error logged if secrets.toml is malformed (before: silently empty).

### Multipage (https://docs.streamlit.io/develop/concepts/multipage-apps/overview)
Two ways: `pages/` folder (simplest, automatic sidebar) or `st.Page` + `st.navigation` — docs: "the preferred and more customizable method is to use `st.navigation`."
```python
import streamlit as st
pg = st.navigation([st.Page("chat.py", title="Chat"), st.Page("about.py", title="About")])
pg.run()
```
(sketch; page shows no verbatim example — syntax consistent with API reference, test before class.)

### Auth (optional mention)
`st.login()` / `st.logout()` / `st.user.is_logged_in` — OIDC login (Google, Microsoft etc.) configured in `[auth]` of secrets.toml; needs `Authlib>=1.3.2`. https://docs.streamlit.io/develop/api-reference/user/st.login

### Minimal chat app examples (current API)

**A. Official tutorial (verbatim structure, model name replaced).** Source: https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps — tutorial uses Chat Completions with `gpt-3.5-turbo`; key from `st.secrets["OPENAI_API_KEY"]`.

**B. Recommended for class: OpenAI Responses API + st.write_stream (native since 1.59).**
```python
# app.py   (pip install streamlit openai)
import streamlit as st
from openai import OpenAI

st.title("Мой первый AI-чат")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Спросите что-нибудь"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        stream = client.responses.create(
            model="gpt-6-luna",                 # cheapest current, see L11 notes
            input=st.session_state.messages,    # list of {"role","content"}
            stream=True,
        )
        answer = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": answer})
```
- Streaming event used under the hood: `response.output_text.delta` (`event.delta`). https://developers.openai.com/api/docs/guides/streaming-responses (example there uses `gpt-6-astra`).
- `gpt-6-luna` $0.10/$0.50 per 1M (L11 notes, 2026-10-16). Passing a role/content list as `input` is standard Responses usage; **run once before class** (UNVERIFIED today in a live call).

**C. Free path: Gemini (google-genai, Interactions API) — needs a generator wrapper.**
```python
# pip install streamlit google-genai ; secrets.toml: GEMINI_API_KEY = "..."
import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def gemini_stream(prompt, prev_id):
    stream = client.interactions.create(
        model="gemini-3.8-flash", input=prompt,
        previous_interaction_id=prev_id, stream=True)
    for event in stream:
        if event.event_type == "step.delta" and event.delta.type == "text":
            yield event.delta.text
        # interaction id for the next turn: UNVERIFIED which event carries it
```
- Sources: quickstart https://ai.google.dev/gemini-api/docs/quickstart (`client.interactions.create`, `gemini-3.8-flash`, `interaction.output_text`); streaming https://ai.google.dev/gemini-api/docs/streaming (updated 2026-09-23: events `interaction.created`, `step.start`, `step.delta`, `step.stop`, `interaction.completed`; text in `event.delta.text`); multi-turn via `previous_interaction_id` https://ai.google.dev/gemini-api/docs/interactions (updated 2026-10-15). `generateContent` "remains fully supported" (legacy).
- Simpler beginner alternative: keep Gemini non-streaming (`st.markdown(client.interactions.create(...).output_text)`) or use `client.models.generate_content_stream` (legacy, stable) — exact legacy streaming signature not rechecked today: UNVERIFIED.
- Getting `interaction.id` from a stream for multi-turn: UNVERIFIED → for class, either non-streaming turns (`resp.id`) or stateless mode.

**D. Mock first (keep from old deck).** A `def answer(prompt): return "Демо-ответ: ..."` generator with `time.sleep` + `st.write_stream` shows the whole UI with no key. Still the right default for a live class.

## 2. Deploy options and costs

### Streamlit Community Cloud
- Free: streamlit.io/cloud says "Totally free", labelled "Free" vs Snowflake "Pro". https://streamlit.io/cloud
- Needs a **GitHub repo** (app deploys from it; updates from GitHub limited to 5/min; requests `repo` OAuth scope for private repos). https://docs.streamlit.io/deploy/streamlit-community-cloud/status
- **Visibility:** app from a public repo is **public by default**; private repo → private app; "You are only allowed one private app at a time." Viewers are invited by email (Google sign-in or emailed one-time link). https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app
  - Note conflict: marketing page streamlit.io/cloud says "Public apps only"; docs allow 1 private app. Teach: "assume public".
- **Limits** (docs say "approximately… as of February 2024"): CPU 0.078–2 cores, memory 690 MB–2.7 GB, storage up to 50 GB. **Sleeps after 12 hours without traffic**; visitor wakes it with "Yes, get this app back up!" https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app
- **Secrets:** paste TOML into **Advanced settings → Secrets** when deploying, or later in app Settings. "this `secrets.toml` file should never be committed to your repository." https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management

### Hugging Face Spaces (changed — important)
- Overview docs today: New Space SDK options are **Gradio, Docker and static HTML** — Streamlit is **not** in the list. https://huggingface.co/docs/hub/spaces-overview
- Same page: "Static Spaces are free for everyone. Gradio and Docker Spaces run on compute and require a paid plan to create: PRO for personal accounts…"; free accounts "can still host up to 2 Gradio Spaces running on ZeroGPU".
- Old Streamlit SDK page still exists (`sdk: streamlit`, example `sdk_version: 1.25.0`, port 8501) — looks stale. https://huggingface.co/docs/hub/spaces-sdks-streamlit
- Forum users report the paywall arrived without announcement: https://discuss.huggingface.co/t/docker-sdk-now-marked-as-paid-when-creating-a-new-space/177580
- Free hardware CPU Basic 2 vCPU / 16 GB; Spaces sleep when unused; secrets in Settings → Secrets (exposed as env vars); Spaces Secrets Scanner warns about hard-coded keys.
- PRO price: not rechecked today → UNVERIFIED (historically $9/month).
- **Conclusion for class: HF Spaces is no longer a free Streamlit host. Don't recommend it to beginners.**

### Streamlit in Snowflake
- Build/run Streamlit inside Snowflake; warehouse or container runtime; access by Snowflake roles (RBAC). https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit
- Cost: billed via Snowflake compute (credits) — exact numbers not on that page: UNVERIFIED. Trial offered from streamlit.io/cloud ("Start the trial now!"). Enterprise option, not for beginners.

### Other (one line, not verified today)
Running on own laptop (`streamlit run`, free, only you see it) is the default for class. Render / Railway / Google Cloud Run / Docker — possible, not checked today: UNVERIFIED.

## 3. Alternatives for rapid AI prototypes (Oct 2026)

| Tool | One line | Free tier (checked today) | Source |
|---|---|---|---|
| **Gradio** | Python lib for ML/AI demos; `gr.ChatInterface(fn=...)` gives a chat UI in ~5 lines; fn gets `(message, history)` with OpenAI-style dicts | **6.30.0**, Apache-2.0, Python >= 3.10; free (hosting on HF now paid except 2 ZeroGPU Spaces) | https://pypi.org/project/gradio/ ; https://www.gradio.app/docs/gradio/chatinterface |
| **Google AI Studio — Build** | Prompt → working web app (React frontend + Node.js backend, or Android Kotlin); live preview; GitHub two-way sync, ZIP export, deploy to Cloud Run; apps private by default; Gemini key kept server-side as `GEMINI_API_KEY` | Free to try; shared apps' Gemini calls count against **your** limits; paid models/Cloud Run may cost | https://ai.google.dev/gemini-api/docs/aistudio-build-mode (updated 2026-08-20) |
| **Claude Artifacts** | Claude builds a small interactive app/page next to the chat; "AI-powered artifacts" call Claude with no API key — each viewer uses their own Claude plan | Free plan: yes for creating artifacts; dashboards, connected apps, storage → Pro/Max/Team/Enterprise; storage 20 MB/artifact | https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them |
| **ChatGPT canvas** | Side panel for code/text; renders React/HTML in a sandbox | Sharing available on all plans incl. Free (search snippet); help page also says canvas "not supported by GPT-5.5 or later models" — page 403 to fetch: **UNVERIFIED today** | https://help.openai.com/en/articles/9930697 |
| **Apps in ChatGPT (Apps SDK)** | Developers build apps that run inside ChatGPT, on top of MCP (links back to L12) | Status/submission in Oct 2026 **UNVERIFIED** (launched Oct 2025 as preview) | https://techcrunch.com/2025/10/06/openai-launches-apps-inside-of-chatgpt/ |
| **Lovable** | Chat → full web app (frontend + backend + hosting) | Free: **5 build credits/day, max 30/month**; 20 Cloud credits/month. Pro price not shown on page (3rd-party: $25/mo — UNVERIFIED) | https://lovable.dev/pricing |
| **Bolt.new** | Chat → full-stack web app in browser | Free: **300K tokens/day, 1M/month**; Pro **$25/mo** | https://bolt.new/pricing |
| **v0 (Vercel)** | Chat → React/Next.js UI and apps, deploy to Vercel | Free **$0, 7 messages/day**; Plus $30/user/mo | https://v0.app/pricing |
| **Replit (Agent)** | Cloud IDE + Agent builds and publishes apps | Free Starter exists per 3rd-party guides (daily Agent credits, 1 published app) — **UNVERIFIED** on official page; Core $20/mo ($18 annual) | https://replit.com/pricing |

Teaching framing: Streamlit = you own Python code, runs locally, connects to any model (L03/L10 local Ollama/L11). No-code builders = fastest, but code/hosting/limits belong to the platform.

## 4. Vibe-coding a Streamlit app with a coding agent — official guidance

- **Streamlit agent skills (official).** Since 1.57.0 the pip package bundles "developing-with-streamlit" AI agent skills; since 1.58.0 `streamlit skills` CLI installs them; since 1.59.0 Streamlit suggests installing them on app startup. https://docs.streamlit.io/develop/quick-reference/release-notes/2026
- CLI: `streamlit skills` (project mode: symlinks `.agents/skills/` and `.claude/skills/` to the bundled skills; auto-update on Streamlit upgrade), `streamlit skills --global` / `-g` (user-level meta skill), `-y` non-interactive. https://docs.streamlit.io/develop/api-reference/cli/skills
- Snowflake guide "Build Streamlit Apps with Agent Skills" (updated 2026-03-24): 17 sub-skills + 9 app templates + 8 theme templates in GitHub `streamlit/agent-skills`; names **Claude Code** (`~/.claude/skills/`), Cursor, **OpenAI Codex** (`.codex/skills/`), Gemini CLI (`.gemini/skills/`), Snowflake CoCo. Example prompt: sales dashboard with KPI cards, line chart, sidebar date filters, sample data → `streamlit run app.py`. https://www.snowflake.com/en/developers/guides/build-streamlit-apps-with-agent-skills/
- Repo layout changed 2026-05-13 per a third-party write-up (classmethod.jp) → prefer `streamlit skills` CLI over manual copying.
- Antigravity: no official Streamlit-specific guidance found — UNVERIFIED (generic agent-skills format should work, not confirmed).
- Claude Code / Codex official docs: no Streamlit-specific pages found; only the Streamlit/Snowflake guidance above — treat as "the official guidance comes from Streamlit".
- Suggested class flow (ours): `pip install streamlit` → `streamlit skills` → ask agent "build a Streamlit chat app that answers from our FAQ, key from st.secrets, mock mode if no key" → `streamlit run app.py` → read the code with the agent.

## 5. Security basics for prototypes

- **Never commit keys.** Streamlit docs: add `.streamlit/secrets.toml` to `.gitignore`; Community Cloud docs: secrets.toml "should never be committed to your repository". Ship `secrets.example.toml` with placeholders instead.
- **Cloud secrets:** Community Cloud → Advanced settings / App settings → Secrets (TOML). HF Spaces → Settings → Secrets (private, not copied when duplicated) vs Variables (public).
- **GitHub push protection** for users is "enabled by default" and "Stops you from pushing secrets to public repositories on GitHub." — a safety net, not a guarantee. https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection
- **Public app = public data + your bill.** Community Cloud app from a public repo is public by default and the repo code is visible; anyone with the link can use your API key through the app (same point in AI Studio docs: shared apps' calls count against your limits). Don't upload real customer/personal data to a public prototype; use synthetic data. Set spending limits on the API account (provider dashboards; not rechecked today).
- `st.cache_resource` objects are **shared across all users** → never cache per-user data/keys there.
- Optional gate: `st.login()` (OIDC) or a private Community Cloud app (1 allowed) with email invites.
- Agent-generated code: review before running/deploying; check it didn't hard-code a key it saw in chat (teaching advice, ours).

## Primary URLs (all checked 2026-10-16)
- https://pypi.org/project/streamlit/
- https://docs.streamlit.io/develop/quick-reference/release-notes/2026
- https://docs.streamlit.io/develop/api-reference/chat
- https://docs.streamlit.io/develop/api-reference/chat/st.chat_input
- https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream
- https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps
- https://docs.streamlit.io/develop/concepts/architecture/caching
- https://docs.streamlit.io/develop/concepts/connections/secrets-management
- https://docs.streamlit.io/develop/concepts/multipage-apps/overview
- https://docs.streamlit.io/develop/api-reference/user/st.login
- https://docs.streamlit.io/develop/api-reference/cli/skills
- https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app
- https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app
- https://docs.streamlit.io/deploy/streamlit-community-cloud/status
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management
- https://streamlit.io/cloud
- https://huggingface.co/docs/hub/spaces-overview
- https://huggingface.co/docs/hub/spaces-sdks-streamlit
- https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit
- https://www.snowflake.com/en/developers/guides/build-streamlit-apps-with-agent-skills/
- https://pypi.org/project/gradio/ ; https://www.gradio.app/docs/gradio/chatinterface
- https://ai.google.dev/gemini-api/docs/aistudio-build-mode
- https://ai.google.dev/gemini-api/docs/quickstart ; /streaming ; /interactions
- https://developers.openai.com/api/docs/guides/streaming-responses
- https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them
- https://lovable.dev/pricing ; https://bolt.new/pricing ; https://v0.app/pricing ; https://replit.com/pricing
- https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection
