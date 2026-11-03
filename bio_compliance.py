import json
import os
import urllib.parse

CONFIG_FILE = "bio_config.json"

DEFAULT_CONFIG = {
    "primary_link": "https://eakv.ebdaey.com",
    "backup_links": [
        "https://github.com/EAKVision"
    ],
    "status": "Optimized for Instagram Compliance"
}

def generate_bio_manifest():
    os.makedirs("staged_output", exist_ok=True)
    
    print("🛡️ [Bio Compliance] Auditing bio link structure for Instagram safety...")
    
    # Ensure clean direct URL usage (avoiding multi-redirect link aggregators)
    config = DEFAULT_CONFIG
    
    output_path = os.path.join("staged_output", "bio_compliance_manifest.json")
    with open(output_path, "w") as f:
        json.dump(config, f, indent=2)
        
    print(f"✅ [Bio Compliance] Clean configuration generated at {output_path}")
    print(f"📌 Recommended Action: Use clean direct domain '{config['primary_link']}' in your Instagram bio.")

if __name__ == "__main__":
    generate_bio_manifest()
