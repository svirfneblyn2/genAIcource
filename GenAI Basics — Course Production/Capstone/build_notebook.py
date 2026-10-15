"""Builds the Capstone 1 Colab notebook ("Voice Brief -> Image").

Usage:  python build_notebook.py [example.json]
Writes Capstone1_Voice_to_Image.ipynb next to this file.

Everything runs inside Google Colab with no API keys and no payment:
  speech -> text   Whisper small (open model, in Colab)
  text -> prompt   Gemini built into Colab (google.colab.ai, explicit model name + timeout)
  prompt -> image  SD-Turbo (open model, in Colab; runs on the free CPU runtime, uses a GPU if one is attached)

example.json (optional) fills the read-only "Example" section with a real run; image paths are
relative to the json file.
"""
import base64, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

STYLES = ["photo", "watercolor", "3D", "flat illustration", "anime"]
FORMATS = ["square", "landscape 16:9", "portrait 9:16"]
SRC_AUTO, SRC_MAN = "SD-Turbo in Colab", "upload manually"

SETUP = r'''
import subprocess, sys, os, time, base64, io, random, textwrap, concurrent.futures as _cf
os.environ.update(HF_HUB_VERBOSITY="error", TRANSFORMERS_VERBOSITY="error", HF_HUB_DISABLE_PROGRESS_BARS="1",
                  TRANSFORMERS_NO_ADVISORY_WARNINGS="1")
print("Installing and downloading models. This takes 2-5 minutes...")
subprocess.run([sys.executable, "-m", "pip", "-q", "install", "openai-whisper"], check=True,
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
import warnings, logging
warnings.filterwarnings("ignore")
for _n in ("diffusers", "transformers", "huggingface_hub"):
    logging.getLogger(_n).setLevel(logging.ERROR)
import torch, whisper
from diffusers import AutoPipelineForText2Image
from diffusers.utils import logging as _dlog
from transformers.utils import logging as _tlog
_dlog.set_verbosity_error(); _dlog.disable_progress_bar(); _tlog.set_verbosity_error()
from IPython.display import display, Audio, HTML, Image
from google.colab import ai, files
from google.colab.output import eval_js

class StopCell(Exception):
    pass
get_ipython().set_custom_exc((StopCell,), lambda *a, **k: None)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
STYLE_EN = {"photo": "photorealistic photo", "watercolor": "watercolor illustration", "3D": "3D render",
            "flat illustration": "flat vector illustration", "anime": "anime illustration"}
FMT = {"square": (512, 512, "square 1:1"), "landscape 16:9": (768, 432, "landscape 16:9"),
       "portrait 9:16": (432, 768, "portrait 9:16")}
GEMINI_MODELS = ["google/gemini-2.5-flash", "google/gemini-2.5-flash-lite"]
SEED = random.randint(1, 999999)
S = {}
_ex = _cf.ThreadPoolExecutor(8)

def say(text):
    print(textwrap.fill(text, 100))

def log(n, text):
    print(f"[STEP {n}] {text}")

def need(*keys_steps):
    for key, n in keys_steps:
        if key not in S:
            print(f"Run step {n} first."); raise StopCell

def ask_gemini(prompt):
    """Gemini built into Colab, no key. Explicit model + timeout: without them a call can hang."""
    for m in GEMINI_MODELS:
        t = time.time()
        f = _ex.submit(ai.generate_text, prompt, model_name=m)
        try:
            out = f.result(timeout=60).strip().strip("`").strip().strip('"*').strip()
            return out, m, time.time() - t
        except Exception:
            continue
    print("Gemini error. Wait 1 minute and run the cell again. If it fails 3 times, "
          "use the prompt fallback (section 10 of the assignment).")
    raise StopCell

def make_image(prompt, w, h):
    t = time.time()
    g = torch.Generator(DEVICE).manual_seed(SEED)
    img = PIPE(prompt, num_inference_steps=1, guidance_scale=0.0, width=w, height=h, generator=g).images[0]
    buf = io.BytesIO(); img.save(buf, format="JPEG", quality=90)
    return buf.getvalue(), time.time() - t

def upload_one():
    print('Press "Choose Files" and pick your file.')
    up = files.upload()
    if not up:
        print("No file selected. Run the cell again."); raise StopCell
    return next(iter(up.items()))

def to_jpeg(data):
    from PIL import Image as _P
    buf = io.BytesIO(); _P.open(io.BytesIO(data)).convert("RGB").save(buf, format="JPEG", quality=90)
    return buf.getvalue()

def get_image(n, prompt, w, h, source):
    if source == "__SRC_MAN__":
        name, data = upload_one()
        log(n, "image: uploaded manually")
        return to_jpeg(data)
    try:
        data, secs = make_image(prompt, w, h)
    except Exception as e:
        print(f"Error: image not created ({type(e).__name__}). Run the cell again. If it fails 3 times, "
              "use the image fallback (section 10 of the assignment).")
        raise StopCell
    log(n, f"image: model sd-turbo, {secs:.1f} s")
    return data

def show_img(data, width=420):
    display(Image(data=data, width=width))

def row(items, width=380):
    cells = "".join(f'<td style="vertical-align:top;padding:6px;text-align:center"><b>{c}</b><br>'
                    f'<img src="data:image/jpeg;base64,{base64.b64encode(d).decode()}" style="width:{width}px"></td>'
                    for c, d in items)
    display(HTML(f"<table><tr>{cells}</tr></table>"))

REC_JS = """
async function rec(){
  let stream;
  try { stream = await navigator.mediaDevices.getUserMedia({audio:true}); }
  catch(e) { return "ERR"; }
  const box=document.createElement('div');
  const btn=document.createElement('button');
  btn.textContent='● Record'; btn.style='font-size:18px;padding:8px 18px;cursor:pointer';
  const info=document.createElement('span'); info.style='margin-left:12px;font-size:15px';
  box.appendChild(btn); box.appendChild(info); document.body.appendChild(box);
  await new Promise(r=>btn.onclick=r);
  const chunks=[]; const mr=new MediaRecorder(stream);
  mr.ondataavailable=e=>chunks.push(e.data);
  mr.start(); btn.textContent='■ Stop'; info.textContent='Recording... press Stop when you are done.';
  await new Promise(r=>btn.onclick=r);
  const done=new Promise(r=>mr.onstop=r); mr.stop(); await done;
  stream.getTracks().forEach(t=>t.stop());
  btn.disabled=true; info.textContent='Recording saved.';
  const b=new Uint8Array(await new Blob(chunks).arrayBuffer());
  let s=''; for(let i=0;i<b.length;i+=8192){ s+=String.fromCharCode.apply(null,b.subarray(i,i+8192)); }
  return btoa(s);
}
rec();
"""

WHISPER = whisper.load_model("small", device=DEVICE)
PIPE = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sd-turbo", variant="fp16",
    torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32).to(DEVICE)
PIPE.set_progress_bar_config(disable=True)
print("DONE. Go to step 1. (Each image will take 1-2 minutes to draw.)" if DEVICE == "cpu" else "DONE. Go to step 1.")
'''.replace("__SRC_MAN__", SRC_MAN)

