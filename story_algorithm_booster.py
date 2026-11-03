import json

data = {
    "account": "ELITE AKV",
    "total_followers": 1403,
    "current_avg_story_views": 35,
    "target_story_views": 250,
    "current_reach_pct": round((35 / 1403) * 100, 2),
    "target_reach_pct": 18.0,
    "clean_up_batches": [
        {"batch_id": 1, "status": "Pending", "target_removed": 100, "category": "No Profile Pic / 0 Posts"},
        {"batch_id": 2, "status": "Pending", "target_removed": 150, "category": "Least Interacted With"}
    ],
    "action_plan": [
        "1. 24-Hour Story Blackout (Reset Meta Impression Cache)",
        "2. Follower Hygiene Purge (Remove bot/ghost accounts via IG 'Least Interacted With')",
        "3. High-Tap Sticker Hook Post (Poll/Slider on Slide 1)",
        "4. Non-Follower Reel Push (Part 2 upload via 60fps opt_reel pipeline)"
    ]
}

with open("story_booster_config.json", "w") as f:
    json.dump(data, f, indent=4)

print("✅ Story Booster & Follower Hygiene Dashboard initialized successfully!")
print(f"📊 Current Story Reach Rate: {data['current_reach_pct']}% (Goal: {data['target_reach_pct']}%)")
