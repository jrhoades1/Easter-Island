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
├── cross_referencer.py         # Cross-reference generator CLI
├── language_scraper.py         # Rapa Nui vocabulary scraper
├── run_agent.py                # LLM agent runner CLI
├── scraper.py                  # Easter Island Wikipedia scraper
├── config.py                   # Configuration and mappings
│
├── models/
│   ├── glyphs.py               # BoundingBox, GlyphInstance, GlyphCluster, RongorongoLexicon
│   ├── language.py             # LanguageEntry, Translation, Etymology
│   └── cross_reference.py      # CrossReference, GlyphSemanticProfile, ShapeTag
│
├── processors/
│   ├── glyph_processor.py      # CV detection pipeline (OpenCV, DBSCAN)
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
        "hu_sign_mode": "unsigned",
        "same_line_allograph_merge": True,
        "split_wide_ligatures": True,
        "split_fragment_allograph_merge": True,
        "wide_profile_allograph_merge": True,
        "split_inconsistent_types": True,
        "delimiter_slot_merge": True,
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
- Guy, J.B.M. (1990). "The lunar calendar of Tablet Mamari." *Journal de la Société des Océanistes* 91: 135–149. doi:10.3406/jso.1990.2882.
- Pozdniakov, K. (1996). "Les bases du déchiffrement de l'écriture de l'île de Pâques." *Journal de la Société des Océanistes*.
- Horley, P. (2011). "Lunar calendar in rongorongo texts and rock art of Easter Island." *Journal de la Société des Océanistes* 132: 17–38. doi:10.4000/jso.6314.
- Horley, P. (2011). "Rongorongo Tablet Keiti." *Rapa Nui Journal* 25(1).

