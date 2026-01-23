"""Historical validator for cross-references against known Rapa Nui context."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from ..base import LLMMessage, LLMProvider


class InconsistencyType(Enum):
    """Types of historical inconsistencies."""
    TEMPORAL = "temporal"  # Conflicts with known chronology
    CULTURAL = "cultural"  # Conflicts with cultural practices
    LINGUISTIC = "linguistic"  # Conflicts with sound change patterns
    SEMANTIC = "semantic"  # Meaning doesn't fit context
    ARCHAEOLOGICAL = "archaeological"  # Conflicts with material evidence


@dataclass
class HistoricalContext:
    """Known historical context for validation."""

    # Known text types (partial claims from Rongorongo scholarship)
    KNOWN_TEXT_TYPES = {
        "calendar": {
            "description": "Lunar/seasonal calendrical texts",
            "expected_domains": ["time", "nature", "agriculture"],
            "expected_patterns": ["repetitive sequences", "numerical markers"],
            "sources": ["Barthel 1958", "Fischer 1997"],
        },
        "genealogical": {
            "description": "Lists of names/lineages",
            "expected_domains": ["kinship", "social", "body"],
            "expected_patterns": ["list structures", "repetitive openings"],
            "sources": ["Routledge 1919", "Métraux 1940"],
        },
        "chant": {
            "description": "Ritual or ceremonial chants",
            "expected_domains": ["culture", "nature", "action"],
            "expected_patterns": ["formulaic phrases", "parallelism"],
            "sources": ["Englert 1948"],
        },
        "inventory": {
            "description": "Lists of items or tributes",
            "expected_domains": ["quantity", "food", "possession"],
            "expected_patterns": ["enumerations", "category markers"],
            "sources": ["Barthel 1958"],
        },
    }

    # Known historical facts about Rapa Nui
    CULTURAL_FACTS = {
        "manu": "Bird cult (tangata manu) was important after ~1500 CE",
        "moai": "Moai construction peaked ~1250-1500 CE",
        "rongorongo": "Script likely developed after European contact (~1770) or just before",
        "makemake": "Creator deity, central to bird cult",
        "ariki": "Paramount chief, holder of sacred power (mana)",
        "toromiro": "Endemic tree, culturally significant, used for rongorongo tablets",
    }

    # Proto-Polynesian reflexes expected in Rapa Nui
    EXPECTED_SOUND_CHANGES = {
        "*t": "t",  # Proto-Polynesian *t > Rapa Nui t
        "*k": "ʔ",  # Proto-Polynesian *k > Rapa Nui glottal stop
        "*ng": "ng",  # Proto-Polynesian *ng > Rapa Nui ng
        "*f": "h",  # Proto-Polynesian *f > Rapa Nui h
        "*s": "h",  # Proto-Polynesian *s > Rapa Nui h
        "*w": "v",  # Proto-Polynesian *w > Rapa Nui v
    }


@dataclass
class Inconsistency:
    """A flagged inconsistency in a cross-reference."""

    reference_id: str
    inconsistency_type: InconsistencyType
    severity: str  # "minor", "moderate", "major"
    description: str
    evidence: str
    suggested_resolution: Optional[str] = None
    confidence: float = 0.0


@dataclass
class HistoricalValidationResult:
    """Result of historical validation."""

    reference_id: str
    is_consistent: bool
    consistency_score: float  # 0.0 to 1.0
    inconsistencies: list[Inconsistency] = field(default_factory=list)
    supporting_evidence: list[str] = field(default_factory=list)
    text_type_match: Optional[str] = None
    llm_analysis: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "reference_id": self.reference_id,
            "is_consistent": self.is_consistent,
            "consistency_score": self.consistency_score,
            "inconsistencies": [
                {
                    "type": i.inconsistency_type.value,
                    "severity": i.severity,
                    "description": i.description,
                    "evidence": i.evidence,
                    "suggested_resolution": i.suggested_resolution,
                    "confidence": i.confidence,
                }
                for i in self.inconsistencies
            ],
            "supporting_evidence": self.supporting_evidence,
            "text_type_match": self.text_type_match,
            "llm_analysis": self.llm_analysis,
        }


class HistoricalValidator:
    """Validates cross-references against known Rapa Nui historical context."""

    def __init__(self, llm_provider: Optional[LLMProvider] = None):
        """
        Initialize the historical validator.

        Args:
            llm_provider: Optional LLM for advanced analysis
        """
        self.llm = llm_provider
        self.context = HistoricalContext()

    def validate(
        self,
        reference: dict,
        glyph_profile: Optional[dict] = None,
        tablet_context: Optional[dict] = None,
    ) -> HistoricalValidationResult:
        """
        Validate a cross-reference against historical context.

        Args:
            reference: Cross-reference to validate
            glyph_profile: Optional glyph shape/position data
            tablet_context: Optional tablet-level context

        Returns:
            Validation result with inconsistencies flagged
        """
        ref_id = reference.get("reference_id", "unknown")
        word = reference.get("language_entry_word", "")
        semantic_domain = reference.get("semantic_domain", "")
        proto_root = reference.get("proto_polynesian_root", "")

        inconsistencies = []
        supporting = []
        text_type = None

        # Check semantic domain against known text types
        for type_name, type_info in HistoricalContext.KNOWN_TEXT_TYPES.items():
            if semantic_domain in type_info["expected_domains"]:
                text_type = type_name
                supporting.append(
                    f"Semantic domain '{semantic_domain}' matches {type_name} text type"
                )
                break

        # Check for cultural consistency
        cultural_check = self._check_cultural_consistency(word, semantic_domain)
        if cultural_check:
            if cultural_check["is_consistent"]:
                supporting.append(cultural_check["evidence"])
            else:
                inconsistencies.append(Inconsistency(
                    reference_id=ref_id,
                    inconsistency_type=InconsistencyType.CULTURAL,
                    severity=cultural_check.get("severity", "moderate"),
                    description=cultural_check["description"],
                    evidence=cultural_check["evidence"],
                    confidence=0.7,
                ))

        # Check linguistic consistency (sound changes)
        if proto_root:
            ling_check = self._check_linguistic_consistency(word, proto_root)
            if ling_check:
                if ling_check["is_consistent"]:
                    supporting.append(ling_check["evidence"])
                else:
                    inconsistencies.append(Inconsistency(
                        reference_id=ref_id,
                        inconsistency_type=InconsistencyType.LINGUISTIC,
                        severity="moderate",
                        description=ling_check["description"],
                        evidence=ling_check["evidence"],
                        suggested_resolution=ling_check.get("suggestion"),
                        confidence=0.8,
                    ))

        # Check positional patterns if glyph profile available
        if glyph_profile:
            pattern_check = self._check_positional_patterns(
                glyph_profile, semantic_domain, text_type
            )
            if pattern_check and not pattern_check["is_consistent"]:
                inconsistencies.append(Inconsistency(
                    reference_id=ref_id,
                    inconsistency_type=InconsistencyType.SEMANTIC,
                    severity="minor",
                    description=pattern_check["description"],
                    evidence=pattern_check["evidence"],
                    confidence=0.5,
                ))

        # Calculate consistency score
        if inconsistencies:
            severity_weights = {"minor": 0.1, "moderate": 0.3, "major": 0.75}
            penalty = sum(
                severity_weights.get(i.severity, 0.2) * i.confidence
                for i in inconsistencies
            )
            consistency_score = max(0.0, 1.0 - penalty)
        else:
            consistency_score = 1.0

        # Boost for supporting evidence (but not enough to overcome major issues)
        if not any(i.severity == "major" for i in inconsistencies):
            consistency_score = min(1.0, consistency_score + 0.1 * len(supporting))

        is_consistent = consistency_score >= 0.5 and not any(
            i.severity == "major" for i in inconsistencies
        )

        result = HistoricalValidationResult(
            reference_id=ref_id,
            is_consistent=is_consistent,
            consistency_score=consistency_score,
            inconsistencies=inconsistencies,
            supporting_evidence=supporting,
            text_type_match=text_type,
        )

        # LLM analysis if available
        if self.llm and (inconsistencies or not is_consistent):
            result = self._analyze_with_llm(result, reference)

        return result

    def _check_cultural_consistency(
        self, word: str, semantic_domain: str
    ) -> Optional[dict]:
        """Check if word/domain is culturally consistent."""
        word_lower = word.lower()

        # Check known cultural terms
        for term, context in HistoricalContext.CULTURAL_FACTS.items():
            if term in word_lower:
                return {
                    "is_consistent": True,
                    "evidence": f"'{word}' relates to known cultural concept: {context}",
                }

        # Check for anachronistic terms
        anachronisms = {
            "metal", "iron", "horse", "wheat", "cow", "sheep",
            "european", "spanish", "christian",
        }
        for term in anachronisms:
            if term in word_lower or term in semantic_domain.lower():
                return {
                    "is_consistent": False,
                    "severity": "major",
                    "description": f"Anachronistic term detected: {term}",
                    "evidence": "These concepts were introduced after European contact (1722)",
                }

        return None

    def _check_linguistic_consistency(
        self, word: str, proto_root: str
    ) -> Optional[dict]:
        """Check if word follows expected sound correspondences."""
        # Extract proto form
        proto_clean = proto_root.replace("*", "").split()[0].lower()
        word_lower = word.lower()

        # Check for expected reflexes
        issues = []

        # *k > ʔ in Rapa Nui
        if "k" in proto_clean and "k" in word_lower:
            issues.append("Expected *k > ʔ (glottal stop), but 'k' retained")

        # *ng should be preserved
        if "ng" in proto_clean and "ng" not in word_lower and "n" not in word_lower:
            issues.append("Expected *ng reflex not found")

        if issues:
            return {
                "is_consistent": False,
                "description": "; ".join(issues),
                "evidence": f"Proto form {proto_root} vs Rapa Nui '{word}'",
                "suggestion": "Verify sound correspondences with Polynesian comparative data",
            }

        return {
            "is_consistent": True,
            "evidence": f"Sound correspondences appear regular for {proto_root}",
        }

    def _check_positional_patterns(
        self,
        glyph_profile: dict,
        semantic_domain: str,
        text_type: Optional[str],
    ) -> Optional[dict]:
        """Check if glyph position matches expected patterns."""
        if not text_type:
            return None

        type_info = HistoricalContext.KNOWN_TEXT_TYPES.get(text_type, {})
        expected_patterns = type_info.get("expected_patterns", [])

        # Check position data
        positions = glyph_profile.get("positions", {})
        avg_position = positions.get("avg_position_in_line", 0.5)

        # Calendar texts often have markers at line beginnings
        if text_type == "calendar" and "time" in semantic_domain:
            if avg_position > 0.7:
                return {
                    "is_consistent": False,
                    "description": "Calendar markers typically appear line-initial",
                    "evidence": f"Average position {avg_position:.2f} suggests line-final",
                }

        # Genealogical texts have repetitive openings
        if text_type == "genealogical" and "kinship" in semantic_domain:
            line_dist = positions.get("line_distribution", {})
            if len(line_dist) < 3:
                return {
                    "is_consistent": False,
                    "description": "Kinship terms expected across multiple lines",
                    "evidence": f"Only found in {len(line_dist)} lines",
                }

        return None

    def _analyze_with_llm(
        self,
        result: HistoricalValidationResult,
        reference: dict,
    ) -> HistoricalValidationResult:
        """Use LLM to analyze inconsistencies."""
        inconsistency_text = "\n".join(
            f"- {i.inconsistency_type.value}: {i.description}"
            for i in result.inconsistencies
        )

        prompt = f"""Analyze this Rongorongo cross-reference for historical consistency.

