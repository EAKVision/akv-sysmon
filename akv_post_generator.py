#!/usr/bin/env python3
# ============================================================================
# AKV UNIFIED MULTI-PLATFORM POST GENERATOR (v5.1)
# Cross-Syndication across IG, TikTok, Twitter/X, Threads & GitHub
# ============================================================================

import sys

def generate_all_posts():
    print("========================================================")
    print("⚡ AKV MULTI-PLATFORM CONTENT GENERATOR v5.1 ⚡")
    print("========================================================")

    caption_ig = (
        "3.07 seconds. Water doesn't care about excuses—speed is pure physics.\n"
        "From wrestling to swimming to low-level C architecture, one mindset rules them all. ♟️\n\n"
        "💻 System telemetry & C source code: github.com/EAKVision/akv-sysmon\n\n"
        "#SystemProgramming #BareMetal #CProgramming #PerformanceMindset #Reels"
    )

    caption_tiktok = (
        "3.07s World Record split. Pure physics, zero excuses. ⚡\n"
        "Building bare-metal systems & hitting peak performance.\n"
        "#CProgramming #TechGrowth #Fitness #WorldRecord #EAKVision"
    )

    thread_x = (
        "Most developers never touch manual memory allocation. Most athletes quit at 90%. We do both. ♟️\n\n"
        "1. Bare-metal C binaries compiled with -O3 -march=native\n"
        "2. Zero memory leaks across system monitors\n"
        "3. Global syndication targeting US, UAE, and KSA\n\n"
        "Source code live on GitHub: github.com/EAKVision/akv-sysmon"
    )

    print("\n[+] INSTAGRAM REEL CAPTION & TAGS:")
    print(f"    {caption_ig}\n")

    print("[+] TIKTOK CAPTION (@eakv10):")
    print(f"    {caption_tiktok}\n")

    print("[+] TWITTER / X & THREADS PAYLOAD (@amrkhedrrr):")
    print(f"    {thread_x}\n")

    print("========================================================")
    print("🔥 PAYLOADS GENERATED. READY FOR DEPLOYMENT. 🔥")
    print("========================================================")

if __name__ == "__main__":
    generate_all_posts()
