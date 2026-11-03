import json

def generate_non_follower_payload():
    print("========================================================")
    print("🔥 AKV UNFOLLOWER & EXPLORE REACH MAXIMIZER (v4.0)")
    print("========================================================")
    print("📌 OBJECTIVE: Drive maximum initial watch completion & DM shares.")
    
    payload = {
        "2026_algorithm_weights": {
            "1. Watch Completion Rate": "Crucial. Must aim for >90% completion on 7-12s Reels.",
            "2. DM Shares (Sends per View)": "Highest priority ranking signal for non-follower feeds.",
            "3. Skip Rate (Frame 0:00 - 0:01.5)": "Must stay under 20% to avoid initial distribution caps.",
            "4. Search & Audio SEO": "Captions parsed for niche keywords; exact 5-tag cluster cap."
        },
        "wsl_pre_flight_checks": [
            "✔ Render Profile: 1080x1920 @ 60fps (Smooth motion stops the scroll)",
            "✔ Caption SEO: Primary keywords in first 125 chars (before 'More')",
            "✔ Hashtags: Exactly 3 to 5 targeted tags (#footwork #streetdance #dancereels)",
            "✔ DM Hook: On-screen CTA encouraging shares ('Send this to a dancer')"
        ]
    }

    print("\n📊 2026 ALGORITHM WEIGHTS FOR NON-FOLLOWER FEEDS:")
    for key, val in payload["2026_algorithm_weights"].items():
        print(f"  ↳ {key}: {val}")

    print("\n🚀 PRE-FLIGHT CHECKLIST BEFORE YOU DROP A REEL:")
    for check in payload["wsl_pre_flight_checks"]:
        print(f"  ↳ {check}")

    print("\n========================================================")
    
    with open("unfollower_reach_config.json", "w") as f:
        json.dump(payload, f, indent=4)

if __name__ == "__main__":
    generate_non_follower_payload()
