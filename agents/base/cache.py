"""LLM response caching for cost optimization."""

import hashlib
import json
import os
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from .llm_provider import LLMMessage, LLMResponse


@dataclass
class CacheEntry:
    """A cached LLM response with metadata."""

    response: LLMResponse
    created_at: datetime
    expires_at: Optional[datetime]
    hit_count: int = 0

    def is_expired(self) -> bool:
        """Check if cache entry has expired."""
        if self.expires_at is None:
            return False
        return datetime.now() > self.expires_at

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "response": self.response.to_dict(),
            "created_at": self.created_at.isoformat(),
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "hit_count": self.hit_count,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "CacheEntry":
        """Create from dictionary."""
        return cls(
            response=LLMResponse.from_dict(data["response"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            expires_at=(
                datetime.fromisoformat(data["expires_at"])
                if data["expires_at"]
                else None
            ),
            hit_count=data.get("hit_count", 0),
        )


class LLMCache:
    """
    Cache for LLM responses to reduce API calls and costs.

    Supports both in-memory and file-based persistence.
    """

    def __init__(
        self,
        cache_dir: Optional[str] = None,
        ttl_hours: Optional[int] = 24,
        max_entries: int = 1000,
    ):
        """
        Initialize the cache.

        Args:
            cache_dir: Directory for persistent cache (None for memory-only)
            ttl_hours: Time-to-live in hours (None for no expiration)
            max_entries: Maximum cache entries before eviction
        """
        self._memory_cache: dict[str, CacheEntry] = {}
        self._cache_dir = Path(cache_dir) if cache_dir else None
        self._ttl = timedelta(hours=ttl_hours) if ttl_hours else None
        self._max_entries = max_entries
        self._total_hits = 0
        self._total_misses = 0

        if self._cache_dir:
            self._cache_dir.mkdir(parents=True, exist_ok=True)
            self._load_from_disk()

    def _compute_key(self, messages: list[LLMMessage], **kwargs) -> str:
        """Compute a cache key from messages and parameters."""
        key_data = {
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "kwargs": kwargs,
        }
        key_json = json.dumps(key_data, sort_keys=True)
        return hashlib.sha256(key_json.encode()).hexdigest()[:32]

    def get(
        self, messages: list[LLMMessage], **kwargs
    ) -> Optional[LLMResponse]:
        """
        Get a cached response if available.

        Args:
            messages: The messages to look up
            **kwargs: Additional parameters used in the request

        Returns:
            Cached LLMResponse or None if not found/expired
        """
        key = self._compute_key(messages, **kwargs)
        entry = self._memory_cache.get(key)

        if entry is None:
            self._total_misses += 1
            return None

        if entry.is_expired():
            del self._memory_cache[key]
            self._total_misses += 1
            return None

        entry.hit_count += 1
        self._total_hits += 1

        # Return a copy marked as cached
        response = entry.response
        return LLMResponse(
            content=response.content,
            model=response.model,
            input_tokens=response.input_tokens,
            output_tokens=response.output_tokens,
            cost_usd=0.0,  # No cost for cached responses
            cached=True,
        )

    def set(
        self, messages: list[LLMMessage], response: LLMResponse, **kwargs
    ) -> None:
        """
        Cache a response.

        Args:
            messages: The messages used in the request
            response: The response to cache
            **kwargs: Additional parameters used in the request
        """
        # Evict if at capacity
        if len(self._memory_cache) >= self._max_entries:
            self._evict_oldest()

        key = self._compute_key(messages, **kwargs)
        expires_at = datetime.now() + self._ttl if self._ttl else None

        entry = CacheEntry(
            response=response,
            created_at=datetime.now(),
            expires_at=expires_at,
        )
        self._memory_cache[key] = entry

        if self._cache_dir:
            self._save_entry(key, entry)

    def _evict_oldest(self) -> None:
        """Remove the oldest cache entry."""
        if not self._memory_cache:
            return

        oldest_key = min(
            self._memory_cache.keys(),
            key=lambda k: self._memory_cache[k].created_at,
        )
        del self._memory_cache[oldest_key]

        if self._cache_dir:
            cache_file = self._cache_dir / f"{oldest_key}.json"
            if cache_file.exists():
                cache_file.unlink()

    def _save_entry(self, key: str, entry: CacheEntry) -> None:
        """Save a cache entry to disk."""
        if not self._cache_dir:
            return

        cache_file = self._cache_dir / f"{key}.json"
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(entry.to_dict(), f, indent=2)

    def _load_from_disk(self) -> None:
        """Load cache entries from disk."""
        if not self._cache_dir or not self._cache_dir.exists():
            return

        for cache_file in self._cache_dir.glob("*.json"):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    entry = CacheEntry.from_dict(data)

                    if entry.is_expired():
                        cache_file.unlink()
                        continue

                    key = cache_file.stem
                    self._memory_cache[key] = entry
            except (json.JSONDecodeError, KeyError, ValueError):
                # Invalid cache file, remove it
                cache_file.unlink()

    def clear(self) -> None:
        """Clear all cache entries."""
        self._memory_cache.clear()

        if self._cache_dir:
            for cache_file in self._cache_dir.glob("*.json"):
                cache_file.unlink()

    def get_stats(self) -> dict:
        """Get cache statistics."""
        total_requests = self._total_hits + self._total_misses
        hit_rate = self._total_hits / total_requests if total_requests > 0 else 0.0

        return {
            "entries": len(self._memory_cache),
            "max_entries": self._max_entries,
            "total_hits": self._total_hits,
            "total_misses": self._total_misses,
            "hit_rate": hit_rate,
            "persistent": self._cache_dir is not None,
        }
