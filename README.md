# Web Scraper Python

Command-line web scraper that collects the latest Hacker News titles with Python.

## Highlights

- Uses `requests` and `BeautifulSoup`
- Timeout and error handling for network failures
- Plain text and JSON output modes
- Simple CLI with configurable result limit

## Stack

- Python
- Requests
- Beautiful Soup

## Install

```bash
pip install -r requirements.txt
```

## Run locally

```bash
python scraper.py
```

Fetch a shorter list:

```bash
python scraper.py --limit 5
```

Output JSON:

```bash
python scraper.py --json
```

## Author

Douglas Aparecido Silva
