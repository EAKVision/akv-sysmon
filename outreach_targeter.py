import random
import time

print("\n⚡ ======================================================== ⚡")
print("          ELITE AKV ORGANIC TARGETING & OUTREACH ENGINE     ")
print("⚡ ======================================================== ⚡\n")

pillars = {
    "1": "Systems & C Code Architecture",
    "2": "Peak Performance & World Record (3.07s)",
    "3": "Cinema & Mindset (Interstellar / High Energy)"
}

print("Select target pillar for today's outreach:")
for k, v in pillars.items():
    print(f"{k}) {v}")

choice = input("\nEnter choice (1-3): ").strip()

hashtags = {
    "1": ["#cprogramming", "#systemsprogramming", "#linux", "#lowlevel", "#embedded"],
    "2": ["#hybridathlete", "#swimming", "#wrestling", "#speedtraining", "#peakperformance"],
    "3": ["#interstellar", "#cinematicmindset", "#systemsthinking", "#precision", "#discipline"]
}

comments = {
    "1": [
        "Low-level efficiency is unbeatable. Clean execution! ⚡",
        "Zero latency mindset right here. Great insights! 💻",
        "Most people overlook C memory management—solid breakdown! 🚀"
    ],
    "2": [
        "Precision and technique make all the difference. Respect! 🏆",
        "3.07s discipline. Speed is pure physics! ⚡",
        "Elite energy! Keep breaking limits. 🥋"
    ],
    "3": [
        "When chaos hits, execution is everything. ELITE AK VISION 🌌",
        "Precision under extreme pressure—this hits hard! ⚡",
        "Systems thinking in action. Outstanding edit! 🚀"
    ]
}

selected_tags = hashtags.get(choice, hashtags["1"])
selected_comments = comments.get(choice, comments["1"])

print("\n🔥 DAILY TARGETING PROTOCOL GENERATED 🔥")
print("--------------------------------------------------------")
print("🎯 Target Hashtag Hubs to Visit on IG:")
for tag in selected_tags:
    print(f"   • {tag}")

print("\n💬 High-Converting Engagement Comments to Leave:")
for comment in selected_comments:
    print(f"   💬 \"{comment}\"")

print("\n📋 Execution Strategy:")
print("1. Open Instagram on mobile and search 2-3 target hashtags above.")
print("2. Engage genuinely on 5 recent top posts per hashtag using the templates.")
print("3. Profile visits will surge as creators & commenters check out @amrkhedrrr!")
print("--------------------------------------------------------\n")
