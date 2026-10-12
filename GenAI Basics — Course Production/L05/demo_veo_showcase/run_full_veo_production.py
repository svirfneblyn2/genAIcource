import os, sys, time, pathlib
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

def run():
    # 1. Shot 1
    shot1_path = folder / "shot1.mp4"
    op1_name = "projects/eatzy-503209/locations/us-central1/publishers/google/models/veo-3.1-generate-001/operations/bc5b87e3-25cb-4f81-8195-b77bd2b69c11"
    op1 = types.GenerateVideosOperation(name=op1_name)
    poll_and_save(op1, shot1_path)

    # 2. Trainwreck T2V
    trainwreck_path = folder / "trainwreck_naive_t2v.mp4"
    print("\n[DISPATCH] Launching Trainwreck Naive T2V on Veo 3.1...")
    trainwreck_prompt = (
        "Our friendly Glovo delivery courier enters a warm cozy Scandinavian cafe, "
        "walks up to the wooden counter and picks up a brown paper food delivery bag, "
        "puts it securely inside her turquoise backpack, then cuts to her riding a city bicycle "
        "through the rainy avenue at dusk with glowing streetlights and wet cobblestones, "
        "and then camera zooms in to a digital smartphone map with a glowing navigation route arrow pointing to the delivery address."
    )
    op_tw = client.models.generate_videos(
        model="veo-3.1-generate-001",
        prompt=trainwreck_prompt,
        config={"aspect_ratio": "16:9"}
    )
    poll_and_save(op_tw, trainwreck_path)

    # 3. Shot 2 (Bike rain)
    shot2_path = folder / "shot2.mp4"
    print("\n[DISPATCH] Launching Shot 2 I2V (Bike Rain) on Veo 3.1...")
    img2 = types.Image.from_file(location=str(folder / "shot2_bike_rain.png"))
    op2 = client.models.generate_videos(
        model="veo-3.1-generate-001",
        prompt="Dynamic low-angle tracking shot moving forward alongside the courier. The courier pedals her bicycle forward through the rain-slicked city avenue at twilight. Bicycle wheels spinning smoothly forward with water spray cutting through shallow puddles. Wet cobblestones and asphalt reflecting golden shop lights and sodium streetlamps.",
        image=img2,
        config={"aspect_ratio": "16:9"}
    )
    poll_and_save(op2, shot2_path)

    # 4. Shot 3 (Map zoom)
    shot3_path = folder / "shot3.mp4"
    print("\n[DISPATCH] Launching Shot 3 I2V (Map Route Zoom) on Veo 3.1...")
    img3 = types.Image.from_file(location=str(folder / "shot3_map_route.png"))
    op3 = client.models.generate_videos(
        model="veo-3.1-generate-001",
        prompt="3D isometric digital delivery navigation map in dark mode. Smooth digital camera push-in and subtle tilt. The electric cyan GPS route trajectory line pulses and draws itself smoothly forward along the city street grid toward the orange destination waypoint pin. Clean high-tech UI motion graphics.",
        image=img3,
        config={"aspect_ratio": "16:9"}
    )
    poll_and_save(op3, shot3_path)

    # 5. Assemble final video
    print("\n[MONTAGE] Assembling final video via assemble_montage.py...")
    import subprocess
    subprocess.run([sys.executable, str(folder / "assemble_montage.py")], check=True)
    print("\n[COMPLETE] All real Veo neural videos generated and assembled!")

if __name__ == "__main__":
    run()
