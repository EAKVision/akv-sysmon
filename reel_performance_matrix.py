import json

def analyze_reel_concept():
    print("========================================================")
    print("⚡ AKV REEL PERFORMANCE & ALGORITHM SCORECARD")
    print("========================================================")
    print("📌 GOAL: Compete with your baseline & maximize non-follower reach.\n")

    print("Please rate your Reel concept on the following metrics (1-10):")
    
    try:
        hook_score = float(input("1. Frame 0:00 Visual Hook / Instant Motion (1-10): "))
        dm_share_score = float(input("2. DM Shareability / Relatability Factor (1-10): "))
        retention_score = float(input("3. Pace & High FPS Motion Quality (1-10): "))
        seo_score = float(input("4. Primary Keyword Clarity in first 125 chars (1-10): "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers between 1 and 10.")
        return

    # Algorithm Weights
    total_score = (hook_score * 0.30) + (dm_share_score * 0.35) + (retention_score * 0.20) + (seo_score * 0.15)
    
    print("\n--------------------------------------------------------")
    print(f"📊 OVERALL ALGORITHM COMPLIANCE SCORE: {total_score:.1f} / 10.0")
    print("--------------------------------------------------------")

    if total_score >= 8.5:
        print("🚀 STATUS: PRIME FOR MAXIMUM NON-FOLLOWER REACH.")
        print("   ↳ Strong DM signal & zero-delay visual hook confirmed.")
    elif total_score >= 6.5:
        print("⚠️ STATUS: MODERATE POTENTIAL.")
        print("   ↳ Recommendation: Sharpen the first 1.5s hook & add a direct DM share cue.")
    else:
        print("❌ STATUS: LOW DISTRIBUTION PROBABILITY.")
        print("   ↳ Re-edit for higher pacing, 60fps render, and stronger shareability.")

    print("========================================================")

if __name__ == "__main__":
    analyze_reel_concept()
