cat << 'EOF' > media_ingest.py
import os
import json
import urllib.request
import urllib.parse
import random

MEDIA_DIR = "staged_output/media"

SEARCH_QUERIES = {
    "UAE": ["luxury sports car Dubai", "futuristic skyline sunset", "executive luxury office"],
    "KSA": ["modern architecture night", "executive leadership focus", "high performance training"],
    "US":  ["gym workout motivation", "deep work laptop focus", "cinematic dark aesthetics"]
}

def download_broll_video(region):
    os.makedirs(MEDIA_DIR, exist_ok=True)
    api_key = os.environ.get("PEXELS_API_KEY")

    query = random.choice(SEARCH_QUERIES.get(region, SEARCH_QUERIES["US"]))
    print(f"🎬 [Pexels Ingest] Searching 9:16 footage for [{region}]: '{query}'...")

    manifest_path = os.path.join(MEDIA_DIR, f"video_config_{region.lower()}.json")

    if not api_key:
        print("⚠️ PEXELS_API_KEY secret not found. Falling back to local manifest generation.")
        manifest = {"region": region, "query": query, "status": "Simulated (Missing API Key)"}
        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)
        return

    url = f"https://api.pexels.com/videos/search?query={urllib.parse.quote(query)}&orientation=portrait&per_page=5"
    req = urllib.request.Request(url, headers={"Authorization": api_key})

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            videos = data.get("videos", [])

            if videos:
                selected_video = videos[0]
                video_files = selected_video.get("video_files", [])
                download_url = video_files[0]["link"] if video_files else None

                if download_url:
                    file_path = os.path.join(MEDIA_DIR, f"broll_{region.lower()}.mp4")
                    print(f"⬇️ Downloading video file to {file_path}...")
                    urllib.request.urlretrieve(download_url, file_path)
                    print("✅ Download complete.")
    except Exception as e:
        print(f"⚠️ Error downloading video: {e}")
EOF
