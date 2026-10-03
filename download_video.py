"""Download a TikTok video (no watermark when available).

    python download_video.py https://www.tiktok.com/@tiktok/video/1234567890
"""
import sys

import requests

from omarthing import Client


def main(video):
    info = Client().video_download(video)
    url = info.get("no_watermark_url") or info.get("best_url") or info.get("download_url")
    if not url:
        sys.exit("no downloadable URL in the response")
    name = f"{info.get('author', 'tiktok')}_{video.rstrip('/').split('/')[-1].split('?')[0]}.mp4"
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(name, "wb") as f:
            for chunk in r.iter_content(1 << 16):
                f.write(chunk)
    print("saved", name)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
