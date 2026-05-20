"""Language Router Plugin v4.1 — Planner -> Worker -> Verifier -> Digest with Tree/Self-consistency/Cache/Budget."""
from __future__ import annotations

import json
import logging
import re
import time
from pathlib import Path
from typing import Any, Optional

from hermes_cli.config import cfg_get
from hermes_cli.plugins import PluginContext

from .cache import ClassificationCache
from .prompts import (
    DIGEST_FORMAT_VERSION,
    PLANNER_PROMPT,
    PLANNER_PROMPT_VERSION,
    REASONER_PROMPT,
    REASONER_PROMPT_VERSION,
    VERIFIER_PROMPT,
    VERIFIER_PROMPT_VERSION,
)
from .types import InjectedDigest, ReasoningDraft, ReasoningPlan, VerificationReport

logger = logging.getLogger(__name__)

VERSION = "4.1.0"

LANG_PATTERNS = {
    "ja_hiragana": re.compile(r"[\u3040-\u309f]"),
    "ja_katakana": re.compile(r"[\u30a0-\u30ff]"),
    "zh": re.compile(r"[\u4e00-\u9fff]"),
    "ko": re.compile(r"[\uac00-\ud7af]"),
    "ar": re.compile(r"[\u0600-\u06ff]"),
    "ru": re.compile(r"[\u0400-\u04ff]"),
    "hi": re.compile(r"[\u0900-\u097f]"),
    "th": re.compile(r"[\u0e00-\u0e7f]"),
    "de": re.compile(r"\b(der|die|das|und|ist|ein|eine|auf|mit)\b", re.I),
    "fr": re.compile(r"\b(le|la|les|des|une|est|dans|pour|avec)\b", re.I),
    "es": re.compile(r"\b(el|la|los|las|una|es|en|por|con|para)\b", re.I),
    "pt": re.compile(r"\b(o|a|os|as|uma|é|em|por|com|para)\b", re.I),
    "it": re.compile(r"\b(il|la|gli|le|una|è|in|per|con|di)\b", re.I),
}

LANG_NAMES = {
    "en": "English", "zh": "Chinese", "ja": "Japanese", "ko": "Korean",
    "de": "German", "fr": "French", "es": "Spanish", "pt": "Portuguese",
    "it": "Italian", "ru": "Russian", "ar": "Arabic", "hi": "Hindi",
    "th": "Thai", "mixed": "Mixed language", "user": "the user's language",
}

TECH_TASKS = {"programming", "debug", "math", "logic", "data_analysis", "data", "research", "architecture_design"}
USER_LANG_TASKS = {"creative", "emotion", "culture"}
VERIFIER_TASKS = TECH_TASKS | {"financial_or_medical", "legal_or_policy", "safety_sensitive"}
ALLOWED_MODES = {"off", "simple", "verify", "self_consistency", "tree"}

DEFAULT_CONFIG = {
    "planner": {
        "enabled": True,
        "provider": None,
        "model": None,
        "temperature": 0.0,
        "max_tokens": 300,
        "timeout": 15,
        "disable_reasoning_if_supported": True,
        "confidence_threshold": 0.6,
    },
    "reasoner": {
        "enabled": True,
        "provider": None,
        "model": None,
        "temperature": 0.0,
        "max_tokens": 1200,
        "timeout": 60,
        "default_thinking_language": "en",
        "reasoning_effort": "high",
    },
    "verifier": {
        "enabled": "auto",
        "provider": None,
        "model": None,
        "temperature": 0.0,
        "max_tokens": 700,
        "timeout": 45,
        "confidence_threshold": 0.75,
        "trigger_tasks": sorted(VERIFIER_TASKS),
    },
    "reasoning": {
        "enabled": True,
        "mode": "auto",
        "allowed_modes": ["off", "simple", "verify", "self_consistency", "tree"],
        "self_consistency": {"enabled": True, "max_paths": 3, "trigger_tasks": ["math", "logic", "complex_debug"]},
        "tree": {"enabled": True, "max_branches": 3, "pruning_threshold": 0.6, "trigger_tasks": ["math", "logic", "complex_debug", "architecture_design"]},
        "expose_raw_cot": False,
        "digest_only": True,
    },
    "output": {"preserve_user_language": True, "respect_explicit_language_request": True, "fallback_language": "en"},
    "cache": {"enabled": True, "ttl_seconds": 300, "max_entries": 1000, "cache_plans": True, "cache_reasoning": False},
    "digest": {"max_tokens": 500, "include_plan_summary": True, "include_verifier_summary": True, "include_raw_notes": False},
    "debug": {"show_footer": False, "log_plan": True, "log_verifier": True, "log_digest_metadata": True},
    "latency_budget": {
        "enabled": True,
        "max_total_seconds": 90,
        "skip_verifier_if_budget_low": True,
        "skip_reasoner_if_budget_low": True,
        "degradation_thresholds": {"high": 0.7, "medium": 0.4, "low": 0.2},
    },
}


def _detect_language(text: str) -> str:
    if not text or not text.strip():
        return "en"
    scores: dict[str, int] = {}
    sample = text[:500]
    for lang, pattern in LANG_PATTERNS.items():
        scores[lang] = len(pattern.findall(sample))
    if scores.get("ja_hiragana", 0) or scores.get("ja_katakana", 0):
        return "ja"
    for lang in ["zh", "ko", "ar", "ru", "hi", "th"]:
        if scores.get(lang, 0) > 0:
            return lang
    for lang in ["de", "fr", "es", "pt", "it"]:
        if scores.get(lang, 0) > 3:
            return lang
    return "en"


