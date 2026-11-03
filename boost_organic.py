import time
import os
from instagrapi import Client

cl = Client()
session_file = "session.json"

if not os.path.exists(session_file):
    print("Error: session.json not found! Run python3 set_session.py first.")
    exit(1)

print("Loading saved session...")
cl.load_settings(session_file)

# Target Reel Boost
target_url = "https://www.instagram.com/reel/DfSE91eKy_S/?rpxt=NWZ0cDZocjU4bXdu"
media_pk = cl.media_pk_from_url(target_url)

print(f"Target Media PK: {media_pk}")

# 1. Simulate natural watch time (pauses briefly before interacting)
print("Simulating watch duration...")
time.sleep(3)

# 2. Send Like
cl.media_like(media_pk)
print("✓ Sent Like")

# 3. Save Post (High algorithmic weight for reach)
cl.media_save(media_pk)
print("✓ Sent Save")

# 4. Post an engaging comment
cl.media_comment(media_pk, "🔥 Absolute game changer! Let's go.")
print("✓ Posted Comment")

print("All maximum-reach signals successfully sent to your Reel!")










