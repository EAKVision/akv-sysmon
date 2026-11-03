import socket; _old_gai = socket.getaddrinfo; socket.getaddrinfo = lambda host, port, *args, **kwargs: _old_gai("1.1.1.1" if host == "i.instagram.com" else host, port, *args, **kwargs)
import os
import time
from instagrapi import Client

print("⚡ ======================================================== ⚡")
print("          ELITE AKV UNBREAKABLE UPLOAD ENGINE              ")
print("⚡ ======================================================== ⚡\n")

cl = Client()

# Load Session Safely
if os.path.exists("session.json"):
    try:
        cl.load_settings("session.json")
        print("✅ Session settings loaded.")
    except Exception as e:
        print(f"⚠️ Session warning: {e}")

video_path = input("Enter video file path (e.g., video.mp4): ").strip()
caption_text = input("Enter Reel caption: ").strip()

# Unbreakable Upload Retry Loop (3 Attempts)
max_retries = 3
for attempt in range(1, max_retries + 1):
    try:
        print(f"\n🚀 [Attempt {attempt}/{max_retries}] Uploading Reel to Instagram...")
        media = cl.clip_upload(video_path, caption=caption_text)
        print(f"\n🎉 SUCCESS! Reel uploaded successfully.")
        print(f"🆔 Media ID: {media.pk}")
        print(f"🔗 Direct URL: https://www.instagram.com/reel/{media.code}/")
        
        # Save session state
        cl.dump_settings("session.json")
        print("💾 Session state updated.")
        break
    except Exception as e:
        print(f"❌ Upload failed on attempt {attempt}: {e}")
        if attempt < max_retries:
            print("🔄 Waiting 10 seconds before retrying...")
            time.sleep(10)
        else:
            print("🚨 Max retries reached. Check network or media format!")
