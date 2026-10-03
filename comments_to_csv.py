"""Export the comments of a video to a CSV file.

    python comments_to_csv.py https://www.tiktok.com/@tiktok/video/1234567890 --max 500
"""
import argparse
import csv

from omarthing import Client


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video", help="video id or any TikTok video URL")
    ap.add_argument("--max", type=int, default=200, help="stop after this many comments")
    ap.add_argument("--out", default="comments.csv")
    args = ap.parse_args()

    api = Client()
    rows, cursor = [], None
    while len(rows) < args.max:
        page = api.comments(args.video, cursor=cursor, format="clean")
        rows += page["comments"]
        if not page["has_more"]:
            break
        cursor = page["next_cursor"]
    rows = rows[: args.max]

    cols = ["comment_id", "username", "nickname", "comment", "likes", "replies_count", "created_at"]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"saved {len(rows)} comments to {args.out}")


if __name__ == "__main__":
    main()
