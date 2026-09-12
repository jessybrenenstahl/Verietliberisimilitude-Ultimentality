---
slug: attack-surface-matrix
title: The Attack-Surface Matrix
section: postfalsifiability-and-crystallization
page_type: navigation
formal_status:
  epistemic: Derived
  tier: Exposition
  alethic: inherits per-page accuracy marks; asserts no new world-mapping claim of its own
prerequisites: [two-mark-system, outcomes-of-attack, attack-type-matching]
regulates: ["unlocated attacks", "attack/claim-type mismatch", "page-to-mark drift"]
regulated_by: [self-sealing-test, causal-falsifiability, same-level-attack-rule]
valid_attack: "Show a generated row differs from its source metadata or the metadata misstates the source claim."
isolation_failure: "As a static catalog detached from the causal-falsifiability and self-sealing tests, the matrix becomes a decorative index that no encounter can force to change."
kill_condition: "The index cannot reproduce current source metadata or falsely reports executable coverage."
see_also: [attack-type-matching, same-level-attack-rule, causal-falsifiability, self-sealing-test, outcomes-of-attack, system-invariants, coupling-graph, interaction-matrix, category-error-atlas, kill-table]
application_tags: []
---
[[home|← Ultimentality Wiki]]

# The Attack-Surface Matrix

This table is generated from the current structured metadata of the source pages. It indexes their stated challenges and revision conditions; it does not independently validate those conditions or claim that they exhaust all possible criticism. Pages without structured metadata remain accessible through the [[kill-table|kill-table]] and their linked definitions.

<!-- GENERATED:attacks -->

The published JSON is checked against the same source metadata. A row changes when its source changes, preventing a separate handwritten summary from silently overriding the page. The metadata itself remains reviewable.

“Not registered” means no executable test reference is recorded in this index. It does not prove that no review has occurred, and it does not make a conceptual claim untestable. [[outcomes-of-attack|Supporting evidence, failed objections, and implemented changes]] are separate results; [[self-sealing-test|diagnostic verdicts]] need evidence.

## Data contract and coverage boundary

The current export renders five fields: page, claim type, challenge, revision condition, and executable-test references. The underlying records retain regulators and isolation failures for machine use. The `invalid_attacks` field is currently emitted as an empty list; it does not preserve source-page exclusions. Earlier versions exposed separate `error_surface`, `emergent_property`, and `linked_page` columns; those are not currently separate fields in the export and must be recovered from the source page before this index is treated as a complete audit specification. Their absence here is a compression boundary, not evidence that the relations are absent from the framework.

The source page remains the authority for those richer relations. A conceptual challenge can therefore be fully articulated while its executable fixture is still unregistered; the two states must not be collapsed.

## How to use the index

Read a row as a four-step review path: open the source page, restate the exact claim and scope, test the listed challenge, and record the result and any implemented change. The generated row is a synchronization aid; the source page remains the authority for the claim it describes. A page can acquire a stronger test without acquiring a less-contestable status.

## Formal status

> **E:** Derived, Exposition — a maintained index of page-level challenges and revision conditions. **A:** inherits each page's accuracy marks and aims to reproduce its declared attack surface without implying exhaustive criticism. **Provenance:** treatise-side publication surface generated from current page metadata; “Not registered” records missing executable coverage rather than a philosophical exemption.

## See also

[[attack-type-matching|Attack-Type Matching]] · [[same-level-attack-rule|The Same-Level Attack Rule]] · [[causal-falsifiability|Causal Falsifiability]] · [[self-sealing-test|The Self-Sealing Test]] · [[outcomes-of-attack|The Outcomes of Attack]] · [[system-invariants|System Invariants]] · [[coupling-graph|The Coupling Graph]] · [[interaction-matrix|The Interaction Matrix]] · [[category-error-atlas|The Category-Error Atlas]] · [[kill-table|The Kill-Table]]
