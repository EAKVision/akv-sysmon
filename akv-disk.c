/*
 * ============================================================================
 * AKV-DISK v1.0 - Bare-Metal Disk & I/O Telemetry Module
 * Author: Amr / EAKVision (ELITE AKV)
 * Description: Parses /proc/diskstats directly with zero external dependencies.
 * ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define PROC_DISKSTATS "/proc/diskstats"
#define VERSION "v1.0.0-ELITE"

void render_disk_telemetry() {
    FILE *fp = fopen(PROC_DISKSTATS, "r");
    if (!fp) {
        perror("[-] Failed to open /proc/diskstats");
        return;
    }

    char line[256];
    printf("\033[H\033[J"); // Clear screen for live ANSI refresh
    printf("========================================================\n");
    printf("     👑 AKV-DISK TELEMETRY ENGINE [%s] 👑\n", VERSION);
    printf("========================================================\n");
    printf("%-10s %-12s %-15s %-15s\n", "Device", "Reads Completed", "Sectors Read", "Time Reading (ms)");
    printf("--------------------------------------------------------\n");

    int count = 0;
    while (fgets(line, sizeof(line), fp) && count < 10) {
        int major, minor;
        char devname[32];
        unsigned long reads_completed, sectors_read, time_reading;
        unsigned long writes_completed, sectors_written, time_writing;

        // Parse standard Linux /proc/diskstats format
        if (sscanf(line, "%d %d %31s %lu %*u %lu %*u %lu %*u %lu %*u %*u %*u %*u",
                   &major, &minor, devname,
                   &reads_completed, &sectors_read, &time_reading,
                   &writes_completed, &sectors_written, &time_writing) >= 6) {
            
            // Filter out loop devices and partitions for clean primary disk telemetry
            if (strncmp(devname, "sd", 2) == 0 || strncmp(devname, "nvme", 4) == 0) {
                printf("%-10s %-12lu %-15lu %-15lu\n", devname, reads_completed, sectors_read, time_reading);
                count++;
            }
        }
    }

    fclose(fp);
    printf("========================================================\n");
    printf("⚡ AKV Ecosystem | 360° Vision | All energies. ♟️ Checkmate.\n");
}

int main() {
    while (1) {
        render_disk_telemetry();
        sleep(2); // Refresh every 2 seconds
    }
    return 0;
}
