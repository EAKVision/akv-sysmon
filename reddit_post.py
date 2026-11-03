import praw
import sys

# Fill in your Reddit API credentials below
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
USER_AGENT = "script:akv_sysmon_syndicator:v1.0 (by /u/YOUR_REDDIT_USERNAME)"
USERNAME = "YOUR_REDDIT_USERNAME"
PASSWORD = "YOUR_REDDIT_PASSWORD"

def post_to_reddit(subreddit_name, title, body):
    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT,
            username=USERNAME,
            password=PASSWORD
        )
        
        subreddit = reddit.subreddit(subreddit_name)
        submission = subreddit.submit(title, selftext=body)
        print(f"✅ Successfully posted to r/{subreddit_name}!")
        print(f"🔗 URL: {submission.url}\n")
    except Exception as e:
        print(f"❌ Failed to post to r/{subreddit_name}: {e}\n")

if __name__ == "__main__":
    c_title = "Built a bare-metal Linux system profiler in pure C with sub-1ms latency under load (v1.2.0)"
    c_body = """
Hey everyone,

I recently published `akv-sysmon`, a low-overhead CLI telemetry profiler written in standard C for Linux systems.

Instead of relying on heavy third-party libraries, it parses `/proc/meminfo` and `/proc/stat` directly to calculate accurate real-time CPU utilization deltas and memory metrics.

Engineering Details:
- Optimization: Compiled with `gcc -O3 -Wall -Wextra`.
- Benchmarks: Tested under severe synthetic load via `stress-ng` (2 CPU stressors + 5.8GB RAM allocation). Telemetry parsing finishes in under 0.001s with 0 memory leaks.
- Portable Web Preview: Deployed an xterm web terminal preview on GitHub Pages so you can test CLI commands right in the browser.

Source Code & Telemetry Logs: https://github.com/EAKVision/akv-sysmon
Live Terminal Demo: https://EAKVision.github.io/akv-sysmon/

Feedback on the C parsing architecture or delta calculation logic is welcome!
"""
    
    print("🚀 Auto-publishing to Reddit...")
    post_to_reddit("C_Programming", c_title, c_body)
