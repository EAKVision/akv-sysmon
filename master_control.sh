#!/bin/bash

show_menu() {
    clear
    echo "========================================================"
    echo "                    ELITE AK VISION"
    echo "========================================================"
    echo "⚡ ======================================================== ⚡"
    echo "           ELITE AKV UNBREAKABLE MASTER COMMAND HUB"
    echo "⚡ ======================================================== ⚡"
    echo "Select an operational protocol to run:"
    echo ""
    echo "--- 🔍 SYSTEM DIAGNOSTICS & CORE TRACKING ---"
    echo " 0) 🔍 System & Session Diagnostics     (python3 check_system.py)"
    echo " 2) 📈 Daily Execution Tracker          (./track_progress.sh)"
    echo " 4) 📊 Dashboard & Reach Metrics         (./track_dashboard.sh)"
    echo "13) 📊 Reel Performance & CSV Logger    (python3 track_reel_performance.py)"
    echo ""
    echo "--- 🚀 CONTENT CREATION & PUBLISHING ---"
    echo " 1) 🪝 Generate Content Hooks            (./generate_hooks.sh)"
    echo " 3) 🧵 Tech Thread Generator             (./generate_tech_thread.sh)"
    echo " 7) ⚡ Direct Upload Reel via Python     (python3 upload_reel.py)"
    echo "14) ⏰ Automated US Post Scheduler      (python3 post_scheduler.py)"
    echo ""
    echo "--- 🔥 ALGORITHMIC GROWTH & VIRAL BOOSTERS ---"
    echo " 5) 🎯 IG Growth Engine                  (./ig_growth_engine.sh)"
    echo " 6) 🌍 Global US Reach Optimizer        (./global_reach.sh)"
    echo " 8) 🚀 Free Organic Reel Boost Engine    (python3 boost_organic.py)"
    echo "10) 🎯 Organic Outreach & Niche Targeter (python3 outreach_targeter.py)"
    echo "12) ⚔️ Max Attack Viral Reach Matrix    (python3 viral_matrix.py)"
    echo "16) 🔄 Viral Reel Revival Engine         (python3 revive_reels.py)"
    echo "17) 🔥 Max Reach & Follower Growth Matrix (python3 max_growth_matrix.py)"
    echo ""
    echo "--- 🌐 SYNDICATION, SEO & BOT AUTOMATION ---"
    echo "11) 🛡️ Max Defense & Security Shield    (python3 security_shield.py)"
    echo "15) 🌐 Google SEO & Entity Engine        (python3 google_seo_engine.py)"
    echo "18) 🌍 Multi-Platform Syndicate Engine   (python3 syndicate_engine.py)"
    echo "19) 💬 Comment-Velocity & Engagement Bot (python3 comment_bot.py)"
    echo ""
    echo " 9) 🚀 Run All Daily Protocols"
    echo " x) ❌ Exit"
    echo "--------------------------------------------------------"
}

run_protocol() {
    case $1 in
        0) python3 check_system.py ;;
        1) ./generate_hooks.sh ;;
        2) ./track_progress.sh ;;
        3) ./generate_tech_thread.sh ;;
        4) ./track_dashboard.sh ;;
        5) ./ig_growth_engine.sh ;;
        6) ./global_reach.sh ;;
        7) python3 upload_reel.py ;;
        8) python3 boost_organic.py ;;
        9) echo "🚀 Running all daily protocols..." ; python3 check_system.py ; python3 max_growth_matrix.py ;;
        10) python3 outreach_targeter.py ;;
        11) python3 security_shield.py ;;
        12) python3 viral_matrix.py ;;
        13) python3 track_reel_performance.py ;;
        14) python3 post_scheduler.py ;;
        15) python3 google_seo_engine.py ;;
        16) python3 revive_reels.py ;;
        17) python3 max_growth_matrix.py ;;
        18) python3 syndicate_engine.py ;;
        19) python3 comment_bot.py ;;
        x|X) echo "Exiting AKV Master Hub. Stay focused! ⚡" ; exit 0 ;;
        *) echo "Invalid option selected!" ;;
    esac
}

cd ~/social_system || exit

show_menu
read -p "Enter choice: " choice
run_protocol "$choice"
