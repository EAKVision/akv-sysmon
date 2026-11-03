import subprocess
import sys

def main_menu():
    while True:
        print("\n========================================================")
        print("⚡ ELITE AKV MASTER EXECUTION & REACH DASHBOARD (23-MODULE)")
        print("========================================================")
        print("1. 🧹 Run Rapid Purge Dispatcher (Open 10 profiles in browser)")
        print("2. 🛡️ Log Daily Purge Progress (Update follower baseline)")
        print("3. 🔍 Audit Specific Target Profile (4-point risk test)")
        print("4. 📊 Run Current Reel Library Optimizer (SEO & Keywords)")
        print("5. 🌍 View Worldwide Reach & Video Specs Matrix")
        print("6. 🚀 Run Story Algorithm Booster Dashboard")
        print("7. 🔥 Maximize Unfollower & Explore Reach Engine")
        print("8. ⚡ Run Reel Concept Algorithm Scorecard")
        print("9. 🤖 Run Automated 60fps Reel Processor")
        print("10. 🎯 Render Video Direct from Downloads Folder")
        print("11. 🌍 Run US / UAE / KSA Targeted Geo-Optimizer")
        print("12. 📈 Run Algorithmic Retention Forecaster")
        print("13. 🕒 Check Global Target Region Scheduling Matrix")
        print("14. 🚀 RUN ALL: One-Button Master Orchestrator Sequence")
        print("15. 🧬 RUN 3-IN-1: Elite Growth Suite (Spy + Syndicator + Analytics)")
        print("16. 👤 Build Max-Level IG Profile & Bio SEO Engine")
        print("17. 📩 Run DM Share-Velocity & Virality Engine")
        print("18. 🌍 Run Multi-Region Localizer (US, UAE, KSA)")
        print("19. ⚡ Run 60fps Motion & Stutter Analyzer")
        print("20. 📅 Run 30-Day Content Calendar & Sync Matrix")
        print("21. 👁️ Run Competitor Intelligence Spy")
        print("22. 🧠 Run Multi-Agent Hook & Script Judge")
        print("23. 🛡️ Run Account Health & Shadowban Shield")
        print("0. Exit")
        print("--------------------------------------------------------")
        
        choice = input("Enter choice [0-23]: ").strip()
        
        if choice in [str(i) for i in range(1, 24)]:
            modules = {
                "1": "rapid_purge_dispatcher.py", "2": "hygiene_tracker.py",
                "3": "audit_profiles.py", "4": "current_reel_optimizer.py",
                "5": "global_reach_maximizer.py", "6": "story_algorithm_booster.py",
                "7": "unfollower_reach_booster.py", "8": "reel_performance_matrix.py",
                "9": "auto_reel_uploader.py", "10": "render_download.py",
                "11": "geo_target_optimizer.py", "12": "retention_forecaster.py",
                "13": "global_scheduler.py", "14": "run_all.py",
                "15": "elite_growth_suite.py", "16": "bio_seo_optimizer.py",
                "17": "viral_share_trigger.py", "18": "multi_region_localizer.py",
                "19": "motion_fps_analyzer.py", "20": "calendar_sync_matrix.py",
                "21": "competitor_intelligence.py", "22": "ai_content_refiner.py",
                "23": "shadowban_shield.py"
            }
            subprocess.run([sys.executable, modules[choice]])
            input("\nPress Enter to return to main menu...")
        elif choice == '0':
            print("Exiting Master System. Ready for next cycle! 🚀")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
