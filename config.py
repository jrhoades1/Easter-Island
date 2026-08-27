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

# Language scraping configuration
LANGUAGE_CONFIG = {
    "rapa_nui": {
        "name": "Rapa Nui",
        "native_name": "Vananga rapa nui",
        "iso_639_3": "rap",
        "glottocode": "rapa1244",
        "family": "Austronesian > Polynesian > Eastern",
        "output_file": "rapa_nui_language.json",
        "urls": [
            # Tier 1: Structured linguistic databases
            "https://asjp.clld.org/languages/RAPA_NUI",
            "https://ids.clld.org/contributions/238",
            # Tier 2: Online dictionaries
            "https://glosbe.com/en/rap",
            # Tier 3: Educational resources
            "https://www.omniglot.com/writing/rapanui.htm",
            "https://en.wikipedia.org/wiki/Rapa_Nui_language",
        ],
    }
}

# Semantic category normalization (maps various source labels to standard categories)
SEMANTIC_CATEGORIES = {
    "body": ["the body", "body parts", "anatomy", "the body"],
    "kinship": ["kinship", "family", "relationships"],
    "nature": ["nature", "environment", "animals", "plants", "the physical world"],
    "food": ["food", "cooking", "drink", "food and drink"],
    "time": ["time", "temporal"],
    "space": ["spatial", "location", "direction", "spatial relations"],
    "action": ["action", "motion", "basic actions", "basic actions and technology"],
    "culture": ["culture", "religion", "ceremony", "religion and belief"],
    "animals": ["animals"],
    "clothing": ["clothing", "clothing and grooming"],
    "house": ["house", "the house", "dwelling"],
    "agriculture": ["agriculture", "agriculture and vegetation", "vegetation"],
    "possession": ["possession", "property"],
    "quantity": ["quantity", "number", "numbers"],
    "perception": ["perception", "sense perception", "senses"],
    "emotion": ["emotion", "emotions", "emotions and values", "feelings"],
    "cognition": ["cognition", "thought", "thinking"],
    "speech": ["speech", "speech and language", "language", "communication"],
    "social": ["social", "social and political relations", "politics"],
    "warfare": ["warfare", "warfare and hunting", "hunting", "weapons"],
    "law": ["law", "legal"],
    "modern": ["modern", "modern world", "technology"],
}

# Part of speech normalization
POS_MAPPING = {
    "n": "noun",
    "noun": "noun",
    "n.": "noun",
    "v": "verb",
    "verb": "verb",
    "v.": "verb",
    "adj": "adjective",
    "adjective": "adjective",
    "adj.": "adjective",
    "adv": "adverb",
    "adverb": "adverb",
    "adv.": "adverb",
    "prep": "preposition",
    "preposition": "preposition",
    "prep.": "preposition",
    "pron": "pronoun",
    "pronoun": "pronoun",
    "pron.": "pronoun",
    "conj": "conjunction",
    "conjunction": "conjunction",
    "conj.": "conjunction",
    "interj": "interjection",
    "interjection": "interjection",
    "interj.": "interjection",
    "num": "numeral",
    "numeral": "numeral",
    "num.": "numeral",
    "particle": "particle",
    "part": "particle",
    "part.": "particle",
}

# Glyph cataloger configuration
GLYPH_CONFIG = {
    # Input/output directories
    "input_dir": os.path.join(BASE_DIR, "input", "tablets"),
    "output_dir": os.path.join(BASE_DIR, "output"),
    "output_file": "rongorongo_lexicon.json",

    # Whether to save individual glyph images
    "save_glyph_images": True,

    # Image processing parameters
    "processing": {
        "min_contour_area": 100,      # Minimum pixels for a valid glyph
        "max_contour_area": 50000,    # Maximum pixels for a valid glyph
        "bbox_padding": 5,            # Padding around detected glyphs
        "line_merge_threshold": 20,   # Vertical distance to merge into same line
    },

    # Clustering parameters
    "clustering": {
        "eps": 0.5,                   # DBSCAN epsilon (distance threshold)
        "min_samples": 2,             # Minimum samples for a cluster
        # "unsigned" = abs(signed log-Hu). "signed" = cycle-1 −sign(h)·log10(|h|).
        "hu_sign_mode": "unsigned",
    },
}

# Cross-referencer configuration
CROSS_REFERENCE_CONFIG = {
    "output_file": "cross_reference_lexicon.json",
    "annotations_file": "shape_annotations.yaml",
    "generate_report": True,
    "report_file": "cross_reference_report.md",
}

