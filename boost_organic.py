import os
import sys
from instagrapi import Client

USERNAME = "amrkhedrrr"
PASSWORD = "vR8#qZ2mT9@Kx5$Lp4^Nw7&cH3*Fy6Js8EAKV"  # Replace with actual password

cl = Client()

if os.path.exists("session.json"):
    cl.load_settings("session.json")
    cl.login(USERNAME, PASSWORD)
else:
    print("❌ No session found. Run upload_reel.py first to authenticate.")
    sys.exit(1)

print("⚡ ======================================================== ⚡")
print("        ELITE AKV ORGANIC REEL BOOST ENGINE (FREE)         ")
print("⚡ ======================================================== ⚡\n")

media_id = input("Enter your Reel Media ID (or URL): ").strip()

# Extract numeric PK if URL is provided
if "instagram.com" in media_id:
    media_id = cl.media_pk_from_url(media_id)

print(f"\n🚀 Running organic boost actions for Media ID: {media_id}...")

try:
    # Action 1: Share Reel to your Story
    cl.media_share_to_story(media_id)
    print("1️⃣ [SUCCESS] Shared Reel to your IG Story.")

    # Action 2: Add high-engagement call-to-action comment
    cta_text = "Zero memory leaks in C. Zero excuses in training. ⚡ What's your current stack?"
    cl.media_comment(media_id, cta_text)
    print("2️⃣ [SUCCESS] Posted high-contrast CTA comment.")

    # Action 3: Pin Reel to profile grid
    cl.clip_pin(media_id)
    print("3️⃣ [SUCCESS] Pinned Reel to your profile grid.")

    print("\n🔥 Organic boost sequence completed with 0 ad spend!")

except Exception as e:
    print(f"\n❌ Boost error: {e}")

print("⚡ ======================================================== ⚡")
