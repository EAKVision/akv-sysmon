#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <ctype.h>

int is_digit(const char *str) {
    while (*str) {
        if (!isdigit(*str)) return 0;
        str++;
    }
    return 1;
}

void display_top_processes() {
    DIR *dir = opendir("/proc");
    if (!dir) {
        printf("   [!] Failed to open /proc directory.\n");
        return;
    }

    struct dirent *entry;
    int count = 0;

    printf("   [ACTIVE KERNEL PROCESS INSPECTION]:\n");
    printf("   --------------------------------------------------------\n");
    printf("   %-8s %-30s %-10s\n", "PID", "PROCESS NAME", "STATE");
    printf("   --------------------------------------------------------\n");

    while ((entry = readdir(dir)) != NULL && count < 8) {
        if (is_digit(entry->d_name)) {
            char path[512];
            snprintf(path, sizeof(path), "/proc/%s/stat", entry->d_name);
            
            FILE *f = fopen(path, "r");
            if (f) {
                int pid;
                char comm[256];
                char state;
                if (fscanf(f, "%d (%255[^)]) %c", &pid, comm, &state) == 3) {
                    printf("   %-8d %-30s %-10c\n", pid, comm, state);
                    count++;
                }
                fclose(f);
            }
        }
    }
    closedir(dir);
}

int main() {
    printf("========================================================\n");
    printf("       AKV-TOP v1.0 - KERNEL PROCESS SUBSYSTEM          \n");
    printf("========================================================\n\n");

    display_top_processes();

    printf("\n--------------------------------------------------------\n");
    printf("STATUS: PROCESS SCAN COMPLETE\n");
    printf("--------------------------------------------------------\n");

    return 0;
}
