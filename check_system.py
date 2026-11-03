import os
import sys
from instagrapi import Client

print("\n⚡ ======================================================== ⚡")
print("          ELITE AKV SYSTEM DIAGNOSTICS & SESSION CHECK     ")
print("⚡ ======================================================== ⚡\n")

# Check 1: Session File Existence
if os.path.exists("session.json"):
    print("✅ [OK] session.json found.")
    try:
        cl = Client()
        cl.load_settings("session.json")
        print("✅ [OK] Session configuration loaded successfully.")
    except Exception as e:
        print(f"⚠️  [WARN] Issue loading session settings: {e}")
else:
    print("❌ [FAIL] session.json not found! Please log in via upload_reel.py first.")

# Check 2: Check active directory files
required_files = ["upload_reel.py", "boost_organic.py", "master_control.sh"]
for f in required_files:
    if os.path.exists(f):
        print(f"✅ [OK] Script file present: {f}")
    else:
        print(f"❌ [MISSING] Script missing: {f}")

print("\n⚡ System Check Complete. Ready for deployment! ⚡\n")
