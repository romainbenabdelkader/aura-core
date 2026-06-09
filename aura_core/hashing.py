"""Hashing utilities for AURA assets and manifests.

AURA v0.1 mandates SHA3-256 for asset and manifest digests; see the
AURA standard (specs/AURA_v0.1_Draft.md, "Algorithm MUST be SHA3-256").
"""

from __future__ import annotations

import hashlib
from pathlib import Path


def sha3_256_bytes(data: bytes) -> str:
    """Return the SHA3-256 hex digest for bytes."""
    return hashlib.sha3_256(data).hexdigest()


def sha3_256_file(path: str | Path) -> str:
    """Return the SHA3-256 hex digest for a file."""
    digest = hashlib.sha3_256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compute_hash(path: str | Path) -> str:
    """Compatibility alias for file SHA3-256 hashing."""
    return sha3_256_file(path)
