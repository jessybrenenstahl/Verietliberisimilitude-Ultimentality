---
slug: interaction-matrix
title: The Interaction Matrix
section: synthesis-and-navigation
page_type: navigation
formal_status:
  epistemic: Derived
  tier: Exposition
  alethic: "aspires to record the first-order relations actually borne by the crossed pages; a cell is accurate only insofar as its linked endpoints support it, and inaccuracy shows as a cell the source pages do not sustain"
prerequisites: [coupling-graph, attack-surface-matrix, semantic-closure-and-recursive-marking]
regulates:
  - "vague or unlabeled cross-references between load-bearing pages"
  - "silent relations a reader would otherwise reconstruct by comparing distant pages"
regulated_by:
  - system-invariants
  - attack-surface-matrix
  - coupling-graph
  - "manual review of wiki-interactions.json against the pages each cell claims to index"
valid_attack: "Exhibit a load-bearing relation that no controlled label expresses without loss, forcing a vague label or an assertion the endpoints do not carry."
isolation_failure: "Cut from its source pages and the invariant checklist, the matrix hardens into an unaudited adjacency table whose cells no longer answer to the pages they index."
kill_condition: "A nonempty cell cannot be regenerated from wiki-interactions.json and its linked pages, or the matrix asserts a relation its two endpoints do not bear."
see_also: [coupling-graph, attack-surface-matrix, system-invariants, prohibited-collapses, category-error-atlas, reader-paths, semantic-closure-and-recursive-marking, reciprocal-attack-surfaces, cross-regulated-necessity, one-page-reconstruction]
application_tags: []
---
[[home|← Ultimentality Wiki]]


# The Interaction Matrix

## Definition

The Interaction Matrix is the component-by-component grid in which every load-bearing part of the framework is crossed with every other, and each nonempty cell records the **single controlled relation label** by which the row component acts on the column component. It exists to make explicit the relations a reader would otherwise have to reconstruct by holding several distant pages side by side. Where the [[coupling-graph|Coupling Graph]] shows the highlighted regulatory pairs as a network and the [[attack-surface-matrix|Attack-Surface Matrix]] tabulates each component's defenses, the Interaction Matrix is the dense adjacency view: it answers, for any ordered pair, *what is the load-bearing first-order relation from this one to that one, named in a closed vocabulary.*

The matrix is **directional and non-symmetric.** A cell at row `R`, column `C` reads "`R` **[label]** `C`." The transpose cell `(C, R)` is a separate assertion and may carry a different label, the inverse label, or none. A blank cell (rendered `·`) asserts *no first-order interaction* between that ordered pair — it is silence, not denial. Only a `prohibits` cell is a denial. Every cell is itself **Derived, CV**: a carving, contestable by counter-instance or by a better label, and generated from page metadata under manual review, never a derivation certificate.

## Type and formal status

**E (epistemic):** Derived. As an artifact the page is **Exposition** — it introduces no new load-bearing claim of its own; it indexes relations already asserted on the pages it crosses. Each individual cell, however, is **Derived, CV**: the choice of one label from the controlled set over another is a carving open to a better carving. The matrix inherits, per cell, the more contestable of its two endpoints' marks.

**A (alethic):** The matrix aspires to record the relations the crossed pages actually bear. A cell is accurate insofar as its linked endpoints sustain it; inaccuracy appears as a cell no source page supports, or as a relation on some page that no cell records. The two axes do not predict each other: an **Exposition** mark on the E axis does not lower the A aspiration, and a manually reviewed cell can be at once Derived/CV and accurate. **Contestable here never means probably wrong or merely optional.**

This page is a **treatise-side extension, held contestable** — not canonical, and carrying no priority, exemption, or unmarked status. It is subject to the same [[two-mark-system|two marks]] as every content-bearing claim, including this sentence.

## Controlled relation vocabulary

Every nonempty cell uses exactly one of these labels. Vague labels such as `related`, `similar`, or `connected` are prohibited: they record adjacency without recording *what kind*, and a matrix of adjacency is a matrix of noise.

```text
entails
constrains
regulates
is-regulated-by
binds
couples-with
instantiates
returns-to
tests
can-capture
can-corrupt
preserves
requires
prohibits
```

The labels sort into families, which drive the relation-type filter:

