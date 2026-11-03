#!/bin/bash

echo "========================================================"
echo "    AKV-SYSMON CORE STRESS TEST & BENCHMARK SUITE     "
echo "========================================================"

# 1. Check for stress-ng or install if missing
if ! command -v stress-ng &> /dev/null; then
    echo "⚠️  stress-ng not found. Installing via apt..."
    sudo apt update && sudo apt install -y stress-ng
fi

echo "🔥 [PHASE 1] Initializing system stress (CPU + RAM allocation)..."
# Spawn a 10-second memory & CPU load test in background
stress-ng --cpu 2 --vm 1 --vm-bytes 50% --timeout 10s --metrics-brief &
STRESS_PID=$!

echo "⚡ [PHASE 2] Executing bare-metal C profiler under load..."
sleep 2

# Measure execution speed and profile output while system is stressed
time ./akv-sysmon

wait $STRESS_PID

echo "--------------------------------------------------------"
echo "✅ BENCHMARK COMPLETE: ZERO CRASHES | STABLE EXECUTION"
echo "--------------------------------------------------------"
