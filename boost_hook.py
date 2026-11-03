import os
import sys

print("""
========================================================
⚡ AKV AUTOMATED HOOK CONTRAST & MOTION BOOSTER ⚡
========================================================
""")

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = input("Enter source video filename: ").strip()

if not os.path.exists(input_file):
    print(f"❌ Error: File '{input_file}' not found.")
    sys.exit(1)

output_file = f"boosted_{input_file}"

# Fixed FFmpeg filter syntax using colons instead of commas
print(f"[+] Processing '{input_file}' through FFmpeg optics matrix...")
cmd = f'ffmpeg -i "{input_file}" -vf "eq=contrast=1.3:saturation=1.2" -c:v libx264 -crf 18 -c:a copy "{output_file}" -y'

ret = os.system(cmd)
if ret == 0:
    print(f"\n✅ [SUCCESS] Optimized hook video generated: {output_file}")
    print("   ├── Re-run your evaluation: python3 akv_vision_eval.py", f'"{output_file}"')
else:
    print("\n❌ [ERROR] FFmpeg optimization failed. Check video stream parameters.")
