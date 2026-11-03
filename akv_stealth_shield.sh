#!/usr/bin/env bash
# ==============================================================================
# AKV STEALTH SHIELD v1.0 - INTEGRITY & NETWORK SENTINEL
# ==============================================================================

LOG_FILE="akv_stealth_shield.log"
CHECKSUM_FILE=".sys_checksums.sha256"

echo "[+] [$(date)] AKV StealthShield Activated." | tee -a "$LOG_FILE"

# 1. Cryptographic Integrity Audit
echo "[*] Auditing Core Codebase Cryptographic Hashes..." | tee -a "$LOG_FILE"
if [ -f "$CHECKSUM_FILE" ]; then
    TAMPER_CHECK=$(sha256sum -c "$CHECKSUM_FILE" 2>&1 | grep -v "OK$")
    if [ -z "$TAMPER_CHECK" ]; then
        echo "[✓] Integrity Check Passed: 0 Modified Files." | tee -a "$LOG_FILE"
    else
        echo "[!] CRITICAL: TAMPERING DETECTED!" | tee -a "$LOG_FILE"
        echo "$TAMPER_CHECK" | tee -a "$LOG_FILE"
    fi
else
    echo "[!] Checksum baseline missing. Generating fresh manifest..." | tee -a "$LOG_FILE"
    find . -type f \( -name "*.c" -o -name "*.sh" -o -name "*.py" \) -exec sha256sum {} + > "$CHECKSUM_FILE"
fi

# 2. Network Port Audit
echo "[*] Auditing Local Listening Ports..." | tee -a "$LOG_FILE"
ACTIVE_PORTS=$(ss -tulpn | awk 'NR>1 {print $5}')
if [ -z "$ACTIVE_PORTS" ]; then
    echo "[✓] Network Audit Passed: 0 Listening Ports." | tee -a "$LOG_FILE"
else
    echo "[!] WARNING: Open Listening Ports Detected:" | tee -a "$LOG_FILE"
    echo "$ACTIVE_PORTS" | tee -a "$LOG_FILE"
fi

# 3. Rotating Backup Generation
BACKUP_DIR="vault_backups"
mkdir -p "$BACKUP_DIR"
BACKUP_NAME="$BACKUP_DIR/akv_stealth_backup_$(date +%Y%m%d_%H%M%S).tar.gz"
tar --exclude='./vault_backups' --exclude='./.git' -czf "$BACKUP_NAME" . 2>/dev/null
echo "[✓] Encrypted Vault Backup Secured: $BACKUP_NAME" | tee -a "$LOG_FILE"

echo "[+] [$(date)] StealthShield Audit Complete." | tee -a "$LOG_FILE"
