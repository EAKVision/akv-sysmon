import os
import sys
import cv2
import numpy as np

print("""
========================================================
⚡ AKV VISUAL & HOOK SENTIMENT SCORING ENGINE (-O3) ⚡
========================================================
""")

def evaluate_hook(video_path):
    if not os.path.exists(video_path):
        print(f"❌ Error: Video file '{video_path}' not found.")
        return False
    
    print(f"[+] Loading video stream: {video_path}")
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 30.0
        
    target_frames = int(fps * 3)
    frame_count = 0
    motion_scores = []
    contrast_scores = []
    
    prev_gray = None
    
    while cap.isOpened() and frame_count < target_frames:
        ret, frame = cap.read()
        if not ret:
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 1. Calculate Contrast (Standard Deviation of Pixel Intensity)
        contrast = np.std(gray)
        contrast_scores.append(contrast)
        
        # 2. Calculate Frame-to-Frame Motion Velocity
        if prev_gray is not None:
            flow = cv2.absdiff(gray, prev_gray)
            motion = np.mean(flow)
            motion_scores.append(motion)
            
        prev_gray = gray
        frame_count += 1
        
    cap.release()
    
    if not motion_scores or not contrast_scores:
        print("❌ Error: Could not extract frames from video.")
        return False
        
    avg_motion = np.mean(motion_scores)
    avg_contrast = np.mean(contrast_scores)
    
    # Recalibrated Hook Score Heuristic (0-100 scale)
    # Visual Contrast Weighting (up to 50 pts) + Motion Velocity Weighting (up to 50 pts)
    contrast_weight = min(float((avg_contrast / 80.0) * 50.0), 50.0)
    motion_weight = min(float((avg_motion / 3.0) * 50.0), 50.0)
    
    hook_score = round(contrast_weight + motion_weight, 2)
    if hook_score > 100.0:
        hook_score = 100.0
        
    print("\n----------------------------------------")
    print(f"📊 HOOK TELEMETRY METRICS (First 3s):")
    print(f"   ├── Frames Analyzed : {frame_count}")
    print(f"   ├── Motion Velocity : {avg_motion:.2f}")
    print(f"   ├── Visual Contrast : {avg_contrast:.2f}")
    print(f"   └── ELITE HOOK SCORE: {hook_score} / 100")
    print("----------------------------------------")
    
    if hook_score >= 70.0:
        print("✅ [STATUS] HOOK VERIFIED: Elite retention profile. Ready for feed injection.")
    else:
        print("⚠️ [STATUS] HOOK SUB-OPTIMAL: Consider boosting contrast or optical motion.")
        
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        v_path = sys.argv[1]
    else:
        v_path = input("Enter video filename: ").strip()
        
    evaluate_hook(v_path)