The Ca6–Ca9 scoreboard fixture (`tests/fixtures/mamari_ca6_ca9_barthel.json`) is the Kohaumotu published Barthel-coded transcription of the Mamari lunar/calendar passage ([Ca.html](http://kohaumotu.org/Rongorongo/C/Ca.html)). Guy 1990 Fig. 1 / Table 1 did not extract as text. Cycle 28 vendors that same Ca.html (`tests/fixtures/mamari_ca_html/`) and locks the remainder as a second published passage: Guy's 8-stem delimiter is absent, 600 is not window-adjacent (five hits, no windows), and 040-runs are six isolated tokens on Ca10–Ca12 (12 windowless cells). Cycle 29 locks that remainder's repeating n≥4 freq≥2 profile (`tests/test_mamari_remainder_ngram_profile_scoreboard.py`): 31 distinct n-grams, longest n=9 on Ca10/Ca11, two 8-grams (top is not Guy's delimiter), and the five 600 hits sit outside every repeating n≥4 span. Calendar Ca6–Ca9 is not re-mined. Cycle 30 locks that 9-gram as a motif (`tests/test_mamari_remainder_9gram_motif_scoreboard.py`): exact remainder hits and one-token flanks, the 8-prefix at the same starts, six 002…002 wraps at n=9 (four are not the motif), and calendar-absent on Ca6–Ca9. Cycle 31 locks that wrap family (`tests/test_mamari_remainder_002_wrap_family_scoreboard.py`): for each of the six remainder windows, line, span, nine tokens, whether it is the motif, aligned position matches against the motif, and shared interior stems (bookend 002 excluded; not a delimiter claim). All six share at least one interior stem with the motif besides 002 (the four non-motif wraps share 010 and/or 760, and Ca10[18:27] also shares 070 040 006). Calendar still has none. Cycle 32 vendors the same publisher's tablet-C verso (`tests/fixtures/mamari_cb_html/Cb.html`, [Cb.html](http://kohaumotu.org/Rongorongo/C/Cb.html)) and locks that side only (`tests/test_mamari_cb_side_b_scoreboard.py`): Guy's 8-stem delimiter is absent (freq 0), the 9-gram motif is absent, four 002…002 n=9 wraps (two share a non-bookend interior stem with the motif: Cb7 760, Cb8 070), and 600 appears twice. Ca remainder locks are unchanged. Cycle 33 locks that verso's repeating n≥4 freq≥2 profile (`tests/test_mamari_cb_repeating_ngram_profile_scoreboard.py`): 12 distinct n-grams, longest n=5 (three grams, all freq 2), no repeating 8-gram. Cycle 34 locks those three Cb 5-grams as absent on the Ca calendar and Ca remainder (`tests/test_mamari_cb_5gram_ca_cross_scoreboard.py`). Cycle 35 looks at the already-vendored Ca.html / Cb.html navbars and in-repo ATTRIBUTION / CORPUS_SURVEY / README for a Kohaumotu Barthel page of a different tablet; none is honestly linked from those navbars (`tests/test_mamari_off_tablet_c_ceiling_scoreboard.py`). Cycle 36 opens the parent catalog ([Rongorongo/](http://kohaumotu.org/Rongorongo/)), takes the first non-C tablet with extractable Barthel numbers (A / Tahua), vendors [Aa.html](http://kohaumotu.org/Rongorongo/A/Aa.html) (`tests/fixtures/tahua_aa_html/`), and locks that side only (`tests/test_mamari_tahua_aa_scoreboard.py`): Guy's 8-stem delimiter is absent (freq 0), the Ca 9-gram is absent, the three Cb 5-grams are absent, 906 stems, longest n with freq≥2 is 10, top 8-gram is 080 004 280 182 048 022 025 025 (freq 2, not Guy). Cycle 37 locks that Aa 10-gram as a motif (`tests/test_mamari_tahua_aa_10gram_motif_scoreboard.py`): exact hits Aa7[55:65] / Aa7[88:98] (freq 2) with one-token flanks 002/009 and 020/256, the cycle-36 top 8-gram is its prefix, and the 10-gram is absent from the Ca calendar, Ca remainder, and Cb fixtures. Cycle 38 vendors the same tablet-A verso (`tests/fixtures/tahua_ab_html/Ab.html`, [Ab.html](http://kohaumotu.org/Rongorongo/A/Ab.html)) and locks that side only (`tests/test_mamari_tahua_ab_scoreboard.py`): the Aa 10-gram is absent, Guy's 8-stem delimiter is absent (freq 0), the Ca 9-gram is absent, 926 stems, longest n with freq≥2 is 9, top 8-gram is 605 003 004 600 004 003 040 003 (freq 2). Cycle 39 locks that Ab 9-gram as a motif (`tests/test_mamari_tahua_ab_9gram_motif_scoreboard.py`): exact hits Ab3[2:11] / Ab5[13:22] (freq 2) with one-token flanks 003/003 and 208/093, the cycle-38 top 8-gram is its prefix, 600 sits at slot 3 in both hits, and the 9-gram is absent from Aa, the Ca calendar, Ca remainder, and Cb fixtures. Cycle 40 locks a 600 inventory on those same fixtures only (`tests/test_mamari_600_inventory_scoreboard.py`): 64 hits (calendar 2, remainder 5, Cb 2, Aa 23, Ab 32) with tablet/side, line, index, one-token flanks, locked-motif membership (Guy window / Ca 9-gram / Aa 10-gram / Ab 9-gram), and calendar window-adjacency. Two calendar hits are window-adjacent (Ca7[32] last facing Guy, Ca8[23] first after Guy); two Ab hits sit inside the Ab 9-gram (Ab3[5], Ab5[16]); none sit inside Guy, the Ca 9-gram, or the Aa 10-gram. Cycle 41 locks the 004 600 004 sandwich on that same inventory (`tests/test_mamari_600_sandwich_scoreboard.py`): three Ab hits (Ab3[4:7] and Ab5[15:18] are the Ab 9-gram 600 slot; Ab7[16:19] is not); none on Ca calendar, Ca remainder, Cb, or Aa. Per-fixture top 600 neighbors (stem, count; line-edge excluded; ties break by earliest stem id): calendar 152/040 (1/1), remainder 007/001 (2/2), Cb 001/003 (1/1), Aa 004/007 (5/5), Ab 003/001 (6/5). Cycle 42 locks the Ab7 sandwich 9-window Hamming vs the Ab 9-gram (`tests/test_mamari_ab7_9gram_hamming_scoreboard.py`): Ab7[14:23] Hamming 6 (shares 004 600 004 only); not a near-copy. Image track stays parked 83/62 / Hamming 6. Cycle 43 opens the same parent catalog, takes the first tablet that is not A and not C with extractable Barthel numbers (B / Aruku-Kurenga), vendors [Br.html](http://kohaumotu.org/Rongorongo/B/Br.html) (`tests/fixtures/aruku_br_html/`), and locks that recto only (`tests/test_mamari_aruku_br_scoreboard.py`): Guy's 8-stem delimiter is absent (freq 0), the Ca 9-gram / Aa 10-gram / Ab 9-gram / 004 600 004 sandwich are absent, 560 stems, longest n with freq≥2 is 6 (384 003 001 470 091 450, freq 2 on Br4), no repeating 8-gram. Existing Aa/Ab/C scoreboards are unchanged. Cycle 44 vendors the same tablet-B verso (`tests/fixtures/aruku_bv_html/Bv.html`, [Bv.html](http://kohaumotu.org/Rongorongo/B/Bv.html)) and locks that side only (`tests/test_mamari_aruku_bv_scoreboard.py`): Guy's 8-stem delimiter is absent (freq 0), the Ca 9-gram / Aa 10-gram / Ab 9-gram / 004 600 004 sandwich are absent, 738 stems, longest n with freq≥2 is 8 (002 065 042 300 385 003 065 200, freq 2 on Bv5/Bv6), one repeating 8-gram (not Guy). Existing Aa/Ab/Br/C scoreboards are unchanged. Cycle 45 locks that Bv 8-gram as a motif (`tests/test_mamari_aruku_bv_8gram_motif_scoreboard.py`): exact hits Bv5[18:26] / Bv6[39:47] (freq 2) with one-token flanks 663/236 and 673/092, and the 8-gram is absent from Br, Aa, Ab, the Ca calendar, Ca remainder, and Cb fixtures. Cycle 46 opens the same parent catalog, takes tablet I / Santiago Staff from the already-vendored tablets.html, vendors [Ia.html](http://kohaumotu.org/Rongorongo/I/Ia.html) (`tests/fixtures/santiago_ia_html/`; Ir.html is not a published page), and locks that page only (`tests/test_mamari_santiago_ia_scoreboard.py`): Guy's 8-stem delimiter is absent (freq 0), the Ca 9-gram / Aa 10-gram / Ab 9-gram / Bv 8-gram / 004 600 004 sandwich are absent, 2469 stems, longest n with freq≥2 is 5 (999 071 076 010 079, freq 3 on Ia4/Ia5), no repeating 8-gram. Existing A/B/C scoreboards are unchanged. Cycle 47 locks 999 on that same Ia.html (`tests/test_mamari_santiago_ia_999_scoreboard.py`): Ia.html / ATTRIBUTION name no role (not gap, damage, line-end, or a Barthel type); 97 stems (3 are the cycle-46 5-gram prefix, 94 isolated; forms 999×87, 999h×6, 999t×3, 999.440.076×1). As a stem the longest n-gram stays 999 071 076 010 079 (freq 3). As a break (split sequences at 999) the remaining 2372 stems still have longest n=5 (four grams, all freq 2) and no repeating 8-gram. No Ib scrape. No invented URL or digits. Further cell tables on the original 101 tokens are not a new corpus. The unit test fails if the repeating delimiter is missing from the top-N n-grams of matching length, or if same-length noise outranks it. A seeded shuffle of the same Barthel stems is the negative control: the published delimiter must not reappear as a repeating 8-gram. Cycle 48 locks 076 inventory on that same Ia.html (564 hits; top neighbors 090/071). Cycle 49 locks inter-076 cells (578 cells, median 3, top length 3×203, empty 17). Cycle 50 locks 076 rate per existing fixture (`tests/test_mamari_santiago_ia_076_rate_scoreboard.py`): calendar 0/101, remainder 0/416, Cb 0/487, Aa 3/906, Ab 0/926, Br 4/560, Bv 4/738, Ia 564/2469; only Ia is ≥ 0.10. Cycle 51 locks 090 and 071 rates on those same fixtures (`tests/test_mamari_santiago_ia_090_071_rate_scoreboard.py`): 090 calendar 0/101, remainder 0/416, Cb 1/487, Aa 4/906, Ab 2/926, Br 0/560, Bv 0/738, Ia 114/2469; 071 calendar 0/101, remainder 0/416, Cb 2/487, Aa 3/906, Ab 2/926, Br 3/560, Bv 2/738, Ia 93/2469; no fixture is ≥ 0.10 for either stem (Ia is not the only clearer). Cycle 52 locks consecutive 090 076 / 076 071 / 090 076 071 hit counts on those same fixtures (`tests/test_mamari_santiago_ia_090_076_071_ngram_scoreboard.py`): 090 076 is 69 on Ia and 0 elsewhere; 076 071 is 43 on Ia and 0 elsewhere; 090 076 071 is 6 on Ia and 0 elsewhere. No new tablet. Image track stays parked 83/62 / Hamming 6. Cycle 59 vendors London (tablet K) recto [Kr.html](http://kohaumotu.org/Rongorongo/K/Kr.html) from the same parent catalog (`tests/fixtures/small_london_kr_html/`; Ka.html is unpublished — K/index.html lists Kr.html, same Gr vs Ga lesson) and locks that page only (`tests/test_mamari_small_london_kr_scoreboard.py`): A/B/C motifs and the Ia top 5-gram are absent, 131 stems, 076 rate 0/131 (rate < 0.10), 090 076 / 076 071 / 430 076 / 076 200 all 0. Kv.html is not scraped. Existing A/B/C/I/G scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 60 vendors the same tablet-K verso [Kv.html](http://kohaumotu.org/Rongorongo/K/Kv.html) (`tests/fixtures/small_london_kv_html/`) and locks that page only (`tests/test_mamari_small_london_kv_scoreboard.py`): A/B/C motifs and the Ia top 5-gram are absent, 95 stems, 076 rate 0/95 (rate < 0.10), 090 076 / 076 071 / 430 076 / 076 200 all 0. Tablet D is not scraped. Existing A/B/C/I/G/Kr scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 61 locks the longest exact shared stem n-gram between already-vendored Small Santiago (Gr+Gv) and London (Kr+Kv) (`tests/test_mamari_small_santiago_london_parallel_ngram_scoreboard.py`): combined n=17 (380 001 003 005 006 010 380 001 003 315 380 001 003 090 001 380 001, freq 1/1); shared n≥4 exists, so the published G/K parallel holds on this Barthel stemming. Per-side: Gr vs Kr n=17, Gr vs Kv n=15, Gv vs Kr/Kv n=2 (no n≥4). 076 is not in the 17-gram. No new tablet. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 62 (focused-batch 1/5) locks that exact 17-gram's hit count on the twelve already-vendored fixtures (`tests/test_mamari_small_santiago_london_17gram_hit_scoreboard.py`): calendar 0, remainder 0, Cb 0, Aa 0, Ab 0, Br 0, Bv 0, Ia 0, Gr 1, Gv 0, Kr 1, Kv 0. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 63 (focused-batch 2/5) locks each of those two hits' line/index and one-token flanks (`tests/test_mamari_small_santiago_london_17gram_flank_scoreboard.py`): Gr4[3] 001/003, Kr5[0] START/316; the two hits do not share flanks. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 64 (focused-batch 3/5) locks the nearest other 17-window by Hamming vs that motif (`tests/test_mamari_small_santiago_london_17gram_hamming_scoreboard.py`): exclude the two exact hits; nearest is Kv3[5] Hamming 6; no non-exact window has Hamming ≤ 4. Per-fixture best: calendar 16, remainder 12, Cb 10, Aa 14, Ab 13, Br 14, Bv 14, Ia 14, Gr 9, Gv 15, Kr 9, Kv 6. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 65 (focused-batch 4/5) locks the 17-gram's internal 3-gram 380 001 003 (slots 0, 6, 10) on those same twelve fixtures (`tests/test_mamari_small_santiago_london_380_001_003_scoreboard.py`): calendar 0, remainder 0, Cb 1, Aa 0, Ab 0, Br 0, Bv 0, Ia 0, Gr 30, Gv 0, Kr 6, Kv 11. Gr and Kr are not the only fixtures with hits ≥ 3 (the internal repeat count); Kv also has 11. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 66 (focused-batch 5/5) locks the exact Gr vs Kv longest shared stem n-gram (`tests/test_mamari_small_santiago_london_gr_kv_15gram_scoreboard.py`): n=15 (079 450 019 069 380 001 003 162 522 050 002 450 380 001 003, freq 1/1) at Gr7[0] / Kv4[7]. The 15-gram overlaps the cycle-61/62 17-gram (shared run 380 001 003); it is not a prefix, suffix, or disjoint. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 67 locks every exact shared stem n≥8 between already-vendored G (Gr+Gv, and per-side) and K (Kr+Kv, and per-side) (`tests/test_mamari_small_santiago_london_shared_n8_scoreboard.py`): 139 distinct sequences, all freq 1/1, which are exactly the n≥8 subspans of six maximal islands — Gr4[3]/Kr5[0] n=17, Gr7[0]/Kv4[7] n=15, Gr2[4]/Kr2[16] n=13, Gr1[4]/Kr1[2] n=12, Gr6[33]/Kv3[15] n=10, Gr3[28]/Kr4[12] n=10. Per-side: Gr–Kr 97, Gr–Kv 42, Gv vs K 0. Coverage of stems inside at least one shared n≥8 is Gr 77/355, Gv 0/359, Kr 52/131, Kv 25/95 (77 stems on each tablet). Not same-text (Gv uncovered; six disjoint islands). Not two formulas. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 68 locks those six maximal islands' exact hit counts on the already-vendored non-G/K fixtures only (`tests/test_mamari_small_santiago_london_island_off_gk_scoreboard.py`): calendar 0, remainder 0, Cb 0, Aa 0, Ab 0, Br 0, Bv 0, Ia 0 for each of the six sequences. No island hits anywhere off G/K. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 69 vendors the published H/P Grand Tradition parallel from the same parent catalog: tablet H / Great Santiago [Hr.html](http://kohaumotu.org/Rongorongo/H/Hr.html) / [Hv.html](http://kohaumotu.org/Rongorongo/H/Hv.html) (`tests/fixtures/large_santiago_hr_html/`, `tests/fixtures/large_santiago_hv_html/`; Ha.html is unpublished — H/index.html lists Hr.html, same Gr vs Ga lesson) and tablet P / Great St. Petersburg [Pr.html](http://kohaumotu.org/Rongorongo/P/Pr.html) / [Pv.html](http://kohaumotu.org/Rongorongo/P/Pv.html) (`tests/fixtures/large_st_petersburg_pr_html/`, `tests/fixtures/large_st_petersburg_pv_html/`; Pa.html is unpublished). Stem counts: Hr 771 (67 76 84 82 85 72 65 63 53 58 45 21), Hv 831 (35 65 63 67 81 79 75 72 79 79 69 67), Pr 825 (66 78 105 95 105 82 87 78 46 45 38), Pv 739 (32 41 47 72 74 76 94 87 72 79 65). The six G–K islands are 0 on every H/P side (`tests/test_mamari_large_santiago_st_petersburg_vendor_scoreboard.py`). Shared n≥8 inventory (`tests/test_mamari_large_santiago_st_petersburg_shared_n8_scoreboard.py`): 237 distinct sequences, all freq 1/1, which are exactly the n≥8 subspans of 18 maximal disjoint islands (longest n=22 at Hr5[6]/Pr4[71]). Per-side: Hr–Pr 215, Hv–Pv 22, cross-side 0. Coverage: Hr 119/771, Hv 70/831, Pr 119/825, Pv 70/739 (189 stems on each tablet). Shared n≥8 exists and is not 1–2 short formulas, so the published H/P parallel holds on this Barthel stemming. Tablet Q is not scraped in cycle 69. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 70 vendors the third Grand Tradition witness from the same parent catalog: tablet Q / Small St. Petersburg [Qr.html](http://kohaumotu.org/Rongorongo/Q/Qr.html) / [Qv.html](http://kohaumotu.org/Rongorongo/Q/Qv.html) (`tests/fixtures/small_st_petersburg_qr_html/`, `tests/fixtures/small_st_petersburg_qv_html/`; Qa.html is unpublished — Q/index.html lists Qr.html, same Gr vs Ga lesson). Stem counts: Qr 503 (18 59 66 60 69 50 59 63 59), Qv 423 (57 62 57 52 52 45 46 41 11). The six G–K islands are 0 on both Q sides (`tests/test_mamari_small_st_petersburg_vendor_scoreboard.py`). Shared n≥8 vs H and vs P (`tests/test_mamari_small_st_petersburg_shared_n8_scoreboard.py`): Q vs H 503 distinct / 15 maximal disjoint islands (longest n=31 at Qr3[19]/Hr3[39]); Q vs P 147 distinct / 8 islands (longest n=17 at Qv4[12]/Pv3[30]). Per-side: Qr–Hr 468, Qv–Hv 35, Qr–Pr 71, Qv–Pv 76, cross-side 0. Coverage Q–H Qr 159/503, Qv 32/423, Hr 159/771, Hv 32/831 (191 stems on each tablet); Q–P Qr 56/503, Qv 39/423, Pr 56/825, Pv 39/739 (95 stems on each tablet). Shared n≥8 with H and P exists and is not 1–2 short formulas, so Q participates in the published H/P parallel on this Barthel stemming. Tablet D is not scraped. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 71 locks the H∩P∩Q triple of those already-vendored sides (`tests/test_mamari_hpq_triple_n8_scoreboard.py`): 33 distinct n≥8 sequences present on all three tablets, all freq 1/1/1, which are exactly the n≥8 subspans of five maximal disjoint islands (longest n=12 at Hr8[0]/Pr7[29]/Qr7[47]). Per-side: Hr–Pr–Qr 32, Hv–Pv–Qv 1, cross-side 0. Coverage: Hr 41/771, Hv 8/831, Pr 41/825, Pv 8/739, Qr 41/503, Qv 8/423 (49 stems on each tablet). Not empty. Not 1–2 short formulas. A real multi-island tradition. Tablet D is not scraped. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 72 locks those five maximal islands' exact hit counts on the already-vendored non-H/P/Q fixtures only (`tests/test_mamari_hpq_island_off_hpq_scoreboard.py`): calendar 0, remainder 0, Cb 0, Aa 0, Ab 0, Br 0, Bv 0, Ia 0, Gr 0, Gv 0, Kr 0, Kv 0 for each of the five sequences. No island hits anywhere off H/P/Q. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 73 locks the reading-order of the four recto H∩P∩Q islands on already-vendored Hr/Pr/Qr (`tests/test_mamari_hpq_island_recto_order_scoreboard.py`): sort by line then index is the same sequence on H, P, and Q — n=11 at *r3, n=10 at *r5, n=8 at *r7, n=12 later on *r7/*r8 (Hr3[27]/Hr5[36]/Hr7[47]/Hr8[0], Pr3[14]/Pr5[9]/Pr7[10]/Pr7[29], Qr3[7]/Qr5[15]/Qr7[28]/Qr7[47]). The verso n=8 island stays a separate Hv2[32]/Pv4[50]/Qv5[11] row and is not mixed into that order. Same order, not a bag of formulas. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 74 locks the three inter-island gaps on those same Hr/Pr/Qr sites (`tests/test_mamari_hpq_island_recto_gap_scoreboard.py`): lengths 164/184/123, 158/178/122, 10/11/11; longest triple-shared n-grams 7 / 7 / 2 (pairwise H–P / H–Q / P–Q 22/31/7, 11/13/7, 2/2/3). No gap has a triple-shared n≥8. Waypoints, not copied pages. Verso stays out. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 75 locks the exact gap-1 pairwise grams on those same sites (`tests/test_mamari_hpq_island_recto_gap1_pairwise_scoreboard.py`): H–Q n=31 at Hr3[39]/Qr3[19] (interior on both; coverage 31/164 and 31/123); H–P n=22 at Hr5[6]/Pr4[71] (interior on both; coverage 22/164 and 22/184). P has no exact hit of the H–Q 31-gram on Pr gap 1. H and Q share filler there; P is waypoint-only for that gram. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 74 locks the reading-order of the six G–K maximal islands on already-vendored Gr/Kr/Kv (`tests/test_mamari_small_santiago_london_island_order_scoreboard.py`): Gr line/index order is n=12 at Gr1[4], n=13 at Gr2[4], n=10 at Gr3[28], n=17 at Gr4[3], n=10 at Gr6[33], n=15 at Gr7[0]. The four Gr–Kr islands keep that relative order on Kr (Kr1[2], Kr2[16], Kr4[12], Kr5[0]) — colinear, not scrambled. The two Gr–Kv islands keep that relative order on Kv (Kv3[15], Kv4[7]). No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 75 locks the four same-side inter-island gaps on already-vendored Gr/Kr/Kv (`tests/test_mamari_small_santiago_london_island_gap_scoreboard.py`): Gr–Kr 1→2 / 2→3 / 3→4 lengths 28/28, 51/41, 5/2 with longest shared n 4 / 7 / 0; Gr–Kv 5→6 lengths 11/11 with longest shared n=10 (`380 001 003 003 003 004 215 380 001 003`). No full gap-string match. One gap has shared n≥8, so copied pages, not waypoints (same n≥8 operationalization as cycle 74). The Gr-only 4→5 stretch (102 stems) is a Kr→Kv side-switch, not a comparable gap. Gv stays 0. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 76 locks whether Gr–Kv islands 5 + the 10-gram gap + island 6 are one contiguous shared passage (`tests/test_mamari_small_santiago_london_grkv_block_scoreboard.py`): windows 36/36 from island 5 start through island 6 end; Hamming 1 (066 vs 009 immediately after island 5); the gap 10-gram sits immediately before island 6, not immediately after island 5; combined shared n=25 ≥ 8 but two flattened maximals (n=25 and n=10), not one run. two_islands_plus_filler, not one_block. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 77 locks those six G–K islands (Gr order) plus the cycle-76 n=25 (gap 10-gram + island 6) as exact hit counts on already-vendored Hr/Hv/Pr/Pv/Qr/Qv only (`tests/test_mamari_gk_islands_off_hpq_scoreboard.py`): 0 on every side for each of the seven sequences. any_hit is false; all_zero is true. No leak onto H/P/Q. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 78 locks whether the old Gr–Kv island 6 n=15 is still a separate maximal or a suffix of that n=25 (`tests/test_mamari_small_santiago_london_grkv_maximal_scoreboard.py`): on Gr and Kv the n=15 sits inside the n=25 at the same sites (n=25 starts 10 stems earlier at the gap 10-gram, Gr6[44]/Kv3[26]; both end at Gr7[14]/Kv4[21]); flattened maximals n≥8 through that window are n=10 (island 5) and n=25 (gap+6), not n=10 and n=15. island6_is_suffix is true; island6_is_maximal is false; gr_kv_maximals is [10, 25]. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 79 vendors tablet D / Échancrée [Da.html](http://kohaumotu.org/Rongorongo/D/Da.html) / [Db.html](http://kohaumotu.org/Rongorongo/D/Db.html) from the same parent catalog (`tests/fixtures/echancree_da_html/`, `tests/fixtures/echancree_db_html/`; Dr.html is unpublished) and locks that tablet only (`tests/test_mamari_echancree_vendor_scoreboard.py`): G–K islands + n=25 and H∩P∩Q n≥8 are exact-0 on D; longest repeating n=4 (no 8-gram). Claim: closed-tradition hold-out. Cycle 80 vendors tablet E / Keiti [Er.html](http://kohaumotu.org/Rongorongo/E/Er.html) / [Ev.html](http://kohaumotu.org/Rongorongo/E/Ev.html) (`tests/fixtures/keiti_er_html/`, `tests/fixtures/keiti_ev_html/`; Ea.html / Eb.html / E.html are unpublished 404s — E/index.html lists Er.html / Ev.html) and locks that tablet only (`tests/test_mamari_keiti_vendor_scoreboard.py`): Er 462 / Ev 424 stems; G–K islands + n=25 and H∩P∩Q n≥8 are exact-0 on E; longest repeating n=9 (four 8-grams). Claim: closed-tradition hold-out. Cycle 81 locks that n=9's sites on already-vendored Er/Ev (`tests/test_mamari_keiti_n9_scoreboard.py`): 300 040 300 028 004 430 022 380 203 at Er2[11] and Er2[28] (er_hits 2, ev_hits 0); side_local is true (Er-only); off_e_hits 0 on already-vendored A, B, C, D, G, K, H, P, Q, I (closed). No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 82 locks Ev's own longest repeating n-gram on already-vendored Ev (`tests/test_mamari_keiti_ev_longest_scoreboard.py`): n=6 (002 034 002 001 002 034) at Ev1[1] and Ev6[29]; ev_has_n_ge_8 is false; E's 4 eightgrams sit on Er (0 on Ev; the n=9's 8-prefix/suffix are Er). No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 83 locks those 4 eightgrams on already-vendored Er (`tests/test_mamari_keiti_eightgram_scoreboard.py`): two are the n=9 8-prefix/suffix (Er2[11]/[28] and Er2[12]/[29] plus suffix also at Er3[11]); two are independent (040 300 040 300 028 004 430 022 at Er2[27]/Er4[1]; 092 050 006 670 092 050 006 670 at Er7[7]/Er7[11]); all_from_n9 is false; has_independent_8gram is true. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 84 locks that independent Er7 doubled 4-gram on already-vendored fixtures (`tests/test_mamari_keiti_er7_double_scoreboard.py`): 092 050 006 670 and its 8-gram double 092 050 006 670 092 050 006 670 at Er7[7]/Er7[11] (er7_hits 2); off_e_hits 0 on already-vendored A, B, C, D, G, K, H, P, Q, I, Ev; e_only is true. No new tablet. No meanings. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 85 vendors tablet F / Stephen-Chauvet Fragment [Fa.html](http://kohaumotu.org/Rongorongo/F/Fa.html) / [Fb.html](http://kohaumotu.org/Rongorongo/F/Fb.html) (`tests/fixtures/chauvet_fa_html/`, `tests/fixtures/chauvet_fb_html/`; Fr.html / Fv.html / F.html are unpublished 404s — F/index.html lists Fa.html / Fb.html, same a/b lesson as D) and locks that tablet only (`tests/test_mamari_chauvet_vendor_scoreboard.py`): Fa 44 / Fb 12 stems; G–K islands + n=25, H∩P∩Q n≥8, E n=9, and Er7 doubled 4-gram are exact-0 on F; longest repeating n=0 (no n≥4 freq≥2). Claim: known islands absent. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 86 vendors tablet J / Reimiro 1 [Ja.html](http://kohaumotu.org/Rongorongo/J/Ja.html) (`tests/fixtures/reimiro_ja_html/`; Jb.html / Jr.html / Jv.html are unpublished 404s — J/index.html lists Ja.html as Lines; J.html is the 200 item+lines overview with the same two codes, not a second side) and locks that tablet only (`tests/test_mamari_reimiro_vendor_scoreboard.py`): Ja 2 stems; G–K islands + n=25, H∩P∩Q n≥8, E n=9, and Er7 doubled 4-gram are exact-0 on J; longest repeating n=0 (no n≥4 freq≥2). Claim: known islands absent. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 87 vendors tablet L / Reimiro 2 [La.html](http://kohaumotu.org/Rongorongo/L/La.html) (`tests/fixtures/reimiro_la_html/`; Lb.html / Lr.html / Lv.html are unpublished 404s — L/index.html lists La.html as Lines; L.html is the 200 item overview with no Line_N Barthel codes, not a second side) and locks that tablet only (`tests/test_mamari_reimiro2_vendor_scoreboard.py`): La 51 stems; G–K islands + n=25, H∩P∩Q n≥8, E n=9, and Er7 doubled 4-gram are exact-0 on L; longest repeating n=0 (no n≥4 freq≥2). Claim: known islands absent. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 88 vendors tablet M / Great Vienna [Ma.html](http://kohaumotu.org/Rongorongo/M/Ma.html) (`tests/fixtures/vienna_ma_html/`; Mb.html / Mr.html / Mv.html / M.html are unpublished 404s — M/index.html lists Ma.html as Lines; only one side legible) and locks that tablet only (`tests/test_mamari_vienna_vendor_scoreboard.py`): Ma 65 stems (0 23 15 13 6 4 0 0 4); G–K islands + n=25, H∩P∩Q n≥8, E n=9, and Er7 doubled 4-gram are exact-0 on M; longest repeating n=4 (006 022 006 022 on Ma2; no n≥8). Claim: known islands absent. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6. Cycle 89 vendors tablet N / Small Vienna [Na.html](http://kohaumotu.org/Rongorongo/N/Na.html) / [Nb.html](http://kohaumotu.org/Rongorongo/N/Nb.html) (`tests/fixtures/vienna_na_html/`, `tests/fixtures/vienna_nb_html/`; Nr.html / Nv.html / N.html are unpublished 404s — N/index.html lists Na.html / Nb.html, same a/b lesson as D/F) and locks that tablet only (`tests/test_mamari_small_vienna_vendor_scoreboard.py`): Na 151 / Nb 106 stems; G–K islands + n=25, H∩P∩Q n≥8, E n=9, Er7 doubled 4-gram, and M's n=4 006 022 006 022 are exact-0 on N; longest repeating n=6 (004 064 034 006 004 064 on Na1; no n≥8). Claim: known islands absent. Existing scoreboards are unchanged. Image track stays parked 83/62 / Hamming 6.

The image-side scoreboard (`tests/test_mamari_image_scoreboard.py`) runs stock `GlyphProcessor` on the Kohaumotu Ca7–Ca8 Barthel tracings (`tests/fixtures/mamari_ca7_ca8/`; CEIPP drawings, not MIT — see that directory's ATTRIBUTION). Cataloger IDs stay G00n; there is no invented Barthel map. `input/tablets/sample_tablet.png` is a synthetic CV dummy (circles/triangles), not Mamari. The honest proxy is a repeating 8-gram of frequency ≥2; that assertion is an expected failure today. Cycle 16 surveyed public Kohaumotu / CEIPP sources for a larger Ca7–Ca8 raster and locked a GIF ceiling: no new image. Cycle 17 searches the full G00n reading-order sequence (concatenated Ca7+Ca8, and each line) for any 8-gram of frequency ≥2 and for the longest mixed n-gram of frequency ≥2 anywhere (`tests/test_mamari_unconstrained_ngram_scoreboard.py`). None; longest mixed n stays 2. Cycle 18 locked nearest length-8 Hamming (`tests/test_mamari_nearest_8window_scoreboard.py`): concat min 3 at Ca7[0:8] vs Ca7[1:9] (adjacent overlapping windows on the six-G001 night-sign run; both overlap the first published delimiter); published-window min 7 (first pair Ca7[6:14] vs Ca8[3:11]). Cycle 19 merges one leftover same-slot crop pair that clears the cycle-13 NCC/chamfer gate and drops published-window min Hamming to 6 (Ca7[19:27] vs Ca8[15:23]). Concat min stays 3. Instances/types stay 83/62. `delimiter_slot_crop_hamming_merge=False` restores the cycle-18 published-H=7 lock. Cycle 20 applies the two remaining crop-clear leftover pairs together (slot 2 Ca7[8]/Ca8[31], slot 3 Ca7[9]/Ca8[32]); published min stays 6, so crop-NCC leftovers are exhausted at 6. `delimiter_slot_crop_leftover_merge` defaults False; True unions those leftovers (83/60, slot unique (4, 6, 5, 5, 5, 6, 6, 4)) without dropping Hamming. Slot 0 leftovers are not merged. Cycle 21 retries those slot-0 leftovers under {identity, hflip, vflip, 180°} at the same NCC ≥ 0.45 / chamfer ≤ 0.80 gate; best leftover is 0.247 / 1.224 (Ca7[33] vs Ca8[29] hflip), so flip-invariant crop cannot buy a Hamming point. `delimiter_slot_crop_invariant_merge` stays False.

The position-alignment scoreboard (`tests/test_mamari_position_alignment_scoreboard.py`) maps mixed repeating G00n n-gram indexes onto the published Ca7/Ca8 Barthel stems (same 43+40 reading-order slots; no type map). Each hit records the published stem pair/triple and whether that slice is a contiguous subsequence of Guy's delimiter or of the published ligatures 390.041 / 008.078.711.

The neighbor-allograph scoreboard (`tests/test_mamari_neighbor_allograph_scoreboard.py`) applies the existing unsigned-Hu / area / width (and tall-thin aspect) gates to tokens immediately left or right of those mixed hits. Corresponding Ca8 3-gram neighbors fail those gates, so the repeating mixed n-gram stays length 3. No G00n→Barthel map.

The wide-profile scoreboard (`tests/test_mamari_wide_profile_scoreboard.py`) adds a column-ink profile correlation used only on boxes with aspect > 0.5. Same-line adjacent or delimiter-adjacent (corresponding neighbors of a repeating mixed n-gram) wide instances merge if Pearson ≥ 0.85. The cycle-7 Ca8 left-neighbor pair is wide and size-similar but Pearson is ~0.04, so the stitch does not fire and the mixed n-gram stays length 3. Tall-thin Hu gates are unchanged.

The stem-consistency scoreboard (`tests/test_mamari_stem_consistency_scoreboard.py`) lists the published Barthel stems under each G00n ID in the mixed hits. It is a positional alignment table, not a type map. Cycle 10 splits split-fragment types whose members fail unsigned Hu < 2.0 or column-ink r ≥ 0.85 (no Barthel in the splitter). Cycle 11 re-applies those gates to the remaining 2-stem IDs (G003, G008); every member pair passes, so the shared IDs stay. Cycle 12 then unions same-slot occupants that pass those same gates (Hu < 2.0 and/or wide-profile r ≥ 0.85). Cycle 13 crop-compares the four remaining slot-0 IDs; leftovers fail NCC/chamfer. Cycle 15 applies that same keep-ID gate globally after DBSCAN: 83/62 / 43+40; mixed n=2 (`G007 G006` off the delimiter, plus `G011 G013` on two Ca8 delimiter slices); no 8-gram; G007→040/600, G011→041/390, G013→041/378. Slot-0 390s still occupy four IDs. Slot matches stay 0/8. The former G009 pair (Ca8[7] vs Ca8[18], r≈0.74) remains split. The gate is not lowered.

The delimiter-window scoreboard (`tests/test_mamari_delimiter_window_scoreboard.py`) is the image-side north-star beside a repeating 8-gram. At each published Guy delimiter on Ca7/Ca8 it reads the eight aligned G00n IDs (not a type map) and counts how many of those 8 slots have the same ID across all repetitions. Cycle 12 merges passing pairs in slots 0, 4, and 7. Cycle 13 compares the four remaining slot-0 IDs on the 64×64 bbox crop (NCC and chamfer). Already-merged pairs sit at NCC 0.504 / chamfer 0.544 and 0.909 / 0.117; leftover ceiling is NCC 0.229 / chamfer 1.017. Column-ink leftover max r is 0.584, below the 0.70 adjacent-nonmatch ceiling, so r is not lowered. Leftovers stay distinct. Cycle 14 jointly offsets every published window start by {-2,-1,0,+1,+2} on the existing G00n sequence (no re-cluster). Every offset is 0/8; -2 / -1 / 0 share mean unique 5.500, so offset 0 stays locked. Cycle 15 global keep-ID clustering drops types 64→62 and does not raise any slot to unanimity. Lock: 0/8, slot unique (4, 6, 6, 6, 5, 6, 6, 5). Cycle 16 surveyed public Kohaumotu / CEIPP rasters for a Ca7–Ca8 source larger than the 522×74 GIFs (`tests/fixtures/mamari_ca7_ca8/SOURCE_SURVEY.json`). Ca.html PNGs are the same 522×74; `ca.jpg` is 980×630 with no published Ca7–Ca8 pixel bounds; lunar.html color GIFs fight `THRESH_BINARY_INV`. No crop was invented. Result: GIF ceiling, lock unchanged 83/62 / 0/8. Cycle 17 then searches the standing G00n sequence itself, not just the six published windows: no unconstrained 8-gram (concat / Ca7 / Ca8); longest mixed n anywhere is 2 (`G007 G006` overlaps slot-0 390, `G011 G013` sits inside two Ca8 windows). Cycle 18 records nearest 8-window Hamming on that same sequence: concat min 3 (Ca7[0:8] / Ca7[1:9], both overlap Ca7[6:14)); published-window min 7 (four pairs; first is Ca7[6:14] vs Ca8[3:11], shared G003). Cycle 19 then crop-compares leftover same-slot occupants across all eight published slots. Three pairs clear NCC ≥ 0.45 / chamfer ≤ 0.80; only slot 7 Ca7[26] vs Ca8[22] (Hu 2.32, so keep-ID fails) also drops published min Hamming, 7→6. Slot 2 G020/G060 and slot 3 G019/G061 pass crop but would leave min Hamming at 7 alone. Cycle 20 unions those two leftovers together on top of the slot-7 merge; published min stays 6 (now two pairs at 6), so the extra merges stay off. Cycle 21 applies the same crop numbers to slot-0 leftovers after {identity, hflip, vflip, 180°}; none clear (best NCC 0.247 / chamfer 1.224). The G023/G006 pair would drop published Hamming 6→5 but fails the gate. Window stays 0/8; slot unique stays (4, 6, 6, 6, 5, 6, 6, 4). Mixed n stays 2. Instances/types stay 83/62.

The type-identity scoreboard (`tests/test_mamari_type_identity_scoreboard.py`) locks stock cluster identity on those same GIFs: instances per strip, unique G00n count, unique/instance ratio, max n in 1..8 with any n-gram of frequency ≥2, whether a mixed (more than one type) n-gram of length ≥2 repeats, and Ca7/Ca8 sequence lengths vs published stem counts (43 and 40). Stock clustering uses unsigned log-Hu (`ProcessorConfig.hu_sign_mode="unsigned"`). After DBSCAN, `global_type_consistency_merge` applies the cycle 7–8 keep-ID gate (unsigned Hu < 2.0 and, when both profiles exist, Pearson r ≥ 0.85) to every instance pair, not only delimiter slots; connected components are re-partitioned so a failing pair is never forced onto one ID. A same-line allograph stitch then unions adjacent tall-thin crescents (unsigned-Hu distance below the observed crescent diameter), and a second, instance-local stitch unions valley-split fragments (unsigned Hu < 2.0, area ratio ≤ 1.1, bbox-width ratio ≤ 1.08). After those stitches, `split_inconsistent_types` re-partitions split-fragment members so a shared ID still requires the keep-ID gate. `delimiter_slot_merge` then unions instances that occupy the same published Guy slot (starts only, not stem meanings) when they pass type-consistency and/or the wide-profile gate. Slot 0 also consults bbox-crop NCC ≥ 0.45 and chamfer ≤ 0.80; leftovers fail that gate, so the slot is not forced to one ID. `delimiter_slot_crop_hamming_merge` then unions at most one leftover same-slot crop pair on any slot if that union drops published-window min Hamming; the slot-7 Ca7[26]/Ca8[22] pair fires (published H 7→6). `delimiter_slot_crop_leftover_merge` would then union remaining crop-clear leftovers (slot 2 and slot 3) without a Hamming-drop requirement; jointly they leave published H at 6, so the flag stays False. `delimiter_slot_crop_invariant_merge` would union at most one leftover slot-0 pair after flip/180 if it cleared those same crop numbers and dropped published Hamming; no leftover clears, so the flag stays False. Detection splits only wide connected blobs (width ≥70, aspect ≥0.90) at a deep vertical ink-projection valley; inner contours on these GIFs are holes, not stems. `global_type_consistency_merge=False` restores the cycle-14 64-type / 0/8 lock. `delimiter_slot_merge=False` restores the cycle-11 lock. `delimiter_slot_crop_hamming_merge=False` restores the cycle-18 published-H=7 lock. `delimiter_slot_crop_leftover_merge=True` is the cycle-20 experiment (83/60, published H still 6). `delimiter_slot_crop_merge=False` restores the cycle-12 crop path (leftovers still fail). `split_inconsistent_types=False` restores the cycle-9 lock. `split_fragment_allograph_merge=False` restores the cycle-4 lock. `split_wide_ligatures=False` restores the cycle-3 lock. The signed cycle-1 path and `same_line_allograph_merge=False` remain available. A diagnostic isolates the six adjacent night-sign crescents on `sca0701`. No G00n→Barthel map.

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
