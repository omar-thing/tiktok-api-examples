"""Read the live chat of a TikTok LIVE in your terminal.

    python live_chat_reader.py tiktok
Looks up the room, then polls /live_chat and passes the returned cursor back in.
"""
import sys
import time

from omarthing import Client


def read(api, room_id, delay=2.0, stop=lambda: False):
    cursor = None
    while not stop():
        page = api.live_chat(room_id, cursor=cursor)
        for m in page["messages"]:
            if m.get("text"):
                print(f"{m.get('username') or m.get('nickname')}: {m.get('text', '')}", flush=True)
        cursor = page.get("next_cursor") or cursor
        time.sleep(delay)


def main(username):
    api = Client()
    info = api.room_id(username)
    if not info["is_live"]:
        sys.exit(f"{username} is not live right now")
    read(api, info["room_id"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1].lstrip("@"))
