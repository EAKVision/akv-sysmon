import os
import json
import requests

class MetaAutoPublisher:
    def __init__(self):
        self.access_token = os.getenv("META_ACCESS_TOKEN", "")
        self.instagram_account_id = os.getenv("IG_USER_ID", "")
        self.graph_api_version = "v18.0"

    def publish_reel(self, video_url, caption):
        """
        Automates publishing high-performance reels to Instagram via Meta Graph API.
        """
        if not self.access_token or not self.instagram_account_id:
            print("⚠️ Meta credentials (META_ACCESS_TOKEN or IG_USER_ID) not found. Staging for manual push.")
            return False

        print(f"🚀 [Meta Publisher] Initializing container upload for global distribution...")
        
        # Step 1: Create Media Container
        container_url = f"https://graph.facebook.com/{self.graph_api_version}/{self.instagram_account_id}/media"
        payload = {
            'media_type': 'REELS',
            'video_url': video_url,
            'caption': caption,
            'access_token': self.access_token
        }
        
        response = requests.post(container_url, data=payload)
        result = response.json()
        
        if 'id' not in result:
            print(f"❌ Failed to create media container: {result}")
            return False
            
        creation_id = result['id']
        print(f"📦 Media container created: {creation_id}. Publishing...")

        # Step 2: Publish Container
        publish_url = f"https://graph.facebook.com/{self.graph_api_version}/{self.instagram_account_id}/media_publish"
        publish_payload = {
            'creation_id': creation_id,
            'access_token': self.access_token
        }
        
        pub_response = requests.post(publish_url, data=publish_payload)
        pub_result = pub_response.json()

        if 'id' in pub_result:
            print(f"✅ Successfully published reel to Instagram! Post ID: {pub_result['id']}")
            return True
        else:
            print(f"❌ Failed to publish reel: {pub_result}")
            return False

if __name__ == '__main__':
    publisher = MetaAutoPublisher()
    publisher.publish_reel("https://eakv.ebdaey.com/sample.mp4", "Elite AKV | Global execution ⚡")
