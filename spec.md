# AURA Core Specification

## 1. Scope

This specification defines the AURA Core manifest format.

AURA Core specifies how factual claims about a digital asset
can be expressed, signed, and verified.

It intentionally does not define:

- identity verification
  
- legal legitimacy
  
- rights enforcement
  
- usage monitoring
  
- licensing mechanisms

These concerns are explicitly out of scope.

---

## 2. Design Principles

AURA Core is designed according to the following principles:

- Minimality: only facts strictly required for evidentiary purposes
  
- Neutrality: no execution, no enforcement, no policy logic
  
- Portability: verification without reliance on a platform
  
- Survivability: usability even under partial or fragmented adoption
  
- Explicit limitations: no claim beyond what can be proven

---

## 3. Core Claims

An AURA manifest MAY assert the following facts:

- The existence of a digital asset at a given time
  
- The integrity of the asset via a cryptographic hash
  
- An attribution claim made by an entity controlling a key
  
- A temporal assertion associated with the declaration

AURA Core does not assert the legal validity of these claims.

---

## 4. Manifest Structure (Informative)

An AURA manifest is a structured document containing at minimum:

- asset_hash
  
- signing_key
  
- declaration
  
- signature

Additional fields MAY be included as extensions.

---

## 5. Signatures

Manifests MUST be signed using a cryptographic key controlled
by the declaring entity.

The signature proves control of the key at the time of signing.
It does not prove legal identity or rights.

---

## 6. Temporal Assertions

Trusted timestamping mechanisms (e.g. RFC 3161) MAY be included
to strengthen evidentiary value but are not mandatory.

When present, a trusted timestamp binds the manifest hash
to a third-party time authority, reducing backdating risks.

## 6.1 Trusted Timestamping (Optional)

AURA Core supports optional trusted timestamping using
independent Time Stamping Authorities (TSAs), such as those
defined in RFC 3161.

When used, the timestamp token MUST cryptographically bind
the manifest hash to the timestamp authority response.

Trusted timestamping:

- increases evidentiary strength

- does not introduce execution or enforcement

- does not create dependency on a single authority

Multiple timestamp authorities MAY be used.
---

## 7. Anchors (Non-Normative)

Manifests MAY reference external anchors such as:

- DNS records
  
- well-known endpoints
  
- operator attestations
  
- web-of-trust assertions

Anchors increase contextual confidence but are not authoritative.

---

## 8. Explicit Non-Goals

AURA Core does NOT aim to:

- prove ownership or legitimacy
  
- prevent copying, scraping, or reuse
  
- enforce compliance or policy
  
- replace judicial or regulatory processes
  
- guarantee adoption or dominance

---

## 9. Threat Model (Assumed Limitations)

AURA Core assumes the following limitations:

- Keys may be compromised
  
- Anchors may be spoofed or centralized
  
- Timestamps may be disputed without third-party corroboration
  
- Many assets will circulate without any AURA manifest

These limitations are inherent and acknowledged.

AURA Core reduces evidentiary uncertainty.
It does not eliminate disputes.

---

## 10. Relationship to Implementations

This specification defines a format, not an implementation.

Tools, services, operators, or platforms MAY implement AURA Core
but are not required for verification.

Verification MUST remain possible without reliance on any operator.

### Informative Timestamp Field Example

An implementation MAY represent a trusted timestamp as:

- timestamp.authority

- timestamp.token

- timestamp.signed_at

This structure is informative and non-normative.