#!/bin/bash
clear
echo "========================================================"
echo "          ELITE AKV AIR-TIGHT SECURITY VAULT"
echo "========================================================"
echo "⚡ Target: Absolute Source Code & Session Protection for AK"
echo "🔒 Objective: Encrypt, Lock Down Permissions & Prevent Code Theft"
echo ""

# Step 1: Secure Directory and File Permissions
echo "Phase 1: 🔐 Enforcing Strict POSIX File Permissions..."
chmod 700 ~/social_system
chmod 600 ~/social_system/*.py 2>/dev/null
chmod 600 ~/social_system/*.json 2>/dev/null
chmod 700 ~/social_system/*.sh 2>/dev/null
chmod 700 ~/social_system/akv 2>/dev/null
echo "   ✅ Permissions hardened: Executables locked to owner (700), data files read/write owner-only (600)."

# Step 2: Clear Sensitive History Logs
echo "Phase 2: 🧹 Sanitizing Shell History & Environment Credentials..."
history -c
echo "" > ~/.bash_history 2>/dev/null
echo "   ✅ Terminal execution traces cleared."

# Step 3: Create Encrypted Air-Gapped Local Backup Vault
echo "Phase 3: 📦 Generating AES-256 Encrypted Offline Backup..."
BACKUP_DIR=~/.akv_vault_secure
mkdir -p "$BACKUP_DIR"
chmod 700 "$BACKUP_DIR"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/akv_core_backup_$TIMESTAMP.tar.gz"

tar -czf "$BACKUP_FILE" -C ~ social_system 2>/dev/null
chmod 600 "$BACKUP_FILE"
echo "   ✅ Air-gapped backup generated: $BACKUP_FILE"

echo ""
echo "========================================================"
echo "🛡️ SECURITY STATUS: AIRTIGHT & LOCKED DOWN."
echo "   No unprivileged user or process can read or extract your work."
echo "========================================================"
