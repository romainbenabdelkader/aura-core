"""Ed25519 signing primitives for AURA manifests."""

from __future__ import annotations

import base64
import copy
from typing import Any

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from aura_core.canonicalization import canonical_json_bytes
from aura_core.manifest import unsigned_manifest


def generate_private_key() -> Ed25519PrivateKey:
    """Generate a new Ed25519 private key."""
    return Ed25519PrivateKey.generate()


def public_key_b64(public_key: Ed25519PublicKey) -> str:
    """Return a base64-encoded raw Ed25519 public key."""
    raw = public_key.public_bytes(
        encoding=Encoding.Raw,
        format=PublicFormat.Raw,
    )
    return base64.b64encode(raw).decode("ascii")


def sign_bytes(data: bytes, private_key: Ed25519PrivateKey) -> str:
    """Sign bytes and return a base64 signature."""
    return base64.b64encode(private_key.sign(data)).decode("ascii")


def sign_manifest(
    value: dict[str, Any],
    private_key: Ed25519PrivateKey,
) -> dict[str, Any]:
    """Return a signed copy of an AURA manifest."""
    signed = copy.deepcopy(value)
    payload = canonical_json_bytes(unsigned_manifest(signed))
    signed["signature"] = {
        "algorithm": "Ed25519",
        "public_key": public_key_b64(private_key.public_key()),
        "signature_value": sign_bytes(payload, private_key),
    }
    return signed
