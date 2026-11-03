import json

def audit_target_profile():
    print("========================================================")
    print("🔍 AKV TARGET PROFILE AUDIT MATRIX")
    print("========================================================")
    print("Evaluate a suspicious follower against these 4 elimination criteria:\n")
    
    no_pfp = input("1. Does the account have a default/blank profile picture? (y/n): ").strip().lower() == 'y'
    zero_posts = input("2. Does the account have 0 posts? (y/n): ").strip().lower() == 'y'
    suspicious_chars = input("3. Is the username a random string of numbers/letters (e.g., user837492)? (y/n): ").strip().lower() == 'y'
    no_activity = input("4. Has the account shown zero likes/comments on your past content? (y/n): ").strip().lower() == 'y'
    
    score = sum([no_pfp, zero_posts, suspicious_chars, no_activity])
    
    print("\n--------------------------------------------------------")
    if score >= 3:
        print(f"🚨 RISK SCORE: {score}/4 -> HIGH PROBABILITY BOT/GHOST.")
        print("👉 ACTION: Immediate target for today's 25-account removal batch.")
    elif score == 2:
        print(f"⚠️ RISK SCORE: {score}/4 -> MODERATE INACTIVITY.")
        print("👉 ACTION: Review manually on Instagram and remove if inactive.")
    else:
        print(f"✅ RISK SCORE: {score}/4 -> LOW RISK / KEEP.")
        print("👉 ACTION: Retain this follower.")
    print("========================================================")

if __name__ == "__main__":
    audit_target_profile()