SRC_PARAM = f'source = "{SRC_AUTO}"  # @param ["{SRC_AUTO}", "{SRC_MAN}"]'

CODE = {}
CODE["s0"] = SETUP
CODE["s1"] = '''method = "Record here"  # @param ["Record here", "Upload a file"]
import whisper.audio as _wa
if method == "Record here":
    b64 = eval_js(REC_JS, timeout_sec=900)
    if not b64 or b64 == "ERR":
        print('The microphone did not turn on. If Colab showed a permissions window, press "Accept" and run '
              'the cell again. If there was no window or it did not help, choose "Upload a file".')
        raise StopCell
    path = "voice.webm"
    open(path, "wb").write(base64.b64decode(b64))
else:
    name, data = upload_one()
    path = "voice_" + name.replace(" ", "_")
    open(path, "wb").write(data)
try:
    secs = len(_wa.load_audio(path)) / 16000
except Exception:
    print("Could not read this file. Use mp3, m4a, wav or ogg and run the cell again."); raise StopCell
S.clear(); S["audio"] = path
log(1, f"recording: {secs:.0f} s")
display(Audio(path))
print("Listen to the recording. If you hear nothing, record again.")
'''
CODE["s2"] = '''corrected_transcript = ""  # @param {type:"string"}
need(("audio", 1))
if S.get("whisper_for") != S["audio"]:
    t = time.time()
    S["whisper"] = WHISPER.transcribe(S["audio"], fp16=(DEVICE == "cuda"))["text"].strip()
    S["whisper_for"] = S["audio"]
    S["whisper_log"] = f"transcript: model whisper-small, {time.time() - t:.1f} s"
log(2, S["whisper_log"])
print("Transcript (what Whisper heard):"); print(S["whisper"]); print()
new = corrected_transcript.strip() or S["whisper"]
if S.get("transcript") != new:
    for k in ("prompt", "img4", "prompt5", "prompt5_for", "img5", "img6"):
        S.pop(k, None)
S["transcript"] = new
if corrected_transcript.strip():
    log(2, "using the corrected transcript")
    print("Text that goes further:"); print(S["transcript"])
'''
CODE["s3"] = f'''style = "photo"  # @param {json.dumps(STYLES)}
image_format = "square"  # @param {json.dumps(FORMATS)}
manual_prompt = ""  # @param {{type:"string"}}
need(("transcript", 2))
S["style"], S["fmt"] = STYLE_EN[style], FMT[image_format]
if manual_prompt.strip():
    S["prompt"] = manual_prompt.strip(); log(3, "prompt: entered manually")
else:
    req = ("You are a prompt engineer for an image generation model. Rewrite the client's brief below into ONE "
           "English image prompt: a single paragraph of 30-50 words (the image model reads only "
           "the first ~75 words), covering, in this order: subject, key details, style, composition and camera "
           "angle, lighting, mood. "
           f"The style must be: {{S['style']}}. The format is {{S['fmt'][2]}}. "
           "If the brief asks for text on the image, keep that text exactly and put it in double quotes. "
           "Do not add objects or ideas the client did not ask for. Output only the prompt, nothing else.\\n\\n"
           "Client brief: " + S["transcript"])
    out, model, secs = ask_gemini(req)
    S["prompt"] = out; log(3, f"prompt: model {{model}}, {{secs:.1f}} s")
S.pop("img4", None)
print("Image prompt:"); say(S["prompt"])
'''
CODE["s4"] = f'''{SRC_PARAM}
need(("prompt", 3))
w, h, _ = S["fmt"]
S["img4"] = get_image(4, S["prompt"], w, h, source)
show_img(S["img4"])
'''
CODE["s5"] = f'''edit = ""  # @param {{type:"string"}}
{SRC_PARAM}
manual_prompt = ""  # @param {{type:"string"}}
need(("img4", 4))
if not edit.strip():
    print('Fill in the "edit" field and run the cell again.'); raise StopCell
key = (edit.strip(), S["prompt"])
if manual_prompt.strip():
    S["prompt5"] = manual_prompt.strip(); S.pop("prompt5_for", None); log(5, "prompt: entered manually")
elif S.get("prompt5_for") == key:
    log(5, "prompt: same edit as the previous run, prompt reused")
else:
    req = ("Here is an image prompt:\\n" + S["prompt"] + "\\n\\nThe client asks for this change: " + edit.strip()
           + "\\nRewrite the prompt so that the change is impossible to miss: state it explicitly in the FIRST "
           "sentence (for example, if the change is 'make the sky purple', the first sentence must say the sky is "
           "purple), and remove any words that contradict it. Keep everything else the same. "
           "Output only the new prompt.")
    out, model, secs = ask_gemini(req)
    S["prompt5"] = out; S["prompt5_for"] = key; log(5, f"prompt: model {{model}}, {{secs:.1f}} s")
if S["prompt5"].strip() == S["prompt"].strip():
    print("Note: the prompt did not change, so the image will be the same. "
          "Write your edit more concretely and run the cell again.")
print("New prompt after the edit:"); say(S["prompt5"]); print()
w, h, _ = S["fmt"]
S["img5"] = get_image(5, S["prompt5"], w, h, source)
row([("Before the edit (step 4)", S["img4"]), ("After the edit (step 5)", S["img5"])])
'''
CODE["s6"] = f'''{SRC_PARAM}
need(("img4", 4))
w, h, _ = S["fmt"]
S["img6"] = left = get_image(6, S["transcript"], w, h, source)
row([("As said (raw transcript)", left), ("After rewriting (step 4 image)", S["img4"])])
'''
CODE["ba"] = '''name, data = upload_one()
print("Your image from another service:")
show_img(to_jpeg(data))
'''
CODE["bb"] = '''scene_1 = ""  # @param {type:"string"}
scene_2 = ""  # @param {type:"string"}
scene_3 = ""  # @param {type:"string"}
need(("prompt", 3))
scenes = [scene_1.strip(), scene_2.strip(), scene_3.strip()]
if not all(scenes):
    print("Fill in all three scene fields and run the cell again."); raise StopCell
req = ("From this image prompt, write ONLY a short English description (15-30 words) of the main character or "
       "object: appearance, colours, clothing or materials. No background, no action. Output only the description."
       "\\n\\n" + S["prompt"])
subj, model, secs = ask_gemini(req)
log("B", "hero description for the series: " + subj)
w, h, _ = S["fmt"]
imgs = []
for sc in scenes:
    try:
        d, secs = make_image(f"{sc}. {subj} {S['style']}.", w, h)
    except Exception as e:
        print(f"Error: image not created ({type(e).__name__}). Run the cell again."); raise StopCell
    imgs.append((sc, d))
log("B", f"3 images: model sd-turbo")
row(imgs, width=260)
'''

