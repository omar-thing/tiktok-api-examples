"""Show what people search for on TikTok right now, per country.

    python trending_by_country.py US GB BR --count 10
"""
import argparse

from omarthing import Client


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("regions", nargs="+", help="ISO country codes, e.g. US GB SA")
    ap.add_argument("--count", type=int, default=10)
    args = ap.parse_args()
    api = Client()
    for region in args.regions:
        data = api.trending_searches(region=region.upper(), count=args.count)
        print(f"\n== {region.upper()} ==")
        for i, w in enumerate(data["words"], 1):
            print(f"{i:>2}. {w['trendingSearchWord']}")


if __name__ == "__main__":
    main()
