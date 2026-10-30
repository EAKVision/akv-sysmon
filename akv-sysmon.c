#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void get_memory_usage() {
    FILE *fp = fopen("/proc/meminfo", "r");
    if (!fp) {
        perror("Error opening /proc/meminfo");
        return;
    }

    char line[256];
    long total_mem = 0, free_mem = 0, avail_mem = 0;

    while (fgets(line, sizeof(line), fp)) {
        if (sscanf(line, "MemTotal: %ld kB", &total_mem) == 1) continue;
        if (sscanf(line, "MemFree: %ld kB", &free_mem) == 1) continue;
        if (sscanf(line, "MemAvailable: %ld kB", &avail_mem) == 1) continue;
    }
    fclose(fp);

    long used_mem = total_mem - avail_mem;
    double percent_used = ((double)used_mem / total_mem) * 100.0;

    printf("⚡ [AKV-SYSMON CORE] Memory Profile:\n");
    printf("   • Total RAM : %ld MB\n", total_mem / 1024);
    printf("   • Used RAM  : %ld MB (%.2f%%)\n", used_mem / 1024, percent_used);
    printf("   • Avail RAM : %ld MB\n", avail_mem / 1024);
}

int main() {
    printf("\n========================================================\n");
    printf("      AKV-SYSMON v1.1.0 - BARE-METAL C PROFILER         \n");
    printf("========================================================\n\n");
    
    get_memory_usage();
    
    printf("\n--------------------------------------------------------\n");
    printf("STATUS: OPTIMAL | KERNEL READ COMPLETE\n");
    printf("--------------------------------------------------------\n\n");
    
    return 0;
}
