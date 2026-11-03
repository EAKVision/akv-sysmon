#!/usr/bin/env bash
# ============================================================================
# AKV SYSTEM HEALTH & LOG ROTATION AUDIT
# ============================================================================
LOG_FILE="daemon.log"
MAX_SIZE=$((2 * 1024 * 1024)) # 2MB limit

if [ -f "$LOG_FILE" ]; then
    FILE_SIZE=$(stat -f%z "$LOG_FILE" 2>/dev/null || stat -c%s "$LOG_FILE" 2>/dev/null)
    if [ "$FILE_SIZE" -gt "$MAX_SIZE" ]; then
        echo "[+] Rotating daemon.log (size exceeded 2MB)..."
        mv "$LOG_FILE" "daemon_old.log"
        touch "$LOG_FILE"
    fi
fi

echo "[+] Verifying python script syntax across modules..."
python3 -m py_compile interstellar_lock.py boost_organic.py syndicate_engine.py comment_bot.py 2>/dev/null && \
    echo "[OK] All Python modules syntax-verified."
