"""Parser for Glosbe online dictionary."""

import re

from models.language import LanguageEntry

from .base import BaseLanguageParser


class GlosbeParser(BaseLanguageParser):
    """Parser for Glosbe dictionary entries."""

    source_name = "Glosbe Dictionary"
    source_url_pattern = "glosbe.com"

    def can_parse(self, url: str) -> bool:
        """Check if this parser can handle the given URL."""
        return "glosbe.com" in url and "/rap" in url

    def parse(self, html: str, url: str) -> list[LanguageEntry]:
        """Parse Glosbe dictionary page and return language entries."""
        soup = self.get_soup(html)
        entries = []
        metadata = self.create_metadata(url, confidence="medium")

        # Method 1: Parse "Recent changes" section
        # Format: "word" en → "translation" rap
        page_text = soup.get_text()

        # Look for translation pairs in format: "word" lang → "translation" lang
        pattern = r'"([^"]+)"\s*(?:en|eng)\s*→\s*"([^"]+)"\s*(?:rap|rapa)'
        matches = re.findall(pattern, page_text, re.IGNORECASE)
        for english, rapa_nui in matches:
            if rapa_nui and english:
                entry = LanguageEntry(
                    word=rapa_nui.strip(),
                    translations=[self.create_translation(english.strip())],
                    metadata=metadata,
                )
                entries.append(entry)

        # Also try reverse pattern (Rapa Nui → English)
        pattern_reverse = r'"([^"]+)"\s*(?:rap|rapa)\s*→\s*"([^"]+)"\s*(?:en|eng)'
        matches_reverse = re.findall(pattern_reverse, page_text, re.IGNORECASE)
        for rapa_nui, english in matches_reverse:
            if rapa_nui and english:
                entry = LanguageEntry(
                    word=rapa_nui.strip(),
                    translations=[self.create_translation(english.strip())],
                    metadata=metadata,
                )
                entries.append(entry)

        # Method 2: Look for structured translation divs
        for entry_div in soup.find_all(["div", "li"], class_=lambda x: x and (
            "translation" in str(x).lower() or
            "phrase" in str(x).lower() or
            "entry" in str(x).lower()
        )):
            word = ""
            translation = ""

            source = entry_div.find(class_=lambda x: x and "source" in str(x).lower())
            target = entry_div.find(class_=lambda x: x and ("target" in str(x).lower() or "translation" in str(x).lower()))

            if source:
                word = self.clean_text(source.get_text())
            if target:
                translation = self.clean_text(target.get_text())

            if word and translation:
                entry = LanguageEntry(
                    word=word,
                    translations=[self.create_translation(translation)],
                    metadata=metadata,
                )
                entries.append(entry)

        # Method 3: Look for tables with word pairs
        for table in soup.find_all("table"):
            rows = table.find_all("tr")
            for row in rows:
                cols = row.find_all(["td", "th"])
                if len(cols) >= 2:
                    word = self.clean_text(cols[0].get_text())
                    translation = self.clean_text(cols[1].get_text())
                    if word and translation and word != translation:
                        entry = LanguageEntry(
                            word=word,
                            translations=[self.create_translation(translation)],
                            metadata=metadata,
                        )
                        entries.append(entry)

        # Method 4: Look for definition lists
        for dl in soup.find_all("dl"):
            terms = dl.find_all("dt")
            definitions = dl.find_all("dd")
            for dt, dd in zip(terms, definitions):
                word = self.clean_text(dt.get_text())
                translation = self.clean_text(dd.get_text())
                if word and translation:
                    entry = LanguageEntry(
                        word=word,
                        translations=[self.create_translation(translation)],
                        metadata=metadata,
                    )
                    entries.append(entry)

        # Method 5: Look for phrase examples
        for example_div in soup.find_all(["div", "p"], class_=lambda x: x and "example" in str(x).lower()):
            text = self.clean_text(example_div.get_text())
            if text:
                for sep in [" - ", " – ", " — ", " = ", ": "]:
                    if sep in text:
                        parts = text.split(sep, 1)
                        if len(parts) == 2:
                            word, translation = parts
                            entry = LanguageEntry(
                                word=word.strip(),
                                translations=[self.create_translation(translation.strip())],
                                metadata=metadata,
                            )
                            entries.append(entry)
                            break

        return entries
