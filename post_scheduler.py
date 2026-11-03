import json
import os
import time
from datetime import datetime

print("\n⏰ ======================================================== ⏰")
print("          ELITE AKV AUTOMATED US POST SCHEDULER             ")
print("⏰ ======================================================== ⏰\n")

queue_file = "scheduled_queue.json"

def load_queue():
    if os.path.exists(queue_file):
        with open(queue_file, "r") as f:
            return json.load(f)
    return []

def save_queue(queue):
    with open(queue_file, "w") as f:
        json.dump(queue, f, indent=4)

print("1) ➕ Add Reel to Queue")
print("2) 📋 View Scheduled Queue")
print("3) 🚀 Run Scheduler Loop (Background Worker)")
choice = input("\nEnter choice (1-3): ").strip()

queue = load_queue()

if choice == "1":
    video_path = input("Enter video file path (e.g., video.mp4): ").strip()
    caption = input("Enter Reel caption: ").strip()
    target_time = input("Enter target upload time (YYYY-MM-DD HH:MM in 24h UTC): ").strip()
    
    queue.append({
        "video_path": video_path,
        "caption": caption,
        "target_time": target_time,
        "status": "pending"
    })
    save_queue(queue)
    print("\n✅ Post successfully added to scheduled queue!")

elif choice == "2":
    print("\n📋 CURRENT SCHEDULED QUEUE:")
    print("--------------------------------------------------------")
    if not queue:
        print("Queue is empty.")
    else:
        for idx, item in enumerate(queue, 1):
            print(f"{idx}. [{item['status'].upper()}] Time: {item['target_time']} UTC | File: {item['video_path']}")
    print("--------------------------------------------------------")

elif choice == "3":
    print("\n⏳ Scheduler worker running... Monitoring queue for execution times (Press Ctrl+C to exit).\n")
    try:
        while True:
            now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
            updated = False
            for item in queue:
                if item["status"] == "pending" and now_str >= item["target_time"]:
                    print(f"🚀 [TIME TRIGGER] Executing scheduled upload for: {item['video_path']}")
                    cmd = f'python3 upload_reel.py "{item["video_path"]}" "{item["caption"]}"'
                    os.system(cmd)
                    item["status"] = "published"
                    updated = True
            if updated:
                save_queue(queue)
            time.sleep(30)
    except KeyboardInterrupt:
        print("\n🛑 Scheduler worker stopped.")

else:
    print("Invalid choice.")

print("\n--------------------------------------------------------\n")
