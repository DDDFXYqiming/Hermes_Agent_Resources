"""Language Router Plugin v3.1 — Universal Research-Enhanced Multilingual Thinking.

Based on academic research:
- "The Impact of Language Mixing on Bilingual LLM Reasoning" (EMNLP 2025)
- "Could Thinking Multilingually Empower LLM Reasoning?" (2025)
- "AdaMCoT: Adaptive Multilingual Chain-of-Thought" (AAAI 2025)

KEY DESIGN PRINCIPLE: UNIVERSALITY
- Thinking language: Task-adaptive based on classifier decision
- Output language: ALWAYS aligned with user's input language (auto-detected)
- Works for ANY language pair, not just Chinese-English

Research findings implemented:
1. Language mixing ENHANCES reasoning (5.6% accuracy drop when forced monolingual)
2. Multilingual thinking has HIGHER upper bound (~10 Acc@k points)
3. Different tasks benefit from different thinking languages
4. Output should always match user's language for best UX

Config in $HERMES_HOME/config.yaml:
  plugins:
    entries:
      language-router:
        config: {}
"""

from __future__ import annotations

import logging
import re
from typing import Any, Optional, Dict, List, Tuple

from hermes_cli.plugins import PluginContext
from hermes_cli.config import cfg_get

from .classifier import TaskClassifier, ClassificationResult
from .cache import ClassificationCache

logger = logging.getLogger(__name__)

# Language detection patterns (universal)
# Priority: Check unique scripts first (Hiragana/Katakana for Japanese)
LANG_PATTERNS = {
    "ja_hiragana": re.compile(r'[\u3040-\u309f]'),  # Japanese Hiragana (unique)
    "ja_katakana": re.compile(r'[\u30a0-\u30ff]'),  # Japanese Katakana (unique)
    "zh": re.compile(r'[\u4e00-\u9fff]'),           # Chinese characters
    "ko": re.compile(r'[\uac00-\ud7af]'),            # Korean
    "ar": re.compile(r'[\u0600-\u06ff]'),            # Arabic
    "ru": re.compile(r'[\u0400-\u04ff]'),            # Russian
    "hi": re.compile(r'[\u0900-\u097f]'),            # Hindi
    "th": re.compile(r'[\u0e00-\u0e7f]'),            # Thai
    # Latin-based languages detected by common word patterns
    "de": re.compile(r'\b(der|die|das|und|ist|ein|eine|auf|mit)\b', re.I),
    "fr": re.compile(r'\b(le|la|les|des|une|est|dans|pour|avec)\b', re.I),
    "es": re.compile(r'\b(el|la|los|las|una|es|en|por|con|para)\b', re.I),
    "pt": re.compile(r'\b(o|a|os|as|uma|é|em|por|com|para)\b', re.I),
    "it": re.compile(r'\b(il|la|gli|le|una|è|in|per|con|di)\b', re.I),
}

# Research-based task-language mapping (universal)
TASK_LANGUAGE_STRATEGY = {
    # Technical tasks: English primary (research shows better formal reasoning)
    "math": {"primary": "en", "mix_ratio": 0.3},
    "programming": {"primary": "en", "mix_ratio": 0.2},
    "debug": {"primary": "en", "mix_ratio": 0.2},
    "logic": {"primary": "en", "mix_ratio": 0.3},
    "data": {"primary": "en", "mix_ratio": 0.2},
    
    # Creative/emotional tasks: User's language primary
    "creative": {"primary": "user", "mix_ratio": 0.1},
    "emotion": {"primary": "user", "mix_ratio": 0.0},
    "culture": {"primary": "user", "mix_ratio": 0.1},
    
    # General: Balanced
    "general": {"primary": "en", "mix_ratio": 0.2},
    "translation": {"primary": "source", "mix_ratio": 0.0},
}

# Language code to human-readable name mapping
LANG_NAMES = {
    "en": "English", "zh": "Chinese", "ja": "Japanese", "ko": "Korean",
    "de": "German", "fr": "French", "es": "Spanish", "pt": "Portuguese",
    "it": "Italian", "ru": "Russian", "ar": "Arabic", "hi": "Hindi",
    "th": "Thai", "vi": "Vietnamese", "nl": "Dutch", "pl": "Polish",
    "tr": "Turkish", "sv": "Swedish", "da": "Danish", "fi": "Finnish",
    "no": "Norwegian", "id": "Indonesian", "ms": "Malay", "tl": "Filipino",
}

DEFAULTS = {
    "temperature": 0.0,
    "max_tokens_classifier": 200,
    "max_tokens_reasoning": 1500,
    "timeout_classifier": 15,
    "timeout_reasoning": 60,
    "reasoning_effort": "high",
}


