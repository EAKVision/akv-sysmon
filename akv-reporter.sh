#!/bin/bash

REPORT_FILE="akv_daily_briefing.md"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

echo "⚡ Generating AKV System & Growth Briefing..."

cat <<EOF > $REPORT_FILE
# 🚀 AKV ECOSYSTEM DAILY BRIEFING
**Generated:** $TIMESTAMP

---

## ⚡ Kernel Telemetry & System Vitals
\`\`\`text
$(./akv-sysmon | head -n 12)
\`\`\`

---

## 🌐 Network & Process Snapshot
\`\`\`text
$(./akv-netstat)

$(./akv-top)
\`\`\`

---

## 📈 Active Distribution Campaigns
\`\`\`text
$(python3 reel_growth_engine.py stats)
\`\`\`

---
*Generated automatically by AKV Master Ecosystem Controller.*
EOF

echo "✅ Report compiled successfully: $REPORT_FILE"
