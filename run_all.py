import subprocess
import sys

def run_master_sequence():
    print("========================================================")
    print("⚡ ELITE AKV ONE-BUTTON MASTER ORCHESTRATOR (v7.0)")
    print("========================================================")
    
    print("\n[STEP 1/3] 🛡️ Running Follower Hygiene Baseline Check...")
    try:
        subprocess.run([sys.executable, "hygiene_tracker.py"], check=False)
    except Exception as e:
        print(f"  ↳ Notice during hygiene check: {e}")

    print("\n[STEP 2/3] 📈 Running Algorithmic Retention Forecaster...")
    try:
        subprocess.run([sys.executable, "retention_forecaster.py"], check=False)
    except Exception as e:
        print(f"  ↳ Notice during retention check: {e}")

    print("\n[STEP 3/3] 🕒 Evaluating Global Target Region Windows...")
    try:
        subprocess.run([sys.executable, "global_scheduler.py"], check=False)
    except Exception as e:
        print(f"  ↳ Notice during scheduler check: {e}")

    print("\n========================================================")
    print("✅ SEQUENCE COMPLETE: Systems primed for Elite AKV distribution.")
    print("========================================================")

if __name__ == "__main__":
    run_master_sequence()
