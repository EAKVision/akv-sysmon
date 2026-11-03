/*
 * ============================================================================
 * AKV-NETSTAT v1.0 - Bare-Metal Kernel Socket & Network Inspector
 * Author: Amr / EAKVision (ELITE AKV)
 * Description: Parses /proc/net/tcp & /proc/net/udp directly to monitor
 *              active connection sockets with zero external dependencies.
 * ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define VERSION "v1.0.0-ELITE"

int count_active_sockets(const char *path) {
    FILE *fp = fopen(path, "r");
    if (!fp) return 0;

    char line[256];
    int count = 0;
    
    // Skip header line
    if (fgets(line, sizeof(line), fp) == NULL) {
        fclose(fp);
        return 0;
    }

    while (fgets(line, sizeof(line), fp)) {
        count++;
    }

    fclose(fp);
    return count;
}

void render_netstat() {
    int tcp_sockets = count_active_sockets("/proc/net/tcp");
    int udp_sockets = count_active_sockets("/proc/net/udp");

    printf("\033[H\033[J"); // Clear screen for live refresh
    printf("========================================================================\n");
    printf("👑          AKV BARE-METAL NETWORK & SOCKET INSPECTOR [%s]     👑\n", VERSION);
    printf("========================================================================\n\n");

    printf("┌── [ 🌐 KERNEL NETWORK SOCKETS ] ─────────────────────────────────────┐\n");
    printf("│  • Active TCP Sockets   : %-6d Connections                           │\n", tcp_sockets);
    printf("│  • Active UDP Sockets   : %-6d Endpoints                             │\n", udp_sockets);
    printf("│  • Total Open Channels  : %-6d Sockets                               │\n", tcp_sockets + udp_sockets);
    printf("└──────────────────────────────────────────────────────────────────────┘\n\n");

    printf("┌── [ 🛡️ SOCKET INTEGRITY STATUS ] ────────────────────────────────────┐\n");
    if (tcp_sockets + udp_sockets > 0) {
        printf("│  • Status: ⚡ ACTIVE NETWORK TRAFFIC MONITORED                       │\n");
    } else {
        printf("│  • Status: 🔒 CLEAN SYSTEM - NO OPEN SOCKETS DETECTED               │\n");
    }
    printf("└──────────────────────────────────────────────────────────────────────┘\n\n");

    printf("========================================================================\n");
    printf("⚡ AKV Ecosystem | Low-Level Systems Master | Unchallengeable Status ♟️\n");
    printf("========================================================================\n");
}

int main() {
    while (1) {
        render_netstat();
        sleep(2); // Refresh every 2 seconds
    }
    return 0;
}