- **Dependency** — `entails`, `requires`, `constrains`, `prohibits`
- **Regulation** — `regulates`, `is-regulated-by`
- **Composition** — `binds`, `couples-with`
- **Instantiation** — `instantiates`
- **Feedback** — `returns-to`, `tests`
- **Corruption / capture** — `can-corrupt`, `can-capture`
- **Preservation** — `preserves`

Two distinctions are load-bearing and must not be flattened. First, **`couples-with` is not `regulates`.** `couples-with` names ⊕ composition — two feeling-regulators or controllers wired so that a property *emerges* which is in neither part; it is emphatically **not** addition (see [[force|Force]]). `regulates` names one term *bounding the characteristic excess* of another without producing a new composite. Second, a **symmetric pair of `regulates` cells is cross-regulation, not circular proof.** When `(R, C)` and `(C, R)` both read `regulates`, each term bounds a *different* excess of the other; the reciprocity is [[cross-regulated-necessity|necessary architecture]], and a failed attack on one direction is never logged as confirmation of the whole.

`is-regulated-by` is the inverse of `regulates`. Reading any column top-to-bottom already yields the `is-regulated-by` view of that component; explicit `is-regulated-by` cells are reserved for pairs where the passive direction is the load-bearing one.

## Reading the matrix

- **Rows act; columns receive.** Cell `(R, C)` = "`R` **[label]** `C`."
- **Codes** in the header expand through the legend below into wikilinked page titles.
- **`·`** = no asserted first-order interaction. Absence is not a prohibition; a prohibition is written `prohibits`.
- **The diagonal** is normally blank. It is nonblank only where a component acts on itself in a load-bearing way — here, [[splcw|SPLCW]] carries `returns-to` on its own diagonal, because the Ring returns to itself through a *changed world*.
- **A cell that needs explanation links out.** The showcase pair and the extended interactions below carry links to the dedicated relation pages; the matrix records the label, the relation page carries the argument.

### The core interaction matrix

Ten core components. The full matrix over every load-bearing page is machine-generated (see *Data source*); this rendered core exhibits the pattern and the controlled vocabulary in use. The table scrolls horizontally on narrow viewports.

| ↓ R \ C → | AX | DV | CL | SA | TM | DP | PB | FO | SP | TE |
|---|---|---|---|---|---|---|---|---|---|---|
| **AX** | · | entails | · | · | entails | · | · | · | · | constrains |
| **DV** | · | · | constrains | · | · | · | · | · | · | · |
| **CL** | instantiates | · | · | regulates | · | · | · | · | · | · |
| **SA** | · | · | regulates | · | tests | · | · | · | · | · |
| **TM** | · | requires | constrains | · | · | · | · | · | · | · |
| **DP** | instantiates | · | · | · | · | · | · | · | · | · |
| **PB** | · | · | · | · | · | binds | · | · | · | · |
| **FO** | · | · | · | · | · | · | couples-with | · | · | · |
| **SP** | · | · | · | · | · | · | · | · | returns-to | · |
| **TE** | requires | · | · | · | · | · | · | · | requires | · |

**Legend.**
AX = [[axiom|The Axiom]] · DV = [[derived|Derived]] · CL = [[formal-closure-claim|The Formal Closure Claim]] · SA = [[self-application|Self-Application]] · TM = [[two-mark-system|The Two-Mark System]] · DP = [[directional-primitives|The Directional Primitives]] · PB = [[predicate-binding|Predicate Binding]] · FO = [[force|Force]] · SP = [[splcw|SPLCW]] · TE = [[telos|The Telos]]

**The showcase pair — read `CL ⇄ SA`.** Cell `(CL, SA)` and cell `(SA, CL)` both read `regulates`. This is the reciprocity the whole wiki turns on: [[formal-closure-claim|closure]] regulates the regress-excess of [[self-application|recursive marking]] by keeping every corrective operation inside one semantic domain, and recursive marking regulates the totalization-excess of closure by refusing any formulation of closure an exempt or final status. The symmetric pair is exactly how the matrix encodes what [[semantic-closure-and-recursive-marking|Semantic Closure and Recursive Marking]] states as `U = C ⊕ M` and what [[reciprocal-attack-surfaces|Reciprocal Attack Surfaces]] writes as `e_C -> M`, `e_M -> C`. It is **not** a single `couples-with`, because the emergent object is not a new composite feeling but a bounded, mortal, finite participation; and it is **not** two mutually confirming assertions, because each cell names a distinct isolation failure the other prevents.

