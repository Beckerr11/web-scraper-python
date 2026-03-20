import argparse
import json
from typing import List

import requests
from bs4 import BeautifulSoup


DEFAULT_URL = "https://news.ycombinator.com"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
    )
}


def fetch_titles(limit: int) -> List[dict]:
    response = requests.get(DEFAULT_URL, headers=HEADERS, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title_nodes = soup.select("span.titleline a")

    entries = []
    for index, node in enumerate(title_nodes[:limit], start=1):
        entries.append(
            {
                "rank": index,
                "title": node.get_text(strip=True),
                "url": node.get("href", DEFAULT_URL),
            }
        )

    return entries


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scrape the latest Hacker News titles from the terminal."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum number of news titles to return.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the result as JSON instead of plain text.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        items = fetch_titles(max(1, args.limit))
    except requests.RequestException as error:
        print(f"Unable to fetch Hacker News titles: {error}")
        raise SystemExit(1) from error

    if args.json:
        print(json.dumps(items, indent=2, ensure_ascii=False))
        return

    print("\nLatest Hacker News titles")
    print("-------------------------")
    for item in items:
        print(f"{item['rank']:>2}. {item['title']}")
        print(f"    {item['url']}")


if __name__ == "__main__":
    main()
