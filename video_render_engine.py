import os
import json
import glob
import subprocess
import asyncio
import edge_tts

async def generate_voiceover(text, output_audio_path="temp_voice.mp3"):
communicate = edge_tts.Communicate(text, "en-US-ChristopherNeural")
await communicate.save(output_audio_path)

def render_manifest_video(manifest_path, output_dir="staged_output/rendered_videos"):
os.makedirs(output_dir, exist_ok=True)
if not os.path.exists(manifest_path):
    return None

with open(manifest_path, 'r') as f:
    data = json.load(f)

region = data.get("region", "GLOBAL")
hook_text = data.get("hook", {}).get("text", "EXECUTION IS EVERYTHING")
clean_hook = hook_text.replace("'", "").replace(":", "-")
output_file = os.path.join(output_dir, f"render_{region.lower()}_final.mp4")

print(f"🎙️ [AI Voice Engine] Generating Neural Voiceover for [{region}]...")
audio_path = "temp_voice.mp3"
asyncio.run(generate_voiceover(hook_text, audio_path))

print(f"🎬 [Video Engine] Rendering high-motion 9:16 vertical video with AI voice overlay...")

ffmpeg_cmd = [
    "ffmpeg", "-y",
    "-f", "lavfi", "-i", "color=c=0x0f172a:s=1080x1920:d=6",
    "-i", audio_path,
    "-vf", f"drawtext=text='{clean_hook}':fontcolor=white:fontsize=52:bold=1:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.8:boxborderw=30",
    "-c:v", "libx264", "-c:a", "aac", "-pix_fmt", "yuv420p",
    "-shortest", output_file
]

try:
    res = subprocess.run(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if os.path.exists(audio_path):
        os.remove(audio_path)
    if res.returncode == 0:
        print(f"✅ [Video Engine] Viral AI-powered video rendered -> {output_file}")
        return output_file
    else:
        print(f"❌ [Video Engine] Render failed: {res.stderr[-200:]}")
        return None
except Exception as e:
    print(f"⚠️ [Video Engine Error]: {e}")
    return None

def render_all_staged():
manifests = glob.glob("staged_output/manifest_*.json")
for m in manifests:
    render_manifest_video(m)

if __name__ == "__main__":
render_all_staged()
