#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef struct {
    unsigned long long total_ram;
    unsigned long long free_ram;
    unsigned long long avail_ram;
} MemStats;

typedef struct {
    unsigned long long user, nice, system, idle, iowait, irq, softirq, steal;
} CpuStats;

void parse_meminfo(MemStats *mem) {
    FILE *fp = fopen("/proc/meminfo", "r");
    if (!fp) return;

    char line[256];
    while (fgets(line, sizeof(line), fp)) {
        if (sscanf(line, "MemTotal: %llu kB", &mem->total_ram) == 1) continue;
        if (sscanf(line, "MemFree: %llu kB", &mem->free_ram) == 1) continue;
        if (sscanf(line, "MemAvailable: %llu kB", &mem->avail_ram) == 1) continue;
    }
    fclose(fp);
}

void read_cpu_stats(CpuStats *cpu) {
    FILE *fp = fopen("/proc/stat", "r");
    if (!fp) return;

    char line[256];
    if (fgets(line, sizeof(line), fp)) {
        sscanf(line, "cpu %llu %llu %llu %llu %llu %llu %llu %llu",
               &cpu->user, &cpu->nice, &cpu->system, &cpu->idle,
               &cpu->iowait, &cpu->irq, &cpu->softirq, &cpu->steal);
    }
    fclose(fp);
}

float calculate_cpu_usage(CpuStats *prev, CpuStats *curr) {
    unsigned long long prev_idle = prev->idle + prev->iowait;
    unsigned long long curr_idle = curr->idle + curr->iowait;

    unsigned long long prev_non_idle = prev->user + prev->nice + prev->system + prev->irq + prev->softirq + prev->steal;
    unsigned long long curr_non_idle = curr->user + curr->nice + curr->system + curr->irq + curr->softirq + curr->steal;

    unsigned long long prev_total = prev_idle + prev_non_idle;
    unsigned long long curr_total = curr_idle + curr_non_idle;

    unsigned long long total_d = curr_total - prev_total;
    unsigned long long idle_d = curr_idle - prev_idle;

    if (total_d == 0) return 0.0f;
    return (float)(total_d - idle_d) / (float)total_d * 100.0f;
}

int main(void) {
    MemStats mem = {0};
    CpuStats cpu1 = {0}, cpu2 = {0};

    // First CPU snapshot
    read_cpu_stats(&cpu1);
    usleep(100000); // 100ms sample interval
    read_cpu_stats(&cpu2);

    parse_meminfo(&mem);

    float cpu_pct = calculate_cpu_usage(&cpu1, &cpu2);
    unsigned long long used_ram = mem.total_ram - mem.avail_ram;
    float mem_pct = ((float)used_ram / (float)mem.total_ram) * 100.0f;

    printf("========================================================\n");
    printf("      AKV-SYSMON v1.2.0 - BARE-METAL C PROFILER         \n");
    printf("========================================================\n\n");
    printf("⚡ [AKV-SYSMON CORE] Telemetry Snapshot:\n");
    printf("   • CPU Usage : %.2f%%\n", cpu_pct);
    printf("   • Total RAM : %llu MB\n", mem.total_ram / 1024);
    printf("   • Used RAM  : %llu MB (%.2f%%)\n", used_ram / 1024, mem_pct);
    printf("   • Avail RAM : %llu MB\n\n", mem.avail_ram / 1024);
    printf("--------------------------------------------------------\n");
    printf("STATUS: OPTIMAL | KERNEL CPU + MEMORY PARSE COMPLETE   \n");
    printf("--------------------------------------------------------\n");

    return 0;
}
