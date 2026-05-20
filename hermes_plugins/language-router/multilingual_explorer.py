"""Multilingual Thinking Explorer (Improvement #3).

Based on: "Could Thinking Multilingually Empower LLM Reasoning?"
- Multilingual thinking boosts GPQA from ~45 to ~90
- Random 4 languages ≈ optimal combination (robust to language choice)
- Majority voting merges multilingual drafts effectively
"""
from __future__ import annotations

import json
import logging
import random
from typing import Any, Optional

from .types import ReasoningPlan, ReasoningDraft, MultilingualResult

logger = logging.getLogger(__name__)

# Language affinities by task type (from paper findings)
AFFINITY_MAP: dict[str, list[str]] = {
    "math": ["zh", "ja"],
    "logic": ["de", "fr"],
    "complex_debug": ["zh", "ja"],
    "programming": ["en", "zh"],
}

LANG_NAMES = {
    "en": "English", "zh": "Chinese", "ja": "Japanese", "ko": "Korean",
    "de": "German", "fr": "French", "es": "Spanish", "pt": "Portuguese",
    "it": "Italian", "ru": "Russian", "ar": "Arabic", "hi": "Hindi",
    "th": "Thai",
}

EXPLORATION_LANGS = list(LANG_NAMES.keys())


class MultilingualThinkingExplorer:
    """Explore reasoning in 4 languages in parallel, merge via majority voting."""

    def __init__(self, ctx: Any, config: dict):
        self._ctx = ctx
        self._config = config or {}
        self._max_languages = int(self._config.get("max_languages", 4))
        self._trigger_tasks = set(self._config.get("trigger_tasks", ["math", "logic", "complex_debug"]))

    def should_explore(self, task_type: str, reasoning_mode: str) -> bool:
        """Check if multilingual exploration should be triggered."""
        if not self._config.get("enabled", True):
            return False
        if task_type not in self._trigger_tasks:
            return False
        if reasoning_mode not in ("tree", "self_consistency"):
            return False
        return True

    def select_candidates(self, task_type: str, user_lang: str) -> list[str]:
        """Select up to N candidate languages for exploration.

        Strategy:
        1. Always include user's language
        2. Always include English (dominant in training data)
        3. Add task-specific affinity languages
        4. Fill remaining slots randomly from diverse pool
        """
        candidates: list[str] = []

        # 1. User language always first
        if user_lang not in candidates:
            candidates.append(user_lang)

        # 2. English always included
        if "en" not in candidates:
            candidates.append("en")

        # 3. Task-specific affinity languages
        affinity = AFFINITY_MAP.get(task_type, [])
        for lang in affinity:
            if lang not in candidates and len(candidates) < self._max_languages:
                candidates.append(lang)

        # 4. Fill with random diverse languages
        if len(candidates) < self._max_languages:
            available = [l for l in EXPLORATION_LANGS if l not in candidates]
            random.shuffle(available)
            candidates.extend(available[:self._max_languages - len(candidates)])

        return candidates[:self._max_languages]

    def explore(self, user_message: str, plan: ReasoningPlan) -> Optional[MultilingualResult]:
        """Run reasoning in multiple languages and merge results.

        Uses the existing _reason method from the plugin, called once per
        candidate language.  Results are merged via majority voting.
        """
        candidates = self.select_candidates(plan.task_type, plan.user_language)
        logger.info("MultilingualExplorer: candidates=%s for task=%s", candidates, plan.task_type)

        if len(candidates) < 2:
            return None

        drafts: list[tuple[str, ReasoningDraft]] = []
        for lang in candidates:
            draft = self._reason_with_language(user_message, plan, lang)
            if draft:
                drafts.append((lang, draft))

        if not drafts:
            return None

        merged = self._merge_multilingual_drafts(drafts)
        return MultilingualResult(
            languages=[lang for lang, _ in drafts],
            merged_draft=merged,
            per_language_confidence={lang: d.confidence for lang, d in drafts},
        )

    def _reason_with_language(self, user_message: str, plan: ReasoningPlan, lang: str) -> Optional[ReasoningDraft]:
        """Run the reasoner with a specific thinking language override."""
        from .prompts import REASONER_PROMPT
        from . import _json_for_prompt, _get_lang_name

        try:
            # Clone plan with overridden thinking language
            plan_dict = {
                "user_language": plan.user_language,
                "explicit_output_language": plan.explicit_output_language,
                "final_output_language": plan.final_output_language,
                "task_type": plan.task_type,
                "task_complexity": plan.task_complexity,
                "risk_level": plan.risk_level,
                "confidence": plan.confidence,
                "thinking_language": lang,  # KEY: override thinking language
                "reasoning_mode": plan.reasoning_mode,
                "verifier_required": plan.verifier_required,
                "self_consistency_paths": plan.self_consistency_paths,
                "tree_branches": plan.tree_branches,
                "constraints": plan.constraints,
                "reasoning_instructions": plan.reasoning_instructions,
            }
            payload = {
                "plan": plan_dict,
                "path_index": 1,
                "branch_id": f"multi_{lang}",
                "user_message": user_message[:2000],
            }
            lang_name = LANG_NAMES.get(lang, lang)
            result = self._ctx.llm.complete_structured(
                instructions=REASONER_PROMPT + f"\nThinking language: {lang_name}.\nPlan JSON:\n{_json_for_prompt(plan_dict)}",
                input=[{"type": "text", "text": json.dumps(payload, ensure_ascii=False, default=str)}],
                json_mode=True,
                temperature=0.0,
                max_tokens=1200,
                timeout=60,
                purpose="language_router_multilingual_explorer",
            )
            parsed = result.parsed if isinstance(getattr(result, "parsed", None), dict) else {}
            return self._parse_draft(parsed, f"multi_{lang}")
        except Exception as exc:
            logger.warning("MultilingualExplorer: reasoner failed for lang=%s: %s", lang, exc)
            return None

    @staticmethod
    def _parse_draft(parsed: dict, branch_id: str) -> ReasoningDraft:
        from . import _as_list, _clamp_confidence
        return ReasoningDraft(
            task_understanding=str(parsed.get("task_understanding") or ""),
            key_points=_as_list(parsed.get("key_points")),
            candidate_conclusions=_as_list(parsed.get("candidate_conclusions")),
            assumptions=_as_list(parsed.get("assumptions")),
            risks=_as_list(parsed.get("risks")),
            missing_information=_as_list(parsed.get("missing_information")),
            suggested_answer_outline=_as_list(parsed.get("suggested_answer_outline")),
            confidence=_clamp_confidence(parsed.get("confidence"), 0.5),
            branch_id=branch_id,
        )

    @staticmethod
    def _merge_multilingual_drafts(drafts: list[tuple[str, ReasoningDraft]]) -> ReasoningDraft:
        """Merge multilingual drafts using majority voting (per paper findings).

        Items that appear in multiple languages get higher priority.
        """
        if not drafts:
            return None
        if len(drafts) == 1:
            return drafts[0][1]

        # Task understanding: pick longest from highest-confidence draft
        best_draft = max(drafts, key=lambda x: x[1].confidence)[1]
        task_understanding = best_draft.task_understanding

        merged = ReasoningDraft(
            task_understanding=task_understanding,
            confidence=sum(d.confidence for _, d in drafts) / len(drafts),
            branch_id="multilingual_merged",
        )

        # Majority voting for list fields
        for field in ("key_points", "candidate_conclusions", "assumptions",
                      "risks", "missing_information", "suggested_answer_outline"):
            counts: dict[str, int] = {}
            for _, d in drafts:
                for item in getattr(d, field) or []:
                    counts[item] = counts.get(item, 0) + 1
            # Sort by frequency (desc), then alphabetically for stability
            sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            setattr(merged, field, [item for item, _ in sorted_items[:8]])

        return merged