**Reading three more cells.** `AX entails DV` — the closed medium entails that every content-bearing claim is [[derived|Derived]]; unavoidability of the condition does not manufacture a Forced tier. `DV constrains CL` — Derived status holds the closure claim to a marked, revisable formulation, so `C` is never promoted to founded. `PB binds DP` — a [[predicate-binding|predicate binding]] binds a primitive [[directional-primitives|directional actuator]] to the regulated error it reduces, `B(p) = (p, eₚ)`; this is regulation toward a setpoint, not a conserved invariant, and a bound emotion is never a primitive.

### Extended interactions (data-source excerpt)

The remaining controlled labels appear across the full component set. This excerpt of `wiki-interactions.json` demonstrates each. Targets are components where a slug exists and named excesses where the relation lands on an excess rather than a page.

- **[[submission|Submission]] — `instantiates` → [[force|Force]]** — a named ⊕ composite, Love ⊕ Fear under opposed-gradient contention.
- **[[reconciliation|Reconciliation]] — `instantiates` → [[force|Force]]** — a sequential-gated composite, Apology ⊕ Gratitude; Fear is not one of its ingredients.
- **[[love|Love]] — `couples-with` → [[fear|Fear]]** — emergent: Submission. `couples-with` is coupled-controller composition, never a sum.
- **[[apology|Apology]] — `couples-with` → [[gratitude|Gratitude]]** — emergent: Reconciliation. Own the fault first, then carry value outward.
- **[[predicate-binding|Predicate Binding]] — `binds` → [[regulated-error-signal|Regulated Error Signal]]** — an actuator bound to the error it reduces.
- **[[vls|VLS]] — `couples-with` → [[transparentocracy|Transparentocracy]]** — accurate participation-without-possession coupled to answerable governance.
- **[[transparentocracy|Transparentocracy]] — `is-regulated-by` → [[capture-of-corrective-layer|Capture of the Corrective Layer]]** — the passive direction is load-bearing: governance authority is bounded by the standing possibility of corrective capture.
- **[[capture-of-corrective-layer|Corrective Capture]] — `can-capture` → [[answerability-predicate|Answerability]]** — captured correction becomes ornamental while the governed telos runs unchanged; see [[effective-and-ornamental-answerability|Effective and Ornamental Answerability]].
- **[[theodicytes|The Theodicytes]] — `can-corrupt` → [[splcw|SPLCW]]** — a role absolutized past its function; corruptions are over-presences, never absences ([[role-corruption-affinities|Role–Corruption Affinities]]).
- **[[theodicytes|The Theodicytes]] — `can-corrupt` → [[telos|The Telos]]** — the answerability predicate dropped, so answerable continuation degrades toward raw outlasting.
- **[[telos|The Telos]] — `preserves` → [[continuity|Continuity]]** — continuation through successors capable of difference, not identity enforcement ([[continuation-and-colonization|Continuation and Colonization]]).
- **[[symbolic-immortality|Symbolic Immortality]] — `requires` → [[answerability-predicate|Answerability]]** — without it, propagation is colonization, not continuation ([[responsible-successor|The Responsible Successor]]).
- **[[self-application|Self-Application]] — `tests` → [[two-mark-system|The Two-Mark System]]** — turns the apparatus on its own formulations; the test must apply to itself.
- **[[splcw|SPLCW]] — `returns-to` → [[splcw|SPLCW]]** — the Ring returns through a changed world and never declares itself closed; answerability comes from the witness outside the ring.
- **[[two-mark-system|The Two-Mark System]] — `prohibits` → a Forced / exempt tier** — the one denial in this excerpt: no unmarked level, the deepest guard ([[prohibited-collapses|The Prohibited Collapses]]).

## Filters

The interactive page exposes three filters; the groupings below are the text alternative so the matrix remains legible without the controls.

