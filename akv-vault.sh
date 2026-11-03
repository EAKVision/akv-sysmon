#!/bin/bash

BACKUP_DIR="vault_backups"
TIMESTAMP=$(date "+%Y%m%d_%H%M%S")
ARCHIVE_NAME="akv_ecosystem_backup_${TIMESTAMP}.tar.gz"

mkdir -p $BACKUP_DIR

echo "🔒 [VAULT PROTOCOL INITIALIZED]..."
echo "📦 Creating compressed archive: $ARCHIVE_NAME"

tar -czf "$BACKUP_DIR/$ARCHIVE_NAME" *.c *.py *.sh *.json 2>/dev/null

if [ $? -eq 0 ]; then
    echo "✅ [SUCCESS]: Ecosystem backup secured in $BACKUP_DIR/$ARCHIVE_NAME"
    echo "📊 Archive Size: $(du -h "$BACKUP_DIR/$ARCHIVE_NAME" | cut -f1)"
else
    echo "❌ [ERROR]: Backup operation failed."
fi
