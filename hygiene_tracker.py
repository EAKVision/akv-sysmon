import json
import os

CONFIG_FILE = "story_booster_config.json"

def log_daily_purge():
    if not os.path.exists(CONFIG_FILE):
        print("❌ Error: Config file missing.")
        return

    with open(CONFIG_FILE, "r") as f:
        data = json.load(f)

    print("========================================================")
    print("🛡️ AKV FOLLOWER HYGIENE & AUDIT ENGINE (v2.0)")
    print("========================================================")
    print(f"📊 Current Followers: {data.get('total_followers', 1403)}")
    print(f"🎯 Target Clean Base: 1100 Followers")
    
    # Simulate daily 25-account purge reduction
    choice = input("⚡ Did you complete today's purge of 25 inactive accounts? (y/n): ").strip().lower()
    
    if choice == 'y':
        data['total_followers'] = max(1100, data.get('total_followers', 1403) - 25)
        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Logged! New follower baseline updated to: {data['total_followers']}")
        print(f"🚀 Engagement ratio increased! Keep pushing.")
    else:
        print("📌 Purge pending. Run this script once you've cleared today's 25 ghost accounts.")
    print("========================================================")

if __name__ == "__main__":
    log_daily_purge()
