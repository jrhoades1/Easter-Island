# Easter Island Language Scraper

A Python web scraper for collecting Rapa Nui language data from multiple online sources for linguistic analysis.

## Features

- **Multi-source scraping** - Collects data from Wikipedia, IDS, ASJP, Glosbe, and Omniglot
- **Structured output** - JSON format with translations, IPA, part of speech, and metadata
- **Deduplication** - Merges entries from multiple sources automatically
- **Extensible** - Modular parser architecture for adding new sources

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/easter-island-scraper.git
cd easter-island-scraper

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Scrape Rapa Nui Language Data

```bash
python language_scraper.py
```

Output is saved to `output/rapa_nui_language.json`.

### Scrape General Easter Island Content

```bash
python scraper.py
```

Output is saved to `output/easter_island.json`.

## Output Format

The language scraper produces JSON with the following structure:

```json
{
  "scraped_at": "2024-01-19T10:30:00.000000",
  "version": "1.0.0",
  "language": {
    "name": "Rapa Nui",
    "native_name": "Vananga rapa nui",
    "iso_639_3": "rap",
    "glottocode": "rapa1244",
    "family": "Austronesian > Polynesian > Eastern"
  },
  "statistics": {
    "total_entries": 39,
    "sources_scraped": 5,
    "entries_by_pos": {"numeral": 20, "pronoun": 10}
  },
  "entries": [
    {
      "word": "tahi",
      "normalized": "tahi",
      "translations": [{"language": "en", "text": "1 (cardinal)"}],
      "part_of_speech": "numeral",
      "metadata": {
        "source_url": "https://en.wikipedia.org/wiki/Rapa_Nui_language",
        "source_name": "Wikipedia",
        "scraped_at": "2024-01-19T10:30:00.000000",
        "confidence": "medium"
      }
    }
  ],
  "sources": [
    {"url": "...", "name": "Wikipedia", "entries_contributed": 30}
  ]
}
```

## Data Sources

| Source | URL | Content |
|--------|-----|---------|
| Wikipedia | en.wikipedia.org/wiki/Rapa_Nui_language | Numerals, pronouns, grammar tables |
| IDS | ids.clld.org | Intercontinental Dictionary Series |
| ASJP | asjp.clld.org | Core vocabulary wordlist |
| Glosbe | glosbe.com/en/rap | Community translations |
| Omniglot | omniglot.com/writing/rapanui.htm | Phrases and alphabet |

## Project Structure

```
easter-island-scraper/
├── language_scraper.py    # Main language scraping script
├── scraper.py             # General Easter Island scraper
├── config.py              # Configuration and URLs
├── models/
│   └── language.py        # LanguageEntry dataclass
├── parsers/
│   └── language/          # Site-specific parsers
│       ├── base.py        # Base parser class
│       ├── wikipedia.py   # Wikipedia parser
│       ├── ids.py         # IDS parser
│       └── ...
├── tests/
│   ├── fixtures/          # Saved HTML for testing
│   ├── test_parsers.py    # Parser unit tests
│   ├── test_models.py     # Model tests
│   └── test_integration.py
└── output/                # Scraped data (gitignored)
```

## Running Tests

```bash
python -m unittest discover -s tests -v
```

## Adding New Sources

1. Create a new parser in `parsers/language/`:

```python
from .base import BaseLanguageParser
from models.language import LanguageEntry

class MyParser(BaseLanguageParser):
    source_name = "My Source"

    def can_parse(self, url: str) -> bool:
        return "mysource.com" in url

    def parse(self, html: str, url: str) -> list[LanguageEntry]:
        # Parse HTML and return entries
        ...
```

2. Register in `parsers/language/__init__.py`
3. Add URL to `config.py` under `LANGUAGE_CONFIG`

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- Rapa Nui language data sourced from publicly available linguistic databases
- Built for linguistic research and language preservation efforts
