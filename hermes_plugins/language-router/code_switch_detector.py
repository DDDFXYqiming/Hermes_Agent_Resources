"""Code-Switching Pattern Detector (Improvement #5).

Based on: "The Impact of Language Mixing on Bilingual LLM Reasoning"
Four code-switching patterns:
1. Phrase-level switching — for precision/efficiency
2. Technical term switching — English for technical vocabulary
3. Format match switching — match reasoning/answer format
4. Full switch — complete language change under cognitive load

Key finding: Enforcing monolingual decoding REDUCES accuracy by 5.6 points.
"""
from __future__ import annotations

import logging
import re
from typing import Any, Optional

logger = logging.getLogger(__name__)

# Pattern type constants
PATTERN_PHRASE = "phrase"
PATTERN_TECHNICAL_TERM = "technical_term"
PATTERN_FORMAT_MATCH = "format_match"
PATTERN_FULL_SWITCH = "full_switch"

ALL_PATTERNS = {PATTERN_PHRASE, PATTERN_TECHNICAL_TERM, PATTERN_FORMAT_MATCH, PATTERN_FULL_SWITCH}

# Technical term indicators (English-centric as per paper finding)
TECHNICAL_PATTERNS = re.compile(
    r"\b(API|SDK|HTTP|REST|JSON|XML|SQL|CPU|GPU|RAM|LLM|GPT|BERT|transformer|"
    r"gradient|backprop|epoch|batch|tensor|numpy|pandas|docker|kubernetes|"
    r"recursion|polymorphism|inheritance|async|await|thread|mutex|"
    r"algorithm|complexity|optimization|convergence|derivative|integral)\b",
    re.I,
)

# Format section indicators (code blocks, math blocks, lists)
FORMAT_PATTERNS = re.compile(
    r"```|```python|```json|```sql|\$\$|\\begin\{|\\end\{|"
    r"^\s*\d+[\.\)]\s|^\s*[-*]\s|"
    r"def |class |function |import |from |return |if |else |for |while ",
    re.I | re.M,
)

# Cognitive load indicators (complex reasoning signals)
COGNITIVE_LOAD_PATTERNS = re.compile(
    r"however|nevertheless|on the other hand|conversely|although|but wait|"
    r"let me reconsider|actually|wait,|hold on|反过来说|但是|然而|不过|"
    r"另一方面|重新考虑|等等|慢着",
    re.I,
)


class CodeSwitchingPatternDetector:
    """Detect and guide code-switching patterns in multilingual reasoning."""

    def __init__(self, config: dict):
        self._config = config or {}
        self._enabled = bool(self._config.get("enabled", True))
        self._guidance_injection = bool(self._config.get("guidance_injection", True))

    @property
    def enabled(self) -> bool:
        return self._enabled

    def detect_pattern(
        self,
        context: str,
        current_lang: str,
        new_lang: str,
    ) -> str:
        """Detect which code-switching pattern is needed.

        Args:
            context: The current reasoning context / user message
            current_lang: Current thinking language code
            new_lang: Target language code

        Returns:
            One of: "phrase", "technical_term", "format_match", "full_switch"
        """
        if not self._enabled:
            return PATTERN_PHRASE

        has_technical = bool(TECHNICAL_PATTERNS.search(context))
        is_format_section = bool(FORMAT_PATTERNS.search(context))
        cognitive_load = self._estimate_cognitive_load(context)

        # Decision tree (from paper's observed patterns)
        if new_lang == "en" and has_technical:
            return PATTERN_TECHNICAL_TERM
        if is_format_section and new_lang != current_lang:
            return PATTERN_FORMAT_MATCH
        if cognitive_load > 0.7:
            return PATTERN_FULL_SWITCH
        return PATTERN_PHRASE

    def get_switching_guidance(
        self,
        pattern: str,
        current_lang: str,
        new_lang: str,
    ) -> str:
        """Provide guidance text to inject into the reasoning context.

        Based on the detected pattern, this returns a brief instruction
        that tells the reasoner HOW to switch languages appropriately.
        """
        if not self._guidance_injection:
            return ""

        lang_name = _LANG_NAMES.get(new_lang, new_lang)
        guidance_map = {
            PATTERN_TECHNICAL_TERM: (
                f"[Code-Switch] Switch to {lang_name} for technical terminology "
                f"to improve precision. Resume {current_lang} after the term."
            ),
            PATTERN_FORMAT_MATCH: (
                f"[Code-Switch] Use {lang_name} to match the reasoning/answer "
                f"format for consistency."
            ),
            PATTERN_FULL_SWITCH: (
                f"[Code-Switch] Full switch to {lang_name} is beneficial here "
                f"due to cognitive complexity. Think entirely in {lang_name} "
                f"for this section."
            ),
            PATTERN_PHRASE: (
                f"[Code-Switch] Use phrase-level switching to {lang_name} "
                f"for efficiency where natural."
            ),
        }
        return guidance_map.get(pattern, "")

    def analyze_and_guide(
        self,
        context: str,
        current_lang: str,
        new_lang: str,
    ) -> tuple[str, str]:
        """Convenience: detect pattern + get guidance in one call.

        Returns:
            (pattern_type, guidance_text)
        """
        pattern = self.detect_pattern(context, current_lang, new_lang)
        guidance = self.get_switching_guidance(pattern, current_lang, new_lang)
        return pattern, guidance

    @staticmethod
    def _estimate_cognitive_load(context: str) -> float:
        """Estimate cognitive load from context (0.0 to 1.0).

        Heuristic: count cognitive load signals relative to text length.
        """
        if not context:
            return 0.0
        matches = COGNITIVE_LOAD_PATTERNS.findall(context)
        # Normalize: 0 matches = 0.0, 3+ matches = 1.0
        load = min(1.0, len(matches) / 3.0)
        return load


_LANG_NAMES = {
    "en": "English", "zh": "Chinese", "ja": "Japanese", "ko": "Korean",
    "de": "German", "fr": "French", "es": "Spanish", "pt": "Portuguese",
    "it": "Italian", "ru": "Russian", "ar": "Arabic", "hi": "Hindi",
    "th": "Thai",
}
