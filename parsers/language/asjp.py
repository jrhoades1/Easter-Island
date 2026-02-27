"""Parser for ASJP (Automated Similarity Judgment Program) database."""

from models.language import Etymology, LanguageEntry

from .base import BaseLanguageParser


class ASJPParser(BaseLanguageParser):
    """Parser for ASJP database wordlists."""

    source_name = "ASJP Database"
    source_url_pattern = "asjp.clld.org"

    def can_parse(self, url: str) -> bool:
        """Check if this parser can handle the given URL."""
        return "asjp.clld.org" in url

    def parse(self, html: str, url: str) -> list[LanguageEntry]:
        """Parse ASJP wordlist page and return language entries."""
        soup = self.get_soup(html)
        entries = []
        metadata = self.create_metadata(url, confidence="high")

        # Find the wordlist table
        table = soup.find("table", class_="table")
        if not table:
            return entries

        rows = table.find_all("tr")
        for row in rows[1:]:  # Skip header row
            cols = row.find_all("td")
            if len(cols) < 4:
                continue

            # ASJP table structure:
            # col 0: ID, col 1: Parameter (meaning), col 2: Segments, col 3: Form (word)
            meaning = self.clean_text(cols[1].get_text())
            word = self.clean_text(cols[3].get_text())

            if not word or not meaning:
                continue

            # Check for loan word indicator (if present)
            is_loan = False
            if len(cols) > 4:
                loan_text = cols[4].get_text(strip=True).lower()
                is_loan = loan_text in ("true", "yes", "1")

            # Create entry
            entry = LanguageEntry(
                word=word,
                translations=[self.create_translation(meaning)],
                etymology=Etymology(loan=is_loan) if is_loan else None,
                metadata=metadata,
            )
            entries.append(entry)

        return entries
