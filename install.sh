#!/bin/bash
echo -e "\033[38;2;212;175;55m[+] Building Elite AKV System Profiler...\033[0m"
gcc -O3 akv_sysmon.c -o /usr/local/bin/akv-sysmon 2>/dev/null || gcc -O3 akv_sysmon.c -o ./akv-sysmon
echo -e "\033[38;2;0;255;102m[+] Successfully installed! Run 'akv-sysmon' in your terminal.\033[0m"
