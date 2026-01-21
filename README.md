# Easter Island Research Tools

A Python toolkit for Easter Island linguistic and archaeological research, featuring:
- **Language Scraper** - Collects Rapa Nui language data from multiple online sources
- **Glyph Cataloger** - Uses computer vision to identify and catalog Rongorongo glyphs
- **Cross-Referencer** - Creates symbolic links between glyphs and Proto-Polynesian linguistic roots
- **LLM Agents** - AI-powered analysis for segmentation, pattern mining, and lexical validation

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

### Symbolic Cross-Referencer
- Links Rongorongo glyph shapes to Proto-Polynesian linguistic roots
- Shape category classification (avian, anthropomorphic, phytomorphic, etc.)
- Evidence-based confidence scoring with multiple evidence types
- Optional manual shape annotations via YAML
- Generates cross-reference lexicon with full provenance

> **Note:** Rongorongo is undeciphered. All cross-references are speculative hypotheses for research exploration.

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

### Create Symbolic Cross-References

```bash
# Requires both glyph and language lexicons to exist first
python cross_referencer.py
```

Output:
- `output/cross_reference_lexicon.json` - Cross-references with evidence and confidence
- `output/cross_reference_report.md` - Human-readable report

Options:
```bash
# With manual shape annotations
python cross_referencer.py --annotations input/shape_annotations.yaml

# Custom confidence threshold
python cross_referencer.py --min-confidence 0.3

# Skip markdown report
python cross_referencer.py --no-report
```

### Scrape General Easter Island Content

```bash
python scraper.py
```

Output is saved to `output/easter_island.json`.

### Run LLM Agents

The toolkit includes three LLM-powered agents for advanced analysis:

```bash
# Glyph Segmentation - LLM-guided boundary decisions
python run_agent.py segmentation --image input/tablets/tablet_a.jpg

# Pattern Mining - Discover n-gram sequences and structural patterns
python run_agent.py pattern-mining --lexicon output/rongorongo_lexicon.json

# Lexical Validation - Validate against Polynesian corpora
python run_agent.py lexical-validation --cross-refs output/cross_reference_lexicon.json
```

Agent options:
```bash
# Use different LLM providers
python run_agent.py pattern-mining --lexicon output/rongorongo_lexicon.json --provider anthropic
python run_agent.py pattern-mining --lexicon output/rongorongo_lexicon.json --provider openai

# Specify model
python run_agent.py segmentation --image tablet.jpg --provider anthropic --model claude-3-opus-20240229

# Disable caching
python run_agent.py lexical-validation --cross-refs output/cross_reference_lexicon.json --no-cache

# Show verbose output
python run_agent.py pattern-mining --lexicon output/rongorongo_lexicon.json --verbose
```

Output files:
- `output/segmentation_results.json` - Refined glyph boundaries with LLM decisions
- `output/pattern_mining_results.json` - N-gram patterns, structural analysis, visual clusters
- `output/lexical_validation_results.json` - Validated cross-references with cognate evidence

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

### Cross-Reference Output

```json
{
  "version": "1.0.0",
  "methodology": {
    "warning": "Rongorongo is undeciphered. All associations are speculative."
  },
  "statistics": {
    "total_glyphs_profiled": 11,
    "total_cross_references": 25,
    "by_confidence_level": {"speculative": 15, "tentative": 8, "plausible": 2}
  },
  "glyph_profiles": [
    {
      "cluster_id": "G001",
      "shape_tags": [{"category": "avian", "confidence": 0.9}],
      "primary_category": "avian",
      "cross_reference_ids": ["XR001", "XR002"]
    }
  ],
  "cross_references": [
    {
      "reference_id": "XR001",
      "glyph_cluster_id": "G001",
      "language_entry_word": "manu",
      "overall_confidence": 0.42,
      "confidence_level": "tentative",
      "semantic_domain": "animals",
      "proto_polynesian_root": "*manu (bird)",
      "evidence": [
        {"type": "shape_semantic", "strength": 0.6, "description": "Avian glyph matches bird domain"}
      ]
    }
  ]
}
```

## Project Structure

```
easter-island/
├── language_scraper.py       # Rapa Nui language scraping
├── glyph_cataloger.py        # Rongorongo glyph cataloging
├── cross_referencer.py       # Symbolic cross-referencing
├── run_agent.py              # LLM agent CLI
├── scraper.py                # General Easter Island scraper
├── config.py                 # Configuration settings
├── models/
│   ├── language.py           # Language entry dataclass
│   ├── glyphs.py             # Glyph data models
│   └── cross_reference.py    # Cross-reference models
├── parsers/
│   └── language/             # Site-specific language parsers
│       ├── maori_parser.py   # Maori dictionary parser
│       ├── hawaiian_parser.py # Hawaiian dictionary parser
│       └── tahitian_parser.py # Tahitian dictionary parser
├── processors/
│   ├── glyph_processor.py    # CV processing pipeline
│   └── cross_reference_processor.py  # Semantic matching
├── agents/                   # LLM-powered analysis agents
│   ├── base/                 # Agent infrastructure
│   │   ├── llm_provider.py   # Abstract LLM interface
│   │   ├── agent.py          # Base agent class
│   │   ├── cache.py          # Response caching
│   │   └── providers/        # LLM provider implementations
│   ├── segmentation/         # Glyph segmentation agent
│   ├── pattern_mining/       # Pattern discovery agent
│   └── lexical_validation/   # Cognate validation agent
├── input/
│   ├── tablets/              # Input tablet images
│   └── shape_annotations.yaml  # Optional manual annotations
├── tests/
│   ├── fixtures/             # Test data
│   ├── test_parsers.py       # Parser tests
│   ├── test_glyph_*.py       # Glyph cataloger tests
│   ├── test_cross_reference_*.py  # Cross-referencer tests
│   ├── test_agents_base.py   # Agent infrastructure tests
│   └── ...
└── output/                   # Generated data (gitignored)
```

## Configuration

Edit `config.py` to customize:

### Language Scraper
- `LANGUAGE_CONFIG["rapa_nui"]["urls"]` - Source URLs to scrape

### Glyph Cataloger
- `GLYPH_CONFIG["processing"]` - Detection parameters (contour area, padding)
- `GLYPH_CONFIG["clustering"]` - DBSCAN parameters (eps, min_samples)

### Cross-Referencer
- `SHAPE_SEMANTIC_MAPPING` - Shape category to semantic domain mappings
- `CONFIDENCE_LEVELS` - Threshold ranges for confidence levels
- `EVIDENCE_WEIGHTS` - Weights for different evidence types

## Shape Annotations

Create `input/shape_annotations.yaml` for manual glyph classification:

```yaml
G001:
  category: avian
  confidence: 0.9
  subcategory: frigate_bird
  visual_features: [wings, forked_tail]

G002:
  category: anthropomorphic
  confidence: 0.8
  visual_features: [standing_figure, arms]

G003:
  category: geometric
  confidence: 0.7
```

Valid categories: `avian`, `anthropomorphic`, `phytomorphic`, `ichthyomorphic`, `geometric`, `composite`, `undetermined`

## Running Tests

```bash
# Run all tests
python -m unittest discover -s tests -v

# Run only glyph cataloger tests
python -m unittest discover -s tests -p "test_glyph*.py" -v

# Run only cross-referencer tests
python -m unittest discover -s tests -p "test_cross_reference*.py" -v
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
- **YAML parsing**: PyYAML
- **LLM providers** (optional): anthropic, openai

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- Rapa Nui language data sourced from publicly available linguistic databases
- Built for linguistic research and language preservation efforts
- Rongorongo glyph analysis designed to support decipherment research
