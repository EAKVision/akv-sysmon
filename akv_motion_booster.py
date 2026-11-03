import os
import sys

print("""
========================================================
⚡ AKV ELITE OPTICAL MOTION & ZOOM BOOSTER (-O3) ⚡
========================================================
""")

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = input("Enter source video filename: ").strip()

if not os.path.exists(input_file):
    print(f"❌ Error: File '{input_file}' not found.")
    sys.exit(1)

output_file = f"elite_motion_{input_file}"

# Advanced FFmpeg filter:
# 1. Applies dynamic zoom-in over the first 90 frames (3 seconds at 30fps)
# 2. Boosts contrast and color saturation simultaneously
print(f"[+] Injecting high-velocity optical zoom and contrast matrix into '{input_file}'...")
cmd = f'ffmpeg -i "{input_file}" -vf "zoompan=z=\'min(zoom+0.0015,1.15)\':d=90:s=576x1024,eq=contrast=1.35:saturation=1.25" -c:v libx264 -crf 18 -c:a copy "{output_file}" -y'

ret = os.system(cmd)
if ret == 0:
    print(f"\n✅ [SUCCESS] Elite motion-boosted video generated: {output_file}")
    print(f"   ├── Run verification: python3 akv_vision_eval.py \"{output_file}\"")
else:
    print("\n❌ [ERROR] Optical motion injection failed.")