- **By section.** Components carry their navigation section. Core/epistemic apparatus: `axiom`, `derived`, `formal-closure-claim`, `self-application`, `two-mark-system`. Structural interlocks: `semantic-closure-and-recursive-marking`, `reciprocal-attack-surfaces`, `cross-regulated-necessity`. Directional core: `directional-primitives`, `predicate-binding`, `force`. Meaning engine: `splcw`. Answerability and anti-capture: `telos`, `answerability-predicate`, `symbolic-immortality`, `continuity`, `transparentocracy`, `capture-of-corrective-layer`, `vls`.
- **By relation type.** Filter to any family above (Dependency, Regulation, Composition, Instantiation, Feedback, Corruption/capture, Preservation) to isolate, for example, only the `regulates`/`is-regulated-by` skeleton or only the `can-corrupt`/`can-capture` threat edges.
- **By formal status.** Filter cells by the inherited mark — FT, CV, AC, or Exposition. Every cell is at least Derived, CV; the filter surfaces which cells rest on an FT relation between their endpoints and which are the more contestable carvings.

## Data source and maintenance

The matrix is generated from `wiki-interactions.json`, itself assembled from each page's front matter (`regulates`, `regulated_by`, `see_also`) and then **manually reviewed** — the metadata proposes edges, a reviewer assigns the controlled label and prunes what the pages do not bear. Page slugs are the stable identifiers; titles are display values only. The matrix is regulated by [[system-invariants|System Invariants]] (no cell may contradict an invariant), by the [[attack-surface-matrix|Attack-Surface Matrix]] (each component's row must be consistent with its declared attack surface), and by the [[coupling-graph|Coupling Graph]] (highlighted couplings must appear as their corresponding cells). The matrix is a **live artifact**: it is regenerated whenever a load-bearing page changes, and it is never declared complete.

### Valid attack surface and kill condition

The matrix as artifact remains answerable. A **valid attack** exhibits a genuine load-bearing relation that no controlled label captures without loss — forcing a vague label or an unbacked assertion — or shows a cell the endpoints do not sustain. The **kill condition:** a nonempty cell cannot be regenerated from `wiki-interactions.json` together with its two linked pages, or the matrix asserts a relation neither endpoint bears. The residue: the controlled vocabulary is itself a CV carving; a demonstrated relation that is real, recurrent, and irreducible to the fourteen labels is a live counter-instance that would expand or recut the set. A cell surviving attack is not thereby confirmed — it is only not yet defeated.

## Prohibited misreadings

- **Reading a blank cell as a denial.** `·` is *no asserted first-order interaction*, silence, not prohibition. Only `prohibits` denies. Absence records the limit of the review, not a claim about the world.
- **Reading `couples-with` as `+`.** ⊕ is coupled-controller composition; the emergent property lives in the wiring, not in a sum of parts. The additive reading is inaccurate, not merely disallowed.
- **Mirroring a cell.** The matrix is directional. Do not assume `(C, R)` from `(R, C)`; regulation, instantiation, and feedback are frequently one-way or sequential, and `couples-with` reciprocity is a separately asserted fact, not a symmetry to be inferred.
- **Reading a symmetric `regulates` pair as circular proof.** Cross-regulation means each term bounds a *different* excess of the other; it is architecture, not a verbal loop, and a failed attack on either direction is logged as a failed attack, never as confirmation.
- **Reading a filled cell as forced or founded.** Every cell is Derived, CV — a manually reviewed carving. No cell promotes its endpoints toward an exempt, founded, or unmarked tier; asserting one would be the textual Nephilim.
- **Treating the matrix as complete.** New load-bearing pages add rows and columns; the artifact is regenerated, never sealed. Completion would be totalization by another route.
- **Using the matrix to launder authority.** Recording an edge does not make the relation true; it makes it *inspectable*. The relation pages carry the argument and the kill conditions; the matrix carries only the label and the link.

## See also

[[coupling-graph|The Coupling Graph]] · [[attack-surface-matrix|The Attack-Surface Matrix]] · [[system-invariants|System Invariants]] · [[prohibited-collapses|The Prohibited Collapses]] · [[category-error-atlas|The Category-Error Atlas]] · [[reader-paths|Reader Paths]] · [[semantic-closure-and-recursive-marking|Semantic Closure and Recursive Marking]] · [[reciprocal-attack-surfaces|Reciprocal Attack Surfaces]] · [[cross-regulated-necessity|Cross-Regulated Necessity]] · [[one-page-reconstruction|Ultimentality in One Page]]
