"""Dynamic Language Selector (Improvement #4).

Based on: AdaMCoT — Adaptive Multilingual Chain-of-Thought
- Different languages offer unique advantages for different tasks
- Dynamic routing learns to select optimal intermediate languages
- Historical performance tracked via exponential moving average
"""
from __future__ import annotations

import json
import logging
import re
from typing import Any, Optional

from .types import ReasoningPlan

logger = logging.getLogger(__name__)

# Default initial scores per language (from paper: English dominant)
DEFAULT_INITIAL_SCORES: dict[str, float] = {
    "en": 0.7, "zh": 0.6, "ja": 0.5, "de": 0.5, "fr": 0.5,
    "es": 0.4, "ko": 0.4, "ru": 0.4, "ar": 0.3, "hi": 0.3,
    "th": 0.3, "pt": 0.3, "it": 0.3,
}

# Language-task affinity scores (from AdaMCoT findings)
AFFINITY_SCORES: dict[str, dict[str, float]] = {
    "math":          {"en": 0.6, "zh": 0.9, "ja": 0.8, "de": 0.5, "fr": 0.5},
    "logic":         {"en": 0.6, "zh": 0.5, "ja": 0.5, "de": 0.9, "fr": 0.8},
    "complex_debug": {"en": 0.8, "zh": 0.7, "ja": 0.6, "de": 0.4, "fr": 0.4},
    "programming":   {"en": 0.9, "zh": 0.6, "ja": 0.5, "de": 0.4, "fr": 0.4},
    "research":      {"en": 0.8, "zh": 0.5, "ja": 0.4, "de": 0.6, "fr": 0.5},
    "data_analysis": {"en": 0.8, "zh": 0.5, "ja": 0.4, "de": 0.4, "fr": 0.4},
    "architecture_design": {"en": 0.8, "zh": 0.6, "ja": 0.5, "de": 0.5, "fr": 0.5},
    "debug":         {"en": 0.8, "zh": 0.7, "ja": 0.6, "de": 0.4, "fr": 0.4},
}

# Weight configuration
SCORE_WEIGHTS = {
    "historical": 0.4,
    "affinity": 0.3,
    "lang_match": 0.2,
    "diversity": 0.1,
}

LANG_PATTERNS_QUICK = {
    "zh": re.compile(r"[\u4e00-\u9fff]"),
    "ja": re.compile(r"[\u3040-\u30ff]"),
    "ko": re.compile(r"[\uac00-\ud7af]"),
    "en": re.compile(r"[a-zA-Z]"),
}


class DynamicLanguageSelector:
    """Select optimal thinking language based on learned performance + task affinity."""

    def __init__(self, config: dict):
        self._config = config or {}
        self._learning_rate = float(self._config.get("learning_rate", 0.1))
        self._performance_history: dict[str, dict[str, float]] = {}
        self._initial_scores = dict(DEFAULT_INITIAL_SCORES)
        # Allow config overrides
        for lang, score in self._config.get("initial_scores", {}).items():
            self._initial_scores[lang] = float(score)

    def select_optimal_language(
        self,
        task_type: str,
        user_message: str,
        user_lang: str,
        available_langs: list[str] | None = None,
    ) -> tuple[str, float]:
        """Select the best thinking language and return (lang_code, confidence).

        Scoring:
        1. Historical performance (40%) — learned from past tasks
        2. Language-task affinity (30%) — from paper findings
        3. Message language match (20%) — user lang bonus
        4. Diversity bonus (10%) — encourage non-English
        """
        langs = available_langs or list(DEFAULT_INITIAL_SCORES.keys())
        scores: dict[str, float] = {}

        for lang in langs:
            scores[lang] = self._compute_score(lang, task_type, user_lang)

        if not scores:
            return "en", 0.5

        best_lang = max(scores, key=scores.get)
        total = sum(scores.values())
        confidence = scores[best_lang] / total if total > 0 else 0.5

        logger.info(
            "DynamicSelector: task=%s user_lang=%s best=%s confidence=%.2f scores=%s",
            task_type, user_lang, best_lang, confidence,
            {k: round(v, 3) for k, v in sorted(scores.items(), key=lambda x: -x[1])[:5]},
        )
        return best_lang, confidence

    def _compute_score(self, lang: str, task_type: str, user_lang: str) -> float:
        """Compute composite score for a language."""
        # 1. Historical performance (40%)
        hist = self._performance_history.get(task_type, {}).get(lang)
        if hist is None:
            hist = self._initial_scores.get(lang, 0.5)
        hist_score = hist

        # 2. Language-task affinity (30%)
        affinity = AFFINITY_SCORES.get(task_type, {}).get(lang, 0.5)

        # 3. Message language match (20%)
        lang_match = 1.0 if lang == user_lang else 0.3

        # 4. Diversity bonus (10%) — encourage non-English
        diversity = 0.1 if lang != "en" else 0.0

        w = SCORE_WEIGHTS
        return (hist_score * w["historical"] +
                affinity * w["affinity"] +
                lang_match * w["lang_match"] +
                diversity * w["diversity"])

    def update_performance(self, task_type: str, lang: str, success: bool) -> None:
        """Update historical performance after task completion.

        Uses exponential moving average (EMA) with configured learning rate.
        """
        if task_type not in self._performance_history:
            self._performance_history[task_type] = {}

        current = self._performance_history[task_type].get(lang, self._initial_scores.get(lang, 0.5))
        alpha = self._learning_rate
        new_score = alpha * (1.0 if success else 0.0) + (1 - alpha) * current
        self._performance_history[task_type][lang] = new_score

        logger.info(
            "DynamicSelector: updated task=%s lang=%s success=%s old=%.3f new=%.3f",
            task_type, lang, success, current, new_score,
        )

    def get_history(self) -> dict[str, dict[str, float]]:
        """Return a copy of the performance history (for diagnostics)."""
        return {k: dict(v) for k, v in self._performance_history.items()}
