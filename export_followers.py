"""Export an account's followers to CSV (cursor-paginated).

    python export_followers.py tiktok --max 1000
"""
import argparse
import csv

from omarthing import Client


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("username")
    ap.add_argument("--max", type=int, default=500)
    ap.add_argument("--out", default="followers_export.csv")
    args = ap.parse_args()

    api = Client()
    rows, cursor = [], None
    while len(rows) < args.max:
        page = api.followers(args.username, cursor=cursor, format="clean")
        rows += page["followers"]
        if not page["has_more"]:
            break
        cursor = page["next_cursor"]
    rows = rows[: args.max]

    cols = ["nickname", "sec_uid", "country", "follower_count", "following_count", "aweme_count", "is_private", "signature"]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"saved {len(rows)} followers to {args.out}")


if __name__ == "__main__":
    main()
