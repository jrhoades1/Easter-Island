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
