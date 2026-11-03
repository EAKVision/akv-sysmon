import datetime
import os

timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
log_entry = f"[{timestamp}] REEL DEPLOYED: suits_transform.mp4 | Caption: Option 3 | Geotag: US Prime-Time Matrix | Status: SUCCESS\n"

with open("deployment_audit.log", "a") as f:
    f.write(log_entry)

print("[+] Deployment logged successfully to deployment_audit.log")
