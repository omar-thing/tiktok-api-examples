# tiktok-api-examples

Small scripts built on the [Omar-Thing TikTok API](https://dev.omar-thing.site) (Python).
Each one is a single file, copy what you need.

```bash
pip install omarthing requests
export OMARTHING_API_KEY=YOUR_API_KEY    # key from https://dev.omar-thing.site
```

| Script | What it does |
|---|---|
| `follower_tracker.py` | Logs follower counts to a CSV on every run and prints the change (good for cron) |
| `live_alert.py` | Prints (and optionally posts to a Discord webhook) when accounts go live |
| `comments_to_csv.py` | Exports a video's comments to CSV |
| `export_followers.py` | Exports an account's followers to CSV |
| `download_video.py` | Downloads a video, no watermark when available |
| `trending_by_country.py` | Trending searches per country |
| `live_chat_reader.py` | Prints a live stream's chat in the terminal |

```bash
python follower_tracker.py tiktok khaby.lame
python live_alert.py someuser --every 60
python comments_to_csv.py https://www.tiktok.com/@tiktok/video/1234567890 --max 500
python trending_by_country.py US GB BR --count 10
```

Endpoint reference: https://dev.omar-thing.site/docs.html

MIT. Unofficial: not affiliated with or endorsed by TikTok or ByteDance.
