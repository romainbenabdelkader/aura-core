# AURA Core — Reference Implementation Primitives

AURA Core provides minimal, reusable primitives for implementing the AURA evidentiary model.

> AURA establishes facts. It does not enforce rights.

This repository currently provides a reference specification and evolving implementation primitives.  
The AURA CLI testbed demonstrates a working implementation of these concepts.

This repository contains the technical building blocks used to:
- generate manifests
- canonicalize data
- sign declarations
- verify integrity and signatures

It is designed to be:
- minimal
- auditable
- platform-independent

---

## Purpose

AURA Core is not an application.

It is a low-level library intended to:
- support implementations of AURA
- ensure consistency across environments
- provide a reference for developers and auditors

---

## Position in the AURA ecosystem

- **AURA-STANDARD** → specification
- **aura-core** → implementation primitives
- **aura-cli** → demonstrator

---

## What it provides

- hashing utilities (SHA256)
- manifest construction
- canonical JSON handling
- Ed25519 signing
- signature verification
- integrity checks

---

## What it does NOT provide

- CLI
- UI
- platform integration
- watermarking
- fingerprinting
- content recognition
- monitoring
- enforcement

---

## Example usage

```python
from aura_core import hashing, manifest, signing, verification

# hash
h = hashing.compute_hash("file.wav")

# manifest
m = manifest.create_manifest(hash=h)

# sign
sig = signing.sign(m, private_key)

# verify
verification.verify(m, sig, public_key)

Design principles
	•	minimal surface
	•	explicit logic
	•	no hidden behaviour
	•	deterministic outputs
	•	separation of concerns

⸻

Status

Reference implementation.
Not production hardened.

⸻

License

Apache License 2.0