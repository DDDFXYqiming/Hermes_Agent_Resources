"""Reward-Based Evaluator (Improvement #7).

Based on: AdaMCoT — uses reward-based mechanism to evaluate candidate
reasoning paths. Optimizes for answer accuracy, consistency, and fluency
using a strong LLM-based evaluator.
"""
from __future__ import annotations

import json
import logging
from typing import Any, Optional

from .types import ReasoningPlan, ReasoningDraft, RewardScores

logger = logging.getLogger(__name__)

REWARD_EVALUATOR_PROMPT = """You are a Reasoning Path Evaluator.
Evaluate the quality of a reasoning path on three dimensions.

Question: {question}
Answer Outline: {answer_outline}
Reasoning Language: {reasoning_lang}
Output Language: {output_lang}

Rate each dimension on a 0.0-1.0 scale:
1. accuracy: Is the reasoning correct and the answer accurate?
2. consistency: Is the reasoning internally consistent? Does it hold across languages?
3. fluency: Is the output natural and fluent in the target language?

Return ONLY JSON:
{{"accuracy": 0.0, "consistency": 0.0, "fluency": 0.0}}
"""


class RewardBasedEvaluator:
    """Evaluate reasoning path quality using LLM-based assessment."""

    def __init__(self, ctx: Any, config: dict):
        self._ctx = ctx
        self._config = config or {}
        self._enabled = bool(self._config.get("enabled", True))
        self._accuracy_weight = float(self._config.get("accuracy_weight", 0.5))
        self._consistency_weight = float(self._config.get("consistency_weight", 0.3))
        self._fluency_weight = float(self._config.get("fluency_weight", 0.2))
        self._min_reward = float(self._config.get("min_reward_threshold", 0.6))

    @property
    def enabled(self) -> bool:
        return self._enabled

    def evaluate_reasoning_path(
        self,
        question: str,
        draft: ReasoningDraft,
        plan: ReasoningPlan,
    ) -> RewardScores:
        """Evaluate reasoning path quality using LLM-based assessment.

        Returns RewardScores with accuracy, consistency, fluency, and overall reward.
        Falls back to heuristic scores on failure.
        """
        if not self._enabled:
            return self._heuristic_scores(draft, plan)

        try:
            prompt = REWARD_EVALUATOR_PROMPT.format(
                question=question[:500],
                answer_outline=json.dumps(draft.suggested_answer_outline[:5], ensure_ascii=False),
                reasoning_lang=plan.thinking_language,
                output_lang=plan.final_output_language,
            )

            result = self._ctx.llm.complete_structured(
                instructions=prompt,
                input=[{"type": "text", "text": question[:500]}],
                json_mode=True,
                temperature=0.0,
                max_tokens=200,
                timeout=15,
                purpose="language_router_reward_evaluator",
            )

            parsed = result.parsed if isinstance(getattr(result, "parsed", None), dict) else {}
            accuracy = self._clamp(parsed.get("accuracy", 0.5))
            consistency = self._clamp(parsed.get("consistency", 0.5))
            fluency = self._clamp(parsed.get("fluency", 0.5))

        except Exception as exc:
            logger.warning("RewardEvaluator: LLM evaluation failed: %s, using heuristic", exc)
            return self._heuristic_scores(draft, plan)

        overall = (accuracy * self._accuracy_weight +
                   consistency * self._consistency_weight +
                   fluency * self._fluency_weight)

        scores = RewardScores(
            accuracy=accuracy,
            consistency=consistency,
            fluency=fluency,
            overall_reward=overall,
        )
        logger.info(
            "RewardEvaluator: accuracy=%.2f consistency=%.2f fluency=%.2f overall=%.2f",
            accuracy, consistency, fluency, overall,
        )
        return scores

    def should_reject(self, scores: RewardScores) -> bool:
        """Check if the reward score is below the minimum threshold."""
        return scores.overall_reward < self._min_reward

    @staticmethod
    def _heuristic_scores(draft: ReasoningDraft, plan: ReasoningPlan) -> RewardScores:
        """Fallback heuristic scoring when LLM evaluation is unavailable."""
        confidence = draft.confidence if draft else 0.5
        # Heuristic: higher confidence → higher accuracy estimate
        accuracy = min(1.0, confidence * 1.1)
        # Heuristic: matching user language → higher consistency
        consistency = 0.8 if plan.thinking_language == plan.user_language else 0.6
        fluency = 0.7  # Default moderate fluency
        overall = (accuracy * 0.5 + consistency * 0.3 + fluency * 0.2)

        return RewardScores(
            accuracy=accuracy,
            consistency=consistency,
            fluency=fluency,
            overall_reward=overall,
        )

    @staticmethod
    def _clamp(value: Any, low: float = 0.0, high: float = 1.0) -> float:
        try:
            return max(low, min(high, float(value)))
        except (TypeError, ValueError):
            return 0.5
