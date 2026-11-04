import os

# 1. Clean up run_all.py and ensure perfect syntax
if os.path.exists("run_all.py"):
with open("run_all.py", "r") as f:
    content = f.read()
if "# --- Module 25" in content:
    content = content.split("# --- Module 25")[0].strip()
else:
content = "# AKV Master Pipeline"

module_25_code = """
# --- Module 25: Direct API Social Publisher ---
print("\\n📡 [Module 25] Executing Autonomous Social Media Broadcaster...")
try:
import upload_reel
upload_reel.publish_all_rendered()
except Exception as e:
print(f"⚠️ [Module 25] Publisher dispatch failed: {e}")
"""

with open("run_all.py", "w") as f:
f.write(content + "\n" + module_25_code)

print("✅ run_all.py successfully locked with 25 modules!")
