# Rongorongo Decipherment Toolkit

A computational approach to analyzing the undeciphered Rongorongo script of Easter Island (Rapa Nui), combining computer vision, Proto-Polynesian linguistics, and LLM-powered analysis.

> **Research Status**: This toolkit produces *hypothetical* mappings for scholarly exploration. Rongorongo remains undeciphered, and all outputs should be treated as research tools rather than definitive translations.

---

## Table of Contents

- [Overview](#overview)
- [The Decipherment Pipeline](#the-decipherment-pipeline)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Glyph Detection & Cataloging](#glyph-detection--cataloging)
- [Statistical Corpus Analysis](#statistical-corpus-analysis)
- [Shape-Semantic Mappings](#shape-semantic-mappings)
- [Cross-Referencing with Proto-Polynesian](#cross-referencing-with-proto-polynesian)
- [LLM-Powered Analysis Agents](#llm-powered-analysis-agents)
- [Sample Outputs & Translations](#sample-outputs--translations)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [References](#references)

---

## Overview

Rongorongo is one of the world's few undeciphered scripts, found on ~26 surviving wooden artifacts from Easter Island. This toolkit approaches decipherment through:

1. **Computer Vision** - Automated glyph detection, feature extraction, and clustering
2. **Linguistic Analysis** - Cross-referencing with Proto-Polynesian roots and Rapa Nui vocabulary
3. **LLM Agents** - Pattern mining, segmentation refinement, and lexical validation

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│  Tablet Images  │────▶│  Glyph Detector  │────▶│  Rongorongo Lexicon │
└─────────────────┘     │  (OpenCV+DBSCAN) │     └──────────┬──────────┘
                        └──────────────────┘                │
                                                            ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│ Rapa Nui Words  │────▶│ Cross-Referencer │────▶│ Hypothesis Lexicon  │
│ Proto-Polynesian│     │ (Evidence-Based) │     │ (Confidence Scores) │
└─────────────────┘     └──────────────────┘     └──────────┬──────────┘
                                                            │
                                                            ▼
                        ┌──────────────────┐     ┌─────────────────────┐
                        │   LLM Agents     │────▶│  Refined Analysis   │
                        │ (Claude/OpenAI)  │     │  Pattern Reports    │
                        └──────────────────┘     └─────────────────────┘
```

---

## The Decipherment Pipeline

### Stage 1: Glyph Extraction

The computer vision pipeline detects individual glyphs from tablet images:

```python
# processors/glyph_processor.py

def detect_glyphs(image_path):
    # 1. Preprocessing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    binary = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )

    # 2. Contour Detection
    contours, _ = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # 3. Feature Extraction (Hu Moments)
    for contour in valid_contours:
        moments = cv2.moments(contour)
        hu_moments = cv2.HuMoments(moments)
        # Log-transform handles 7+ orders of magnitude variance
        features = -np.sign(hu_moments) * np.log10(np.abs(hu_moments) + 1e-10)

    # 4. DBSCAN Clustering - groups similar glyphs
    clustering = DBSCAN(eps=0.5, min_samples=2).fit(features)
    return clusters
```

### Stage 2: Shape Classification

Glyphs are categorized into six semantic classes based on visual morphology:

| Category | Visual Features | Proto-Polynesian Roots | Rapa Nui Words |
|----------|----------------|------------------------|----------------|
| **Avian** | Wings, tail, beak | \*manu, \*lupe, \*kura | manu, manutara, kura, tavake |
| **Anthropomorphic** | Human figures, faces, hands | \*tangata, \*mata, \*rima | tangata, mata, rima, ariki |
| **Phytomorphic** | Plant-like forms | \*rakau, \*kumara | rakau, kumara, taro, toromiro |
| **Ichthyomorphic** | Fish, marine life | \*ika, \*honu, \*feke | ika, honu, heke, kahi |
| **Geometric** | Lines, circles, patterns | \*tahi, \*rua, \*toru | tahi, rua, toru, ha |
| **Composite** | Combined elements | (multiple) | (semantic combinations) |

### Stage 3: Evidence-Based Cross-Referencing

```python
# processors/cross_reference_processor.py

EVIDENCE_WEIGHTS = {
    "shape_semantic": 0.40,    # Visual category matches semantic domain
    "frequency": 0.15,         # Common glyphs ≈ common words
    "positional": 0.15,        # Initial/medial/final position patterns
    "neighbor": 0.10,          # Co-occurrence with similar glyphs
    "published": 0.15,         # From Rongorongo scholarship
    "manual": 0.05,            # Expert annotations
}

def calculate_confidence(evidence_list):
    """Weighted sum of evidence strengths, capped at 1.0"""
    total = sum(
        e.strength * EVIDENCE_WEIGHTS[e.type]
        for e in evidence_list
    )
    return min(total, 1.0)
```

**Confidence Levels:**
| Level | Range | Meaning |
|-------|-------|---------|
| `speculative` | 0-25% | Weak or single evidence source |
| `tentative` | 25-50% | Some supporting evidence |
| `plausible` | 50-75% | Multiple converging lines |
| `strong` | 75-100% | Rare; requires exceptional evidence |

---

## Installation

**Requirements:** Python 3.10+

```bash
# Clone the repository
git clone https://github.com/jrhoades1/Easter-Island.git
cd Easter-Island

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install core dependencies
pip install -r requirements.txt

# Or install with optional dependencies via pyproject.toml
pip install ".[dev]"      # Development tools (pytest, ruff)
pip install ".[llm]"      # LLM providers (anthropic, openai)
pip install ".[dev,llm]"  # Everything
```

### Dependencies

| Category | Packages | Purpose |
|----------|----------|---------|
| Web Scraping | requests, beautifulsoup4, lxml, urllib3 | Linguistic data collection |
| Computer Vision | opencv-python, numpy, Pillow | Glyph detection & processing |
| Machine Learning | scikit-learn | DBSCAN clustering |
| Data | PyYAML | Shape annotations |
| LLM (optional) | anthropic, openai | AI-powered analysis |
| Dev (optional) | pytest, pytest-cov, ruff | Testing and linting |

---

## Quick Start

### 1. Catalog Glyphs from a Tablet Image

```bash
python glyph_cataloger.py --image input/tablets/sample_tablet.png --output output/
```

### 2. Scrape Rapa Nui Language Data

```bash
python language_scraper.py --output output/
```

### 3. Generate Cross-References

```bash
python cross_referencer.py \
    --lexicon output/rongorongo_lexicon.json \
    --language output/rapa_nui_language.json \
    --annotations input/shape_annotations.yaml \
    --output output/
```

### 4. Run LLM Analysis (Optional)

```bash
# Set your API key
export ANTHROPIC_API_KEY="your-key-here"

# Run pattern mining agent
python run_agent.py pattern_mining \
    --input output/rongorongo_lexicon.json \
    --provider anthropic
```

---

## Glyph Detection & Cataloging

### Computer Vision Pipeline

```
Input Image → Grayscale → Gaussian Blur → Adaptive Threshold → Contour Detection
                                                                      ↓
Output Lexicon ← DBSCAN Clustering ← Hu Moment Extraction ← Filter by Size/Aspect
```

### Detection Parameters

```python
# config.py
GLYPH_DETECTION = {
    "min_contour_area": 100,      # Minimum glyph size (pixels²)
    "max_contour_area": 50000,    # Maximum glyph size
    "aspect_ratio_min": 0.2,      # Width/height bounds
    "aspect_ratio_max": 5.0,
    "bbox_padding": 5,            # Pixels around detected glyph
}

CLUSTERING = {
    "algorithm": "DBSCAN",
    "eps": 0.5,                   # Neighborhood radius
    "min_samples": 2,             # Minimum cluster size
}
```

### Sample Detection Output

```json
{
  "version": "1.0.0",
  "source_images": ["sample_tablet.png"],
  "total_glyphs_detected": 26,
  "unique_glyph_types": 11,
  "clusters": [
    {
      "cluster_id": "G001",
      "instance_count": 6,
      "instances": [
        {
          "bbox": {"x": 45, "y": 12, "width": 28, "height": 35},
          "line_number": 1,
          "position_in_line": 0,
          "hu_moments": [-2.34, -5.67, -8.91, -9.12, -18.45, -12.33, -18.67]
        }
      ]
    }
  ],
  "statistics": {
    "avg_glyphs_per_line": 6.5,
    "hapax_legomena": 4,
    "most_frequent_glyphs": ["G001", "G002", "G003", "G004"]
  }
}
```

---

## Statistical Corpus Analysis

The image-based pipeline above re-derives a glyph catalog from photographs,
which is error-prone. When a *transliterated* corpus is available — tablets
already encoded by scholars as glyph-code sequences (e.g. the Barthel
numbering system) — the statistical layer analyzes it directly, resting on the
field's accepted readings rather than on computer-vision guesses.

This layer is deliberately **descriptive, not interpretive**. It reports the
statistical structure of the script and makes *no* claim about what any glyph
means. Structural statistics are the part of computational Rongorongo work
that can be done honestly while the script remains undeciphered.

### Transliteration Format (`.rrt`)

Plain-text, line-oriented. Place files in `data/corpus/` (see
`data/corpus/SOURCES.md` for the full spec and where to obtain a real corpus):

```
@tablet C            # start a tablet, short code "C"
@name Mamari         # common name (optional)
@side recto          # side label (optional)
@synthetic           # mark as non-attested test data (optional)
Ca1: 1 2 6 700 8     # "<line_id>: <space-separated glyph tokens>"
Ca2: 6-700 8 1 2     # "6-700" is a ligature (fused glyphs 6 and 700)
```

### Running the Analysis

```bash
python corpus_stats.py --corpus data/corpus/ --output output/
```

This produces `output/corpus_statistics.json` and a console report covering:

| Metric | What it measures |
|--------|------------------|
| **Sign frequency** | Rank-ordered glyph counts and relative frequencies |
| **Zipf correlation** | Whether the distribution is language-like (near -1.0) |
| **Hapax legomena** | Glyphs occurring exactly once |
| **Type/token ratio** | Sign-inventory richness |
| **N-grams (2-5)** | Recurring glyph sequences |
| **Repeated sequences** | Maximal recurring spans — candidate formulae / parallelism |
| **Positional distribution** | Per-glyph line-initial / medial / final tendencies |

> **Note**: The repository ships only `data/corpus/sample_synthetic.rrt`, which
> contains **invented, non-attested data** for pipeline testing. Every run on
> synthetic data is flagged as such in the output.

---

## Shape-Semantic Mappings

### Annotation Format

```yaml
# input/shape_annotations.yaml

G001:
  category: avian
  subcategory: frigate_bird
  confidence: 0.8
  visual_features:
    - wings
    - forked_tail
  tagged_by: manual
  tagged_at: "2026-01-20T10:30:00Z"

G002:
  category: anthropomorphic
  subcategory: standing_figure
  confidence: 0.7
  visual_features:
    - standing_figure
    - arms

G004:
  category: ichthyomorphic
  confidence: 0.7
  visual_features:
    - fish_shape
```

### Mapping to Proto-Polynesian

```python
# config.py

SHAPE_SEMANTIC_MAPPING = {
    "avian": {
        "proto_polynesian_roots": ["*manu", "*lupe", "*kura"],
        "rapa_nui_words": ["manu", "manutara", "kura", "tavake"],
        "semantic_domains": ["animals", "nature", "spiritual"]
    },
    "anthropomorphic": {
        "proto_polynesian_roots": ["*tangata", "*mata", "*rima"],
        "rapa_nui_words": ["tangata", "mata", "rima", "ariki", "hatu"],
        "semantic_domains": ["body", "kinship", "social", "action"]
    },
    "phytomorphic": {
        "proto_polynesian_roots": ["*rakau", "*kumara"],
        "rapa_nui_words": ["rakau", "kumara", "taro", "toromiro"],
        "semantic_domains": ["agriculture", "nature", "food"]
    },
    "ichthyomorphic": {
        "proto_polynesian_roots": ["*ika", "*honu", "*feke"],
        "rapa_nui_words": ["ika", "honu", "heke", "kahi"],
        "semantic_domains": ["animals", "food", "nature"]
    },
    "geometric": {
        "proto_polynesian_roots": ["*tahi", "*rua", "*toru"],
        "rapa_nui_words": ["tahi", "rua", "toru", "ha", "ono", "hitu"],
        "semantic_domains": ["quantity", "space", "time"]
    }
}
```

---

## Cross-Referencing with Proto-Polynesian

### Evidence Collection Process

```python
# processors/cross_reference_processor.py

def collect_evidence(glyph_cluster, language_entry, glyph_rank, word_rank):
    evidence = []

    # 1. Shape-Semantic Match (40% weight)
    if word in SHAPE_SEMANTIC_MAPPING[category]["rapa_nui_words"]:
        evidence.append(Evidence(
            type="shape_semantic",
            strength=0.6,  # Direct word match
            description=f"'{word}' in {category} word list"
        ))

    # 2. Frequency Correlation (15% weight)
    # Hypothesis: common glyphs represent common words
    rank_diff = abs(glyph_rank - word_rank)
    strength = max(0.2, 1.0 - (rank_diff / 10) * 0.8)
    evidence.append(Evidence(
        type="frequency",
        strength=strength,
        description=f"Glyph rank {glyph_rank}, word rank {word_rank}"
    ))

    # 3. Positional Pattern (15% weight)
    # Initial/medial/final position may indicate grammatical function
    if avg_position < 0.33:
        evidence.append(Evidence(
            type="positional",
            strength=0.3,
            description="Glyph tends toward line-initial position"
        ))

    # 4. Neighbor Context (10% weight)
    if len(common_neighbors) >= 2:
        evidence.append(Evidence(
            type="neighbor",
            strength=0.2,
            description=f"Co-occurs with {', '.join(common_neighbors)}"
        ))

    return evidence
```

### Sample Cross-Reference Output

```json
{
  "reference_id": "XR001",
  "glyph_cluster_id": "G002",
  "language_entry_word": "rima",
  "overall_confidence": 0.469,
  "confidence_level": "tentative",
  "semantic_domain": "body",
  "proto_polynesian_root": "*rima (hand, arm, five)",
  "evidence": [
    {
      "type": "shape_semantic",
      "description": "'rima' (hand/arm) in anthropomorphic word list",
      "strength": 0.6,
      "source": "shape_semantic_mapping"
    },
    {
      "type": "positional",
      "description": "Glyph tends toward initial position (avg: 0.26)",
      "strength": 0.3,
      "source": "positional_analysis"
    },
    {
      "type": "neighbor",
      "description": "Commonly co-occurs with G001, G008, G004",
      "strength": 0.2,
      "source": "neighbor_analysis"
    }
  ],
  "notes": "Hypothetical mapping requiring further validation"
}
```

---

## LLM-Powered Analysis Agents

### Available Agents

| Agent | Purpose | Key Capabilities |
|-------|---------|------------------|
| **Segmentation** | Refine glyph boundaries | Boundary analysis, ligature detection, damage assessment |
| **Pattern Mining** | Find recurring sequences | N-gram analysis, structural patterns, visual clustering |
| **Lexical Validation** | Validate with Polynesian cognates | Cognate finding, etymology verification |

### Segmentation Agent

Analyzes ambiguous cases that pure CV misses:

```python
# agents/segmentation/agent.py

class SegmentationAgent:
    """
    Components:
    - BoundaryAnalyzer: LLM vision analysis of unclear boundaries
    - LigatureDetector: Identifies composite glyphs (merged elements)
    - DamageAssessor: Evaluates tablet damage effects on segmentation
    """

    def detect_ligatures(self, glyph_image):
        """
        Identifies composite glyphs by:
        1. Analyzing contour complexity
        2. Looking for visually distinct components
        3. Checking common patterns: bird+object, human+tool
        4. Evaluating if separation creates meaningful pieces
        """
```

### Pattern Mining Agent

Extracts statistical patterns from glyph sequences:

```python
# agents/pattern_mining/agent.py

class PatternMiningAgent:
    """
    Analysis modes:
    1. N-gram Analysis - Bigrams through 5-grams with frequencies
    2. Structural Patterns - Position correlations, line distributions
    3. Visual Clustering - Variant forms and allographs
    """

# Example n-gram output:
{
    "pattern_id": "P001",
    "sequence": ["G001", "G003", "G002"],
    "frequency": 5,
    "probability": 0.18,
    "positions": ["line_initial", "line_medial"],
    "tablets": ["sample_tablet.png"],
    "llm_hypothesis": "Possible formulaic opening phrase"
}
```

### Lexical Validation Agent

Cross-checks hypotheses against the broader Polynesian language family:

```python
# agents/lexical_validation/agent.py

class LexicalValidationAgent:
    """
    Validates cross-references against:
    - Maori vocabulary (te reo Māori)
    - Hawaiian vocabulary (ʻŌlelo Hawaiʻi)
    - Tahitian vocabulary (Reo Tahiti)

    Boosts confidence when cognates found in 2+ languages.
    """

    min_cognate_languages = 2   # Threshold for validation
    confidence_boost = 0.15      # Boost for validated references
```

### Running Agents

```bash
# Glyph Segmentation
python run_agent.py segmentation --image input/tablets/tablet.jpg --provider anthropic

# Pattern Mining
python run_agent.py pattern-mining --lexicon output/rongorongo_lexicon.json --provider anthropic

# Lexical Validation
python run_agent.py lexical-validation --cross-refs output/cross_reference_lexicon.json --provider openai

# Options
--provider anthropic|openai    # LLM provider
--model claude-3-opus-20240229 # Specific model
--no-cache                     # Disable response caching
--verbose                      # Detailed output
```

---

## Sample Outputs & Translations

### Glyph Frequency Distribution

```
Glyph   Count   Category          Hypothetical Mappings
───────────────────────────────────────────────────────────
G001    6       avian             manu (bird), manutara (sooty tern)
G002    4       anthropomorphic   tangata (person), rima (hand)
G003    4       geometric         tahi (one), marker/delimiter
G004    3       ichthyomorphic    ika (fish), kahi (tuna)
G005    2       phytomorphic      rakau (tree), toromiro
G006    1       undetermined      [no hypothesis]
G007    1       avian             kura (red feather)
G008    2       anthropomorphic   mata (eye/face), ariki (chief)
...
```

### Cross-Reference Summary

```
Total glyph profiles: 11
Total cross-references: 6

By confidence level:
  ● Plausible (50-75%): 5 references
  ○ Tentative (25-50%): 1 reference
  ◌ Speculative (0-25%): 0 references

By shape category:
  Avian.............. 1    Anthropomorphic..... 1
  Geometric.......... 1    Ichthyomorphic...... 1
  Phytomorphic....... 1    Undetermined........ 6
```

### Hypothetical Translation Example

> **Important Disclaimer**: This is a *speculative* reading for demonstration purposes only. Rongorongo remains undeciphered, and this should not be cited as a translation.

```
Tablet Line: G001 G002 G001 G003 G004

Glyph Analysis:
  G001 (avian, conf: 0.52)           → manu (bird)
  G002 (anthropomorphic, conf: 0.47) → tangata (person) OR rima (hand)
  G001 (avian, conf: 0.52)           → manu (bird)
  G003 (geometric, conf: 0.38)       → [delimiter?] OR tahi (one)
  G004 (ichthyomorphic, conf: 0.45)  → ika (fish)

Possible Readings:
  Reading A: "Bird person bird [?] fish"
  Reading B: "Bird hand bird one fish"
  Reading C: Formulaic phrase (birds frame the content)

Confidence: SPECULATIVE
Notes: Multiple valid interpretations possible. The repetition of G001
       may indicate a bracket structure or emphasis pattern.
```

### Language Lexicon Sample

```json
{
  "word": "rima",
  "normalized": "rima",
  "part_of_speech": "noun",
  "translations": [
    {"language": "en", "text": "hand"},
    {"language": "en", "text": "arm"},
    {"language": "en", "text": "five (numeral)"}
  ],
  "etymology": {
    "proto_polynesian": "*rima",
    "cognates": ["Maori: rima", "Hawaiian: lima", "Tahitian: rima"]
  }
}
```

---

## Project Structure

```
Easter-Island/
├── glyph_cataloger.py          # Main glyph detection CLI
├── corpus_stats.py             # Statistical corpus analysis CLI
├── cross_referencer.py         # Cross-reference generator CLI
├── language_scraper.py         # Rapa Nui vocabulary scraper
├── run_agent.py                # LLM agent runner CLI
├── scraper.py                  # Easter Island Wikipedia scraper
├── config.py                   # Configuration and mappings
│
├── data/
│   └── corpus/                 # Transliterated (.rrt) corpus + SOURCES.md
│
├── models/
│   ├── glyphs.py               # BoundingBox, GlyphInstance, GlyphCluster, RongorongoLexicon
│   ├── corpus.py               # CorpusLine, Tablet, RongorongoCorpus (transliterated text)
│   ├── language.py             # LanguageEntry, Translation, Etymology
│   └── cross_reference.py      # CrossReference, GlyphSemanticProfile, ShapeTag
│
├── processors/
│   ├── glyph_processor.py      # CV detection pipeline (OpenCV, DBSCAN)
│   ├── corpus_loader.py        # .rrt transliteration file parser
│   ├── corpus_statistics.py    # Descriptive corpus statistics engine
│   └── cross_reference_processor.py  # Evidence-based semantic linking
│
├── parsers/language/           # Web scrapers for linguistic data
│   ├── base.py                 # Abstract parser interface
│   ├── wikipedia.py            # Wikipedia language pages
│   ├── glosbe.py               # Glosbe dictionary
│   ├── maori_parser.py         # Maori Dictionary
│   ├── hawaiian_parser.py      # Hawaiian Dictionary
│   └── tahitian_parser.py      # Tahitian Dictionary
│
├── agents/
│   ├── base/                   # LLM provider abstraction
│   │   ├── llm_provider.py     # Abstract interface
│   │   ├── agent.py            # Base agent class
│   │   ├── cache.py            # Response caching
│   │   └── providers/          # Anthropic, OpenAI, Mock implementations
│   ├── segmentation/           # Boundary refinement agent
│   │   ├── agent.py
│   │   ├── boundary_analyzer.py
│   │   ├── ligature_detector.py
│   │   └── damage_assessor.py
│   ├── pattern_mining/         # Sequence analysis agent
│   │   ├── agent.py
│   │   ├── ngram_analyzer.py
│   │   ├── structural_patterns.py
│   │   └── visual_clustering.py
│   └── lexical_validation/     # Cognate validation agent
│       ├── agent.py
│       ├── cognate_finder.py
│       └── etymology_verifier.py
│
├── input/
│   ├── tablets/                # Tablet images for processing
│   └── shape_annotations.yaml  # Manual glyph annotations
│
├── output/                     # Generated lexicons and reports
│   ├── rongorongo_lexicon.json
│   ├── rapa_nui_language.json
│   ├── cross_reference_lexicon.json
│   └── glyphs/                 # Extracted glyph images
│
└── tests/                      # Comprehensive test suite
```

---

## Configuration

Edit `config.py` to customize behavior:

```python
# Glyph Detection
GLYPH_CONFIG = {
    "processing": {
        "min_contour_area": 100,
        "max_contour_area": 50000,
        "aspect_ratio_min": 0.2,
        "aspect_ratio_max": 5.0,
    },
    "clustering": {
        "eps": 0.5,
        "min_samples": 2,
    }
}

# Cross-Reference Evidence Weights
EVIDENCE_WEIGHTS = {
    "shape_semantic": 0.40,
    "frequency": 0.15,
    "positional": 0.15,
    "neighbor": 0.10,
    "published": 0.15,
    "manual": 0.05,
}

# Confidence Level Thresholds
CONFIDENCE_LEVELS = {
    "speculative": (0.00, 0.25),
    "tentative": (0.25, 0.50),
    "plausible": (0.50, 0.75),
    "strong": (0.75, 1.01),
}
```

---

## Running Tests

```bash
# Install dev dependencies
pip install ".[dev]"

# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test modules
pytest tests/test_glyph_processor.py -v
pytest tests/test_cross_reference_processor.py -v
pytest tests/test_agents_base.py -v
```

---

## Contributing

Contributions are welcome! Areas of particular interest:

- **Tablet Images** - Higher resolution scans of Rongorongo artifacts
- **Shape Annotations** - Expert glyph categorizations and visual analysis
- **Polynesian Language Data** - Expanded vocabulary from related languages
- **Pattern Analysis** - Novel statistical approaches to sequence analysis
- **LLM Prompts** - Improved prompts for agent analysis

Please open an issue to discuss significant changes before submitting a PR.

---

## References

### Rongorongo Scholarship

- Fischer, S.R. (1997). *Rongorongo: The Easter Island Script*. Oxford University Press.
- Barthel, T.S. (1958). *Grundlagen zur Entzifferung der Osterinselschrift*. Hamburg.
- Pozdniakov, K. (1996). "Les bases du déchiffrement de l'écriture de l'île de Pâques." *Journal de la Société des Océanistes*.
- Horley, P. (2011). "Rongorongo Tablet Keiti." *Rapa Nui Journal* 25(1).

### Proto-Polynesian Linguistics

- Greenhill, S.J. & Clark, R. (2011). *POLLEX-Online: The Polynesian Lexicon Project Online*.
- Biggs, B. (1978). "The history of Polynesian phonology." *Second International Conference on Austronesian Linguistics*.
- Pawley, A. (1966). "Polynesian languages: A subgrouping based on shared innovations in morphology." *Journal of the Polynesian Society*.

### Computer Vision & Machine Learning

- Hu, M.K. (1962). "Visual pattern recognition by moment invariants." *IRE Transactions on Information Theory*.
- Ester, M. et al. (1996). "A density-based algorithm for discovering clusters in large spatial databases with noise." *KDD-96*.

### Related AI Decipherment Projects

- Luo, J. et al. (2019). "Neural Decipherment via Minimum-Cost Flow." *ACL 2019*.
- Assael, Y. et al. (2022). "Restoring and attributing ancient texts using deep neural networks." *Nature*.

---

## License

MIT License - See [LICENSE](LICENSE) for details.

---

<p align="center">
  <i>Ko te rongo o Rapa Nui</i><br>
  <i>The voice of Rapa Nui</i><br><br>
  <b>E tahi te manu, e tahi te tangata</b><br>
  <i>One bird, one person</i>
</p>
