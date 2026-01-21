"""Cross-Polynesian cognate finder."""

from dataclasses import dataclass
from typing import Optional

from ..base import LLMMessage, LLMProvider, LLMResponse


@dataclass
class Cognate:
    """A cognate word in another Polynesian language."""

    language: str
    iso_code: str
    word: str
    meaning: str
    similarity_score: float
    sound_correspondences: list[str]


@dataclass
class CognateSet:
    """Set of cognates across Polynesian languages for a word."""

    rapa_nui_word: str
    proto_polynesian: Optional[str]
    cognates: list[Cognate]
    confidence: float
    semantic_field: str
    llm_analysis: Optional[str] = None


@dataclass
class PolynesianWord:
    """A word from a Polynesian language."""

    language: str
    iso_code: str
    word: str
    meanings: list[str]
    part_of_speech: Optional[str] = None


class CognateFinder:
    """
    Finds cognates across Polynesian languages.

    Uses sound correspondence patterns and semantic similarity
    to identify related words across the Polynesian family.
    """

    # Regular sound correspondences in Polynesian
    SOUND_CORRESPONDENCES = {
        # Proto-Polynesian -> Rapa Nui, Maori, Hawaiian, Tahitian
        "*t": {"rap": "t", "mri": "t", "haw": "k", "tah": "t"},
        "*k": {"rap": "ʔ", "mri": "k", "haw": "ʔ", "tah": "ʔ"},
        "*ng": {"rap": "ng", "mri": "ng", "haw": "n", "tah": "n"},
        "*r": {"rap": "r", "mri": "r", "haw": "l", "tah": "r"},
        "*l": {"rap": "r", "mri": "r", "haw": "l", "tah": "r"},
        "*s": {"rap": "h", "mri": "h", "haw": "h", "tah": "h"},
        "*f": {"rap": "h", "mri": "wh", "haw": "h", "tah": "f"},
        "*w": {"rap": "v", "mri": "w", "haw": "w", "tah": "v"},
    }

    SYSTEM_PROMPT = """You are an expert in Polynesian comparative linguistics,
specializing in identifying cognate relationships across the language family.

Polynesian languages share a common ancestor (Proto-Polynesian) and exhibit
regular sound correspondences:
- Hawaiian /k/ often corresponds to /t/ in other Polynesian languages
- Hawaiian /l/ corresponds to /r/ in most others
- Glottal stop (ʔ) often comes from Proto-Polynesian *k
- /h/ often comes from Proto-Polynesian *s or *f

When analyzing potential cognates:
1. Check for regular sound correspondences
2. Compare semantic fields (meanings may have shifted)
3. Consider morphological structure (prefixes, reduplication)
4. Note any irregular correspondences that might indicate borrowing

Common shared vocabulary includes:
- Body parts (mata 'eye', rima 'hand/five')
- Nature (moana 'ocean', maunga 'mountain')
- Basic verbs (kai 'eat', haere 'go')
- Numbers (tahi, rua, toru...)"""

    def __init__(self, llm_provider: Optional[LLMProvider] = None):
        """
        Initialize the cognate finder.

        Args:
            llm_provider: Optional LLM for cognate analysis
        """
        self.llm = llm_provider

    def calculate_phonetic_similarity(
        self,
        word1: str,
        word2: str,
        lang1_code: str,
        lang2_code: str,
    ) -> tuple[float, list[str]]:
        """
        Calculate phonetic similarity accounting for sound correspondences.

        Args:
            word1: First word
            word2: Second word
            lang1_code: ISO code for first language
            lang2_code: ISO code for second language

        Returns:
            (similarity score, list of correspondence descriptions)
        """
        # Normalize words
        w1 = word1.lower().strip()
        w2 = word2.lower().strip()

        # Simple length-normalized edit distance as baseline
        max_len = max(len(w1), len(w2))
        if max_len == 0:
            return 1.0, []

        # Calculate edit distance
        distance = self._edit_distance(w1, w2)
        base_similarity = 1.0 - (distance / max_len)

        # Check for known correspondences
        correspondences = []
        bonus = 0.0

        # Check each known correspondence
        for proto, reflexes in self.SOUND_CORRESPONDENCES.items():
            reflex1 = reflexes.get(lang1_code, "")
            reflex2 = reflexes.get(lang2_code, "")

            if reflex1 and reflex2 and reflex1 != reflex2:
                # Check if this correspondence appears in the words
                if reflex1 in w1 and reflex2 in w2:
                    correspondences.append(f"{reflex1} ({lang1_code}) ~ {reflex2} ({lang2_code}) from {proto}")
                    bonus += 0.1

        # Boost similarity for regular correspondences
        adjusted_similarity = min(1.0, base_similarity + bonus)

        return adjusted_similarity, correspondences

    def _edit_distance(self, s1: str, s2: str) -> int:
        """Calculate Levenshtein edit distance."""
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1],
                    )

        return dp[m][n]

    def find_cognates(
        self,
        target_word: str,
        target_meaning: str,
        polynesian_lexicons: dict[str, list[PolynesianWord]],
        similarity_threshold: float = 0.5,
    ) -> CognateSet:
        """
        Find cognates for a Rapa Nui word across Polynesian languages.

        Args:
            target_word: Rapa Nui word to find cognates for
            target_meaning: Meaning of the target word
            polynesian_lexicons: Map of language code to word lists
            similarity_threshold: Minimum similarity to consider

        Returns:
            CognateSet with discovered cognates
        """
        cognates = []

        for lang_code, words in polynesian_lexicons.items():
            best_match = None
            best_score = 0.0
            best_correspondences = []

            for word_entry in words:
                # Check phonetic similarity
                score, correspondences = self.calculate_phonetic_similarity(
                    target_word, word_entry.word, "rap", lang_code
                )

                # Boost for semantic similarity
                if self._meanings_overlap(target_meaning, word_entry.meanings):
                    score = min(1.0, score + 0.2)

                if score > best_score and score >= similarity_threshold:
                    best_score = score
                    best_match = word_entry
                    best_correspondences = correspondences

            if best_match:
                cognates.append(
                    Cognate(
                        language=best_match.language,
                        iso_code=lang_code,
                        word=best_match.word,
                        meaning="; ".join(best_match.meanings),
                        similarity_score=best_score,
                        sound_correspondences=best_correspondences,
                    )
                )

        # Calculate overall confidence
        avg_similarity = (
            sum(c.similarity_score for c in cognates) / len(cognates)
            if cognates
            else 0.0
        )
        coverage = len(cognates) / max(len(polynesian_lexicons), 1)
        confidence = (avg_similarity + coverage) / 2

        return CognateSet(
            rapa_nui_word=target_word,
            proto_polynesian=None,  # Will be filled by etymology verifier
            cognates=cognates,
            confidence=confidence,
            semantic_field=self._infer_semantic_field(target_meaning),
        )

    def _meanings_overlap(self, meaning1: str, meanings2: list[str]) -> bool:
        """Check if meanings have semantic overlap."""
        m1_words = set(meaning1.lower().split())
        for m2 in meanings2:
            m2_words = set(m2.lower().split())
            if m1_words & m2_words:
                return True
        return False

    def _infer_semantic_field(self, meaning: str) -> str:
        """Infer semantic field from meaning."""
        meaning_lower = meaning.lower()

        fields = {
            "body": ["eye", "hand", "head", "foot", "mouth", "ear", "nose"],
            "nature": ["ocean", "sea", "mountain", "tree", "sun", "moon", "star"],
            "animals": ["bird", "fish", "turtle", "dog", "rat"],
            "numbers": ["one", "two", "three", "four", "five", "1", "2", "3"],
            "kinship": ["father", "mother", "child", "brother", "sister"],
            "actions": ["eat", "go", "come", "see", "hear", "speak"],
        }

        for field, keywords in fields.items():
            if any(kw in meaning_lower for kw in keywords):
                return field

        return "general"

    def analyze_cognate_set(
        self,
        cognate_set: CognateSet,
    ) -> CognateSet:
        """
        Use LLM to analyze cognate set and reconstruct proto-form.

        Args:
            cognate_set: Cognate set to analyze

        Returns:
            Cognate set with LLM analysis
        """
        if not self.llm or not cognate_set.cognates:
            return cognate_set

        cognate_list = "\n".join(
            f"- {c.language} ({c.iso_code}): {c.word} '{c.meaning}' "
            f"(similarity: {c.similarity_score:.2f})"
            for c in cognate_set.cognates
        )

        user_prompt = f"""Analyze this potential cognate set:

Rapa Nui: {cognate_set.rapa_nui_word}
Semantic field: {cognate_set.semantic_field}

Proposed cognates:
{cognate_list}

Provide analysis in JSON:
{{
    "is_valid_cognate_set": true|false,
    "proto_polynesian_reconstruction": "*form or null",
    "analysis": "explanation of sound correspondences and semantic connections",
    "confidence_adjustment": -0.2 to 0.2,
    "notes": "any caveats or observations"
}}"""

        messages = [
            LLMMessage(role="system", content=self.SYSTEM_PROMPT),
            LLMMessage(role="user", content=user_prompt),
        ]

        response = self.llm.complete(messages, max_tokens=600, temperature=0.1)

        return self._apply_analysis(cognate_set, response)

    def _apply_analysis(
        self, cognate_set: CognateSet, response: LLMResponse
    ) -> CognateSet:
        """Apply LLM analysis to cognate set."""
        import json

        try:
            content = response.content.strip()
            if content.startswith("```"):
                lines = content.split("\n")
                content = "\n".join(lines[1:-1])

            data = json.loads(content)

            cognate_set.proto_polynesian = data.get("proto_polynesian_reconstruction")
            cognate_set.llm_analysis = data.get("analysis")

            # Adjust confidence
            adjustment = data.get("confidence_adjustment", 0)
            cognate_set.confidence = max(0, min(1, cognate_set.confidence + adjustment))

        except (json.JSONDecodeError, KeyError):
            pass

        return cognate_set