Reference:
- Word: {reference.get('language_entry_word', 'unknown')}
- Semantic domain: {reference.get('semantic_domain', 'unknown')}
- Proto-Polynesian: {reference.get('proto_polynesian_root', 'unknown')}
- Confidence: {reference.get('overall_confidence', 0)}

Flagged inconsistencies:
{inconsistency_text if inconsistency_text else "None"}

Supporting evidence:
{chr(10).join('- ' + e for e in result.supporting_evidence) if result.supporting_evidence else "None"}

Consider:
1. Is this association plausible given Rapa Nui cultural context?
2. Are there alternative interpretations that resolve inconsistencies?
3. What additional evidence would strengthen or weaken this association?

Provide a brief analysis (2-3 sentences) and rate confidence (low/medium/high)."""

        messages = [
            LLMMessage(
                role="system",
                content="You are an expert in Polynesian linguistics and Rapa Nui cultural history. "
                "Analyze cross-references critically but fairly. Rongorongo is undeciphered, "
                "so all associations are speculative.",
            ),
            LLMMessage(role="user", content=prompt),
        ]

        response = self.llm.complete(messages)
        result.llm_analysis = response.content

        return result

    def validate_batch(
        self,
        references: list[dict],
        glyph_profiles: Optional[dict] = None,
    ) -> list[HistoricalValidationResult]:
        """
        Validate a batch of cross-references.

        Args:
            references: List of cross-references
            glyph_profiles: Optional dict mapping cluster_id to profile

        Returns:
            List of validation results
        """
        results = []
        profiles = glyph_profiles or {}

        for ref in references:
            cluster_id = ref.get("glyph_cluster_id", "")
            profile = profiles.get(cluster_id)
            result = self.validate(ref, profile)
            results.append(result)

        return results

    def generate_report(
        self,
        results: list[HistoricalValidationResult],
    ) -> str:
        """Generate a human-readable validation report."""
        report = ["# Historical Validation Report\n"]

        # Summary
        consistent = sum(1 for r in results if r.is_consistent)
        total = len(results)
        avg_score = sum(r.consistency_score for r in results) / total if total else 0

        report.append(f"## Summary\n")
        report.append(f"- Total references: {total}")
        report.append(f"- Consistent: {consistent} ({100*consistent/total:.1f}%)")
        report.append(f"- Average consistency score: {avg_score:.2f}\n")

        # Inconsistencies by type
        all_inconsistencies = [i for r in results for i in r.inconsistencies]
        by_type = {}
        for i in all_inconsistencies:
            by_type.setdefault(i.inconsistency_type.value, []).append(i)

        if by_type:
            report.append("## Inconsistencies by Type\n")
            for type_name, items in sorted(by_type.items()):
                report.append(f"### {type_name.title()} ({len(items)})\n")
                for item in items[:5]:  # Show top 5
                    report.append(f"- **{item.reference_id}**: {item.description}")
                if len(items) > 5:
                    report.append(f"- ... and {len(items) - 5} more\n")

        # Text type matches
        text_types = {}
        for r in results:
            if r.text_type_match:
                text_types.setdefault(r.text_type_match, []).append(r.reference_id)

        if text_types:
            report.append("\n## Text Type Classifications\n")
            for type_name, refs in sorted(text_types.items()):
                report.append(f"- **{type_name}**: {len(refs)} references")

        return "\n".join(report)
