# AURA Core

Minimal Python primitives for the AURA evidentiary model.

AURA Core provides reusable building blocks for creating, signing and verifying technical proof manifests for digital assets.

> AURA establishes technical facts. It does not enforce rights.

This repository is the implementation-primitives layer of the AURA ecosystem. It is intentionally small, auditable and platform-independent.

## Position In The AURA Ecosystem

- **AURA-STANDARD**: conceptual and specification layer
  https://github.com/romainbenabdelkader/AURA-STANDARD
- **aura-core**: reusable implementation primitives
  this repository
- **aura-cli**: command-line demonstrator
  https://github.com/romainbenabdelkader/aura-cli

## What AURA Core Provides

- SHA3-256 file hashing
- deterministic JSON canonicalization
- minimal AURA manifest construction
- Ed25519 manifest signing
- Ed25519 signature verification
- file integrity verification against a manifest
- structured verification results

## What AURA Core Does Not Provide

AURA Core is not an application and does not provide:

- CLI workflows
- UI
- DRM
- watermarking
- fingerprinting
- similarity detection
- content recognition
- usage monitoring
- platform-side enforcement
- legal ownership decisions
- infringement or liability decisions

AURA provides a verifiable technical artefact. It does not decide legal ownership, infringement or liability. Law, audit, regulator or court decide.

## Installation

For local development:

```bash
git clone https://github.com/romainbenabdelkader/aura-core
cd aura-core
python -m pip install -e .
```

If your system exposes Python 3 as `python3`, use:

```bash
python3 -m pip install -e .
```

## Example Usage

```python
from aura_core import hashing, manifest, signing, verification

asset_hash = hashing.compute_hash("file.wav")

unsigned_manifest = manifest.create_manifest(
    asset_hash=asset_hash,
    issuer_id="LOCAL-ISSUER",
    asset_type="audio_file",
    asset_title="file.wav",
    asset_filename="file.wav",
    aura_id="AURA-LOCAL-TEST",
)

private_key = signing.generate_private_key()
signed_manifest = signing.sign_manifest(unsigned_manifest, private_key)

result = verification.verify_asset_manifest("file.wav", signed_manifest)

if result.valid:
    print("VALID")
else:
    print(f"INVALID: {result.reason}")
```

## Verification Results

`verification.verify_asset_manifest(...)` returns a structured result with:

- `valid`
- `reason`
- `asset_hash_ok`
- `signature_ok`
- `asset_hash`
- `manifest_hash`

Expected failure reasons:

- `file hash mismatch`
- `manifest signature mismatch`

## Design Principles

- minimal surface
- explicit logic
- deterministic outputs
- no hidden network dependency
- separation of concerns
- no enforcement logic

## Run Tests

```bash
python -m unittest discover
```

or:

```bash
python3 -m unittest discover
```

## Repository Contents

- `aura_core/`: reusable Python primitives
- `tests/`: minimal test coverage for signing and verification
- `spec.md`: human-readable AURA Core specification notes
- `AURA Core Specification.pdf`: PDF version of the specification
- `LICENSE`: Apache License 2.0

## Status

Reference implementation primitives. Not production hardened.

## License

Apache License 2.0
