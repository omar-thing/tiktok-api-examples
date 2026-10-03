"""Get notified when TikTok accounts go live.

    python live_alert.py tiktok someuser --every 60
    DISCORD_WEBHOOK=https://discord.com/api/webhooks/... python live_alert.py someuser
Prints a line when an account goes live; also posts to a Discord webhook if set.
"""
import argparse
import os
import time

import requests

from omarthing import Client, OmarThingError


def notify(text):
    print(text, flush=True)
    hook = os.environ.get("DISCORD_WEBHOOK")
    if hook:
        requests.post(hook, json={"content": text}, timeout=15)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("usernames", nargs="+")
    ap.add_argument("--every", type=int, default=60, help="seconds between checks")
    args = ap.parse_args()
    api = Client()
    was_live = {}
    while True:
        for name in args.usernames:
            try:
                live = bool(api.room_id(name)["is_live"])
            except OmarThingError as e:
                print(f"{name}: {e}")
                continue
            if live and not was_live.get(name):
                notify(f"{name} is LIVE: https://www.tiktok.com/@{name}/live")
            was_live[name] = live
        time.sleep(args.every)


if __name__ == "__main__":
    main()
