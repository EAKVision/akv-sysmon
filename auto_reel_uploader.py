import os
import subprocess
import json

def process_and_prepare_reel(input_file):
    print("========================================================")
    print("⚡ AKV AUTOMATED REEL PROCESSOR & DISPATCHER")
    print("========================================================")
    
    if not os.path.exists(input_file):
        print(f"❌ Error: Source file '{input_file}' not found in directory.")
        return

    output_file = "optimized_ready_reel.mp4"
    
    print(f"🔄 Processing '{input_file}' to Instagram 60fps standard...")
    
    # FFmpeg command to enforce 1080x1920, 60fps, H.264 video & AAC audio compliance
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", input_file,
        "-vf", "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
        "-r", "60",
        "-c:v", "libx264", "-preset", "slow", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        output_file
    ]
    
    result = subprocess.run(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        print("❌ FFmpeg processing failed. Ensure ffmpeg is installed.")
        print(result.stderr.decode('utf-8')[-300:])
        return

    print(f"✅ Success! Video optimized and rendered: {output_file}")
    print("📌 Ready for high-velocity non-follower distribution test.")
    print("========================================================")

if __name__ == "__main__":
    target = input("Enter path to raw video file (e.g., raw_clip.mp4): ").strip()
    process_and_prepare_reel(target)
