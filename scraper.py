"""Easter Island web scraper - collects information and outputs JSON."""

import json
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import config


def fetch_page(url):
    """Fetch a web page and return its HTML content."""
    try:
        response = requests.get(url, headers=config.HEADERS, timeout=config.TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_wikipedia(html):
    """Parse Wikipedia page and extract structured content."""
    soup = BeautifulSoup(html, "lxml")

    # Get title
    title_elem = soup.find("h1", {"id": "firstHeading"})
    title = title_elem.get_text(strip=True) if title_elem else "Unknown"

    # Get summary (first paragraph)
    content_div = soup.find("div", {"id": "mw-content-text"})
    summary = ""
    if content_div:
        first_p = content_div.find("p", class_=lambda x: x != "mw-empty-elt")
        if first_p:
            summary = first_p.get_text(strip=True)

    # Get sections
    sections = []
    for heading in soup.find_all(["h2", "h3"]):
        headline = heading.find("span", class_="mw-headline")
        if headline:
            section_title = headline.get_text(strip=True)
            # Skip unwanted sections
            if section_title.lower() in ["see also", "references", "external links", "notes", "further reading"]:
                continue

            # Get content following the heading
            content_parts = []
            for sibling in heading.find_next_siblings():
                if sibling.name in ["h2", "h3"]:
                    break
                if sibling.name == "p":
                    text = sibling.get_text(strip=True)
                    if text:
                        content_parts.append(text)

            if content_parts:
                sections.append({
                    "title": section_title,
                    "content": " ".join(content_parts[:2])  # First 2 paragraphs
                })

    return {
        "title": title,
        "content": {
            "summary": summary,
            "sections": sections[:10]  # Limit to 10 sections
        }
    }


def scrape_all():
    """Scrape all configured URLs and return combined data."""
    sources = []

    for url in config.URLS:
        print(f"Scraping: {url}")
        html = fetch_page(url)

        if html:
            if "wikipedia.org" in url:
                parsed = parse_wikipedia(html)
            else:
                # Generic parsing for other sites
                soup = BeautifulSoup(html, "lxml")
                parsed = {
                    "title": soup.title.string if soup.title else "Unknown",
                    "content": {"summary": soup.get_text()[:1000]}
                }

            sources.append({
                "url": url,
                **parsed
            })

    return {
        "scraped_at": datetime.now().isoformat(),
        "sources": sources
    }


def save_json(data, filename):
    """Save data to a JSON file."""
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(config.OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Saved to: {filepath}")
    return filepath


def main():
    """Main entry point."""
    print("Easter Island Web Scraper")
    print("=" * 40)

    data = scrape_all()

    if data["sources"]:
        save_json(data, config.OUTPUT_FILE)
        print(f"\nScraped {len(data['sources'])} source(s) successfully.")
    else:
        print("\nNo data was scraped.")


if __name__ == "__main__":
    main()
