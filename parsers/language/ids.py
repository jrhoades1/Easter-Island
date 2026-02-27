"""Parser for IDS (Intercontinental Dictionary Series) database."""

from models.language import LanguageEntry

from .base import BaseLanguageParser

# IDS semantic category mapping
IDS_CATEGORIES = {
    "1": "the physical world",
    "2": "kinship",
    "3": "animals",
    "4": "the body",
    "5": "food and drink",
    "6": "clothing and grooming",
    "7": "the house",
    "8": "agriculture and vegetation",
    "9": "basic actions and technology",
    "10": "motion",
    "11": "possession",
    "12": "spatial relations",
    "13": "quantity",
    "14": "time",
    "15": "sense perception",
    "16": "emotions and values",
    "17": "cognition",
    "18": "speech and language",
    "19": "social and political relations",
    "20": "warfare and hunting",
    "21": "law",
    "22": "religion and belief",
    "23": "modern world",
}


class IDSParser(BaseLanguageParser):
    """Parser for IDS database entries."""

    source_name = "IDS - Intercontinental Dictionary Series"
    source_url_pattern = "ids.clld.org"

    def can_parse(self, url: str) -> bool:
        """Check if this parser can handle the given URL."""
        return "ids.clld.org" in url

    def parse(self, html: str, url: str) -> list[LanguageEntry]:
        """Parse IDS contribution page and return language entries."""
        soup = self.get_soup(html)
        entries = []
        metadata = self.create_metadata(url, confidence="high")

        # IDS pages have tables with word entries
        # Look for the main data table
        tables = soup.find_all("table", class_="table")

        for table in tables:
            rows = table.find_all("tr")
            for row in rows[1:]:  # Skip header
                cols = row.find_all("td")
                if len(cols) < 2:
                    continue

                # Try to extract word and meaning
                # Structure varies but typically: meaning/concept | word form
                meaning = ""
                word = ""
                category = None

                # Look for links which often contain the actual data
                links = row.find_all("a")
                for link in links:
                    href = link.get("href", "")
                    text = self.clean_text(link.get_text())

                    if "/parameters/" in href:
                        # This is the meaning/concept
                        meaning = text
                        # Extract category from parameter ID if possible
                        param_id = href.split("/")[-1].split("-")[0]
                        if param_id.isdigit():
                            cat_num = param_id.split(".")[0] if "." in param_id else param_id[:2].rstrip("0123456789") or param_id[0]
                            category = IDS_CATEGORIES.get(cat_num)
                    elif "/values/" in href or "/forms/" in href:
                        # This is the word form
                        word = text

                # Fallback: just use column text
                if not word and len(cols) >= 2:
                    word = self.clean_text(cols[-1].get_text())
                if not meaning and len(cols) >= 1:
                    meaning = self.clean_text(cols[0].get_text())

                if not word or not meaning:
                    continue

                entry = LanguageEntry(
                    word=word,
                    translations=[self.create_translation(meaning)],
                    semantic_category=category,
                    metadata=metadata,
                )
                entries.append(entry)

        # Also check for definition lists (dl/dt/dd)
        for dl in soup.find_all("dl"):
            terms = dl.find_all("dt")
            definitions = dl.find_all("dd")
            for dt, dd in zip(terms, definitions):
                meaning = self.clean_text(dt.get_text())
                word = self.clean_text(dd.get_text())
                if word and meaning:
                    entry = LanguageEntry(
                        word=word,
                        translations=[self.create_translation(meaning)],
                        metadata=metadata,
                    )
                    entries.append(entry)

        return entries
