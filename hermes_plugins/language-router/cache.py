"""LRU cache for classification results to avoid redundant LLM calls."""

from __future__ import annotations

import hashlib
import time
import threading
from collections import OrderedDict
from dataclasses import dataclass
from typing import Optional

from .classifier import ClassificationResult


@dataclass
class CacheEntry:
    """A cached classification result."""
    result: ClassificationResult
    timestamp: float
    hit_count: int = 0


class ClassificationCache:
    """Thread-safe LRU cache for task classification results.
    
    Caches based on message content hash to avoid redundant LLM calls
    for similar or repeated messages.
    """
    
    def __init__(self, max_entries: int = 1000, ttl_seconds: int = 300):
        self._cache: OrderedDict[str, CacheEntry] = OrderedDict()
        self._max_entries = max_entries
        self._ttl_seconds = ttl_seconds
        self._lock = threading.Lock()
        self._hits = 0
        self._misses = 0
    
    def _compute_key(self, message: str) -> str:
        """Compute a cache key from message content."""
        # Normalize: lowercase, strip whitespace, take first 200 chars
        normalized = message.lower().strip()[:200]
        return hashlib.md5(normalized.encode('utf-8')).hexdigest()
    
    def get(self, message: str) -> Optional[ClassificationResult]:
        """Get a cached classification result.
        
        Returns:
            ClassificationResult if cache hit, None if miss or expired
        """
        key = self._compute_key(message)
        
        with self._lock:
            entry = self._cache.get(key)
            if entry is None:
                self._misses += 1
                return None
            
            # Check TTL
            if time.time() - entry.timestamp > self._ttl_seconds:
                del self._cache[key]
                self._misses += 1
                return None
            
            # Cache hit
            entry.hit_count += 1
            self._hits += 1
            # Move to end (most recently used)
            self._cache.move_to_end(key)
            return entry.result
    
    def put(self, message: str, result: ClassificationResult) -> None:
        """Cache a classification result."""
        key = self._compute_key(message)
        
        with self._lock:
            # Remove oldest if at capacity
            if len(self._cache) >= self._max_entries:
                self._cache.popitem(last=False)
            
            self._cache[key] = CacheEntry(
                result=result,
                timestamp=time.time(),
            )
    
    def get_stats(self) -> dict:
        """Get cache statistics."""
        with self._lock:
            total = self._hits + self._misses
            return {
                "size": len(self._cache),
                "max_size": self._max_entries,
                "hits": self._hits,
                "misses": self._misses,
                "hit_rate": self._hits / total if total > 0 else 0.0,
                "ttl_seconds": self._ttl_seconds,
            }
    
    def clear(self) -> None:
        """Clear the cache."""
        with self._lock:
            self._cache.clear()
            self._hits = 0
            self._misses = 0
