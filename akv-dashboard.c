#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <dirent.h>
#include <ctype.h>

void render_dashboard() {
    // ----------------------------------------------------
    // 1. CPU & RAM TELEMETRY
    // ----------------------------------------------------
    FILE *f_mem = fopen("/proc/meminfo", "r");
    long mem_total = 0, mem_free = 0, mem_avail = 0;
    char buffer[256];

    if (f_mem) {
        while (fgets(buffer, sizeof(buffer), f_mem)) {
            if (sscanf(buffer, "MemTotal: %ld kB", &mem_total) == 1) continue;
            if (sscanf(buffer, "MemFree: %ld kB", &mem_free) == 1) continue;
            if (sscanf(buffer, "MemAvailable: %ld kB", &mem_avail) == 1) continue;
        }
        fclose(f_mem);
    }

    FILE *f_stat = fopen("/proc/stat", "r");
    long user, nice, system, idle, iowait, irq, softirq;
    double cpu_usage = 0.0;

    if (f_stat) {
        if (fgets(buffer, sizeof(buffer), f_stat)) {
            sscanf(buffer, "cpu %ld %ld %ld %ld %ld %ld %ld",
                   &user, &nice, &system, &idle, &iowait, &irq, &softirq);
        }
        fclose(f_stat);
        long total_idle = idle + iowait;
        long total_non_idle = user + nice + system + irq + softirq;
        long total = total_idle + total_non_idle;
        if (total > 0) {
            cpu_usage = ((double)total_non_idle / total) * 100.0;
        }
    }

    long ram_used_mb = (mem_total - mem_avail) / 1024;
    long ram_total_mb = mem_total / 1024;
    double ram_pct = mem_total > 0 ? ((double)(mem_total - mem_avail) / mem_total) * 100.0 : 0.0;

    // ----------------------------------------------------
    // 2. DISK TELEMETRY
    // ----------------------------------------------------
    FILE *f_disk = fopen("/proc/diskstats", "r");
    long reads_comp = 0, writes_comp = 0;
    if (f_disk) {
        char dev_name[64];
        while (fgets(buffer, sizeof(buffer), f_disk)) {
            long r_c, w_c;
            if (sscanf(buffer, "%*d %*d %63s %ld %*d %*d %*d %ld", dev_name, &r_c, &w_c) == 3) {
                if (strcmp(dev_name, "sda") == 0 || strcmp(dev_name, "nvme0n1") == 0) {
                    reads_comp = r_c;
                    writes_comp = w_c;
                    break;
                }
            }
        }
        fclose(f_disk);
    }

    // ----------------------------------------------------
    // 3. NETWORK SOCKET TELEMETRY (/proc/net/tcp)
    // ----------------------------------------------------
    FILE *f_net = fopen("/proc/net/tcp", "r");
    int active_tcp_sockets = 0;
    if (f_net) {
        while (fgets(buffer, sizeof(buffer), f_net)) {
            if (strstr(buffer, ":")) active_tcp_sockets++;
        }
        fclose(f_net);
    }

    // ----------------------------------------------------
    // ANSI CLEAR SCREEN & DASHBOARD HEADER
    // ----------------------------------------------------
    printf("\033[H\033[J"); // Clear ANSI terminal
    printf("⚡ ======================================================================== ⚡\n");
    printf("👑             AKV UNIFIED LIVE KERNEL ANSI DASHBOARD v1.0                 ⚡\n");
    printf("⚡ ======================================================================== ⚡\n\n");

    // PANEL 1: SYSTEM VITALS & DISK I/O
    printf("┌── [ 📊 SYSTEM VITALS & DISK TELEMETRY ] ────────────────────────────────┐\n");
    printf("│  • CPU Load     : %-6.2f%%                                              │\n", cpu_usage);
    printf("│  • RAM Usage    : %ld MB / %ld MB (%.2f%%)                               │\n", ram_used_mb, ram_total_mb, ram_pct);
    printf("│  • Active Sockets: %-4d Active TCP Connections                           │\n", active_tcp_sockets);
    printf("│  • Disk I/O     : Reads: %-8ld | Writes: %-8ld                   │\n", reads_comp, writes_comp);
    printf("└─────────────────────────────────────────────────────────────────────────┘\n\n");

    // PANEL 2: ACTIVE KERNEL PROCESS INSPECTION
    printf("┌── [ 🔍 TOP KERNEL PROCESSES ] ──────────────────────────────────────────┐\n");
    printf("│  %-8s %-24s %-12s                       │\n", "PID", "PROCESS NAME", "STATE");
    printf("├─────────────────────────────────────────────────────────────────────────┤\n");

    DIR *dir = opendir("/proc");
    struct dirent *entry;
    int count = 0;

    if (dir) {
        while ((entry = readdir(dir)) != NULL && count < 6) {
            if (!isdigit(entry->d_name[0])) continue;

            char stat_path[512];
            snprintf(stat_path, sizeof(stat_path), "/proc/%s/stat", entry->d_name);
            FILE *f_proc = fopen(stat_path, "r");

            if (f_proc) {
                int pid;
                char comm[256], state;
                if (fscanf(f_proc, "%d (%255[^)]) %c", &pid, comm, &state) == 3) {
                    printf("│  %-8d %-24s %-12c                       │\n", pid, comm, state);
                    count++;
                }
                fclose(f_proc);
            }
        }
        closedir(dir);
    }
    printf("└─────────────────────────────────────────────────────────────────────────┘\n\n");
    printf("---------------------------------------------------------------------------\n");
    printf("STATUS: LIVE RUNNING | REFRESH: REALTIME | PRESS CTRL+C TO EXIT            \n");
    printf("---------------------------------------------------------------------------\n");
}

int main() {
    for (int i = 0; i < 3; i++) {
        render_dashboard();
        sleep(1);
    }
    return 0;
}
