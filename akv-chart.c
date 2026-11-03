#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define HISTORY_LEN 40

static double cpu_history[HISTORY_LEN] = {0};
static double ram_history[HISTORY_LEN] = {0};

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

void render_chart() {
    double cpu, ram;
    get_sys_vitals(&cpu, &ram);

    // Shift history left
    for (int i = 0; i < HISTORY_LEN - 1; i++) {
        cpu_history[i] = cpu_history[i + 1];
        ram_history[i] = ram_history[i + 1];
    }
    cpu_history[HISTORY_LEN - 1] = cpu;
    ram_history[HISTORY_LEN - 1] = ram;

    printf("\033[H\033[J"); // Clear screen
    printf("⚡ ======================================================== ⚡\n");
    printf("👑             AKV REAL-TIME TERMINAL CHARTING v1.0         ⚡\n");
    printf("⚡ ======================================================== ⚡\n\n");

    printf("📊 Live CPU Load Graph (Current: %.2f%%):\n", cpu);
    printf("┌─────────────────────────────────────────┐\n│ ");
    for (int i = 0; i < HISTORY_LEN; i++) {
        double val = cpu_history[i];
        if (val < 5.0) printf(" ");
        else if (val < 25.0) printf("▂");
        else if (val < 50.0) printf("▄");
        else if (val < 75.0) printf("▆");
        else printf("█");
    }
    printf(" │\n└─────────────────────────────────────────┘\n\n");

    printf("💾 Live RAM Usage Graph (Current: %.2f%%):\n", ram);
    printf("┌─────────────────────────────────────────┐\n│ ");
    for (int i = 0; i < HISTORY_LEN; i++) {
        double val = ram_history[i];
        if (val < 10.0) printf(" ");
        else if (val < 30.0) printf("▂");
        else if (val < 50.0) printf("▄");
        else if (val < 75.0) printf("▆");
        else printf("█");
    }
    printf(" │\n└─────────────────────────────────────────┘\n\n");
    printf("--------------------------------------------------------\n");
    printf("STATUS: LIVE GRAPHING | REFRESH: REALTIME | CTRL+C TO EXIT\n");
    printf("--------------------------------------------------------\n");
}

int main() {
    for (int i = 0; i < 3; i++) {
        render_chart();
        sleep(1);
    }
    return 0;
}