def _detect_language(text: str) -> str:
    """Detect the primary language of text.
    
    Returns ISO 639-1 language code (e.g., 'en', 'zh', 'ja').
    Falls back to 'en' if detection fails.
    
    Detection priority:
    1. Unique scripts (Hiragana/Katakana for Japanese)
    2. CJK characters (Chinese, Korean)
    3. Other non-Latin scripts (Arabic, Russian, Hindi, Thai)
    4. Latin-based languages (German, French, Spanish, etc.)
    """
    if not text or not text.strip():
        return "en"
    
    # Pattern-based detection (fast, no dependencies)
    scores = {}
    for lang, pattern in LANG_PATTERNS.items():
        matches = pattern.findall(text[:300])
        scores[lang] = len(matches)
    
    # Check Japanese first (Hiragana/Katakana are unique to Japanese)
    if scores.get("ja_hiragana", 0) > 0 or scores.get("ja_katakana", 0) > 0:
        return "ja"
    
    # Check other non-Latin scripts (CJK, Arabic, Russian, etc.)
    for lang in ["zh", "ko", "ar", "ru", "hi", "th"]:
        if scores.get(lang, 0) > 0:
            return lang
    
    # For Latin-based languages, check word patterns
    if scores.get("de", 0) > 3:
        return "de"
    if scores.get("fr", 0) > 3:
        return "fr"
    if scores.get("es", 0) > 3:
        return "es"
    if scores.get("pt", 0) > 3:
        return "pt"
    if scores.get("it", 0) > 3:
        return "it"
    
    # Default to English for Latin script
    return "en"


def _get_lang_name(lang_code: str) -> str:
    """Get human-readable language name from code."""
    return LANG_NAMES.get(lang_code, lang_code.upper())


def _load_plugin_config() -> dict:
    """Load plugin config from config.yaml."""
    from hermes_constants import get_hermes_home
    config_path = get_hermes_home() / "config.yaml"
    if not config_path.exists():
        return {}
    try:
        import yaml
        with open(config_path, encoding="utf-8") as f:
            all_config = yaml.safe_load(f) or {}
        return cfg_get(all_config, "plugins", "entries", "language-router", "config", default={}) or {}
    except Exception:
        return {}


def _build_llm_params(section_cfg: dict) -> dict:
    """Build LLM call params from config section."""
    params = {}
    if section_cfg.get("provider"):
        params["provider"] = section_cfg["provider"]
    if section_cfg.get("model"):
        params["model"] = section_cfg["model"]
    params["temperature"] = section_cfg.get("temperature", DEFAULTS["temperature"])
    params["timeout"] = section_cfg.get("timeout", DEFAULTS["timeout_classifier"])
    return params


