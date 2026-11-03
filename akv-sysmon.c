#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_sys_metrics() {
    FILE *f_mem = fopen("/proc/meminfo", "r");
    if (!f_mem) return;

    long mem_total = 0, mem_free = 0, mem_avail = 0;
    char buffer[256];

    while (fgets(buffer, sizeof(buffer), f_mem)) {
        if (sscanf(buffer, "MemTotal: %ld kB", &mem_total) == 1) continue;
        if (sscanf(buffer, "MemFree: %ld kB", &mem_free) == 1) continue;
        if (sscanf(buffer, "MemAvailable: %ld kB", &mem_avail) == 1) continue;
    }
    fclose(f_mem);

    FILE *f_stat = fopen("/proc/stat", "r");
    if (!f_stat) return;

    long user, nice, system, idle, iowait, irq, softirq;
    if (fgets(buffer, sizeof(buffer), f_stat)) {
        sscanf(buffer, "cpu %ld %ld %ld %ld %ld %ld %ld",
               &user, &nice, &system, &idle, &iowait, &irq, &softirq);
    }
    fclose(f_stat);

    long total_idle = idle + iowait;
    long total_non_idle = user + nice + system + irq + softirq;
    long total = total_idle + total_non_idle;

    double cpu_usage = 0.0;
    if (total > 0) {
        cpu_usage = ((double)total_non_idle / total) * 100.0;
    }

    long ram_used_mb = (mem_total - mem_avail) / 1024;
    long ram_total_mb = mem_total / 1024;
    double ram_pct = ((double)(mem_total - mem_avail) / mem_total) * 100.0;

    // Disk I/O Telemetry Read from /proc/diskstats
    FILE *f_disk = fopen("/proc/diskstats", "r");
    long reads_completed = 0, writes_completed = 0;
    if (f_disk) {
        char dev_name[64];
        while (fgets(buffer, sizeof(buffer), f_disk)) {
            long r_comp, w_comp;
            if (sscanf(buffer, "%*d %*d %63s %ld %*d %*d %*d %ld", dev_name, &r_comp, &w_comp) == 3) {
                if (strcmp(dev_name, "sda") == 0 || strcmp(dev_name, "nvme0n1") == 0) {
                    reads_completed = r_comp;
                    writes_completed = w_comp;
                    break;
                }
            }
        }
        fclose(f_disk);
    }

    printf("\033[H\033[J"); // Clear ANSI terminal
    printf("========================================================\n");
    printf("       AKV-SYSMON v1.4.0 - LIVE TERMINAL DASHBOARD      \n");
    printf("========================================================\n\n");
    printf("⚡ [KERNEL TELEMETRY]:\n");
    printf("   • CPU Usage    : %.2f%%\n", cpu_usage);
    printf("   • Total RAM    : %ld MB\n", ram_total_mb);
    printf("   • Used RAM     : %ld MB (%.2f%%)\n", ram_used_mb, ram_pct);
    printf("   • Avail RAM    : %ld MB\n\n", mem_avail / 1024);
    printf("💾 [DISK TELEMETRY]:\n");
    printf("   • Read Ops     : %ld\n", reads_completed);
    printf("   • Write Ops    : %ld\n\n", writes_completed);
    printf("--------------------------------------------------------\n");
    printf("STATUS: ACTIVE | REFRESH: REALTIME | PRESS CTRL+C TO EXIT\n");
    printf("--------------------------------------------------------\n");
}

int main() {
    for (int i = 0; i < 3; i++) {
        get_sys_metrics();
        sleep(1);
    }
    return 0;
}
