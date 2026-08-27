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

The Ca6–Ca9 scoreboard fixture (`tests/fixtures/mamari_ca6_ca9_barthel.json`) is the Kohaumotu published Barthel-coded transcription of the Mamari lunar/calendar passage ([Ca.html](http://kohaumotu.org/Rongorongo/C/Ca.html)). Guy 1990 Fig. 1 / Table 1 did not extract as text. Cycle 28 vendors that same Ca.html (`tests/fixtures/mamari_ca_html/`) and locks the remainder as a second published passage: Guy's 8-stem delimiter is absent, 600 is not window-adjacent (five hits, no windows), and 040-runs are six isolated tokens on Ca10–Ca12 (12 windowless cells). Cycle 29 locks that remainder's repeating n≥4 freq≥2 profile (`tests/test_mamari_remainder_ngram_profile_scoreboard.py`): 31 distinct n-grams, longest n=9 on Ca10/Ca11, two 8-grams (top is not Guy's delimiter), and the five 600 hits sit outside every repeating n≥4 span. Calendar Ca6–Ca9 is not re-mined. Cycle 30 locks that 9-gram as a motif (`tests/test_mamari_remainder_9gram_motif_scoreboard.py`): exact remainder hits and one-token flanks, the 8-prefix at the same starts, six 002…002 wraps at n=9 (four are not the motif), and calendar-absent on Ca6–Ca9. Cycle 31 locks that wrap family (`tests/test_mamari_remainder_002_wrap_family_scoreboard.py`): for each of the six remainder windows, line, span, nine tokens, whether it is the motif, aligned position matches against the motif, and shared interior stems (bookend 002 excluded; not a delimiter claim). All six share at least one interior stem with the motif besides 002 (the four non-motif wraps share 010 and/or 760, and Ca10[18:27] also shares 070 040 006). Calendar still has none. Cycle 32 vendors the same publisher's tablet-C verso (`tests/fixtures/mamari_cb_html/Cb.html`, [Cb.html](http://kohaumotu.org/Rongorongo/C/Cb.html)) and locks that side only (`tests/test_mamari_cb_side_b_scoreboard.py`): Guy's 8-stem delimiter is absent (freq 0), the 9-gram motif is absent, four 002…002 n=9 wraps (two share a non-bookend interior stem with the motif: Cb7 760, Cb8 070), and 600 appears twice. Ca remainder locks are unchanged. Cycle 33 locks that verso's repeating n≥4 freq≥2 profile (`tests/test_mamari_cb_repeating_ngram_profile_scoreboard.py`): 12 distinct n-grams, longest n=5 (three grams, all freq 2), no repeating 8-gram. Cycle 34 locks those three Cb 5-grams as absent on the Ca calendar and Ca remainder (`tests/test_mamari_cb_5gram_ca_cross_scoreboard.py`). Cycle 35 looks at the already-vendored Ca.html / Cb.html navbars and in-repo ATTRIBUTION / CORPUS_SURVEY / README for a Kohaumotu Barthel page of a different tablet; none is honestly linked from those navbars (`tests/test_mamari_off_tablet_c_ceiling_scoreboard.py`). Cycle 36 opens the parent catalog ([Rongorongo/](http://kohaumotu.org/Rongorongo/)), takes the first non-C tablet with extractable Barthel numbers (A / Tahua), vendors [Aa.html](http://kohaumotu.org/Rongorongo/A/Aa.html) (`tests/fixtures/tahua_aa_html/`), and locks that side only (`tests/test_mamari_tahua_aa_scoreboard.py`): Guy's 8-stem delimiter is absent (freq 0), the Ca 9-gram is absent, the three Cb 5-grams are absent, 906 stems, longest n with freq≥2 is 10, top 8-gram is 080 004 280 182 048 022 025 025 (freq 2, not Guy). Cycle 37 locks that Aa 10-gram as a motif (`tests/test_mamari_tahua_aa_10gram_motif_scoreboard.py`): exact hits Aa7[55:65] / Aa7[88:98] (freq 2) with one-token flanks 002/009 and 020/256, the cycle-36 top 8-gram is its prefix, and the 10-gram is absent from the Ca calendar, Ca remainder, and Cb fixtures. Cycle 38 vendors the same tablet-A verso (`tests/fixtures/tahua_ab_html/Ab.html`, [Ab.html](http://kohaumotu.org/Rongorongo/A/Ab.html)) and locks that side only (`tests/test_mamari_tahua_ab_scoreboard.py`): the Aa 10-gram is absent, Guy's 8-stem delimiter is absent (freq 0), the Ca 9-gram is absent, 926 stems, longest n with freq≥2 is 9, top 8-gram is 605 003 004 600 004 003 040 003 (freq 2). Cycle 39 locks that Ab 9-gram as a motif (`tests/test_mamari_tahua_ab_9gram_motif_scoreboard.py`): exact hits Ab3[2:11] / Ab5[13:22] (freq 2) with one-token flanks 003/003 and 208/093, the cycle-38 top 8-gram is its prefix, 600 sits at slot 3 in both hits, and the 9-gram is absent from Aa, the Ca calendar, Ca remainder, and Cb fixtures. Cycle 40 locks a 600 inventory on those same fixtures only (`tests/test_mamari_600_inventory_scoreboard.py`): 64 hits (calendar 2, remainder 5, Cb 2, Aa 23, Ab 32) with tablet/side, line, index, one-token flanks, locked-motif membership (Guy window / Ca 9-gram / Aa 10-gram / Ab 9-gram), and calendar window-adjacency. Two calendar hits are window-adjacent (Ca7[32] last facing Guy, Ca8[23] first after Guy); two Ab hits sit inside the Ab 9-gram (Ab3[5], Ab5[16]); none sit inside Guy, the Ca 9-gram, or the Aa 10-gram. Cycle 41 locks the 004 600 004 sandwich on that same inventory (`tests/test_mamari_600_sandwich_scoreboard.py`): three Ab hits (Ab3[4:7] and Ab5[15:18] are the Ab 9-gram 600 slot; Ab7[16:19] is not); none on Ca calendar, Ca remainder, Cb, or Aa. Per-fixture top 600 neighbors (stem, count; line-edge excluded; ties break by earliest stem id): calendar 152/040 (1/1), remainder 007/001 (2/2), Cb 001/003 (1/1), Aa 004/007 (5/5), Ab 003/001 (6/5). Cycle 42 locks the Ab7 sandwich 9-window Hamming vs the Ab 9-gram (`tests/test_mamari_ab7_9gram_hamming_scoreboard.py`): Ab7[14:23] Hamming 6 (shares 004 600 004 only); not a near-copy. Image track stays parked 83/62 / Hamming 6. Cycle 43 opens the same parent catalog, takes the first tablet that is not A and not C with extractable Barthel numbers (B / Aruku-Kurenga), vendors [Br.html](http://kohaumotu.org/Rongorongo/B/Br.html) (`tests/fixtures/aruku_br_html/`), and locks that recto only (`tests/test_mamari_aruku_br_scoreboard.py`): Guy's 8-stem delimiter is absent (freq 0), the Ca 9-gram / Aa 10-gram / Ab 9-gram / 004 600 004 sandwich are absent, 560 stems, longest n with freq≥2 is 6 (384 003 001 470 091 450, freq 2 on Br4), no repeating 8-gram. Existing Aa/Ab/C scoreboards are unchanged. No invented URL or digits. Further cell tables on the original 101 tokens are not a new corpus. The unit test fails if the repeating delimiter is missing from the top-N n-grams of matching length, or if same-length noise outranks it. A seeded shuffle of the same Barthel stems is the negative control: the published delimiter must not reappear as a repeating 8-gram.

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
