# Contributing

aura-core provides the reference primitives for the AURA evidentiary model
(hashing, canonicalization, manifest construction, Ed25519 signing/verification).

Contributions are welcome via GitHub Issues and Pull Requests.

## Scope

In scope:
- correctness and clarity of the cryptographic primitives
- alignment with the AURA standard (SHA3-256, RFC 8785 canonicalization, Ed25519)
- test coverage and documentation

Out of scope:
- CLI, UI, DRM, watermarking, fingerprinting or rights enforcement
- application-level features (these belong to downstream tools)

## How to contribute

- Open an Issue to discuss a change or report a bug
- Submit a focused, tested Pull Request
- Run the test suite before submitting: `python3 -m unittest discover`

## License

By contributing, you agree that your contribution may be included under the
project license (Apache-2.0).
