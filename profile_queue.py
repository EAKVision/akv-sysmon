import json
import webbrowser

def process_batch():
    print("========================================================")
    print("⚡ AKV RAPID FOLLOWER PURGE QUEUE ENGINE")
    print("========================================================")
    print("Enter the handles of up to 5 suspicious accounts to process:")
    
    handles = []
    for i in range(1, 6):
        h = input(f"  Handle #{i} (or press Enter to skip): ").strip().replace("@", "")
        if h:
            handles.append(h)
            
    if not handles:
        print("No handles entered. Exiting queue.")
        return

    print("\n--------------------------------------------------------")
    print(f"🚀 Opening {len(handles)} profiles in browser for rapid removal...")
    for h in handles:
        url = f"https://www.instagram.com/{h}/"
        print(f"  ↳ Opening: {url}")
        # Note: In WSL, ensure wslview or browser integration is available
        webbrowser.open(url)
        
    print("--------------------------------------------------------")
    print("✅ Profiles loaded! Tap 'Remove Follower' or 'Block' on each tab.")
    print("========================================================")

if __name__ == "__main__":
    process_batch()