TITLES = {"s0": "setup", "s1": "voice", "s2": "voice → text", "s3": "text → prompt", "s4": "prompt → image",
          "s5": "edit", "s6": "comparison", "ba": "upload an image", "bb": "series"}

HEAD = """# Capstone 1 • "Voice Brief → Image"

**Read the assignment text before you start.** It explains every step, the grading, and what to do if something does not work.

How to work with this notebook:
1. **File → Save a copy in Drive**, rename the copy to `Capstone1_Surname_Name` and work only in it.
2. The **"Example"** section is read-only: this is what a finished project looks like.
3. In **"Your work"**, run the cells **one by one, top to bottom** with the ▶ button. **Do not use "Run all".**
4. The fields in the cells are a form: fill them in, do not touch the code.
5. Write your answers in the text cells: double-click → type → `Shift+Enter`.

```
your voice → [Whisper] → transcript → [Gemini] → prompt → [SD-Turbo] → image
```

All three models are free and need no API keys: Whisper and SD-Turbo are open models that run inside this notebook, Gemini is built into Colab."""

MD = {
"work": "# Your work\n\nRun the cells one by one, top to bottom.",
"h0": "## Step 0. Setup (2–5 minutes, once)\nPress ▶ and wait for the line that starts with `DONE`.",
"h1": "## Step 1. Voice\nChoose the `method` in the form and press ▶. Then listen to the recording.",
"h2": "## Step 2. Voice → text (Whisper)\nPress ▶. If the transcript has mistakes, copy it into the `corrected_transcript` field, fix it and press ▶ again.",
"a2": "**Were there mistakes in the transcript? Which ones?**\n\nYour answer: ",
"h3": "## Step 3. Text → prompt (Gemini)\nChoose the `style` and `image_format`. Leave `manual_prompt` empty (it is only for the fallback). Press ▶.",
"a3": "**Does the prompt contain everything you asked for? Does it contain anything you did not ask for?**\n\nYour answer: ",
"h4": f"## Step 4. Prompt → image (SD-Turbo)\nLeave `source` as \"{SRC_AUTO}\". Press ▶.",
"h5": "## Step 5. Edit in words\nWrite one edit in the `edit` field using the pattern \"change only X, keep everything else the same\". Leave `source` and `manual_prompt` as they are. Press ▶.",
"a5": "**Did the edit work? What else changed that you did not ask for?**\n\nYour answer: ",
"h6": f"## Step 6. \"As said\" vs \"after rewriting\"\nLeave `source` as \"{SRC_AUTO}\". Press ▶.",
"a6": "1. **Which image is closer to what you wanted?**\n\n   Your answer: \n\n2. **What exactly did the step 3 prompt add (light, composition, style, details)?**\n\n   Your answer: \n\n3. **What did the model get wrong in both images?**\n\n   Your answer: ",
"a7": "## Step 7. Final conclusions\n4–6 sentences with concrete examples from your work: at which step were there the most mistakes and why; what you fixed by hand; what you would do differently next time. If you used a fallback, say so.\n\nYour answer: ",
"hb": "# Bonus (optional, pick one)",
"hba": "## Bonus A. Another service\nMake an image from the step 3 prompt at gemini.google.com, download it, press ▶ below and pick the file.",
"aba": "**Which service did better and why?**\n\nYour answer: ",
"hbb": "## Bonus B. Series\nWrite three scenes (3–8 words each) in `scene_1`, `scene_2`, `scene_3` and press ▶.",
"abb": "**Is the hero recognisable in all three images? What drifted?**\n\nYour answer: ",
}


