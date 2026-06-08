"""Deterministic JSON serialization for AURA demo profiles."""

from __future__ import annotations

import json
from typing import Any


def canonical_json_bytes(value: Any) -> bytes:
    """Return deterministic UTF-8 JSON bytes for signing and hashing."""
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def canonical_json_text(value: Any) -> str:
    """Return deterministic JSON text."""
    return canonical_json_bytes(value).decode("utf-8")
