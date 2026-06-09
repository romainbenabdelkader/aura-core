"""Verification primitives for AURA manifests."""

from __future__ import annotations

import base64
from dataclasses import dataclass
from typing import Any

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from aura_core.canonicalization import canonical_json_bytes
from aura_core.hashing import sha256_file
from aura_core.manifest import manifest_hash, unsigned_manifest


@dataclass(frozen=True)
class VerificationResult:
    """Structured verification result."""

    valid: bool
    reason: str | None
    asset_hash_ok: bool
    signature_ok: bool
    asset_hash: str
    manifest_hash: str


def verify_signature(value: dict[str, Any]) -> bool:
    """Verify the manifest signature against the canonical unsigned manifest."""
    signature = value.get("signature") or {}
    if signature.get("algorithm") != "Ed25519":
        return False

    try:
        public_key = Ed25519PublicKey.from_public_bytes(
            base64.b64decode(signature["public_key"])
        )
        signature_value = base64.b64decode(signature["signature_value"])
        payload = canonical_json_bytes(unsigned_manifest(value))
        public_key.verify(signature_value, payload)
        return True
    except (InvalidSignature, KeyError, TypeError, ValueError):
        return False


def verify_asset_manifest(asset_path: str, value: dict[str, Any]) -> VerificationResult:
    """Verify an asset against its AURA manifest."""
    computed_asset_hash = sha256_file(asset_path)
    signature_ok = verify_signature(value)
    asset_hash_ok = computed_asset_hash == value.get("asset_hash")

    reason = None
    if not signature_ok:
        reason = "manifest signature mismatch"
    elif not asset_hash_ok:
        reason = "file hash mismatch"

    return VerificationResult(
        valid=signature_ok and asset_hash_ok,
        reason=reason,
        asset_hash_ok=asset_hash_ok,
        signature_ok=signature_ok,
        asset_hash=computed_asset_hash,
        manifest_hash=manifest_hash(value),
    )
