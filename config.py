"""Configuration settings for Easter Island web scraper."""

import os

# Target URLs to scrape
URLS = [
    "https://en.wikipedia.org/wiki/Easter_Island",
]

# HTTP request settings
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
TIMEOUT = 30  # seconds

# Output settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_FILE = "easter_island.json"
