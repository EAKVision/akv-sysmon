import os
from pathlib import Path

# Simple manual .env parser since python-dotenv might need an explicit install
env_path = Path('.env')
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                os.environ[k] = v

print("🔍 [AKV Environment Validator] Checking loaded configuration...")

keys_to_check = [
    "PEXELS_API_KEY",
    "TIKTOK_ACCESS_TOKEN",
    "IG_ACCESS_TOKEN",
    "YT_ACCESS_TOKEN",
    "TARGET_REGION",
    "PRIMARY_VOICE"
]

for key in keys_to_check:
    val = os.getenv(key)
    if val and "your_" not in val and "here" not in val:
        print(f"  ✅ {key}: Configured (Active)")
    else:
        print(f"  ⚠️ {key}: Using placeholder or missing (Simulation Mode)")

print("\n🚀 Environment check complete!")
if __name__ == "__main__":
    pass
