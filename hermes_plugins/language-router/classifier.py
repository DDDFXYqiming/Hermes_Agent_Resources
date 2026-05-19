"""Task classifier using LLM with structured output.

Enhanced for v3.1 with universal language support.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Any, Optional

logger = logging.getLogger(__name__)


@dataclass
class ClassificationResult:
    """Result of task classification."""
    task_type: str
    thinking_language: str  # "en", "zh", "user", "source"
    confidence: float
    reasoning: str
    raw_response: str = ""


# Universal task type definitions
TASK_TYPES = {
    # Technical tasks (benefit from English thinking)
    "math": "Mathematical reasoning, calculations, equations, proofs",
    "programming": "Code writing, debugging, software development",
    "debug": "Error diagnosis, troubleshooting, fixing issues",
    "logic": "Logical reasoning, formal analysis, deduction",
    "data": "Data analysis, statistics, metrics interpretation",
    
    # Creative/emotional tasks (benefit from user's language thinking)
    "creative": "Creative writing, storytelling, content creation",
    "emotion": "Emotional support, personal conversation, feelings",
    "culture": "Cultural topics, history, traditions, literature",
    
    # General tasks
    "general": "General knowledge, Q&A, mixed topics",
    "translation": "Translation between languages",
}


class TaskClassifier:
    """Classify user messages to determine optimal thinking language.
    
    Uses a fast LLM with thinking mode disabled for low-latency classification.
    When provider/model are not configured, uses the host's current session model.
    
    Returns thinking_language as:
    - "en": Use English for thinking (technical tasks)
    - "zh": Use Chinese for thinking (if applicable)
    - "user": Use the user's detected language for thinking
    - "source": Use the source language (for translation tasks)
    """
    
    def __init__(self, llm: Any, config: dict):
        self._llm = llm
        self._config = config
        self._prompt_template = self._load_prompt()
    
    def _load_prompt(self) -> str:
        """Load the classification prompt template."""
        from .prompts import TASK_CLASSIFICATION_PROMPT
        return TASK_CLASSIFICATION_PROMPT
    
    def classify(self, user_message: str) -> ClassificationResult:
        """Classify a user message and return the optimal thinking language.
        
        Args:
            user_message: The user's input message
            
        Returns:
            ClassificationResult with task_type, thinking_language, confidence, reasoning
        """
        if not user_message or not user_message.strip():
            return ClassificationResult(
                task_type="general",
                thinking_language="user",
                confidence=1.0,
                reasoning="Empty message, default to user language"
            )
        
        # Truncate long messages to save tokens
        truncated = user_message[:500] if len(user_message) > 500 else user_message
        
        try:
            # Build LLM params - only include provider/model if configured
            llm_params = {
                "temperature": self._config.get("temperature", 0.0),
                "max_tokens": self._config.get("max_tokens", 200),
                "timeout": self._config.get("timeout", 15),
                "purpose": "language_router_classification",
            }
            
            # Only override provider/model if explicitly configured
            if self._config.get("provider"):
                llm_params["provider"] = self._config["provider"]
            if self._config.get("model"):
                llm_params["model"] = self._config["model"]
            
            # Call LLM with structured output
            result = self._llm.complete_structured(
                instructions=self._prompt_template + truncated,
                input=[{"type": "text", "text": truncated}],
                json_mode=True,
                **llm_params,
            )
            
            if result.parsed and isinstance(result.parsed, dict):
                task_type = result.parsed.get("task_type", "general")
                # Validate task_type
                if task_type not in TASK_TYPES:
                    task_type = "general"
                
                return ClassificationResult(
                    task_type=task_type,
                    thinking_language=result.parsed.get("thinking_language", "user"),
                    confidence=float(result.parsed.get("confidence", 0.5)),
                    reasoning=result.parsed.get("reasoning", ""),
                    raw_response=result.text,
                )
            else:
                logger.warning("Classification returned non-JSON: %s", result.text[:100])
                return self._fallback_classify(user_message)
                
        except Exception as e:
            logger.warning("Classification failed: %s", e)
            return self._fallback_classify(user_message)
    
    def _fallback_classify(self, user_message: str) -> ClassificationResult:
        """Fallback classification using simple heuristics when LLM fails."""
        msg_lower = user_message.lower()
        
        # Technical keywords → English thinking
        tech_keywords = {
            'code', 'python', 'javascript', 'bug', 'error', 'function', 'variable',
            'algorithm', 'debug', 'compile', 'runtime', 'api', 'database', 'sql',
            '计算', '公式', '数学', '证明', '方程', '算法', '代码', '编程', '调试',
            'git', 'docker', 'linux', 'terminal', 'command', 'script', 'json', 'yaml',
            'rechnen', 'formel', 'mathématiques', 'calcul', 'calcolo', '公式', '計算',
        }
        
        # Math keywords
        math_keywords = {
            'math', 'calculate', 'equation', 'integral', 'derivative', 'matrix',
            '数学', '计算', '积分', '微分', '方程', '矩阵', '概率', '统计',
            'mathematik', 'berechnen', 'mathématiques', 'calculer', 'matematica', 'calcolo',
        }
        
        # Creative/emotional keywords → User language thinking
        creative_keywords = {
            '写', '创作', '文案', '故事', '诗', '创意', '文章', '作文',
            '感觉', '心情', '难过', '开心', '爱', '想念', '聊聊', '谈心',
            '画', '设计', '音乐', '歌', '电影', '小说', '散文',
            'write', 'create', 'story', 'poem', 'creative', 'article',
            'feeling', 'mood', 'sad', 'happy', 'love', 'miss', 'chat',
            'schreiben', 'Geschichte', 'Gedicht', 'écrire', 'histoire', 'poème',
            'scrivere', 'storia', 'poesia',
        }
        
        # Translation keywords
        translation_keywords = {
            'translate', '翻译', '译', '转换成', '转换为',
            'übersetzen', 'traduire', 'tradurre', 'traducir',
        }
        
        if any(kw in msg_lower for kw in math_keywords):
            return ClassificationResult(
                task_type="math",
                thinking_language="en",
                confidence=0.7,
                reasoning="Fallback: detected math keywords"
            )
        elif any(kw in msg_lower for kw in tech_keywords):
            return ClassificationResult(
                task_type="programming",
                thinking_language="en",
                confidence=0.7,
                reasoning="Fallback: detected technical keywords"
            )
        elif any(kw in msg_lower for kw in translation_keywords):
            return ClassificationResult(
                task_type="translation",
                thinking_language="source",
                confidence=0.7,
                reasoning="Fallback: detected translation keywords"
            )
        elif any(kw in msg_lower for kw in creative_keywords):
            return ClassificationResult(
                task_type="creative",
                thinking_language="user",
                confidence=0.7,
                reasoning="Fallback: detected creative/emotional keywords"
            )
        else:
            return ClassificationResult(
                task_type="general",
                thinking_language="en",
                confidence=0.5,
                reasoning="Fallback: default to English for general tasks"
            )
