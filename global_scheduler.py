from datetime import datetime, timezone, timedelta

def calculate_global_windows():
    print("========================================================")
    print("🌍 ELITE AKV GLOBAL TARGETING & SCHEDULING MATRIX")
    print("========================================================")
    
    now_utc = datetime.now(timezone.utc)
    print(f"🕒 Current Universal Time (UTC): {now_utc.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Target windows conversion
    us_est = now_utc.astimezone(timezone(timedelta(hours=-5)))
    uae_gst = now_utc.astimezone(timezone(timedelta(hours=4)))
    ksa_ast = now_utc.astimezone(timezone(timedelta(hours=3)))
    
    print("\n📍 TARGET MARKET LOCAL TIMES RIGHT NOW:")
    print(f"  🇺🇸 United States (EST): {us_est.strftime('%I:%M %p')}")
    print(f"  🇦🇪 United Arab Emirates (GST): {uae_gst.strftime('%I:%M %p')}")
    print(f"  🇸🇦 Saudi Arabia (AST): {ksa_ast.strftime('%I:%M %p')}")
    
    print("\n🎯 OPTIMAL DEPLOYMENT WINDOWS:")
    print("  • US Peak Window:       19:00 - 23:00 UTC (1:00 PM - 5:00 PM EST)")
    print("  • UAE / KSA Peak Window: 15:00 - 18:00 UTC (7:00 PM - 10:00 PM GST)")
    print("========================================================")

if __name__ == "__main__":
    calculate_global_windows()
