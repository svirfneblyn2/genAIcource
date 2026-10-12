import sys
from pathlib import Path

sys.path.insert(0, r"D:\Repos\genai-assets")
from genai_assets.client import GenaiAssets

PROMPT = (
    "Create a photorealistic character reference sheet based on the attached real photographs of Ihar Rubanovich. "
    "The character is the exact same adult man shown in the reference photos, not a generic male model. "
    "Preserve his authentic facial identity: exact face shape, forehead, eyes, eyebrows, nose, lips, jawline, ears, "
    "hairline, hairstyle, facial hair, skin tone, proportions, and distinguishing features. Do not beautify, rejuvenate, "
    "stylize, or replace his face. Show the same man exactly four times in one horizontal lineup: front view, "
    "three-quarter view, strict side profile, and back view. Full body, head to toe, consistent height, body proportions, "
    "outfit, hairstyle, and realistic anatomy across every angle. Neutral standing posture, arms relaxed. "
    "Outfit: bright yellow waterproof courier jacket with a horizontal reflective grey stripe across the chest, "
    "black cargo trousers, clean white sneakers, and a large square turquoise insulated food delivery backpack with "
    "realistic black straps and buckles. Professional studio photography, plain light grey background, even soft "
    "lighting, natural skin texture, sharp focus. No text, logos, brand names, watermark, or extra people. "
    "Highest priority: faithful reproduction of the real man's identity from the supplied photographs."
)

REFERENCES = [
    r"D:\Repos\genAIcource\GenAI Basics — Course Production\L01\assets\speaker\speaker_igor_color.jpg",
    r"G:\My Drive\Itbranch ihar\1674904862523.jpg",
    r"G:\My Drive\Itbranch ihar\1674904862530.jpg",
]

OUT_PATH = r"D:\Repos\genAIcource\GenAI Basics — Course Production\L04\assets\examples\C1_sheet_ihar.png"

def main():
    print("Initializing GenaiAssets client...")
    assets = GenaiAssets()
    print("Submitting image generation job...")
    job = assets.image(
        prompt=PROMPT,
        client="genai-course",
        aspect_ratio="16:9",
        size="1K",
        references=REFERENCES,
        out=OUT_PATH,
    )
    print("Job status:", job.get("state"))
    print("Output saved to:", job.get("saved_to"))
    if "provider" in job:
        print("Provider used:", job.get("provider"))
    if "attempts" in job:
        print("Attempts:", len(job.get("attempts", [])))

if __name__ == "__main__":
    main()
