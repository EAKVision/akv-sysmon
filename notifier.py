import os
import sys
import requests

WEBHOOK_URL = os.getenv("TELEGRAM_WEBHOOK_URL", "")

def send_alert(message: str):
    print(f"[TELEMETRY] {message}")
    if WEBHOOK_URL:
        try:
            requests.post(WEBHOOK_URL, json={"content": message}, timeout=5)
        except Exception as e:
            print(f"[TELEMETRY ERROR] Could not reach webhook: {e}")

if __name__ == "__main__":
    msg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "AKV System Telemetry Ping"
    send_alert(f"🚀 [ELITE AKV HUB]: {msg}")
