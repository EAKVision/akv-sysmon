#!/bin/bash
echo "🌐 Generating static GitHub Pages web preview configuration..."
mkdir -p public
cat << 'HTML' > public/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AKV-Sysmon Web Terminal</title>
  <style>
    body { background: #0d1117; color: #58a6ff; font-family: monospace; padding: 20px; }
    .term { border: 1px solid #30363d; padding: 15px; border-radius: 6px; background: #161b22; }
    .green { color: #3fb950; }
  </style>
</head>
<body>
  <h2>⚡ AKV-SYSMON ONLINE TERMINAL INTERFACE</h2>
  <div class="term">
    <p class="green">[SYSTEM STATUS: OPTIMAL]</p>
    <p>Target: Linux Kernel Proc FS Parser (v1.1.0)</p>
    <p>Execution Latency: &lt; 0.001s</p>
    <p>Repo: github.com/EAKVision/akv-sysmon</p>
  </div>
</body>
</html>
HTML
echo "✅ Preview asset created in ./public/index.html"
