import csv
import os
from datetime import datetime

print("\n📊 ======================================================== 📊")
print("          ELITE AKV REEL PERFORMANCE & REACH LOG ENGINE      ")
print("📊 ======================================================== 📊\n")

csv_file = "reel_performance_log.csv"
file_exists = os.path.exists(csv_file)

reel_url = input("🔗 Enter Reel URL or Title ID: ").strip()
views = input("👁️  Enter Total Views: ").strip()
non_followers_pct = input("🌍 Enter Non-Follower Reach % (e.g., 85%): ").strip()
saves_shares = input("⚡ Enter Total Shares & Saves: ").strip()

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(csv_file, mode='a', newline='') as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["Timestamp", "Reel_URL", "Views", "Non_Follower_Reach_%", "Shares_Saves"])
    writer.writerow([timestamp, reel_url, views, non_followers_pct, saves_shares])

print(f"\n✅ Performance metrics saved to {csv_file}!")
print("--------------------------------------------------------\n")
