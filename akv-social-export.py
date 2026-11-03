import os
import sys

def export_social_briefing():
    report_file = "akv_daily_briefing.md"
    
    if not os.path.exists(report_file):
        print("❌ Report file not found. Run ./akv-reporter.sh first.")
        return

    with open(report_file, "r") as f:
        content = f.read()

    print("⚡ ======================================================== ⚡")
    print("📱        AKV SOCIAL MEDIA MULTI-PLATFORM EXPORTER          ⚡")
    print("⚡ ======================================================== ⚡\n")

    print("📌 [TWITTER / X THREAD READY SNIPPET]:")
    print("--------------------------------------------------------")
    print("⚡ Bare-Metal C System Telemetry Report:")
    print("Built zero-dependency profilers in C reading /proc directly.\n")
    print("• High-performance CPU & Memory Profiling")
    print("• TCP Socket & Kernel Process Inspection")
    print("• Native WSL2 Execution with 0% Framework Overhead\n")
    print("🔗 Code repository linked in bio! #cprogramming #linux #systems engineering #EAKV")
    print("--------------------------------------------------------\n")

    print("📌 [LINKEDIN / INSTAGRAM CAROUSEL CAPTION]:")
    print("--------------------------------------------------------")
    print("🚀 Bare-Metal Telemetry & Custom Kernel Profiling in C\n")
    print("Why rely on heavy third-party monitoring agents when Linux provides high-speed telemetry natively via /proc?\n")
    print("Here is today's automated system snapshot generated from my custom WSL command center:\n")
    print(content[:300] + "...\n")
    print("👇 Drop a comment if you want the open-source repo link!")
    print("--------------------------------------------------------")

if __name__ == "__main__":
    export_social_briefing()
