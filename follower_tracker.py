"""Track follower counts over time. Run it daily from cron.

    python follower_tracker.py tiktok khaby.lame
Appends one row per account to followers.csv and prints the change since last run.
"""
import csv
import os
import sys
from datetime import datetime, timezone

from omarthing import Client

FILE = "followers.csv"


def last_counts():
    if not os.path.exists(FILE):
        return {}
    last = {}
    with open(FILE, newline="") as f:
        for row in csv.DictReader(f):
            last[row["username"]] = int(row["followers"])
    return last


def main(usernames):
    api = Client()
    previous = last_counts()
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["time_utc", "username", "followers"])
        for name in usernames:
            followers = api.profile(username=name, format="clean")["followers"]
            w.writerow([datetime.now(timezone.utc).isoformat(timespec="seconds"), name, followers])
            diff = followers - previous[name] if name in previous else None
            print(f"{name}: {followers:,}" + (f" ({diff:+,} since last run)" if diff is not None else ""))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