class LanguageRouterPlugin:
    """Research-enhanced language router with universal language support."""
    
    def __init__(self, ctx: PluginContext):
        self._ctx = ctx
        self._config = _load_plugin_config()
        logger.info("Language Router v3.1 config loaded: %s", self._config)
        
        # Build classifier params
        classifier_cfg = self._config.get("classifier", {})
        self._classifier_params = _build_llm_params(classifier_cfg)
        self._classifier_params["max_tokens"] = classifier_cfg.get("max_tokens", DEFAULTS["max_tokens_classifier"])
        
        # Initialize classifier
        self._classifier = TaskClassifier(
            llm=ctx.llm,
            config=classifier_cfg if classifier_cfg else {"provider": None, "model": None},
        )
        
        # Build reasoning params
        reasoning_cfg = self._config.get("reasoning", {})
        self._reasoning_params = _build_llm_params(reasoning_cfg)
        self._reasoning_params["max_tokens"] = reasoning_cfg.get("max_tokens", DEFAULTS["max_tokens_reasoning"])
        self._reasoning_effort = reasoning_cfg.get("reasoning_effort", DEFAULTS["reasoning_effort"])
        
        # Initialize cache
        cache_cfg = self._config.get("cache", {})
        self._cache = ClassificationCache(
            max_entries=cache_cfg.get("max_entries", 1000),
            ttl_seconds=cache_cfg.get("ttl_seconds", 300),
        )
        
        # Stats
        self._total_classifications = 0
        self._cache_hits = 0
        self._two_pass_calls = 0
        self._detected_languages = {}
        
        logger.info("Language Router v3.1 initialized (universal)")
    
    def _classify(self, user_message: str) -> ClassificationResult:
        """Classify the user message."""
        self._total_classifications += 1
        
        cached_result = self._cache.get(user_message)
        if cached_result:
            self._cache_hits += 1
            return cached_result
        
        classification = self._classifier.classify(user_message)
        self._cache.put(user_message, classification)
        
        logger.info(
            "Language router classified: task=%s, thinking_lang=%s, confidence=%.2f",
            classification.task_type, classification.thinking_language, classification.confidence,
        )
        return classification
    
    def _build_reasoning_prompt(
        self,
        user_message: str,
        task_type: str,
        user_lang: str,
        thinking_lang: str,
    ) -> Tuple[str, str]:
        """Build reasoning system prompt based on research.
        
        Returns: (system_prompt, output_instruction)
        """
        effort = self._reasoning_effort
        user_lang_name = _get_lang_name(user_lang)
        
        # Determine actual thinking language
        if thinking_lang == "user":
            actual_thinking_lang = user_lang
            actual_thinking_lang_name = user_lang_name
        elif thinking_lang == "source":
            actual_thinking_lang = user_lang
            actual_thinking_lang_name = user_lang_name
        else:
            actual_thinking_lang = thinking_lang
            actual_thinking_lang_name = _get_lang_name(thinking_lang)
        
        # Build thinking instruction based on research
        strategy = TASK_LANGUAGE_STRATEGY.get(task_type, TASK_LANGUAGE_STRATEGY["general"])
        mix_ratio = strategy.get("mix_ratio", 0.0)
        
        if actual_thinking_lang != "en" and mix_ratio > 0:
            thinking_instruction = (
                f"Think primarily in {actual_thinking_lang_name}. "
                f"You may switch to English for technical terms or complex reasoning steps. "
                f"Language mixing is allowed if it improves reasoning clarity."
            )
        elif actual_thinking_lang == "en":
            thinking_instruction = (
                f"Think step by step in English. "
                f"You may use technical terms from other languages if appropriate."
            )
        else:
            thinking_instruction = f"Think step by step in {actual_thinking_lang_name}."
        
        # Output instruction: ALWAYS match user's language
        output_instruction = (
            f"Your final answer MUST be in {user_lang_name} to match the user's input language. "
            f"Do not output in any other language."
        )
        
        system_prompt = (
            f"You are a reasoning assistant optimized for {task_type} tasks. "
            f"{thinking_instruction} "
            f"Reasoning effort level: {effort}. "
            f"Provide detailed analysis and reasoning. "
            f"{output_instruction}"
        )
        
        return system_prompt, output_instruction
    
    def _two_pass_reasoning(
        self,
        user_message: str,
        task_type: str,
        user_lang: str,
        thinking_lang: str,
    ) -> str:
        """Execute Two-Pass reasoning with universal language support."""
        system_prompt, _ = self._build_reasoning_prompt(
            user_message, task_type, user_lang, thinking_lang
        )
        
        truncated_message = user_message[:500] if len(user_message) > 500 else user_message
        
        try:
            params = dict(self._reasoning_params)
            params["purpose"] = "language_router_reasoning"
            
            result = self._ctx.llm.complete(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": truncated_message},
                ],
                **params,
            )
            
            self._two_pass_calls += 1
            logger.info("Two-Pass reasoning completed: task=%s, user_lang=%s", task_type, user_lang)
            return result.text
            
        except Exception as e:
            logger.warning("Two-Pass reasoning failed: %s", e)
            return ""
    
    def on_pre_llm_call(
        self,
        user_message: str,
        system_prompt: str = "",
        **kwargs: Any,
    ) -> Optional[dict]:
        """Hook: Universal language routing before LLM call.
        
        Flow:
        1. Detect user's language (auto)
        2. Classify task type (LLM)
        3. Determine thinking language (task-adaptive)
        4. Execute Two-Pass reasoning
        5. Inject with output language alignment
        """
        if not user_message or not user_message.strip():
            return None
        
        # Step 1: Detect user's language (universal)
        user_lang = _detect_language(user_message)
        self._detected_languages[user_lang] = self._detected_languages.get(user_lang, 0) + 1
        logger.debug("Detected user language: %s", user_lang)
        
        # Step 2: Classify the task
        classification = self._classify(user_message)
        
        confidence_threshold = self._config.get("confidence_threshold", 0.6)
        if classification.confidence < confidence_threshold:
            logger.debug("Confidence %.2f below threshold %.2f, skipping",
                        classification.confidence, confidence_threshold)
            return None
        
        task_type = classification.task_type
        thinking_lang = classification.thinking_language
        
        # Step 3: Resolve thinking language
        strategy = TASK_LANGUAGE_STRATEGY.get(task_type, TASK_LANGUAGE_STRATEGY["general"])
        if strategy["primary"] == "user":
            resolved_thinking_lang = user_lang
        else:
            resolved_thinking_lang = thinking_lang if thinking_lang != "source" else user_lang
        
        # Step 4: Execute Two-Pass reasoning
        reasoning_text = self._two_pass_reasoning(
            user_message, task_type, user_lang, resolved_thinking_lang
        )
        
        if reasoning_text:
            # Step 5: Inject reasoning with clear output language instruction
            user_lang_name = _get_lang_name(user_lang)
            return {
                "context": (
                    f"\n\n[Internal reasoning - thinking in {resolved_thinking_lang}]\n"
                    f"{reasoning_text}\n\n"
                    f"[IMPORTANT: Your final answer MUST be in {user_lang_name} "
                    f"to match the user's input language.]\n"
                )
            }
        else:
            user_lang_name = _get_lang_name(user_lang)
            return {
                "context": f"\n\n[Respond in {user_lang_name} to match the user's language.]"
            }
    
    def get_stats(self) -> dict:
        """Get plugin statistics."""
        cache_stats = self._cache.get_stats()
        return {
            "version": "3.1",
            "total_classifications": self._total_classifications,
            "cache_hits": self._cache_hits,
            "cache_hit_rate": self._cache_hits / self._total_classifications if self._total_classifications > 0 else 0.0,
            "llm_calls": self._total_classifications - self._cache_hits,
            "two_pass_calls": self._two_pass_calls,
            "detected_languages": dict(sorted(
                self._detected_languages.items(),
                key=lambda x: -x[1]
            )[:10]),
            "classifier_overrides": {k: v for k, v in self._classifier_params.items() if k in ("provider", "model")},
            "reasoning_overrides": {k: v for k, v in self._reasoning_params.items() if k in ("provider", "model")},
            "reasoning_effort": self._reasoning_effort,
            "cache": cache_stats,
        }


