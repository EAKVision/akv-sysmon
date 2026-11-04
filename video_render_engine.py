import os
import json
import subprocess
import glob

def render_manifest_video(manifest_path, output_dir="staged_output/rendered_videos"):
    os.makedirs(output_dir, exist_ok=True)
    if not os.path.exists(manifest_path):
        print(f"⚠️ Manifest {manifest_path} not found.")
        return None

    with open(manifest_path, 'r') as f:
        data = json.load(f)

    region = data.get("region", "GLOBAL")
    hook_text = data.get("hook", {}).get("text", "EXECUTION IS EVERYTHING")
    clean_hook = hook_text.replace("'", "").replace(":", "-")
    output_file = os.path.join(output_dir, f"render_{region.lower()}_final.mp4")
    
    print(f"🎬 [Video Engine] Rendering 9:16 vertical video for region [{region}]...")

    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=black:s=1080x1920:d=5",
        "-vf", f"drawtext=text='{clean_hook}':fontcolor=white:fontsize=44:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.7:boxborderw=25",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        output_file
    ]

    try:
        res = subprocess.run(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode == 0:
            print(f"✅ [Video Engine] Render completed -> {output_file}")
            return output_file
        else:
            print(f"❌ [Video Engine] Render failed:\n{res.stderr[-300:]}")
            return None
    except Exception as e:
        print(f"⚠️ [Video Engine] Error: {e}")
        return None

if __name__ == "__main__":
    manifests = glob.glob("staged_output/manifest_*.json")
    for m in manifests:
        render_manifest_video(m)
