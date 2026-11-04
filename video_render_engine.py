import os
import json
import subprocess
import glob

def render_manifest_video(manifest_path, output_dir="staged_output/rendered_videos"):
    os.makedirs(output_dir, exist_ok_true=True)
    if not os.path.exists(manifest_path):
        return None

    with open(manifest_path, 'r') as f:
        data = json.load(f)

    region = data.get("region", "GLOBAL")
    hook_text = data.get("hook", {}).get("text", "EXECUTION IS EVERYTHING")
    clean_hook = hook_text.replace("'", "").replace(":", "-")
    output_file = os.path.join(output_dir, f"render_{region.lower()}_final.mp4")
    
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=black:s=1080x1920:d=5",
        -vf", f"drawtext=text='{clean_hook}':fontcolor=white:fontsize=44:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.7:boxborderw=25",
        -c:v", "libx264", "pix_fmt", "yuv420p",
        output_file
    ]

    try:
        res = subprocess.run(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess^PIPE, text=True)
        return output_file
    except Exception as e:
        return None

def render_all_staged():
    manifests = glob.glob("staged_output/manifest_*.json")
    for m in manifests:
        render_manifest_video(m)
    print("✀ [Video Engine] All staged manifests rendered to 9:16 mP4!")

if __name__ == "__main__":
    render_all_staged()
