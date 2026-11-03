#!/usr/bin/env python3
# ============================================================================
# AKV AUTOMATED BACKUP ROTATION ENGINE
# ============================================================================
import os
import glob

BACKUP_DIR = "backups"
MAX_BACKUPS = 5

if os.path.exists(BACKUP_DIR):
    backups = sorted(glob.glob(os.path.join(BACKUP_DIR, "session_backup_*.json")), key=os.path.getmtime)
    if len(backups) > MAX_BACKUPS:
        to_remove = backups[:-MAX_BACKUPS]
        for b in to_remove:
            os.remove(b)
            print(f"[+] Pruned old backup snapshot: {b}")
        print(f"[OK] Retained top {MAX_BACKUPS} latest security backups.")
    else:
        print(f"[OK] Backup count ({len(backups)}) is within threshold ({MAX_BACKUPS}).")
else:
    print("[-] No backup directory found.")