def example_cells(ex, base):
    def img(p, w=360):
        b = base64.b64encode(open(os.path.join(base, p), "rb").read()).decode()
        return f'<img src="data:image/jpeg;base64,{b}" width="{w}">'
    def two(a, ca, b, cb):
        return (f'<table><tr><td align="center"><b>{ca}</b><br>{img(a)}</td>'
                f'<td align="center"><b>{cb}</b><br>{img(b)}</td></tr></table>')
    return [
        "# Example (read-only)\n\nThis is how we did the assignment ourselves. Nothing to run here. " + ex["note"],
        f"### Steps 1–2. Voice → transcript\n**What was said:** \"{ex['said']}\"\n\n"
        f"**What Whisper heard:** \"{ex['transcript']}\"\n\n**Answer:** {ex['a2']}",
        f"### Step 3. Prompt (style: {ex['style']}, format: {ex['format']})\n> {ex['prompt']}\n\n**Answer:** {ex['a3']}",
        f"### Steps 4–5. Image and edit\n**Edit:** \"{ex['edit']}\"\n\n**New prompt:**\n> {ex['prompt5']}\n\n"
        + two(ex["img4"], "Step 4", ex["img5"], "Step 5, after the edit") + f"\n\n**Answer:** {ex['a5']}",
        "### Step 6. \"As said\" vs \"after rewriting\"\n"
        + two(ex["img6"], "As said", ex["img4"], "After rewriting") + "\n\n" + ex["a6"],
        f"### Step 7. Conclusions\n{ex['a7']}",
    ]


