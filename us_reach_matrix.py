import json
import random

def generate_nonfollower_strategy(part_num=2):
    hooks = [
        "Wait for the footwork transition at 0:03... 🇺🇸⚡",
        "Part 2: Proving why elite control hits different. 🕺🔥",
        "They said this transition was impossible to hit clean... ♟️"
    ]
    
    ctas = [
        "Follow @your_handle for Part 3 dropping this week 🥇",
        "Hit follow if you caught that second transition ⚡",
        "Saving this for the footwork breakdown? Follow for more 🇺🇸"
    ]
    
    hashtags = [
        "#dancereels", "#footwork", "#streetdance", "#dancechallenge", "#explorepage"
    ]
    
    return {
        "hook": random.choice(hooks),
        "cta": random.choice(ctas),
        "hashtags": " ".join(hashtags),
        "target_audience": "US Non-Followers / Explore Page"
    }

def calculate_hygiene_plan(current_followers=1403, target_ratio=0.15):
    # Safe manual remove threshold: 25 accounts / day
    daily_remove_limit = 25
    target_clean_followers = 1100
    total_to_remove = current_followers - target_clean_followers
    days_needed = round(total_to_remove / daily_remove_limit)
    
    return {
        "current_followers": current_followers,
        "target_clean_followers": target_clean_followers,
        "daily_remove_limit": daily_remove_limit,
        "estimated_days": days_needed,
        "expected_story_view_lift": "35 views -> 160+ views"
    }

print("========================================================")
print("🚀 AKV NON-FOLLOWER REACH & HYGIENE MATRIX (v1.0)")
print("========================================================")

reel_plan = generate_nonfollower_strategy()
hygiene = calculate_hygiene_plan()

print("\n🎯 REEL NON-FOLLOWER PUSH CONFIG (Part 2):")
print(f"  ↳ Hook Line:    {reel_plan['hook']}")
print(f"  ↳ Profile CTA:  {reel_plan['cta']}")
print(f"  ↳ Niche Tags:   {reel_plan['hashtags']}")

print("\n🧹 FOLLOWER HYGIENE & STORY BOOST PLAN:")
print(f"  ↳ Daily Remove Target: {hygiene['daily_remove_limit']} inactive accounts/day")
print(f"  ↳ Target Clean Base:  {hygiene['target_clean_followers']} real followers")
print(f"  ↳ Projected Timeline:  {hygiene['estimated_days']} days to reset reach")
print(f"  ↳ Story Reach Goal:    {hygiene['expected_story_view_lift']}")
print("========================================================\n")

# Save state
matrix_data = {"reel_plan": reel_plan, "hygiene": hygiene}
with open("reach_matrix_config.json", "w") as f:
    json.dump(matrix_data, f, indent=4)