# Plugin singleton
_plugin_instance: Optional[LanguageRouterPlugin] = None


def _get_plugin() -> Optional[LanguageRouterPlugin]:
    """Get or create the plugin singleton."""
    return _plugin_instance


def _on_pre_llm_call(**kwargs: Any) -> Optional[dict]:
    """Hook wrapper for pre_llm_call."""
    plugin = _get_plugin()
    if plugin:
        return plugin.on_pre_llm_call(**kwargs)
    return None


def _handle_stats_command(raw_args: str) -> str:
    """Slash command to show plugin statistics."""
    plugin = _get_plugin()
    if not plugin:
        return "[language-router] Plugin not initialized."
    
    stats = plugin.get_stats()
    cache = stats["cache"]
    
    classifier_info = stats["classifier_overrides"] or "host default"
    reasoning_info = stats["reasoning_overrides"] or "host default"
    
    lang_lines = []
    for lang, count in stats.get("detected_languages", {}).items():
        lang_name = _get_lang_name(lang)
        lang_lines.append(f"    {lang_name} ({lang}): {count}")
    lang_section = "\n".join(lang_lines) if lang_lines else "    (no data yet)"
    
    lines = [
        "[language-router] Statistics (v3.1 Universal)",
        "=" * 60,
        f"Total classifications: {stats['total_classifications']}",
        f"Cache hits:           {stats['cache_hits']}",
        f"Cache hit rate:       {stats['cache_hit_rate']:.1%}",
        f"LLM calls:            {stats['llm_calls']}",
        f"Two-Pass calls:       {stats['two_pass_calls']}",
        "",
        "Detected Languages:",
        lang_section,
        "",
        "Model Config:",
        f"  Classifier: {classifier_info}",
        f"  Reasoning:  {reasoning_info}",
        f"  Effort:     {stats['reasoning_effort']}",
        "",
        "Cache Status:",
        f"  Size:     {cache['size']}/{cache['max_size']}",
        f"  TTL:      {cache['ttl_seconds']}s",
        f"  Hit rate: {cache['hit_rate']:.1%}",
        "",
        "Design Principles (Universal):",
        "  - Thinking: Task-adaptive language (not fixed)",
        "  - Output: Auto-aligned with user's input language",
        "  - Works for ANY language pair",
        "",
        "Research Basis:",
        "  - Language mixing enhances reasoning (+5.6%)",
        "  - Multilingual thinking higher upper bound",
        "  - Task-adaptive language selection",
    ]
    
    return "\n".join(lines)


def _handle_clear_command(raw_args: str) -> str:
    """Slash command to clear the cache."""
    plugin = _get_plugin()
    if not plugin:
        return "[language-router] Plugin not initialized."
    plugin._cache.clear()
    return "[language-router] Cache cleared."


def register(ctx: PluginContext) -> None:
    """Plugin registration entry point."""
    global _plugin_instance
    _plugin_instance = LanguageRouterPlugin(ctx)
    ctx.register_hook("pre_llm_call", _on_pre_llm_call)
    ctx.register_command(
        "language-router",
        handler=_handle_stats_command,
        description="Show language router statistics (v3.1 universal).",
    )
    ctx.register_command(
        "language-router-clear",
        handler=_handle_clear_command,
        description="Clear the language router cache.",
    )
    logger.info("Language Router plugin v3.1 registered (universal).")
