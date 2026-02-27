"""Parser for Omniglot language resource pages."""

from models.language import LanguageEntry

from .base import BaseLanguageParser


class OmniglotParser(BaseLanguageParser):
    """Parser for Omniglot language pages."""

    source_name = "Omniglot"
    source_url_pattern = "omniglot.com"

    def can_parse(self, url: str) -> bool:
        """Check if this parser can handle the given URL."""
        return "omniglot.com" in url and "rapanui" in url.lower()

    def parse(self, html: str, url: str) -> list[LanguageEntry]:
        """Parse Omniglot page and return language entries."""
        soup = self.get_soup(html)
        entries = []
        metadata = self.create_metadata(url, confidence="medium")

        # Omniglot pages typically have:
        # 1. Alphabet/phonology tables
        # 2. Sample words and phrases
        # 3. Sample texts (like UDHR)

        # Look for tables with vocabulary
        for table in soup.find_all("table"):
            rows = table.find_all("tr")
            for row in rows:
                cols = row.find_all(["td", "th"])
                if len(cols) >= 2:
                    # Could be word | pronunciation | meaning
                    # or word | meaning
                    texts = [self.clean_text(col.get_text()) for col in cols]

                    word = ""
                    translation = ""
                    ipa = None

                    if len(texts) == 2:
                        word, translation = texts
                    elif len(texts) >= 3:
                        # Assume: word, pronunciation/IPA, meaning
                        word = texts[0]
                        # Check if second column looks like IPA
                        if texts[1].startswith("[") or texts[1].startswith("/"):
                            ipa = texts[1]
                            translation = texts[2] if len(texts) > 2 else ""
                        else:
                            translation = texts[1]

                    # Skip header rows and empty entries
                    if not word or not translation:
                        continue
                    if word.lower() in ("word", "phrase", "english", "rapa nui", "rapanui"):
                        continue

                    entry = LanguageEntry(
                        word=word,
                        ipa=ipa,
                        translations=[self.create_translation(translation)],
                        metadata=metadata,
                    )
                    entries.append(entry)

        # Look for phrase sections (often in divs or paragraphs)
        # Common pattern: "Rapa Nui phrase - English translation"
        content_div = soup.find("div", {"id": "content"}) or soup.find("main") or soup

        for p in content_div.find_all("p"):
            text = p.get_text()
            # Look for phrase patterns with separators
            for sep in [" - ", " – ", " = "]:
                if sep in text:
                    lines = text.split("\n")
                    for line in lines:
                        if sep in line:
                            parts = line.split(sep, 1)
                            if len(parts) == 2:
                                word = self.clean_text(parts[0])
                                translation = self.clean_text(parts[1])
                                if word and translation and len(word) < 100:
                                    entry = LanguageEntry(
                                        word=word,
                                        translations=[self.create_translation(translation)],
                                        metadata=metadata,
                                    )
                                    entries.append(entry)

        # Look for headers that indicate phrase sections
        for header in soup.find_all(["h2", "h3", "h4"]):
            header_text = header.get_text().lower()
            if any(kw in header_text for kw in ["phrase", "word", "expression", "vocabulary"]):
                # Get the next sibling elements until next header
                for sibling in header.find_next_siblings():
                    if sibling.name in ["h2", "h3", "h4"]:
                        break
                    if sibling.name in ["table", "ul", "ol"]:
                        # Already handled tables above
                        # Handle lists
                        for li in sibling.find_all("li"):
                            text = li.get_text()
                            for sep in [" - ", " – ", " = ", ": "]:
                                if sep in text:
                                    parts = text.split(sep, 1)
                                    if len(parts) == 2:
                                        word = self.clean_text(parts[0])
                                        translation = self.clean_text(parts[1])
                                        if word and translation:
                                            entry = LanguageEntry(
                                                word=word,
                                                translations=[self.create_translation(translation)],
                                                metadata=metadata,
                                            )
                                            entries.append(entry)
                                    break

        return entries
