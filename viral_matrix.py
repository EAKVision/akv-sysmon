import random

print("\n⚔️ ======================================================== ⚔️")
print("          ELITE AKV MAX ATTACK VIRAL REACH MATRIX            ")
print("⚔️ ======================================================== ⚔️\n")

caption = input("📝 Enter your proposed Reel caption: ").strip()

# High-Velocity Hashtag Matrices mapped to choice keys '1', '2', '3'
us_matrices = {
    "1": ["#cprogramming", "#systemsprogramming", "#lowlevel", "#linux", "#USATech", "#SiliconValley"],
    "2": ["#worldrecord", "#hybridathlete", "#swimming", "#wrestling", "#USAFitness", "#AmericanMindset"],
    "3": ["#interstellar", "#cinematicmindset", "#systemsthinking", "#precision", "#USA", "#NYC"]
}

print("\nSelect Content Pillar for Hashtag Injection:")
print("1) Systems & C Architecture")
print("2) Peak Performance & World Record (3.07s)")
print("3) Cinema & Mindset")
choice = input("Enter choice (1-3): ").strip()

# Safe lookup with fallback to Pillar 1
selected_tags = us_matrices.get(choice, us_matrices["1"])
tag_string = " ".join(selected_tags)

full_caption = f"{caption}\n\n⚡ ELITE AK VISION | 360° Systems\n\n{tag_string}"

# Virality Scoring Logic
score = 75
if len(caption) > 20: score += 15
if "?" in caption: score += 10

print("\n🚀 [ATTACK PROTOCOL READY]")
print("--------------------------------------------------------")
print(f"📊 Virality Potential Score: {score}/100 🔥")
print("\n📋 Optimized Caption Output:")
print("--------------------------------------------------------")
print(full_caption)
print("--------------------------------------------------------\n")
