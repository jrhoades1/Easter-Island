"""Proto-Polynesian etymology verification."""

from dataclasses import dataclass
from typing import Optional

from ..base import LLMMessage, LLMProvider, LLMResponse


@dataclass
class EtymologyVerification:
    """Verification of a Proto-Polynesian etymology."""

    word: str
    proposed_proto_form: str
    is_valid: bool
    confidence: float
    sound_law_violations: list[str]
    semantic_plausibility: float
    attestation_count: int  # Number of daughter languages with reflexes
    reconstructed_meaning: Optional[str]
    scholarly_notes: Optional[str]


@dataclass
class ProtoPolynesianRoot:
    """A Proto-Polynesian reconstructed form."""

    proto_form: str
    meaning: str
    semantic_domain: str
    known_reflexes: dict[str, str]  # Language -> reflex
    confidence_level: str  # "secure", "probable", "tentative"


class EtymologyVerifier:
    """
    Verifies Proto-Polynesian etymologies.

    Checks proposed etymologies against known sound correspondences
    and Proto-Polynesian reconstructions.
    """

    # Known Proto-Polynesian reconstructions (sample)
    KNOWN_RECONSTRUCTIONS = {
        "*tangata": ProtoPolynesianRoot(
            proto_form="*tangata",
            meaning="person, human being",
            semantic_domain="kinship",
            known_reflexes={"rap": "tangata", "mri": "tangata", "haw": "kanaka", "tah": "taʔata"},
            confidence_level="secure",
        ),
        "*manu": ProtoPolynesianRoot(
            proto_form="*manu",
            meaning="bird",
            semantic_domain="animals",
            known_reflexes={"rap": "manu", "mri": "manu", "haw": "manu", "tah": "manu"},
            confidence_level="secure",
        ),
        "*ika": ProtoPolynesianRoot(
            proto_form="*ika",
            meaning="fish",
            semantic_domain="animals",
            known_reflexes={"rap": "ika", "mri": "ika", "haw": "iʔa", "tah": "iʔa"},
            confidence_level="secure",
        ),
        "*mata": ProtoPolynesianRoot(
            proto_form="*mata",
            meaning="eye, face",
            semantic_domain="body",
            known_reflexes={"rap": "mata", "mri": "mata", "haw": "maka", "tah": "mata"},
            confidence_level="secure",
        ),
        "*rima": ProtoPolynesianRoot(
            proto_form="*rima",
            meaning="hand, five",
            semantic_domain="body",
            known_reflexes={"rap": "rima", "mri": "rima", "haw": "lima", "tah": "rima"},
            confidence_level="secure",
        ),
        "*tahi": ProtoPolynesianRoot(
            proto_form="*tahi",
            meaning="one",
            semantic_domain="numbers",
            known_reflexes={"rap": "tahi", "mri": "tahi", "haw": "kahi", "tah": "tahi"},
            confidence_level="secure",
        ),
        "*rua": ProtoPolynesianRoot(
            proto_form="*rua",
            meaning="two",
            semantic_domain="numbers",
            known_reflexes={"rap": "rua", "mri": "rua", "haw": "lua", "tah": "rua"},
            confidence_level="secure",
        ),
        "*toru": ProtoPolynesianRoot(
            proto_form="*toru",
            meaning="three",
            semantic_domain="numbers",
            known_reflexes={"rap": "toru", "mri": "toru", "haw": "kolu", "tah": "toru"},
            confidence_level="secure",
        ),
        "*moana": ProtoPolynesianRoot(
            proto_form="*moana",
            meaning="ocean, deep sea",
            semantic_domain="nature",
            known_reflexes={"rap": "moana", "mri": "moana", "haw": "moana", "tah": "moana"},
            confidence_level="secure",
        ),
        "*rakau": ProtoPolynesianRoot(
            proto_form="*rakau",
            meaning="tree, wood",
            semantic_domain="nature",
            known_reflexes={"rap": "rakau", "mri": "rakau", "haw": "laʔau", "tah": "raʔau"},
            confidence_level="secure",
        ),
    }

    # Sound laws for Proto-Polynesian to daughter languages
    SOUND_LAWS = {
        "rap": {  # Rapa Nui
            "*t": "t",
            "*k": "ʔ",
            "*ng": "ng",
            "*r": "r",
            "*l": "r",
        },
        "mri": {  # Maori
            "*t": "t",
            "*k": "k",
            "*ng": "ng",
            "*r": "r",
            "*l": "r",
        },
        "haw": {  # Hawaiian
            "*t": "k",
            "*k": "ʔ",
            "*ng": "n",
            "*r": "l",
            "*l": "l",
        },
        "tah": {  # Tahitian
            "*t": "t",
            "*k": "ʔ",
            "*ng": "n",
            "*r": "r",
            "*l": "r",
        },
    }

    SYSTEM_PROMPT = """You are an expert in Polynesian historical linguistics,
specializing in Proto-Polynesian reconstruction and etymology verification.

When verifying an etymology:
1. Check if the proposed proto-form follows known sound correspondences
2. Verify semantic plausibility (meaning shifts should be reasonable)
3. Consider attestation across daughter languages
4. Note any irregular correspondences that might indicate borrowing

Standard Proto-Polynesian notation:
- Reconstructed forms are marked with *
- Glottal stop is written as ʔ
- Long vowels may be written doubled (aa) or with macron (ā)

Be conservative - only validate etymologies with strong evidence."""

    def __init__(self, llm_provider: Optional[LLMProvider] = None):
        """
        Initialize the etymology verifier.

        Args:
            llm_provider: Optional LLM for complex verification
        """
        self.llm = llm_provider

    def check_known_reconstruction(
        self,
        proto_form: str,
    ) -> Optional[ProtoPolynesianRoot]:
        """
        Check if proto-form matches a known reconstruction.

        Args:
            proto_form: Proto-Polynesian form to check

        Returns:
            ProtoPolynesianRoot if known, None otherwise
        """
        # Normalize form
        normalized = proto_form.strip().lower()
        if not normalized.startswith("*"):
            normalized = "*" + normalized

        return self.KNOWN_RECONSTRUCTIONS.get(normalized)

    def verify_sound_correspondences(
        self,
        proto_form: str,
        reflexes: dict[str, str],
    ) -> tuple[bool, list[str]]:
        """
        Verify that reflexes follow expected sound correspondences.

        Args:
            proto_form: Proto-Polynesian form
            reflexes: Map of language code to actual reflex

        Returns:
            (is_valid, list of violations)
        """
        violations = []

        # For each language, check if reflex matches expected
        for lang_code, reflex in reflexes.items():
            if lang_code not in self.SOUND_LAWS:
                continue

            # Simplified check - just verify initial consonant
            laws = self.SOUND_LAWS[lang_code]
            proto_initial = proto_form[1] if proto_form.startswith("*") else proto_form[0]

            for proto_sound, expected_reflex in laws.items():
                if proto_sound.endswith(proto_initial):
                    actual_initial = reflex[0] if reflex else ""
                    if actual_initial != expected_reflex:
                        violations.append(
                            f"{lang_code}: expected initial {expected_reflex} "
                            f"from {proto_sound}, got {actual_initial}"
                        )

        return len(violations) == 0, violations

    def verify_etymology(
        self,
        word: str,
        proposed_proto_form: str,
        reflexes: dict[str, str],
        proposed_meaning: str,
    ) -> EtymologyVerification:
        """
        Verify a proposed etymology.

        Args:
            word: The Rapa Nui word
            proposed_proto_form: Proposed Proto-Polynesian reconstruction
            reflexes: Known reflexes in other languages
            proposed_meaning: Proposed meaning of the proto-form

        Returns:
            EtymologyVerification with results
        """
        # Check known reconstructions
        known = self.check_known_reconstruction(proposed_proto_form)

        if known:
            # Verify against known reconstruction
            sound_valid, violations = self.verify_sound_correspondences(
                known.proto_form, reflexes
            )

            return EtymologyVerification(
                word=word,
                proposed_proto_form=proposed_proto_form,
                is_valid=sound_valid,
                confidence=0.9 if sound_valid else 0.5,
                sound_law_violations=violations,
                semantic_plausibility=1.0,
                attestation_count=len(known.known_reflexes),
                reconstructed_meaning=known.meaning,
                scholarly_notes=f"Matches known reconstruction ({known.confidence_level})",
            )

        # Unknown proto-form - verify based on reflexes
        sound_valid, violations = self.verify_sound_correspondences(
            proposed_proto_form, reflexes
        )

        # Estimate confidence based on attestation
        attestation = len(reflexes)
        confidence = min(0.7, 0.3 + (attestation * 0.1))

        if not sound_valid:
            confidence *= 0.5

        return EtymologyVerification(
            word=word,
            proposed_proto_form=proposed_proto_form,
            is_valid=sound_valid and attestation >= 2,
            confidence=confidence,
            sound_law_violations=violations,
            semantic_plausibility=0.7,  # Unknown without LLM
            attestation_count=attestation,
            reconstructed_meaning=proposed_meaning,
            scholarly_notes="Not in known reconstruction database",
        )

    def verify_with_llm(
        self,
        verification: EtymologyVerification,
        additional_context: Optional[str] = None,
    ) -> EtymologyVerification:
        """
        Use LLM for detailed etymology verification.

        Args:
            verification: Initial verification to enhance
            additional_context: Optional additional context

        Returns:
            Enhanced verification with LLM analysis
        """
        if not self.llm:
            return verification

        context_str = f"\nAdditional context: {additional_context}" if additional_context else ""

        user_prompt = f"""Verify this Proto-Polynesian etymology:

Word: {verification.word}
Proposed Proto-Form: {verification.proposed_proto_form}
Proposed Meaning: {verification.reconstructed_meaning}
Attestations: {verification.attestation_count} languages
Sound Law Violations: {verification.sound_law_violations or 'None'}
{context_str}

Evaluate the etymology and provide:
{{
    "is_valid": true|false,
    "confidence_adjustment": -0.3 to 0.3,
    "semantic_plausibility": 0.0-1.0,
    "analysis": "detailed analysis of the etymology",
    "alternative_etymologies": ["other possible origins if any"],
    "scholarly_references": "mention any relevant scholarship"
}}"""

        messages = [
            LLMMessage(role="system", content=self.SYSTEM_PROMPT),
            LLMMessage(role="user", content=user_prompt),
        ]

        response = self.llm.complete(messages, max_tokens=700, temperature=0.1)

        return self._apply_llm_verification(verification, response)

    def _apply_llm_verification(
        self,
        verification: EtymologyVerification,
        response: LLMResponse,
    ) -> EtymologyVerification:
        """Apply LLM verification results."""
        import json

        try:
            content = response.content.strip()
            if content.startswith("```"):
                lines = content.split("\n")
                content = "\n".join(lines[1:-1])

            data = json.loads(content)

            # Update verification
            verification.is_valid = data.get("is_valid", verification.is_valid)
            verification.semantic_plausibility = data.get(
                "semantic_plausibility", verification.semantic_plausibility
            )

            # Adjust confidence
            adjustment = data.get("confidence_adjustment", 0)
            verification.confidence = max(0, min(1, verification.confidence + adjustment))

            # Add scholarly notes
            analysis = data.get("analysis", "")
            refs = data.get("scholarly_references", "")
            verification.scholarly_notes = f"{analysis}\n\nReferences: {refs}" if refs else analysis

        except (json.JSONDecodeError, KeyError):
            pass

        return verification

    def batch_verify(
        self,
        etymologies: list[dict],
    ) -> list[EtymologyVerification]:
        """
        Verify multiple etymologies.

        Args:
            etymologies: List of {"word", "proto_form", "reflexes", "meaning"}

        Returns:
            List of verifications
        """
        results = []
        for etym in etymologies:
            verification = self.verify_etymology(
                word=etym["word"],
                proposed_proto_form=etym["proto_form"],
                reflexes=etym.get("reflexes", {}),
                proposed_meaning=etym.get("meaning", ""),
            )

            if self.llm:
                verification = self.verify_with_llm(verification)

            results.append(verification)

        return results
