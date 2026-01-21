"""Rapa Nui language scraper - collects language examples from multiple sources."""

import json
import os
import time
from datetime import datetime

import requests

import config
from models.language import LanguageEntry
from parsers.language import get_language_parser


def fetch_page(url: str) -> str | None:
    """Fetch a page and return its HTML content."""
    try:
        print(f"  Fetching: {url}")
        response = requests.get(url, headers=config.HEADERS, timeout=config.TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"  Error fetching {url}: {e}")
        return None


def deduplicate_entries(entries: list[LanguageEntry]) -> list[LanguageEntry]:
    """Merge entries for the same word from multiple sources."""
    merged: dict[str, LanguageEntry] = {}

    for entry in entries:
        key = entry.normalized
        if key in merged:
            # Merge with existing entry
            merged[key] = merged[key].merge_with(entry)
        else:
            merged[key] = entry

    return list(merged.values())


def compute_statistics(entries: list[LanguageEntry]) -> dict:
    """Compute statistics about the scraped entries."""
    categories: dict[str, int] = {}
    pos: dict[str, int] = {}

    for entry in entries:
        if entry.semantic_category:
            categories[entry.semantic_category] = categories.get(entry.semantic_category, 0) + 1
        if entry.part_of_speech:
            pos[entry.part_of_speech] = pos.get(entry.part_of_speech, 0) + 1

    return {
        "total_entries": len(entries),
        "sources_scraped": len(config.LANGUAGE_CONFIG["rapa_nui"]["urls"]),
        "entries_by_category": categories,
        "entries_by_pos": pos,
    }


def collect_source_attribution(entries: list[LanguageEntry]) -> list[dict]:
    """Collect source attribution information."""
    sources: dict[str, dict] = {}

    for entry in entries:
        if entry.metadata:
            url = entry.metadata.source_url
            name = entry.metadata.source_name
            if url not in sources:
                sources[url] = {
                    "url": url,
                    "name": name,
                    "license": None,  # Could be extended to include license info
                    "entries_contributed": 0,
                }
            sources[url]["entries_contributed"] += 1

    return list(sources.values())


def scrape_language_data() -> dict:
    """Scrape Rapa Nui language data from all configured sources."""
    lang_config = config.LANGUAGE_CONFIG["rapa_nui"]
    all_entries: list[LanguageEntry] = []

    print(f"Starting Rapa Nui language scraper...")
    print(f"Sources to scrape: {len(lang_config['urls'])}")
    print()

    for i, url in enumerate(lang_config["urls"], 1):
        print(f"[{i}/{len(lang_config['urls'])}] Processing source...")

        # Get the appropriate parser
        parser = get_language_parser(url)
        if not parser:
            print(f"  No parser available for: {url}")
            continue

        print(f"  Using parser: {parser.source_name}")

        # Fetch the page
        html = fetch_page(url)
        if not html:
            continue

        # Parse the content
        try:
            entries = parser.parse(html, url)
            print(f"  Found {len(entries)} entries")
            all_entries.extend(entries)
        except Exception as e:
            print(f"  Error parsing: {e}")

        # Be polite - add a small delay between requests
        if i < len(lang_config["urls"]):
            time.sleep(1)

        print()

    # Deduplicate entries
    print(f"Total entries before deduplication: {len(all_entries)}")
    unique_entries = deduplicate_entries(all_entries)
    print(f"Unique entries after deduplication: {len(unique_entries)}")
    print()

    # Sort entries alphabetically
    unique_entries.sort(key=lambda e: e.normalized)

    # Build output structure
    output = {
        "scraped_at": datetime.now().isoformat(),
        "version": "1.0.0",
        "language": {
            "name": lang_config["name"],
            "native_name": lang_config["native_name"],
            "iso_639_3": lang_config["iso_639_3"],
            "glottocode": lang_config["glottocode"],
            "family": lang_config["family"],
        },
        "statistics": compute_statistics(unique_entries),
        "entries": [entry.to_dict() for entry in unique_entries],
        "sources": collect_source_attribution(unique_entries),
    }

    return output


def save_output(data: dict) -> str:
    """Save the scraped data to a JSON file."""
    # Ensure output directory exists
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)

    output_file = config.LANGUAGE_CONFIG["rapa_nui"]["output_file"]
    output_path = os.path.join(config.OUTPUT_DIR, output_file)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return output_path


def main():
    """Main entry point for the language scraper."""
    print("=" * 60)
    print("Rapa Nui Language Scraper")
    print("=" * 60)
    print()

    # Scrape data
    data = scrape_language_data()

    # Save output
    output_path = save_output(data)

    # Print summary
    print("=" * 60)
    print("Scraping Complete!")
    print("=" * 60)
    print(f"Output saved to: {output_path}")
    print(f"Total unique entries: {data['statistics']['total_entries']}")
    print(f"Sources scraped: {data['statistics']['sources_scraped']}")

    if data["statistics"]["entries_by_category"]:
        print("\nEntries by semantic category:")
        for cat, count in sorted(data["statistics"]["entries_by_category"].items()):
            print(f"  {cat}: {count}")

    if data["statistics"]["entries_by_pos"]:
        print("\nEntries by part of speech:")
        for pos, count in sorted(data["statistics"]["entries_by_pos"].items()):
            print(f"  {pos}: {count}")

    print()


if __name__ == "__main__":
    main()
