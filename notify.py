import os
import json
import urllib.request

def send_discord_notification(message):
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    
    if not webhook_url:
        print("Discord webhook URL not found. Skipping notification.")
        return

    payload = {
        "content": message,
        "username": "Elite AKV System Bot"
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url, 
        data=data, 
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            print("Discord notification sent successfully!")
    except Exception as e:
        print(f"Failed to send Discord notification: {e}")

if __name__ == "__main__":
    send_discord_notification("🚀 **Elite AKV System Update**\nDaily 23-module execution completed successfully!")