def _get_lang_name(lang_code: str) -> str:
    return LANG_NAMES.get(lang_code, lang_code.upper())


def _detect_explicit_output_language(text: str) -> Optional[str]:
    rules = [
        (r"用\s*英文|用英语|英文回答|英语回答|answer\s+in\s+english|reply\s+in\s+english", "en"),
        (r"用\s*中文|中文回答|汉语回答|answer\s+in\s+chinese|reply\s+in\s+chinese", "zh"),
        (r"用\s*日文|用\s*日语|日文回答|日语回答|answer\s+in\s+japanese", "ja"),
        (r"用\s*韩文|用\s*韩语|韩文回答|韩语回答|answer\s+in\s+korean", "ko"),
        (r"answer\s+in\s+german|reply\s+in\s+german", "de"),
        (r"answer\s+in\s+french|reply\s+in\s+french", "fr"),
        (r"answer\s+in\s+spanish|reply\s+in\s+spanish", "es"),
    ]
    for pattern, lang in rules:
        if re.search(pattern, text, re.I):
            return lang
    return None


def _deep_merge(base: dict, override: dict) -> dict:
    merged = dict(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def _load_manifest_default_config() -> dict:
    manifest_path = Path(__file__).with_name("plugin.yaml")
    if not manifest_path.exists():
        return dict(DEFAULT_CONFIG)
    try:
        import yaml
        with open(manifest_path, encoding="utf-8") as f:
            manifest = yaml.safe_load(f) or {}
        manifest_config = manifest.get("default_config") or manifest.get("config") or {}
        return _deep_merge(DEFAULT_CONFIG, manifest_config)
    except Exception as exc:
        logger.warning("Failed to load language-router manifest defaults: %s", exc)
        return dict(DEFAULT_CONFIG)


def _normalize_legacy_config(config: dict) -> dict:
    cfg = _deep_merge(DEFAULT_CONFIG, config or {})
    legacy_classifier = config.get("classifier") if isinstance(config.get("classifier"), dict) else None
    legacy_reasoning = config.get("reasoning") if isinstance(config.get("reasoning"), dict) else None
    if legacy_classifier:
        cfg["planner"] = _deep_merge(cfg.get("planner", {}), legacy_classifier)
        if "confidence_threshold" in config:
            cfg["planner"]["confidence_threshold"] = config["confidence_threshold"]
    if legacy_reasoning:
        reasoner_legacy = {k: v for k, v in legacy_reasoning.items() if k in {"provider", "model", "temperature", "max_tokens", "timeout", "reasoning_effort"}}
        cfg["reasoner"] = _deep_merge(cfg.get("reasoner", {}), reasoner_legacy)
        if legacy_reasoning.get("enabled") is False:
            cfg["reasoning"]["enabled"] = False
            cfg["reasoning"]["mode"] = "off"
    if "confidence_threshold" in config:
        cfg["planner"]["confidence_threshold"] = config["confidence_threshold"]
        cfg["verifier"].setdefault("confidence_threshold", config["confidence_threshold"])
    return cfg


def _load_plugin_config() -> dict:
    from hermes_constants import get_hermes_home
    default_config = _load_manifest_default_config()
    config_path = get_hermes_home() / "config.yaml"
    if not config_path.exists():
        return _normalize_legacy_config(default_config)
    try:
        import yaml
        with open(config_path, encoding="utf-8") as f:
            all_config = yaml.safe_load(f) or {}
        user_config = cfg_get(all_config, "plugins", "entries", "language-router", "config", default={}) or {}
        return _normalize_legacy_config(_deep_merge(default_config, user_config))
    except Exception as exc:
        logger.warning("Failed to load language-router user config: %s", exc)
        return _normalize_legacy_config(default_config)


def _build_llm_params(section_cfg: dict, max_default: int, timeout_default: int, purpose: str) -> dict:
    params: dict[str, Any] = {
        "temperature": section_cfg.get("temperature", 0.0),
        "max_tokens": section_cfg.get("max_tokens", max_default),
        "timeout": section_cfg.get("timeout", timeout_default),
        "purpose": purpose,
    }
    if section_cfg.get("provider"):
        params["provider"] = section_cfg["provider"]
    if section_cfg.get("model"):
        params["model"] = section_cfg["model"]
    return params


def _mode_name(value: Any) -> str:
    if value is False:
        return "off"
    if value is True:
        return "auto"
    return str(value)


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value if str(v).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def _clamp_confidence(value: Any, default: float = 0.5) -> float:
    try:
        return max(0.0, min(1.0, float(value)))
    except Exception:
        return default


def _json_for_prompt(obj: Any) -> str:
    if hasattr(obj, "__dict__"):
        return json.dumps(obj.__dict__, ensure_ascii=False, default=str)
    return json.dumps(obj, ensure_ascii=False, default=str)


class LatencyBudgetManager:
    """管理延迟预算，支持多级降级策略。"""

    def __init__(self, config: dict):
        self._config = config.get("latency_budget", {})
        self._enabled = bool(self._config.get("enabled", True))
        self._max_seconds = float(self._config.get("max_total_seconds", 90))
        self._thresholds = self._config.get("degradation_thresholds", {"high": 0.7, "medium": 0.4, "low": 0.2})
        self._start_time: Optional[float] = None
        self._degradation_level = "none"
        self._notifications: list[str] = []

    def start(self):
        self._start_time = time.time()
        self._degradation_level = "none"
        self._notifications = []

    def get_elapsed(self) -> float:
        if self._start_time is None:
            return 0.0
        return time.time() - self._start_time

    def get_remaining_ratio(self) -> float:
        if not self._enabled or self._max_seconds <= 0:
            return 1.0
        elapsed = self.get_elapsed()
        return max(0.0, 1.0 - (elapsed / self._max_seconds))

    def get_degradation_level(self) -> str:
        if not self._enabled:
            return "none"
        ratio = self.get_remaining_ratio()
        high_threshold = self._thresholds.get("high", 0.7)
        medium_threshold = self._thresholds.get("medium", 0.4)
        low_threshold = self._thresholds.get("low", 0.2)
        if ratio < low_threshold:
            return "critical"
        elif ratio < medium_threshold:
            return "low"
        elif ratio < high_threshold:
            return "medium"
        return "none"

    def should_skip_verifier(self) -> bool:
        if not self._enabled:
            return False
        skip_config = self._config.get("skip_verifier_if_budget_low", True)
        if not skip_config:
            return False
        level = self.get_degradation_level()
        return level in {"low", "critical"}

    def should_skip_reasoner(self) -> bool:
        if not self._enabled:
            return False
        skip_config = self._config.get("skip_reasoner_if_budget_low", True)
        if not skip_config:
            return False
        level = self.get_degradation_level()
        return level == "critical"

    def add_notification(self, message: str):
        self._notifications.append(message)
        logger.info("Latency budget notification: %s", message)

    def get_notifications(self) -> list[str]:
        return list(self._notifications)


class LanguageRouterPlugin:
    """Structured language-router v4.1 pipeline with Tree/Self-consistency/Cache/Budget."""

    def __init__(self, ctx: PluginContext):
        self._ctx = ctx
        self._config = _load_plugin_config()
        cache_cfg = self._config.get("cache", {})
        self._cache_enabled = bool(cache_cfg.get("enabled", True))
        self._cache_plans = bool(cache_cfg.get("cache_plans", True))
        self._cache = ClassificationCache(max_entries=cache_cfg.get("max_entries", 1000), ttl_seconds=cache_cfg.get("ttl_seconds", 300))
        self._stats = {
            "planner_calls": 0, "reasoner_calls": 0, "verifier_calls": 0, "digest_injections": 0,
            "cache_hits": 0, "fallbacks": 0, "failures": 0,
            "tree_branches": 0, "tree_pruned": 0, "self_consistency_merges": 0,
            "budget_degradations": 0,
        }
        self._mode_counts: dict[str, int] = {}
        self._detected_languages: dict[str, int] = {}
        self._last_run: dict[str, Any] = {}
        self._budget_manager = LatencyBudgetManager(self._config)
        logger.info("Language Router v4.1 initialized config=%s", self._config)

    def _heuristic_task(self, user_message: str) -> tuple[str, float]:
        msg = user_message.lower()
        buckets = [
            ("debug", ["traceback", "报错", "错误", "error", "exception", "debug", "排查", "修复", "bug"]),
            ("programming", ["python", "javascript", "代码", "编程", "function", "api", "sql", "docker", "git"]),
            ("math", ["计算", "数学", "积分", "方程", "证明", "calculate", "equation", "integral"]),
            ("research", ["论文", "研究", "搜索", "调研", "research", "paper", "literature"]),
            ("architecture_design", ["架构", "设计", "spec", "方案", "architecture", "design"]),
            ("translation", ["翻译", "translate", "译成"]),
            ("creative", ["写一首", "故事", "文案", "诗", "creative", "story", "poem"]),
            ("emotion", ["心情", "难过", "开心", "陪我", "聊聊", "sad", "happy"]),
            ("culture", ["文化", "历史", "文学", "tradition", "culture"]),
        ]
        for task, words in buckets:
            if any(w in msg for w in words):
                return task, 0.72
        return "general", 0.55

    def _resolve_thinking_language(self, task_type: str, planner_lang: str, user_lang: str) -> str:
        if planner_lang == "source":
            return user_lang
        if planner_lang == "user":
            return user_lang
        if task_type in USER_LANG_TASKS:
            return user_lang
        if task_type in TECH_TASKS:
            return "en"
        return planner_lang or self._config.get("reasoner", {}).get("default_thinking_language", "en")

    def _choose_mode(self, task_type: str, confidence: float, risk_level: str, requested_mode: str, user_message: str) -> str:
        reasoning_cfg = self._config.get("reasoning", {})
        allowed = {_mode_name(m) for m in (reasoning_cfg.get("allowed_modes") or list(ALLOWED_MODES))} & ALLOWED_MODES
        if not reasoning_cfg.get("enabled", True):
            return "off"
        configured = _mode_name(reasoning_cfg.get("mode", "auto"))
        if configured in ALLOWED_MODES:
            return configured if configured in allowed else "simple"

        # Check tree trigger_tasks
        tree_cfg = reasoning_cfg.get("tree", {})
        if tree_cfg.get("enabled") and "tree" in allowed:
            tree_triggers = tree_cfg.get("trigger_tasks", [])
            if task_type in tree_triggers:
                return "tree"

        # Check self_consistency trigger_tasks
        sc_cfg = reasoning_cfg.get("self_consistency", {})
        if sc_cfg.get("enabled") and "self_consistency" in allowed:
            sc_triggers = sc_cfg.get("trigger_tasks", [])
            if task_type in sc_triggers:
                return "self_consistency"

        # Explicit high-cost keywords override
        if self._explicit_high_cost_allowed(user_message):
            if tree_cfg.get("enabled") and "tree" in allowed:
                return "tree"
            if sc_cfg.get("enabled") and "self_consistency" in allowed:
                return "self_consistency"

        if task_type in VERIFIER_TASKS or risk_level in {"medium", "high"} or confidence < self._config.get("verifier", {}).get("confidence_threshold", 0.75):
            return "verify" if "verify" in allowed else "simple"
        if requested_mode in ALLOWED_MODES and requested_mode in allowed:
            if requested_mode == "off":
                return "off"
            return requested_mode
        return "simple" if "simple" in allowed else "off"

    def _explicit_high_cost_allowed(self, user_message: str) -> bool:
        return bool(re.search(r"多角度|复核|验证|算准|self[-_ ]?consistency|tree of thought|多个方案|深度分析", user_message, re.I))

    def _planner_fallback(self, user_message: str, reason: str) -> ReasoningPlan:
        user_lang = _detect_language(user_message)
        explicit = _detect_explicit_output_language(user_message)
        task_type, confidence = self._heuristic_task(user_message)
        risk = "medium" if task_type in VERIFIER_TASKS else "low"
        complexity = "medium" if task_type in TECH_TASKS else "low"
        thinking = self._resolve_thinking_language(task_type, "en" if task_type in TECH_TASKS else "user", user_lang)
        mode = self._choose_mode(task_type, confidence, risk, "auto", user_message)
        tree_cfg = self._config.get("reasoning", {}).get("tree", {})
        return ReasoningPlan(
            user_language=user_lang,
            explicit_output_language=explicit,
            final_output_language=explicit or user_lang or self._config.get("output", {}).get("fallback_language", "en"),
            task_type=task_type,
            task_complexity=complexity,
            risk_level=risk,
            confidence=confidence,
            thinking_language=thinking,
            reasoning_mode=mode,
            verifier_required=mode in {"verify", "self_consistency"},
            self_consistency_paths=self._self_consistency_paths(mode),
            tree_branches=self._tree_branches(mode),
            constraints=["Respect explicit output language" if explicit else "Preserve user's language"],
            reasoning_instructions="Produce a compact structured analysis for the main model.",
            fallback_reason=reason,
        )

    def _self_consistency_paths(self, mode: str) -> int:
        if mode != "self_consistency":
            return 1
        scfg = self._config.get("reasoning", {}).get("self_consistency", {})
        return max(2, min(5, int(scfg.get("max_paths", 3))))

    def _tree_branches(self, mode: str) -> int:
        if mode != "tree":
            return 1
        tcfg = self._config.get("reasoning", {}).get("tree", {})
        return max(2, min(5, int(tcfg.get("max_branches", 3))))

    def _parse_plan(self, parsed: dict, user_message: str) -> ReasoningPlan:
        user_lang = _detect_language(user_message)
        explicit = _detect_explicit_output_language(user_message)
        task_type = str(parsed.get("task_type") or "general")
        if task_type == "data":
            task_type = "data_analysis"
        confidence = _clamp_confidence(parsed.get("confidence"), 0.5)
        risk = str(parsed.get("risk_level") or ("medium" if task_type in VERIFIER_TASKS else "low"))
        complexity = str(parsed.get("task_complexity") or ("medium" if task_type in TECH_TASKS else "low"))
        thinking = self._resolve_thinking_language(task_type, str(parsed.get("thinking_language") or "user"), user_lang)
        mode = self._choose_mode(task_type, confidence, risk, str(parsed.get("reasoning_mode") or "auto"), user_message)
        verifier_enabled = self._config.get("verifier", {}).get("enabled", "auto")
        verifier_required = mode in {"verify", "self_consistency"} and verifier_enabled is not False
        return ReasoningPlan(
            user_language=user_lang,
            explicit_output_language=explicit,
            final_output_language=explicit or user_lang or self._config.get("output", {}).get("fallback_language", "en"),
            task_type=task_type,
            task_complexity=complexity,
            risk_level=risk,
            confidence=confidence,
            thinking_language=thinking,
            reasoning_mode=mode,
            verifier_required=verifier_required,
            self_consistency_paths=self._self_consistency_paths(mode),
            tree_branches=self._tree_branches(mode),
            constraints=_as_list(parsed.get("constraints")),
            reasoning_instructions=str(parsed.get("reasoning_instructions") or "Produce a compact structured analysis for the main model."),
        )

    def _plan(self, user_message: str) -> ReasoningPlan:
        if self._cache_enabled and self._cache_plans:
            cached = self._cache.get(user_message)
            if isinstance(cached, ReasoningPlan):
                self._stats["cache_hits"] += 1
                return cached
        planner_cfg = self._config.get("planner", {})
        if not planner_cfg.get("enabled", True):
            return self._planner_fallback(user_message, "planner_disabled")
        try:
            params = _build_llm_params(planner_cfg, 300, 15, "language_router_planner")
            result = self._ctx.llm.complete_structured(
                instructions=PLANNER_PROMPT + "\nUser message:\n" + user_message[:1000],
                input=[{"type": "text", "text": user_message[:1000]}],
                json_mode=True,
                **params,
            )
            self._stats["planner_calls"] += 1
            parsed = result.parsed if isinstance(getattr(result, "parsed", None), dict) else None
            plan = self._parse_plan(parsed or {}, user_message) if parsed else self._planner_fallback(user_message, "planner_non_json")
        except Exception as exc:
            logger.warning("language_router.planner failed: %s", exc)
            self._stats["failures"] += 1
            plan = self._planner_fallback(user_message, "planner_exception")
        if self._cache_enabled and self._cache_plans:
            self._cache.put(user_message, plan)
        logger.info(
            "language_router.plan task=%s user_lang=%s output_lang=%s thinking_lang=%s mode=%s confidence=%.2f",
            plan.task_type, plan.user_language, plan.final_output_language, plan.thinking_language, plan.reasoning_mode, plan.confidence,
        )
        return plan

    def _parse_draft(self, parsed: dict, branch_id: Optional[str] = None) -> ReasoningDraft:
        return ReasoningDraft(
            task_understanding=str(parsed.get("task_understanding") or ""),
            key_points=_as_list(parsed.get("key_points")),
            candidate_conclusions=_as_list(parsed.get("candidate_conclusions")),
            assumptions=_as_list(parsed.get("assumptions")),
            risks=_as_list(parsed.get("risks")),
            missing_information=_as_list(parsed.get("missing_information")),
            suggested_answer_outline=_as_list(parsed.get("suggested_answer_outline")),
            confidence=_clamp_confidence(parsed.get("confidence"), 0.5),
            raw_notes=str(parsed.get("raw_notes")) if parsed.get("raw_notes") and self._config.get("digest", {}).get("include_raw_notes") else None,
            branch_id=branch_id,
            branch_score=_clamp_confidence(parsed.get("branch_score", 0.5), 0.5),
        )

    def _reason(self, user_message: str, plan: ReasoningPlan, path_index: int = 1, branch_id: Optional[str] = None) -> Optional[ReasoningDraft]:
        if plan.reasoning_mode == "off" or not self._config.get("reasoner", {}).get("enabled", True):
            return None
        cfg = self._config.get("reasoner", {})
        try:
            params = _build_llm_params(cfg, 1200, 60, "language_router_reasoner")
            payload = {"plan": plan.__dict__, "path_index": path_index, "branch_id": branch_id, "user_message": user_message[:2000]}
            branch_instruction = f"Branch ID: {branch_id}. " if branch_id else ""
            result = self._ctx.llm.complete_structured(
                instructions=(REASONER_PROMPT + f"\n{branch_instruction}Thinking language: {_get_lang_name(plan.thinking_language)}.\nPlan JSON:\n{_json_for_prompt(plan)}"),
                input=[{"type": "text", "text": json.dumps(payload, ensure_ascii=False, default=str)}],
                json_mode=True,
                **params,
            )
            self._stats["reasoner_calls"] += 1
            parsed = result.parsed if isinstance(getattr(result, "parsed", None), dict) else {}
            draft = self._parse_draft(parsed, branch_id)
            logger.info("language_router.reasoner complete mode=%s branch=%s confidence=%.2f", plan.reasoning_mode, branch_id, draft.confidence)
            return draft
        except Exception as exc:
            logger.warning("language_router.reasoner failed: %s", exc)
            self._stats["failures"] += 1
            return None

    def _merge_drafts(self, drafts: list[ReasoningDraft]) -> Optional[ReasoningDraft]:
        if not drafts:
            return None
        if len(drafts) == 1:
            return drafts[0]
        merged = ReasoningDraft(
            task_understanding=next((d.task_understanding for d in drafts if d.task_understanding), ""),
            confidence=sum(d.confidence for d in drafts) / len(drafts),
        )
        for d in drafts:
            for field in ["key_points", "candidate_conclusions", "assumptions", "risks", "missing_information", "suggested_answer_outline"]:
                seen = getattr(merged, field)
                for item in getattr(d, field):
                    if item not in seen:
                        seen.append(item)
        return merged

    def _select_best_draft(self, drafts: list[ReasoningDraft]) -> Optional[ReasoningDraft]:
        """Self-consistency: 选择置信度最高的草稿。"""
        if not drafts:
            return None
        return max(drafts, key=lambda d: d.confidence)

    def _vote_conclusions(self, drafts: list[ReasoningDraft]) -> list[str]:
        """Self-consistency: 多数投票选择候选结论。"""
        if not drafts:
            return []
        conclusion_counts: dict[str, int] = {}
        for d in drafts:
            for conclusion in d.candidate_conclusions:
                conclusion_counts[conclusion] = conclusion_counts.get(conclusion, 0) + 1
        sorted_conclusions = sorted(conclusion_counts.items(), key=lambda x: -x[1])
        return [c for c, _ in sorted_conclusions[:5]]

    def _prune_tree_branches(self, drafts: list[ReasoningDraft]) -> list[ReasoningDraft]:
        """Tree模式: 根据置信度剪枝。"""
        if not drafts:
            return []
        tree_cfg = self._config.get("reasoning", {}).get("tree", {})
        pruning_threshold = tree_cfg.get("pruning_threshold", 0.6)
        pruned = [d for d in drafts if d.confidence >= pruning_threshold]
        self._stats["tree_pruned"] += len(drafts) - len(pruned)
        logger.info("Tree pruning: %d -> %d branches (threshold=%.2f)", len(drafts), len(pruned), pruning_threshold)
        return pruned if pruned else [max(drafts, key=lambda d: d.confidence)]

    def _merge_tree_branches(self, drafts: list[ReasoningDraft]) -> Optional[ReasoningDraft]:
        """Tree模式: 合并多个分支的结果。"""
        if not drafts:
            return None
        if len(drafts) == 1:
            return drafts[0]
        best = max(drafts, key=lambda d: d.confidence)
        merged = ReasoningDraft(
            task_understanding=best.task_understanding,
            confidence=best.confidence,
            branch_id="merged",
            branch_score=best.branch_score,
        )
        all_key_points = []
        all_conclusions = []
        for d in drafts:
            all_key_points.extend(d.key_points)
            all_conclusions.extend(d.candidate_conclusions)
        seen_points = set()
        for point in all_key_points:
            if point not in seen_points:
                merged.key_points.append(point)
                seen_points.add(point)
        conclusion_counts: dict[str, int] = {}
        for c in all_conclusions:
            conclusion_counts[c] = conclusion_counts.get(c, 0) + 1
        sorted_conclusions = sorted(conclusion_counts.items(), key=lambda x: -x[1])
        merged.candidate_conclusions = [c for c, _ in sorted_conclusions[:5]]
        for field in ["assumptions", "risks", "missing_information", "suggested_answer_outline"]:
            seen = getattr(merged, field)
            for d in drafts:
                for item in getattr(d, field):
                    if item not in seen:
                        seen.append(item)
        return merged

    def _parse_verification(self, parsed: dict) -> VerificationReport:
        verdict = str(parsed.get("verdict") or "accept")
        if verdict not in {"accept", "revise", "reject", "fallback"}:
            verdict = "accept"
        return VerificationReport(
            verdict=verdict,
            issues=_as_list(parsed.get("issues")),
            unsupported_claims=_as_list(parsed.get("unsupported_claims")),
            missed_constraints=_as_list(parsed.get("missed_constraints")),
            safety_notes=_as_list(parsed.get("safety_notes")),
            revised_key_points=_as_list(parsed.get("revised_key_points")),
            revised_answer_outline=_as_list(parsed.get("revised_answer_outline")),
            confidence=_clamp_confidence(parsed.get("confidence"), 0.5),
        )

    def _verify(self, user_message: str, plan: ReasoningPlan, draft: Optional[ReasoningDraft]) -> Optional[VerificationReport]:
        if not draft or not plan.verifier_required:
            return None
        cfg = self._config.get("verifier", {})
        if cfg.get("enabled") is False:
            return None
        if self._budget_manager.should_skip_verifier():
            self._budget_manager.add_notification("Verifier skipped due to low latency budget")
            self._stats["budget_degradations"] += 1
            return None
        try:
            params = _build_llm_params(cfg, 700, 45, "language_router_verifier")
            payload = {"plan": plan.__dict__, "draft": draft.__dict__, "user_message": user_message[:1500]}
            result = self._ctx.llm.complete_structured(
                instructions=VERIFIER_PROMPT + "\nPlan and draft JSON:\n" + json.dumps(payload, ensure_ascii=False, default=str),
                input=[{"type": "text", "text": json.dumps(payload, ensure_ascii=False, default=str)}],
                json_mode=True,
                **params,
            )
            self._stats["verifier_calls"] += 1
            parsed = result.parsed if isinstance(getattr(result, "parsed", None), dict) else {}
            report = self._parse_verification(parsed)
            logger.info("language_router.verifier verdict=%s issues=%d confidence=%.2f", report.verdict, len(report.issues), report.confidence)
            return report
        except Exception as exc:
            logger.warning("language_router.verifier failed: %s", exc)
            self._stats["failures"] += 1
            return VerificationReport(verdict="fallback", issues=["Verifier failed; downgraded to simple digest"], confidence=0.0)

    def _trim_lines(self, lines: list[str], max_tokens: int) -> list[str]:
        out: list[str] = []
        for line in lines:
            candidate = out + [line]
            if self._estimate_tokens("\n".join(candidate)) > max_tokens:
                break
            out.append(line)
        return out

    def _estimate_tokens(self, text: str) -> int:
        return max(1, len(text) // 4)

    def _build_digest(self, plan: ReasoningPlan, draft: Optional[ReasoningDraft], verification: Optional[VerificationReport]) -> InjectedDigest:
        digest_cfg = self._config.get("digest", {})
        max_tokens = int(digest_cfg.get("max_tokens", 500))
        final_lang_name = _get_lang_name(plan.final_output_language)
        verifier_verdict = verification.verdict if verification else "not_run"
        key_points = list(draft.key_points if draft else [])
        outline = list(draft.suggested_answer_outline if draft else [])
        if verification and verification.verdict == "revise":
            key_points = verification.revised_key_points or key_points
            outline = verification.revised_answer_outline or outline
        if verification and verification.verdict in {"reject", "fallback"} and not key_points:
            key_points = ["Use only the user's message and normal Hermes reasoning; plugin verifier did not accept the draft."]
        lines = [
            "\n\n[language-router internal digest]",
            f"User language: {_get_lang_name(plan.user_language)} ({plan.user_language})",
            f"Explicit output language: {plan.explicit_output_language or 'none'}",
            f"Final output language: {final_lang_name} ({plan.final_output_language})",
            f"Task type: {plan.task_type}",
            f"Thinking language used by worker: {_get_lang_name(plan.thinking_language)} ({plan.thinking_language})",
            f"Reasoning mode: {plan.reasoning_mode}",
            f"Verifier verdict: {verifier_verdict}",
            "",
            "Verified digest:",
        ]
        if draft and draft.task_understanding:
            lines.append(f"- Task understanding: {draft.task_understanding}")
        for point in key_points[:8]:
            lines.append(f"- {point}")
        if draft and draft.candidate_conclusions:
            lines.append("Candidate conclusions:")
            for point in draft.candidate_conclusions[:4]:
                lines.append(f"- {point}")
        caveats = []
        if draft:
            caveats.extend(draft.assumptions[:3])
            caveats.extend(draft.risks[:3])
            caveats.extend(draft.missing_information[:3])
        if verification:
            caveats.extend(verification.issues[:3])
            caveats.extend(verification.unsupported_claims[:3])
            caveats.extend(verification.safety_notes[:3])
        if caveats:
            lines.append("Risks / caveats:")
            for item in caveats[:8]:
                lines.append(f"- {item}")
        if outline:
            lines.append("Recommended answer outline:")
            for item in outline[:6]:
                lines.append(f"- {item}")
        lines.extend([
            "Final answer requirement:",
            f"- Reply in {final_lang_name} unless the user explicitly requested another language.",
            "- Treat this digest as auxiliary context, not as a final answer.",
            "- Do not reveal raw internal reasoning or raw notes.",
            "[/language-router internal digest]\n",
        ])
        budget_notifications = self._budget_manager.get_notifications()
        if budget_notifications:
            lines.append("Budget notifications:")
            for notif in budget_notifications:
                lines.append(f"- {notif}")
        lines = self._trim_lines(lines, max_tokens)
        if not lines or not lines[-1].startswith("[/language-router"):
            lines.append("[/language-router internal digest]\n")
        context = "\n".join(lines)
        debug_footer = None
        if self._config.get("debug", {}).get("show_footer"):
            debug_footer = f"[language-router: task={plan.task_type}, user={plan.user_language}, think={plan.thinking_language}, mode={plan.reasoning_mode}, verifier={verifier_verdict}, cache=miss, budget={self._budget_manager.get_degradation_level()}]"
            context += "\n" + debug_footer
        metadata = {
            "plugin": "language-router",
            "version": VERSION,
            "user_language": plan.user_language,
            "explicit_output_language": plan.explicit_output_language,
            "final_output_language": plan.final_output_language,
            "task_type": plan.task_type,
            "thinking_language": plan.thinking_language,
            "reasoning_mode": plan.reasoning_mode,
            "verifier_verdict": verifier_verdict,
            "planner_prompt_version": PLANNER_PROMPT_VERSION,
            "reasoner_prompt_version": REASONER_PROMPT_VERSION,
            "verifier_prompt_version": VERIFIER_PROMPT_VERSION,
            "digest_format_version": DIGEST_FORMAT_VERSION,
            "token_estimate": self._estimate_tokens(context),
            "fallback_reason": plan.fallback_reason,
            "budget_degradation": self._budget_manager.get_degradation_level(),
            "budget_notifications": budget_notifications,
        }
        self._stats["digest_injections"] += 1
        logger.info("language_router.digest injected tokens=%s mode=%s verifier=%s budget=%s", metadata["token_estimate"], plan.reasoning_mode, verifier_verdict, self._budget_manager.get_degradation_level())
        return InjectedDigest(context=context, metadata=metadata, debug_footer=debug_footer, token_estimate=metadata["token_estimate"])

    def on_pre_llm_call(self, user_message: str, system_prompt: str = "", **kwargs: Any) -> Optional[dict]:
        if not user_message or not user_message.strip():
            return None
        self._budget_manager.start()
        started = time.time()
        plan = self._plan(user_message)
        self._detected_languages[plan.user_language] = self._detected_languages.get(plan.user_language, 0) + 1
        self._mode_counts[plan.reasoning_mode] = self._mode_counts.get(plan.reasoning_mode, 0) + 1
        drafts: list[ReasoningDraft] = []
        if plan.reasoning_mode != "off":
            if plan.reasoning_mode == "tree":
                branches = plan.tree_branches
                for idx in range(branches):
                    branch_id = f"branch_{idx + 1}"
                    draft = self._reason(user_message, plan, idx + 1, branch_id)
                    if draft:
                        drafts.append(draft)
                        self._stats["tree_branches"] += 1
                if drafts:
                    drafts = self._prune_tree_branches(drafts)
                    draft = self._merge_tree_branches(drafts)
                    if draft:
                        drafts = [draft]
                self._stats["self_consistency_merges"] += 1
            elif plan.reasoning_mode == "self_consistency":
                paths = plan.self_consistency_paths
                for idx in range(paths):
                    draft = self._reason(user_message, plan, idx + 1)
                    if draft:
                        drafts.append(draft)
                if drafts:
                    best_draft = self._select_best_draft(drafts)
                    voted_conclusions = self._vote_conclusions(drafts)
                    if best_draft:
                        best_draft.candidate_conclusions = voted_conclusions
                        drafts = [best_draft]
                    self._stats["self_consistency_merges"] += 1
            else:
                paths = plan.self_consistency_paths if plan.reasoning_mode == "self_consistency" else 1
                for idx in range(paths):
                    draft = self._reason(user_message, plan, idx + 1)
                    if draft:
                        drafts.append(draft)
        draft = self._merge_drafts(drafts)
        if draft and draft.confidence < self._config.get("verifier", {}).get("confidence_threshold", 0.75) and plan.reasoning_mode == "simple":
            plan.verifier_required = True
            plan.reasoning_mode = "verify"
        verification = self._verify(user_message, plan, draft)
        digest = self._build_digest(plan, draft, verification)
        self._last_run = dict(digest.metadata)
        self._last_run["latency_seconds"] = round(time.time() - started, 3)
        self._last_run["budget_notifications"] = self._budget_manager.get_notifications()
        return {"context": digest.context, "metadata": digest.metadata, "debug_footer": digest.debug_footer}

    def get_stats(self) -> dict:
        cache_stats = self._cache.get_stats()
        return {
            "version": VERSION,
            **self._stats,
            "mode_counts": dict(self._mode_counts),
            "detected_languages": dict(sorted(self._detected_languages.items(), key=lambda x: -x[1])[:10]),
            "cache_enabled": self._cache_enabled,
            "cache": cache_stats,
            "config_summary": {
                "reasoning_mode": self._config.get("reasoning", {}).get("mode"),
                "debug_show_footer": self._config.get("debug", {}).get("show_footer"),
                "digest_max_tokens": self._config.get("digest", {}).get("max_tokens"),
                "verifier_enabled": self._config.get("verifier", {}).get("enabled"),
                "tree_enabled": self._config.get("reasoning", {}).get("tree", {}).get("enabled"),
                "self_consistency_enabled": self._config.get("reasoning", {}).get("self_consistency", {}).get("enabled"),
            },
            "last_run": dict(self._last_run),
            "budget_manager": {
                "enabled": self._budget_manager._enabled,
                "max_seconds": self._budget_manager._max_seconds,
                "current_level": self._budget_manager.get_degradation_level(),
                "remaining_ratio": self._budget_manager.get_remaining_ratio(),
            },
        }


_plugin_instance: Optional[LanguageRouterPlugin] = None


def _get_plugin() -> Optional[LanguageRouterPlugin]:
    return _plugin_instance


def _on_pre_llm_call(**kwargs: Any) -> Optional[dict]:
    plugin = _get_plugin()
    if plugin:
        return plugin.on_pre_llm_call(**kwargs)
    return None


def _handle_stats_command(raw_args: str) -> str:
    plugin = _get_plugin()
    if not plugin:
        return "[language-router] Plugin not initialized."
    stats = plugin.get_stats()
    cache = stats["cache"]
    last = stats.get("last_run") or {}
    budget = stats.get("budget_manager", {})
    lines = [
        "[language-router] Statistics (v4.1 Tree/Self-consistency/Cache/Budget)",
        "=" * 72,
        f"Planner calls:       {stats['planner_calls']}",
        f"Reasoner calls:      {stats['reasoner_calls']}",
        f"Verifier calls:      {stats['verifier_calls']}",
        f"Digest injections:   {stats['digest_injections']}",
        f"Cache hits:          {stats['cache_hits']}",
        f"Failures/fallbacks:   {stats['failures']}/{stats['fallbacks']}",
        f"Tree branches:       {stats['tree_branches']}",
        f"Tree pruned:         {stats['tree_pruned']}",
        f"SC merges:           {stats['self_consistency_merges']}",
        f"Budget degradations: {stats['budget_degradations']}",
        f"Mode distribution:   {stats['mode_counts'] or {}}",
        "",
        "Cache Status:",
        f"  Enabled:  {stats['cache_enabled']}",
        f"  Size:     {cache['size']}/{cache['max_size']}",
        f"  Hit rate: {cache['hit_rate']:.1%}",
        "",
        "Budget Manager:",
        f"  Enabled:        {budget.get('enabled')}",
        f"  Max seconds:    {budget.get('max_seconds')}",
        f"  Current level:  {budget.get('current_level')}",
        f"  Remaining:      {budget.get('remaining_ratio', 0):.1%}",
        "",
        "Config Summary:",
        *[f"  {k}: {v}" for k, v in stats.get("config_summary", {}).items()],
        "",
        "Last Run:",
    ]
    if last:
        for key in ["task_type", "user_language", "final_output_language", "thinking_language", "reasoning_mode", "verifier_verdict", "token_estimate", "latency_seconds", "budget_degradation"]:
            lines.append(f"  {key}: {last.get(key)}")
        if last.get("budget_notifications"):
            lines.append("  Budget notifications:")
            for notif in last["budget_notifications"]:
                lines.append(f"    - {notif}")
    else:
        lines.append("  (no runs yet)")
    return "\n".join(lines)


def _handle_cache_command(raw_args: str) -> str:
    plugin = _get_plugin()
    if not plugin:
        return "[language-router] Plugin not initialized."
    args = raw_args.strip().split()
    if not args:
        return "[language-router] Usage: /language-router-cache <stats|clear|evict|warmup>"
    subcmd = args[0].lower()
    if subcmd == "stats":
        cache_stats = plugin._cache.get_stats()
        lines = [
            "[language-router] Cache Statistics",
            "=" * 40,
            f"Enabled:    {plugin._cache_enabled}",
            f"Size:       {cache_stats['size']}/{cache_stats['max_size']}",
            f"Hit rate:   {cache_stats['hit_rate']:.1%}",
            f"Cache plans: {plugin._cache_plans}",
        ]
        return "\n".join(lines)
    elif subcmd == "clear":
        plugin._cache.clear()
        return "[language-router] Cache cleared."
    elif subcmd == "evict":
        if len(args) < 2:
            return "[language-router] Usage: /language-router-cache evict <key>"
        key = args[1]
        if plugin._cache.evict(key):
            return f"[language-router] Evicted cache entry: {key}"
        else:
            return f"[language-router] Key not found: {key}"
    elif subcmd == "warmup":
        return "[language-router] Cache warmup not yet implemented."
    else:
        return f"[language-router] Unknown cache subcommand: {subcmd}"


def _handle_clear_command(raw_args: str) -> str:
    plugin = _get_plugin()
    if not plugin:
        return "[language-router] Plugin not initialized."
    plugin._cache.clear()
    return "[language-router] Cache cleared."


def register(ctx: PluginContext) -> None:
    global _plugin_instance
    _plugin_instance = LanguageRouterPlugin(ctx)
    ctx.register_hook("pre_llm_call", _on_pre_llm_call)
    ctx.register_command("language-router", handler=_handle_stats_command, description="Show language router v4.1 statistics.")
    ctx.register_command("language-router-cache", handler=_handle_cache_command, description="Manage language router cache (stats/clear/evict/warmup).")
    ctx.register_command("language-router-clear", handler=_handle_clear_command, description="Clear the language router cache.")
    logger.info("Language Router plugin v4.1 registered.")
