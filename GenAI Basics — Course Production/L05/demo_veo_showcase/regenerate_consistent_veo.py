import os, sys, time, pathlib, subprocess
sys.path.append(r"D:\tools")
from image_generator import find_credentials_path
from google import genai
from google.genai import types

if sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

sa_path = str(find_credentials_path())
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = sa_path
client = genai.Client(vertexai=True, project="eatzy-503209", location="us-central1")
folder = pathlib.Path(__file__).parent

def poll_and_save(op, out_path, max_wait=300):
    print(f"[POLL] Waiting for operation {op.name} -> {out_path.name}...")
    start_t = time.time()
    dummy_op = types.GenerateVideosOperation(name=op.name)
    while True:
        status_op = client.operations.get(dummy_op)
        if status_op.done:
            if status_op.error:
                print(f"[ERROR] Operation failed: {status_op.error}")
                return False
            if status_op.response and status_op.response.generated_videos:
                vb = status_op.response.generated_videos[0].video.video_bytes
                out_path.write_bytes(vb)
                print(f"[SUCCESS] Saved {out_path.name} ({len(vb)} bytes) in {int(time.time() - start_t)}s")
                return True
            else:
                print(f"[ERROR] No generated video in response: {status_op.response}")
                return False
        if time.time() - start_t > max_wait:
            print(f"[TIMEOUT] Exceeded {max_wait}s waiting for {out_path.name}")
            return False
        print(f"  ...still rendering ({int(time.time() - start_t)}s elapsed)")
        time.sleep(10)

def main():
    # 1. Regenerate Shot 1 with consistent character
    shot1_path = folder / "shot1.mp4"
    img1 = types.Image.from_file(location=str(folder / "shot1_cafe_pickup.png"))
    print("\n[DISPATCH] Launching Shot 1 I2V (Consistent Character Pickup) on Veo 3.1...")
    op1 = client.models.generate_videos(
        model="veo-3.1-generate-001",
        prompt="The young courier in yellow jacket with reflective stripe smoothly accepts the brown kraft paper food bag from the barista at the wooden counter, holds it firmly and turns with purpose toward the cafe exit. Natural human kinetics, subtle morning light, realistic motion.",
        image=img1,
        config={"aspect_ratio": "16:9"}
    )
    poll_and_save(op1, shot1_path)

    # 2. Regenerate Shot 2 with consistent character
    shot2_path = folder / "shot2.mp4"
    img2 = types.Image.from_file(location=str(folder / "shot2_bike_rain.png"))
    print("\n[DISPATCH] Launching Shot 2 I2V (Consistent Character Bike Rain) on Veo 3.1...")
    op2 = client.models.generate_videos(
        model="veo-3.1-generate-001",
        prompt="Dynamic tracking shot moving forward alongside the courier. The same courier with short cropped curly hair pedals her bicycle forward through the rain-slicked city avenue at twilight. Wheels spinning smoothly forward with water spray cutting through shallow puddles. Wet cobblestones reflecting warm shop lights and streetlamps.",
        image=img2,
        config={"aspect_ratio": "16:9"}
    )
    poll_and_save(op2, shot2_path)

    # 3. Re-assemble final montage with high compatibility
    print("\n[MONTAGE] Assembling final video via assemble_montage.py...")
    subprocess.run([sys.executable, str(folder / "assemble_montage.py")], check=True)
    print("\n[COMPLETE] Consistent Veo neural showcase updated successfully!")

if __name__ == "__main__":
    main()
