#!/bin/bash
# ELITE AKV - Automated Reels Video Optimizer (WSL)

INPUT_FILE="$1"
OUTPUT_FILE="AKV_OPTIMIZED_$(date +%s).mp4"

if [ -z "$INPUT_FILE" ]; then
  echo "❌ Error: Please provide an input video file."
  echo "Usage: ./prep_reel.sh my_dance_video.mp4"
  exit 1
fi

if [ ! -f "$INPUT_FILE" ]; then
  echo "❌ Error: File '$INPUT_FILE' not found in current directory!"
  echo "💡 Tip: Copy it from Windows using: cp /mnt/c/Users/AK/Downloads/your_video.mp4 ./"
  exit 1
fi

echo "🚀 Processing $INPUT_FILE for Instagram Reels..."

DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$INPUT_FILE")
NEW_DURATION=$(echo "$DURATION - 0.5" | bc)

ffmpeg -i "$INPUT_FILE" \
  -ss 00:00:00 -t "$NEW_DURATION" \
  -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,format=yuv420p" \
  -r 60 \
  -c:v libx264 -preset slow -crf 18 \
  -c:a aac -b:a 192k \
  -map_metadata -1 \
  "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
  echo "✅ Optimization Complete!"
  echo "📁 Output File: $OUTPUT_FILE"
else
  echo "❌ FFmpeg encoding failed."
fi
