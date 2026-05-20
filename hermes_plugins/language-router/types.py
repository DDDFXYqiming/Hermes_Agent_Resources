"""Structured data contracts for language-router v5."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class ReasoningPlan:
    user_language: str
    explicit_output_language: Optional[str]
    final_output_language: str
    task_type: str
    task_complexity: str
    risk_level: str
    confidence: float
    thinking_language: str
    reasoning_mode: str
    verifier_required: bool
    self_consistency_paths: int
    tree_branches: int = 3  # Tree模式分支数
    constraints: list[str] = field(default_factory=list)
    reasoning_instructions: str = ""
    fallback_reason: Optional[str] = None


@dataclass
class ReasoningDraft:
    task_understanding: str
    key_points: list[str] = field(default_factory=list)
    candidate_conclusions: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    missing_information: list[str] = field(default_factory=list)
    suggested_answer_outline: list[str] = field(default_factory=list)
    confidence: float = 0.5
    raw_notes: Optional[str] = None
    branch_id: Optional[str] = None  # Tree模式分支标识
    branch_score: float = 0.0  # Tree模式分支评分


@dataclass
class VerificationReport:
    verdict: str
    issues: list[str] = field(default_factory=list)
    unsupported_claims: list[str] = field(default_factory=list)
    missed_constraints: list[str] = field(default_factory=list)
    safety_notes: list[str] = field(default_factory=list)
    revised_key_points: list[str] = field(default_factory=list)
    revised_answer_outline: list[str] = field(default_factory=list)
    confidence: float = 0.5


@dataclass
class InjectedDigest:
    context: str
    metadata: dict[str, Any]
    debug_footer: Optional[str]
    token_estimate: int


# ── v5.0 新增数据类 ──────────────────────────────────────────


@dataclass
class RewardScores:
    """Reward-based evaluation scores (Improvement #7)."""
    accuracy: float = 0.5
    consistency: float = 0.5
    fluency: float = 0.5
    overall_reward: float = 0.5


@dataclass
class MultilingualResult:
    """Result from Multilingual Thinking Explorer (Improvement #3)."""
    languages: list[str] = field(default_factory=list)
    merged_draft: Optional[ReasoningDraft] = None
    per_language_confidence: dict[str, float] = field(default_factory=dict)
