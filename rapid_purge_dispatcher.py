import subprocess
import sys

def dispatch_removal_batch():
    print("========================================================")
    print("⚡ AKV RAPID PURGE DISPATCHER (WSL -> BROWSER ENGINE)")
    print("========================================================")
    print("Paste a space-separated or comma-separated list of ghost handles:")
    
    raw_input = input("\n🎯 Handles to purge: ").strip()
    if not raw_input:
        print("No handles provided. Exiting.")
        return

    # Clean handles
    handles = [h.strip().replace("@", "") for h in raw_input.replace(",", " ").split() if h.strip()]
    
    # Restrict batch size to 10 at a time to keep browser responsive
    batch = handles[:10]
    
    print(f"\n🚀 Dispatching {len(batch)} target profile tabs to browser...")
    for h in batch:
        url = f"https://www.instagram.com/{h}/"
        print(f"  ↳ Opening: {url}")
        # Launch using Windows default browser safely from WSL
        subprocess.run(["powershell.exe", "-c", f"Start-Process '{url}'"])

    print("--------------------------------------------------------")
    print("✅ Tabs opened! Simply click 'Remove' on each tab.")
    print("========================================================")

if __name__ == "__main__":
    dispatch_removal_batch()
