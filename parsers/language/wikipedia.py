"""Parser for Wikipedia Rapa Nui language pages."""

from models.language import LanguageEntry

from .base import BaseLanguageParser


class WikipediaLanguageParser(BaseLanguageParser):
    """Parser for Wikipedia language articles."""

    source_name = "Wikipedia"
    source_url_pattern = "wikipedia.org"

    def can_parse(self, url: str) -> bool:
        """Check if this parser can handle the given URL."""
        return "wikipedia.org" in url and "rapa_nui" in url.lower()

    def _is_numeral_table(self, headers: list[str]) -> bool:
        """Check if this is a numeral table (numbers as first column)."""
        if not headers:
            return False
        # Check for numeral-related headers
        numeral_keywords = ["cardinal", "counting", "ordinal"]
        return any(kw in h.lower() for h in headers for kw in numeral_keywords)

    def _is_pronoun_table(self, headers: list[str]) -> bool:
        """Check if this is a pronoun table."""
        if not headers:
            return False
        pronoun_keywords = ["singular", "dual", "plural", "1st-person", "2nd-person", "3rd-person"]
        return any(kw in h.lower() for h in headers for kw in pronoun_keywords)

    def _parse_numeral_table(self, rows: list, metadata) -> list[LanguageEntry]:
        """Parse a numeral table where first column is the number."""
        entries = []
        headers = [self.clean_text(th.get_text()).lower() for th in rows[0].find_all(["th", "td"])]

        for row in rows[1:]:
            cols = row.find_all(["td", "th"])
            if len(cols) < 2:
                continue

            # First column is the number (translation/meaning)
            number = self.clean_text(cols[0].get_text())
            if not number or not number.isdigit():
                continue

            # Subsequent columns are Rapa Nui words
            for i, col in enumerate(cols[1:], 1):
                word = self.clean_text(col.get_text())
                if word and word not in ["-", "—", ""]:
                    # Use header as context if available
                    form = headers[i] if i < len(headers) else "numeral"
                    translation = f"{number} ({form})" if form and form != number else number

                    entry = LanguageEntry(
                        word=word,
                        translations=[self.create_translation(translation)],
                        part_of_speech="numeral",
                        metadata=metadata,
                    )
                    entries.append(entry)

        return entries

    def _parse_pronoun_table(self, rows: list, metadata) -> list[LanguageEntry]:
        """Parse a pronoun table."""
        entries = []
        headers = [self.clean_text(th.get_text()).lower() for th in rows[0].find_all(["th", "td"])]

        for row in rows[1:]:
            cols = row.find_all(["td", "th"])
            if len(cols) < 2:
                continue

            # First column usually indicates person (1st, 2nd, 3rd) or inclusivity
            row_label = self.clean_text(cols[0].get_text())

            # Subsequent columns are pronouns for different numbers (singular, dual, plural)
            for i, col in enumerate(cols[1:], 1):
                word = self.clean_text(col.get_text())
                if word and word not in ["-", "—", ""]:
                    # Build description from row label and column header
                    number_form = headers[i] if i < len(headers) else ""
                    translation = f"{row_label} {number_form}".strip()
                    if translation:
                        entry = LanguageEntry(
                            word=word,
                            translations=[self.create_translation(translation)],
                            part_of_speech="pronoun",
                            metadata=metadata,
                        )
                        entries.append(entry)

        return entries

    def parse(self, html: str, url: str) -> list[LanguageEntry]:
        """Parse Wikipedia language page and return language entries."""
        soup = self.get_soup(html)
        entries = []
        metadata = self.create_metadata(url, confidence="medium")

        # Find the main content area
        content = soup.find("div", {"id": "mw-content-text"})
        if not content:
            content = soup

        # Look for vocabulary tables
        for table in content.find_all("table", class_="wikitable"):
            rows = table.find_all("tr")
            if not rows:
                continue

            # Get headers
            headers = [self.clean_text(th.get_text()).lower() for th in rows[0].find_all(["th", "td"])]

            # Skip phonology tables (consonants, vowels)
            phonology_keywords = ["labial", "alveolar", "velar", "glottal", "front", "back", "central", "high", "low"]
            if any(kw in h for h in headers for kw in phonology_keywords):
                continue

            # Skip syntax/grammar structure tables
            syntax_keywords = ["verb", "neg(", "determiner"]
            if any(kw in h for h in headers for kw in syntax_keywords):
                continue

            # Handle special table types
            if self._is_numeral_table(headers):
                entries.extend(self._parse_numeral_table(rows, metadata))
                continue

            if self._is_pronoun_table(headers):
                entries.extend(self._parse_pronoun_table(rows, metadata))
                continue

            # Standard vocabulary table parsing
            rapa_nui_col = -1
            english_col = -1
            ipa_col = -1
            pos_col = -1

            for i, header in enumerate(headers):
                if any(kw in header for kw in ["rapa nui", "rapanui", "word", "term", "native"]):
                    rapa_nui_col = i
                elif any(kw in header for kw in ["english", "meaning", "translation", "gloss"]):
                    english_col = i
                elif any(kw in header for kw in ["ipa", "pronunciation", "phonetic"]):
                    ipa_col = i
                elif any(kw in header for kw in ["pos", "part of speech", "class", "category"]):
                    pos_col = i

            # Skip tables without clear vocabulary structure
            if rapa_nui_col == -1 and english_col == -1:
                continue

            # Parse data rows
            for row in rows[1:]:
                cols = row.find_all(["td", "th"])
                if len(cols) < 2:
                    continue

                word = ""
                translation = ""
                ipa = None
                pos = None

                if 0 <= rapa_nui_col < len(cols):
                    word = self.clean_text(cols[rapa_nui_col].get_text())
                if 0 <= english_col < len(cols):
                    translation = self.clean_text(cols[english_col].get_text())
                if 0 <= ipa_col < len(cols):
                    ipa = self.clean_text(cols[ipa_col].get_text())
                if 0 <= pos_col < len(cols):
                    pos = self.clean_text(cols[pos_col].get_text())

                if word and translation:
                    entry = LanguageEntry(
                        word=word,
                        ipa=ipa,
                        translations=[self.create_translation(translation)],
                        part_of_speech=pos,
                        metadata=metadata,
                    )
                    entries.append(entry)

        # Skip inline text parsing for now as it produces too much noise
        # The table parsing above captures the structured vocabulary data

        return entries