# Shape category to semantic domain mapping for cross-referencing
# Maps visual glyph categories to linguistic semantic domains
SHAPE_SEMANTIC_MAPPING = {
    "avian": {
        "semantic_categories": ["animals", "nature"],
        "proto_roots": ["*manu (bird)", "*lupe (pigeon)", "*kura (red feather)"],
        "rapa_nui_words": ["manu", "manutara", "kura"],
        "description": "Bird-like forms including frigate birds, chickens, and generic avian shapes",
    },
    "anthropomorphic": {
        "semantic_categories": ["body", "kinship", "social"],
        "proto_roots": ["*tangata (person)", "*mata (face/eye)", "*rima (hand)", "*waka (body)"],
        "rapa_nui_words": ["tangata", "mata", "rima", "hatu", "ariki"],
        "description": "Human figures, body parts, and personified forms",
    },
    "phytomorphic": {
        "semantic_categories": ["agriculture", "nature", "food"],
        "proto_roots": ["*rakau (tree/wood)", "*kumara (sweet potato)", "*taro"],
        "rapa_nui_words": ["rakau", "kumara", "taro", "toromiro", "maika"],
        "description": "Plant forms including trees, crops, and vegetation",
    },
    "ichthyomorphic": {
        "semantic_categories": ["animals", "food", "nature"],
        "proto_roots": ["*ika (fish)", "*honu (turtle)", "*feke (octopus)"],
        "rapa_nui_words": ["ika", "honu", "heke", "kahi", "mahore"],
        "description": "Fish and marine life forms",
    },
    "geometric": {
        "semantic_categories": ["quantity", "space", "time"],
        "proto_roots": ["*tahi (one)", "*rua (two)", "*toru (three)", "*ha (four)"],
        "rapa_nui_words": ["tahi", "rua", "toru", "ha", "rima", "ono", "hitu", "varu"],
        "description": "Abstract geometric shapes potentially representing numbers or spatial concepts",
    },
    "composite": {
        "semantic_categories": ["culture", "social", "action"],
        "proto_roots": [],
        "rapa_nui_words": [],
        "description": "Combined elements that may represent complex concepts or actions",
    },
    "undetermined": {
        "semantic_categories": [],
        "proto_roots": [],
        "rapa_nui_words": [],
        "description": "Glyphs that cannot be visually classified into other categories",
    },
}

# Confidence level thresholds for cross-references
# Maps confidence level names to (min, max) score ranges
# Upper bound is exclusive except for "strong" which includes 1.0
CONFIDENCE_LEVELS = {
    "speculative": (0.0, 0.25),   # Weak evidence, purely hypothetical
    "tentative": (0.25, 0.50),    # Some supporting evidence
    "plausible": (0.50, 0.75),    # Multiple lines of evidence
    "strong": (0.75, 1.01),       # Strong converging evidence (rare for Rongorongo)
}

# Evidence type weights for computing overall confidence
# Weights should sum to 1.0
EVIDENCE_WEIGHTS = {
    "shape_semantic": 0.40,    # Visual category matches semantic domain
    "frequency": 0.15,         # Common glyph matches common word
    "positional": 0.15,        # Position pattern correlation
    "neighbor": 0.10,          # Co-occurrence with similar neighbors
    "published": 0.15,         # From Rongorongo scholarship
    "manual": 0.05,            # Expert annotation
}

# LLM Agent configuration
LLM_CONFIG = {
    "default_provider": "mock",  # "anthropic", "openai", or "mock"
    "cache_dir": os.path.join(BASE_DIR, ".cache", "llm"),
    "cache_ttl_hours": 24,
    "max_cache_entries": 1000,

    # Provider-specific settings
    "anthropic": {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 4096,
        "temperature": 0.0,
    },
    "openai": {
        "model": "gpt-4o",
        "max_tokens": 4096,
        "temperature": 0.0,
    },
}

# Polynesian corpora configuration for lexical validation
POLYNESIAN_CORPORA_CONFIG = {
    "maori": {
        "name": "Maori",
        "iso_639_3": "mri",
        "family": "Austronesian > Polynesian > Eastern > Maori",
        "urls": [
            "https://maoridictionary.co.nz/",
        ],
    },
    "hawaiian": {
        "name": "Hawaiian",
        "iso_639_3": "haw",
        "family": "Austronesian > Polynesian > Eastern > Hawaiian",
        "urls": [
            "https://wehewehe.org/",
        ],
    },
    "tahitian": {
        "name": "Tahitian",
        "iso_639_3": "tah",
        "family": "Austronesian > Polynesian > Eastern > Tahitic",
        "urls": [
            "https://farevanaa.pf/dictionnaire.php",
        ],
    },
}

# Agent-specific configuration
AGENT_CONFIG = {
    "segmentation": {
        "analyze_ligatures": True,
        "analyze_damage": True,
        "output_file": "segmentation_results.json",
    },
    "pattern_mining": {
        "max_ngram": 5,
        "min_pattern_frequency": 2,
        "similarity_threshold": 0.7,
        "output_file": "pattern_mining_results.json",
    },
    "lexical_validation": {
        "min_cognate_languages": 2,
        "confidence_boost": 0.15,
        "output_file": "lexical_validation_results.json",
    },
}
