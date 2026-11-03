#!/bin/bash
# ELITE AKV UNBREAKABLE PROCESS WATCHDOG

echo "🛡️ [WATCHDOG] Initializing Unbreakable Guard for post_scheduler.py..."

while true; do
    # Check if post_scheduler.py is currently running
    if ! ps aux | grep "[p]ost_scheduler.py" > /dev/null; then
        echo "⚠️ [WATCHDOG] Process dropped or not found! Auto-restarting now..." >> ~/social_system/scheduler.log
        echo "3" | python3 ~/social_system/post_scheduler.py >> ~/social_system/scheduler.log 2>&1
    fi
    # Check every 5 seconds
    sleep 5
done