def build(ex=None, base=HERE):
    cells = [{"cell_type": "markdown", "metadata": {}, "source": HEAD}]
    if ex:
        cells += [{"cell_type": "markdown", "metadata": {}, "source": s} for s in example_cells(ex, base)]
    order = ["md:work", "md:h0", "c:s0", "md:h1", "c:s1", "md:h2", "c:s2", "md:a2", "md:h3", "c:s3", "md:a3",
             "md:h4", "c:s4", "md:h5", "c:s5", "md:a5", "md:h6", "c:s6", "md:a6", "md:a7",
             "md:hb", "md:hba", "c:ba", "md:aba", "md:hbb", "c:bb", "md:abb"]
    for item in order:
        kind, key = item.split(":")
        if kind == "md":
            cells.append({"cell_type": "markdown", "metadata": {}, "source": MD[key]})
        else:
            body = CODE[key].strip("\n")
            if key != "s0":
                body = 'if "S" not in globals():\n    raise RuntimeError("Run step 0 first.")\n' + body
            cells.append({"cell_type": "code", "metadata": {"cellView": "form"},
                          "source": f"# @title ▶ Run: {TITLES[key]}\n" + body,
                          "outputs": [], "execution_count": None})
    return {"nbformat": 4, "nbformat_minor": 5,
            "metadata": {"colab": {"provenance": []},
                         "kernelspec": {"name": "python3", "display_name": "Python 3"},
                         "language_info": {"name": "python"}},
            "cells": cells}


if __name__ == "__main__":
    import ast
    ex, base = None, HERE
    if len(sys.argv) > 1:
        ex = json.load(open(sys.argv[1], encoding="utf-8"))
        base = os.path.dirname(os.path.abspath(sys.argv[1]))
    nb = build(ex, base)
    for c in nb["cells"]:
        if c["cell_type"] == "code":
            ast.parse(c["source"])
    out = os.path.join(HERE, "Capstone1_Voice_to_Image.ipynb")
    json.dump(nb, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", out, os.path.getsize(out))
