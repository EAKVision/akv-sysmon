import os
import json

STAGING_DIR = "staged_output"

def stage_content(region, hook):
    os.makedirs(STAGING_DIR, exist_ok=True)
    
    package = {
        "target_region": region,
        "selected_hook": hook,
        "format": "Instagram Reel / Story",
        "status": "Staged for 24/7 GitHub Actions Runner"
    }
    
    file_path = os.path.join(STAGING_DIR, f"manifest_{region.lower()}.json")
    with open(file_path, "w") as f:
        json.dump(package, f, indent=2)
        
    print(f"📦 [Staging] Successfully packaged asset bundle for {region} -> {file_path}")

if __name__ == "__main__":
    print("--- Testing Asset Staging Module ---")
    stage_content("UAE", "The standard in the UAE demands 10x output—here's the blueprint:")
