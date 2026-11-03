import os
import subprocess

def process_downloaded_reel():
    print("========================================================")
    print("⚡ AKV DOWNLOADS DIRECT REEL PROCESSOR")
    print("========================================================")
    
    # Path to Windows Downloads folder inside WSL
    win_user = subprocess.run(["cmd.exe", "/c", "echo %USERNAME%"], capture_output=True, text=True).stdout.strip()
    downloads_path = f"/mnt/c/Users/{win_user}/Downloads"
    
    input_file = input("Enter video filename in Downloads (e.g., AKV_OPTIMIZED_1793598153.mp4): ").strip()
    full_input_path = os.path.join(downloads_path, input_file)
    
    if not os.path.exists(full_input_path):
        print(f"❌ Error: File '{full_input_path}' not found!")
        return

    output_file = "STAGED_READY_REEL.mp4"
    
    print(f"🔄 Scaling and rendering '{input_file}' to 1080x1920 @ 60fps...")
    
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", full_input_path,
        "-vf", "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
        "-r", "60",
        "-c:v", "libx264", "-preset", "slow", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        output_file
    ]
    
    res = subprocess.run(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if res.returncode == 0:
        print(f"\n✅ SUCCESS: Rendered 60fps payload to '{output_file}'.")
        print("\n📋 GENERATED SEARCH & KEYWORD CAPTION:")
        print("--------------------------------------------------------")
        print("Mastering street dance footwork control: 3 drills for fast movement.\n")
        print("Send this to a dancer who needs cleaner footwork! ⚡")
        print("#footwork #streetdance #dancereels")
        print("--------------------------------------------------------")
    else:
        print("❌ Error during FFmpeg processing. Make sure ffmpeg is installed.")

if __name__ == "__main__":
    process_downloaded_reel()
