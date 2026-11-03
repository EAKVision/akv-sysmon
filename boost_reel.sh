#!/bin/bash

# --- CONFIGURATION ---
# Replace these with your actual Meta Marketing API credentials
ACCESS_TOKEN="YOUR_ACTUAL_META_TOKEN_HERE"
AD_ACCOUNT_ID="act_YOUR_ACTUAL_NUMERIC_AD_ACCOUNT_ID"

echo "⚡ ======================================================== ⚡"
echo "           ELITE AKV AUTOMATED REEL BOOST PROTOCOL         "
echo "⚡ ======================================================== ⚡"

if [ "$ACCESS_TOKEN" == "YOUR_ACTUAL_META_TOKEN_HERE" ] || [ -z "$ACCESS_TOKEN" ]; then
    echo "❌ Error: ACCESS_TOKEN is not configured inside boost_reel.sh!"
    exit 1
fi

read -p "Enter Instagram Reel Media ID (e.g. from upload_reel.py): " MEDIA_ID

if [ -z "$MEDIA_ID" ]; then
    echo "❌ Error: Media ID is required."
    exit 1
fi

echo -e "\n⏳ Creating Meta Ad Campaign..."
CAMPAIGN_RES=$(curl -s -X POST "https://graph.facebook.com/v26.0/${AD_ACCOUNT_ID}/campaigns" \
  -F "name=WSL Boost Reel - US Reach" \
  -F "objective=OUTCOME_TRAFFIC" \
  -F "status=PAUSED" \
  -F "special_ad_categories=[]" \
  -F "access_token=${ACCESS_TOKEN}")

echo "Response: $CAMPAIGN_RES"

CAMPAIGN_ID=$(echo $CAMPAIGN_RES | grep -o '"id":"[^"]*' | grep -o '[^"]*$')

if [ -n "$CAMPAIGN_ID" ]; then
    echo -e "\n🔥 SUCCESS! Campaign Created with ID: $CAMPAIGN_ID"
    echo "Check Meta Ads Manager to set your daily budget & target locations (US Hubs)."
else
    echo -e "\n❌ Campaign creation failed. Please check your Token permissions and Ad Account ID."
fi

echo "⚡ ======================================================== ⚡"
