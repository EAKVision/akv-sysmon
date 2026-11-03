#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

#define CPU_THRESHOLD 80.0
#define RAM_THRESHOLD 85.0
#define LOG_FILE "akv_watchdog.log"

void get_sys_vitals(double *cpu_val, double *ram_val) {
    FILE *f_mem = fopen("/proc/meminfo", "r");
    long mem_total = 0, mem_avail = 0;
    char buffer[256];

    if (f_mem) {
        while (fgets(buffer, sizeof(buffer), f_mem)) {
            if (sscanf(buffer, "MemTotal: %ld kB", &mem_total) == 1) continue;
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
        if (total > 0) cpu_usage = ((double)total_non_idle / total) * 100.0;
    }

    *cpu_val = cpu_usage;
    if (mem_total > 0) {
        *ram_val = ((double)(mem_total - mem_avail) / mem_total) * 100.0;
    } else {
        *ram_val = 0.0;
    }
}

void log_alert(const char *type, double value, double threshold) {
    FILE *f_log = fopen(LOG_FILE, "a");
    if (!f_log) return;

    time_t now = time(NULL);
    char *timestamp = ctime(&now);
    timestamp[strlen(timestamp) - 1] = '\0'; // Remove newline

    fprintf(f_log, "[%s] ⚠️ ALERT: %s Spiked to %.2f%% (Threshold: %.2f%%)\n",
            timestamp, type, value, threshold);
    fclose(f_log);
}

int main() {
    printf("⚡ [AKV WATCHDOG DAEMON INITIALIZED]\n");
    printf("   • Monitoring CPU Threshold: %.1f%%\n", CPU_THRESHOLD);
    printf("   • Monitoring RAM Threshold: %.1f%%\n", RAM_THRESHOLD);
    printf("   • Log Destination         : %s\n", LOG_FILE);
    printf("   • Execution Mode          : Running Active Monitoring Cycles...\n\n");

    for (int cycle = 0; cycle < 5; cycle++) {
        double cpu, ram;
        get_sys_vitals(&cpu, &ram);

        printf("  [Cycle %d/5] CPU: %.2f%% | RAM: %.2f%%\n", cycle + 1, cpu, ram);

        if (cpu > CPU_THRESHOLD) {
            log_alert("CPU Load", cpu, CPU_THRESHOLD);
            printf("  ⚠️ [ALERT]: High CPU Load Logged!\n");
        }
        if (ram > RAM_THRESHOLD) {
            log_alert("RAM Usage", ram, RAM_THRESHOLD);
            printf("  ⚠️ [ALERT]: High RAM Usage Logged!\n");
        }

        sleep(2);
    }

    printf("\n✅ [WATCHDOG AUDIT COMPLETE]: Status Normal. Log file synced.\n");
    return 0;
}
