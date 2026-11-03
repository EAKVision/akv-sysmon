#!/usr/bin/env python3
import os
import sys
import subprocess
import time

def banner():
    print("""
========================================================
⚡ AKV GLOBAL ECOSYSTEM MASTER CONTROL (v6.0 ELITE) ⚡
========================================================
  1) 🚀 Run Live Stress Test & Diagnostic (akv_live_test.py)
  2) 🇺🇸 Execute US & Global Geo-Reach Matrix (us_reach_matrix.py)
  3) 🧵 Generate Threads & Cross-Post Payload (akv_threads_matrix.py)
  4) 📢 Generate Scam Exposure & Callout Payload (akv_callout_engine.py)
  5) 🛡️ Trigger Master Self-Healing & Audit (akv_auto_heal.sh)
  6) 📊 Run Real-Time Telemetry Dashboard (track_dashboard.sh)
  7) 👁️ Run Visual & Hook Evaluation Engine (akv_vision_eval.py)
  8) ⚡ Run Optical Hook & Contrast Booster (akv_batch_processor.py)
  9) 🏆 Run Autonomous Elite Pipeline (Auto-Evaluate -> Boost -> Global Push)
  0) Exit Launcher
========================================================
""")

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Execution failed: {e}")

def main():
    while True:
        banner()
        choice = input("Enter option [0-9]: ").strip()
        
        if choice == '1':
            run_cmd("python3 akv_live_test.py")
        elif choice == '2':
            run_cmd("python3 us_reach_matrix.py")
        elif choice == '3':
            run_cmd("python3 akv_threads_matrix.py")
        elif choice == '4':
            run_cmd("python3 akv_callout_engine.py")
        elif choice == '5':
            run_cmd("bash akv_auto_heal.sh")
        elif choice == '6':
            run_cmd("bash track_dashboard.sh")
        elif choice == '7':
            v_file = input("Enter video path to evaluate: ").strip()
            run_cmd(f'python3 akv_vision_eval.py "{v_file}"')
        elif choice == '8':
            v_file = input("Enter video path to boost: ").strip()
            run_cmd(f'python3 akv_batch_processor.py "{v_file}"')
        elif choice == '9':
            print("\n[+] INITIATING AUTONOMOUS ELITE DEPLOYMENT SEQUENCE...")
            v_file = input("Enter target video filename (e.g., 'Suits 6 years Diffrence.MP4'): ").strip()
            
            # Step 1: Hook Evaluation
            print("\n[1/3] Evaluating raw hook visual score...")
            run_cmd(f'python3 akv_vision_eval.py "{v_file}"')
            
            # Step 2: Auto-Boost
            print("\n[2/3] Executing Optical Motion & Zoom Matrix...")
            run_cmd(f'python3 akv_batch_processor.py "{v_file}"')
            
            # Step 3: Global Reach Sequence
            boosted_file = f"elite_boosted_{v_file}"
            print(f"\n[3/3] Verifying boosted asset: {boosted_file}")
            run_cmd(f'python3 akv_vision_eval.py "{boosted_file}"')
            
            print("\n🚀 Executing US Geo-Reach and Multi-Platform Syndication...")
            run_cmd("python3 us_reach_matrix.py")
            run_cmd("python3 akv_threads_matrix.py")
            
            print("\n✅ [COMPLETE] Autonomous closed-loop execution successfully deployed!")
            os.system('python3 akv_auto_publisher.py')
            time.sleep(2)
        elif choice == '0':
            print("\n[+] Vault Locked. Returning to terminal.")
            break
        else:
            print("⚠️ Invalid option, try again.")

if __name__ == "__main__":
    main()
