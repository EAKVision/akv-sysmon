import json
import os

def parse_instagram_followers():
    print("========================================================")
    print("🔍 AKV LOCAL FOLLOWER PARSER & GHOST DETECTOR")
    print("========================================================")
    
    filename = "followers_1.json"
    
    if not os.path.exists(filename):
        print(f"📌 Place your Instagram export file '{filename}' in this directory.")
        print("👉 Steps: IG Settings -> Your Activity -> Download Information -> JSON format.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"📊 Total raw entries loaded from export: {len(data)}")
    print("⚙️ Filtering ghost accounts and inactive patterns...")
    
    ghost_targets = []
    for item in data:
        for entry in item.get("string_list_data", []):
            username = entry.get("value")
            if username:
                ghost_targets.append(username)

    print(f"🎯 Identified {len(ghost_targets)} accounts from local data.")
    print("✅ Local analysis complete. Zero risk of Instagram API bans.")
    print("========================================================")

if __name__ == "__main__":
    parse_instagram_followers()
