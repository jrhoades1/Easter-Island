"""Lexical Validation Agent - Validate cross-references against Polynesian corpora."""

import json
from pathlib import Path
from typing import Optional

from ..base import BaseAgent, LLMCache, LLMProvider
from .cognate_finder import CognateFinder, PolynesianWord
from .etymology_verifier import EtymologyVerifier


class LexicalValidationAgent(BaseAgent):
    """
    Lexical validation agent for Rongorongo cross-references.

    Validates proposed glyph-word associations by:
    - Finding cognates across Polynesian languages
    - Verifying Proto-Polynesian etymologies
    - Adjusting confidence based on linguistic evidence
    """

    AGENT_NAME = "lexical_validation"
    VERSION = "1.0.0"

    def __init__(
        self,
        llm_provider: LLMProvider,
        cache: Optional[LLMCache] = None,
    ):
        """
        Initialize the lexical validation agent.

        Args:
            llm_provider: LLM provider for linguistic analysis
            cache: Optional response cache
        """
        super().__init__(llm_provider, cache)
        self.cognate_finder = CognateFinder(llm_provider)
        self.etymology_verifier = EtymologyVerifier(llm_provider)

    def get_input_schema(self) -> dict:
        """Get input schema for lexical validation agent."""
        return {
            "type": "object",
            "required": ["cross_references"],
            "properties": {
                "cross_references": {
                    "type": "object",
                    "description": "Cross-reference lexicon from cross_referencer",
                    "properties": {
                        "cross_references": {"type": "array"},
                        "glyph_profiles": {"type": "array"},
                    },
                },
                "polynesian_corpora": {
                    "type": "object",
                    "description": "Lexicons from Polynesian languages",
                    "properties": {
                        "maori": {"type": "array"},
                        "hawaiian": {"type": "array"},
                        "tahitian": {"type": "array"},
                    },
                },
                "rapa_nui_lexicon": {
                    "type": "object",
                    "description": "Rapa Nui language lexicon",
                },
                "min_cognate_languages": {
                    "type": "integer",
                    "default": 2,
                    "description": "Minimum languages with cognates for validation",
                },
                "confidence_boost": {
                    "type": "number",
                    "default": 0.15,
                    "description": "Confidence boost for validated references",
                },
            },
        }

    def get_output_schema(self) -> dict:
        """Get output schema for lexical validation agent."""
        return {
            "type": "object",
            "properties": {
                "run_metadata": {"type": "object"},
                "validated_references": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "reference_id": {"type": "string"},
                            "original_confidence": {"type": "number"},
                            "validated_confidence": {"type": "number"},
                            "cognate_evidence": {"type": "array"},
                            "proto_polynesian": {"type": "string"},
                        },
                    },
                },
                "new_candidates": {"type": "array"},
                "statistics": {"type": "object"},
            },
        }

    def run(self, input_data: dict) -> dict:
        """
        Execute lexical validation.

        Args:
            input_data: Contains cross_references, polynesian_corpora

        Returns:
            Validated cross-references with cognate evidence
        """
        cross_refs = input_data["cross_references"]
        polynesian_corpora = input_data.get("polynesian_corpora", {})
        rapa_nui_lexicon = input_data.get("rapa_nui_lexicon", {})
        min_cognates = input_data.get("min_cognate_languages", 2)
        conf_boost = input_data.get("confidence_boost", 0.15)

        # Convert corpora to PolynesianWord objects
        poly_lexicons = self._prepare_lexicons(polynesian_corpora)

        # Validate each cross-reference
        validated_refs = []
        references = cross_refs.get("cross_references", [])

        for ref in references:
            validated = self._validate_reference(
                ref, poly_lexicons, min_cognates, conf_boost
            )
            validated_refs.append(validated)

        # Find new candidates
        new_candidates = self._find_new_candidates(
            cross_refs.get("glyph_profiles", []),
            rapa_nui_lexicon,
            poly_lexicons,
        )

        # Compile statistics
        statistics = self._compile_statistics(validated_refs, new_candidates)

        return {
            "validated_references": validated_refs,
            "new_candidates": new_candidates,
            "statistics": statistics,
        }

    def _prepare_lexicons(
        self,
        corpora: dict,
    ) -> dict[str, list[PolynesianWord]]:
        """Convert raw corpora to PolynesianWord objects."""
        lexicons = {}

        lang_info = {
            "maori": ("Maori", "mri"),
            "hawaiian": ("Hawaiian", "haw"),
            "tahitian": ("Tahitian", "tah"),
        }

        for lang_key, entries in corpora.items():
            if lang_key in lang_info:
                lang_name, iso_code = lang_info[lang_key]
                words = []

                for entry in entries:
                    if isinstance(entry, dict):
                        word = entry.get("word", "")
                        meanings = entry.get("meanings", [])
                        if isinstance(meanings, str):
                            meanings = [meanings]

                        # Also check for translations
                        translations = entry.get("translations", [])
                        for t in translations:
                            if isinstance(t, dict) and "text" in t:
                                meanings.append(t["text"])
                            elif isinstance(t, str):
                                meanings.append(t)

                        if word and meanings:
                            words.append(
                                PolynesianWord(
                                    language=lang_name,
                                    iso_code=iso_code,
                                    word=word,
                                    meanings=meanings,
                                    part_of_speech=entry.get("part_of_speech"),
                                )
                            )

                lexicons[iso_code] = words

        return lexicons

    def _validate_reference(
        self,
        ref: dict,
        poly_lexicons: dict[str, list[PolynesianWord]],
        min_cognates: int,
        conf_boost: float,
    ) -> dict:
        """Validate a single cross-reference."""
        ref_id = ref.get("reference_id", "")
        word = ref.get("language_entry_word", "")
        original_conf = ref.get("overall_confidence", 0.0)
        semantic_domain = ref.get("semantic_domain", "unknown")
        existing_proto = ref.get("proto_polynesian_root")

        # Find cognates
        cognate_set = self.cognate_finder.find_cognates(
            target_word=word,
            target_meaning=semantic_domain,
            polynesian_lexicons=poly_lexicons,
        )

        # Analyze with LLM
        cognate_set = self.cognate_finder.analyze_cognate_set(cognate_set)

        # Verify etymology if we have a proto-form
        proto_form = cognate_set.proto_polynesian or existing_proto
        etymology_verification = None

        if proto_form:
            reflexes = {c.iso_code: c.word for c in cognate_set.cognates}
            etymology_verification = self.etymology_verifier.verify_etymology(
                word=word,
                proposed_proto_form=proto_form,
                reflexes=reflexes,
                proposed_meaning=semantic_domain,
            )

            if self.llm:
                etymology_verification = self.etymology_verifier.verify_with_llm(
                    etymology_verification
                )

        # Calculate validated confidence
        validated_conf = original_conf

        # Boost for cognate evidence
        if len(cognate_set.cognates) >= min_cognates:
            validated_conf += conf_boost * cognate_set.confidence

        # Boost/penalty for etymology verification
        if etymology_verification:
            if etymology_verification.is_valid:
                validated_conf += 0.1 * etymology_verification.confidence
            else:
                validated_conf -= 0.05

        validated_conf = max(0.0, min(1.0, validated_conf))

        return {
            "reference_id": ref_id,
            "glyph_cluster_id": ref.get("glyph_cluster_id"),
            "language_entry_word": word,
            "original_confidence": original_conf,
            "validated_confidence": validated_conf,
            "confidence_change": validated_conf - original_conf,
            "cognate_evidence": [
                {
                    "language": c.language,
                    "word": c.word,
                    "meaning": c.meaning,
                    "similarity": c.similarity_score,
                }
                for c in cognate_set.cognates
            ],
            "proto_polynesian": cognate_set.proto_polynesian or existing_proto,
            "semantic_field": cognate_set.semantic_field,
            "etymology_verified": (
                etymology_verification.is_valid if etymology_verification else None
            ),
            "llm_analysis": cognate_set.llm_analysis,
        }

    def _find_new_candidates(
        self,
        glyph_profiles: list[dict],
        rapa_nui_lexicon: dict,
        poly_lexicons: dict[str, list[PolynesianWord]],
    ) -> list[dict]:
        """Find new candidate cross-references based on cognate analysis."""
        candidates = []

        # Get existing associations
        existing_words = set()
        for profile in glyph_profiles:
            for xref_id in profile.get("cross_reference_ids", []):
                # Would need to look up the word, simplified here
                pass

        # Look for Rapa Nui words with strong cognate support
        rn_entries = rapa_nui_lexicon.get("entries", [])

        for entry in rn_entries[:20]:  # Limit for performance
            word = entry.get("word", "")
            if word in existing_words:
                continue

            # Get meanings
            meanings = []
            for t in entry.get("translations", []):
                if isinstance(t, dict):
                    meanings.append(t.get("text", ""))
                elif isinstance(t, str):
                    meanings.append(t)

            if not meanings:
                continue

            meaning = meanings[0]

            # Find cognates
            cognate_set = self.cognate_finder.find_cognates(
                target_word=word,
                target_meaning=meaning,
                polynesian_lexicons=poly_lexicons,
            )

            # High cognate confidence suggests good candidate
            if cognate_set.confidence > 0.6 and len(cognate_set.cognates) >= 2:
                candidates.append({
                    "word": word,
                    "meaning": meaning,
                    "cognate_count": len(cognate_set.cognates),
                    "cognate_confidence": cognate_set.confidence,
                    "semantic_field": cognate_set.semantic_field,
                    "proto_polynesian": cognate_set.proto_polynesian,
                    "suggested_shape_categories": self._suggest_categories(
                        cognate_set.semantic_field
                    ),
                })

        return candidates[:10]  # Return top 10 candidates

    def _suggest_categories(self, semantic_field: str) -> list[str]:
        """Suggest glyph shape categories for a semantic field."""
        field_to_categories = {
            "animals": ["avian", "ichthyomorphic"],
            "body": ["anthropomorphic"],
            "nature": ["phytomorphic", "geometric"],
            "numbers": ["geometric"],
            "kinship": ["anthropomorphic"],
            "actions": ["anthropomorphic", "composite"],
        }
        return field_to_categories.get(semantic_field, ["undetermined"])

    def _compile_statistics(
        self,
        validated: list[dict],
        candidates: list[dict],
    ) -> dict:
        """Compile validation statistics."""
        confidence_changes = [v["confidence_change"] for v in validated]
        avg_change = sum(confidence_changes) / len(confidence_changes) if confidence_changes else 0

        improved = sum(1 for c in confidence_changes if c > 0)
        decreased = sum(1 for c in confidence_changes if c < 0)
        unchanged = len(confidence_changes) - improved - decreased

        cognate_counts = [len(v["cognate_evidence"]) for v in validated]
        avg_cognates = sum(cognate_counts) / len(cognate_counts) if cognate_counts else 0

        verified_count = sum(
            1 for v in validated if v.get("etymology_verified") is True
        )

        return {
            "total_validated": len(validated),
            "confidence_improved": improved,
            "confidence_decreased": decreased,
            "confidence_unchanged": unchanged,
            "average_confidence_change": avg_change,
            "average_cognates_found": avg_cognates,
            "etymologies_verified": verified_count,
            "new_candidates_found": len(candidates),
        }


def save_results(results: dict, output_path: str) -> None:
    """Save validation results to JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
