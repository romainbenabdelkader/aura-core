"""Manifest construction and hashing primitives."""

from __future__ import annotations

import copy
from datetime import datetime, timezone
from typing import Any

from aura_core.canonicalization import canonical_json_bytes
from aura_core.hashing import sha256_bytes

AURA_VERSION = "0.1"


def now_utc_iso() -> str:
    """Return an ISO-8601 UTC timestamp."""
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def create_manifest(
    *,
    asset_hash: str,
    issuer_id: str,
    asset_type: str,
    asset_title: str | None = None,
    asset_filename: str | None = None,
    aura_id: str | None = None,
    issued_at: str | None = None,
    rights_reservation: dict[str, Any] | None = None,
    proof_scope: dict[str, Any] | None = None,
    legal_note: str | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Create a minimal unsigned AURA manifest."""
    data: dict[str, Any] = {
        "aura_version": AURA_VERSION,
        "aura_id": aura_id,
        "issuer_id": issuer_id,
        "asset_type": asset_type,
        "asset_title": asset_title,
        "asset_filename": asset_filename,
        "asset_hash_algorithm": "SHA-256",
        "asset_hash": asset_hash,
        "issued_at": issued_at or now_utc_iso(),
        "rights_reservation": rights_reservation or {},
        "proof_scope": proof_scope or {},
        "legal_note": legal_note or "",
    }

    if extra:
        data.update(extra)

    return {key: value for key, value in data.items() if value is not None}


def unsigned_manifest(value: dict[str, Any]) -> dict[str, Any]:
    """Return a deep copy of a manifest without its signature block."""
    data = copy.deepcopy(value)
    data.pop("signature", None)
    return data


def manifest_hash(value: dict[str, Any]) -> str:
    """Return the SHA-256 hash of the canonical unsigned manifest."""
    return sha256_bytes(canonical_json_bytes(unsigned_manifest(value)))
