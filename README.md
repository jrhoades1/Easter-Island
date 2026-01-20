# Easter Island Research Tools

A Python toolkit for Easter Island linguistic and archaeological research, featuring:
- **Language Scraper** - Collects Rapa Nui language data from multiple online sources
- **Glyph Cataloger** - Uses computer vision to identify and catalog Rongorongo glyphs

## Features

### Language Scraper
- Multi-source scraping from Wikipedia, IDS, ASJP, Glosbe, and Omniglot
- Structured JSON output with translations, IPA, part of speech, and metadata
- Automatic deduplication across sources
- Modular parser architecture for adding new sources

### Glyph Cataloger
- Computer vision-based glyph detection from tablet images
- Feature extraction using Hu moments for shape analysis
- DBSCAN clustering to identify similar glyphs
- Unique ID assignment (G001, G002, ...) for each glyph type
- Lexicon output with frequency counts and positional analysis

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

### Catalog Rongorongo Glyphs

```bash
# Place tablet images in the input directory
cp my_tablet_scans/*.jpg input/tablets/

# Run the glyph cataloger
python glyph_cataloger.py
```

Output:
- `output/rongorongo_lexicon.json` - Glyph lexicon with clusters and statistics
- `output/glyphs/` - Extracted individual glyph images

### Scrape General Easter Island Content

```bash
python scraper.py
```

Output is saved to `output/easter_island.json`.

## Output Formats

### Language Scraper Output

```json
{
  "scraped_at": "2024-01-19T10:30:00.000000",
  "version": "1.0.0",
  "language": {
    "name": "Rapa Nui",
    "iso_639_3": "rap",
    "family": "Austronesian > Polynesian > Eastern"
  },
  "statistics": {
    "total_entries": 39,
    "sources_scraped": 5
  },
  "entries": [
    {
      "word": "tahi",
      "translations": [{"language": "en", "text": "1 (cardinal)"}],
      "part_of_speech": "numeral"
    }
  ]
}
```

### Glyph Cataloger Output

```json
{
  "version": "1.0.0",
  "created_at": "2024-01-20T10:00:00.000000",
  "source_images": ["tablet_a.jpg", "tablet_b.jpg"],
  "total_glyphs_detected": 1247,
  "unique_glyph_types": 412,
  "clusters": [
    {
      "cluster_id": "G001",
      "frequency": 47,
      "representative_image": "output/glyphs/G001_representative.png",
      "positions": {
        "line_distribution": {"1": 12, "2": 15, "3": 8},
        "avg_position_in_line": 0.35,
        "common_neighbors": ["G042", "G108"]
      }
    }
  ],
  "statistics": {
    "avg_glyphs_per_line": 14.2,
    "most_frequent_glyphs": ["G001", "G042", "G108"],
    "hapax_legomena": 89
  }
}
```

## Project Structure

```
easter-island/
├── language_scraper.py     # Rapa Nui language scraping
├── glyph_cataloger.py      # Rongorongo glyph cataloging
├── scraper.py              # General Easter Island scraper
├── config.py               # Configuration settings
├── models/
│   ├── language.py         # Language entry dataclass
│   └── glyphs.py           # Glyph data models
├── parsers/
│   └── language/           # Site-specific language parsers
├── processors/
│   └── glyph_processor.py  # CV processing pipeline
├── input/
│   └── tablets/            # Input tablet images
├── tests/
│   ├── fixtures/           # Test data
│   ├── test_parsers.py     # Parser tests
│   ├── test_glyph_*.py     # Glyph cataloger tests
│   └── ...
└── output/                 # Generated data (gitignored)
```

## Configuration

Edit `config.py` to customize:

### Language Scraper
- `LANGUAGE_CONFIG["rapa_nui"]["urls"]` - Source URLs to scrape

### Glyph Cataloger
- `GLYPH_CONFIG["processing"]` - Detection parameters (contour area, padding)
- `GLYPH_CONFIG["clustering"]` - DBSCAN parameters (eps, min_samples)

## Running Tests

```bash
# Run all tests
python -m unittest discover -s tests -v

# Run only glyph cataloger tests
python -m unittest discover -s tests -p "test_glyph*.py" -v
```

## Adding New Language Sources

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

## Dependencies

- **Web scraping**: requests, beautifulsoup4, lxml
- **Computer vision**: opencv-python, numpy, Pillow
- **Machine learning**: scikit-learn

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- Rapa Nui language data sourced from publicly available linguistic databases
- Built for linguistic research and language preservation efforts
- Rongorongo glyph analysis designed to support decipherment research
