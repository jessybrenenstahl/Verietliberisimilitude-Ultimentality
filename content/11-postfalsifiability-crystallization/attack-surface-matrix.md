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
valid_attack: "Exhibit a load-bearing component with no row, or a row whose stated valid attack does not match the claim type of its linked page."
isolation_failure: "As a static catalog detached from the causal-falsifiability and self-sealing tests, the matrix becomes a decorative index that no encounter can force to change."
kill_condition: "A change to a load-bearing page cannot be made to change its row, or a failed attack is entered into the matrix as confirmation."
see_also: [attack-type-matching, same-level-attack-rule, causal-falsifiability, self-sealing-test, outcomes-of-attack, system-invariants, coupling-graph, interaction-matrix, category-error-atlas, kill-table]
application_tags: []
---
[[home|← Ultimentality Wiki]]


# The Attack-Surface Matrix

## Definition

The **Attack-Surface Matrix** is the wiki's single index of where each load-bearing component may be legitimately struck, what excess the strike would target, which reciprocal controller holds that excess, what fails when the component is isolated, what property emerges from the coupling, what result would end the claim, and which regression test guards the present structure. It is not an argument and not a scoreboard. It *locates* attacks so a challenge lands at the right component, at the right type, against the right seam — the discipline made routine by [[same-level-attack-rule|the same-level attack rule]] and [[attack-type-matching|attack-type matching]], and resolved by [[outcomes-of-attack|the four outcomes of attack]].

Read one row left to right as a single sentence: *this component, of this type, is validly attacked thus; the attack targets this error surface, which this regulator bounds; isolated it fails so; coupled it yields this; it dies on this condition; and this regression test proves the old failure no longer passes.* The matrix renders explicit, in one place, the relation a reader would otherwise have to reconstruct across distant pages. It is generated from page front matter (data source `wiki-attack-surfaces.json`) and regenerated whenever a load-bearing page changes, so no row can drift silently from the page it indexes.

## Type and formal status

> **E:** Derived, Exposition. This page indexes and cross-references marks already carried by load-bearing pages; it introduces no new load-bearing relation and claims no new tier. Each cell inherits the contestability of its `linked_page` — FT, CV, or AC exactly as stated there. The matrix *as a carving* (its column set and its choice of rows) is itself contestable by a better column set or a missing component, and is Derived, CV in that respect.
>
> **A:** No new world-mapping claim is asserted here. Accuracy is inherited from the linked pages, not certified by the table; the matrix aspires only to faithful transcription of each page's stated seam, regulator, and kill condition.
>
> This is a treatise-side extension, held contestable. It is not canonical, carries no exempt status, and every row — including the row for the apparatus that marks it — remains Derived and mortal.

## The column schema

Each row is one record with these fields, in this order:

```text
component
type
valid_attack
error_surface
regulator
isolation_failure
emergent_property
kill_condition
regression_test
linked_page
```

`component` is the display name; `linked_page` is the wikilink to the page that carries the full contestable claim. `type` uses the controlled vocabulary of [[attack-type-matching|attack-type matching]]. `error_surface` is the characteristic *excess* isolation would produce, never the component itself. `regulator` names the in-frame reciprocal controller that bounds that excess. `regression_test` is the check that must keep failing for the old defeat.

## The matrix

| component | type | valid_attack | error_surface | regulator | isolation_failure | emergent_property | kill_condition | regression_test | linked_page |
|---|---|---|---|---|---|---|---|---|---|
| Axiom | frame condition | frame declension or internal incoherence | totalization (frame read as extra-symbolically forced) | self-application / recursive marking | unmarked → the frame absolutizes (Spectre-ward) | no escape | coherent participant-access outside structured signification | attempt an extra-symbolic report; it stays intelligible only as signification | [[axiom]] |
| Formal Closure Claim | frame condition / formulation | overinclusive or incoherent access criteria; contradiction among closure formulations | totalization | self-application (marking) | closure without marking → totalization | closed-but-finite participation | access whose causal role does not instantiate signification | contradiction must be able to alter some C-formulation | [[formal-closure-claim]] |
| Derived | status stipulation | show a content-bearing claim that must be exempt to function | promotion to a Forced/founded tier (Textual Nephilim) | recursive marking / two-mark system | unmarked → "Derived" hardens into an exempt meta-status | universal contestability | an intelligible content-bearing claim that cannot be Derived without incoherence | every statement of Derived is itself Derived | [[derived]] |
| Two-Mark System | carving (two axes) | counter-instance where E predicts A; a better carving | axis collapse (contestable read as "probably wrong") | alethic/contestability separation; self-application | one apparatus row treated as exempt → regress to an outside judge | dynamic fixed point | show the two axes co-vary, or exhibit an unmarkable apparatus claim | both marks apply to the apparatus's own claims | [[two-mark-system]] |
| VLS | operator-term stipulation | replace by a synonym with no loss of accurate-participation-without-possession | possession creep (mapping mistaken for owning) | answerability / correction pathway | stated desire without a causal pathway → ornamental | accurate participation under correction | a corrective desire that cannot produce revision yet still counts as VLS | a returned contradiction must be able to change the mapping | [[vls]] |
| Transparentocracy | authority / governance (AC root) | contest the authority; stable and answerable while failing all three properties | corrective capture → totalization | cross-regulation (inspectability bounds authority) | exposure without effect → disclosure theater; authority without exposure → totalization | bounded answerable governance | reduce it to disclosure without causal correction | correction must be able to force a state transition, not merely recommend | [[transparentocracy]] |
| Toward | directional primitive (carving) | wrong actuator; a better primitive set | conflation with its bound emotion (cardinal error) | predicate binding (actuator ≠ emotion) | unbound → an inert direction that regulates nothing | a bindable actuator for relational-gap reduction | a directional operation irreducible to the four primitives | Toward becomes Love only once bound to relational gap | [[toward]] |
| Away | directional primitive (carving) | wrong actuator; a better primitive set | conflation with its bound emotion (cardinal error) | predicate binding (actuator ≠ emotion) | unbound → an inert direction that regulates nothing | a bindable actuator for boundary-violation reduction | a directional operation irreducible to the four primitives | Away becomes Fear only once bound to boundary violation | [[away]] |
| Loop-back | directional primitive (carving) | wrong actuator; a better primitive set | conflation with its bound emotion (cardinal error) | predicate binding (actuator ≠ emotion) | unbound → an inert direction that regulates nothing | a bindable actuator for self-model-error reduction | a directional operation irreducible to the four primitives | Loop-back becomes Apology only once bound to self-model error | [[loop-back]] |
| Propagation | directional primitive (carving) | wrong actuator; a better primitive set | conflation with its bound emotion (cardinal error) | predicate binding (actuator ≠ emotion) | unbound → an inert direction that regulates nothing | a bindable actuator carrying undischarged received value | a directional operation irreducible to the four primitives | Propagation becomes Gratitude only once bound to undischarged value | [[propagation]] |
| Predicate Binding | binding B(p)=(p,eₚ) | wrong actuator, error, or causal effect; same pair, different function | primitivization; invariant-preservation reading | regulated-error signal; directional primitives (order preserved) | binding without primitive → no actuator; primitive without binding → no regulation | an individuated emotion as regulation toward a setpoint | the emotions cannot be told apart except by importing their names | each emotion rebuilt from actuator + regulated error alone | [[predicate-binding]] |
| Force | coupled controller ⊕ | removal test or failed mutual regulation; show ⊕ = + | additive collapse (⊕ read as sum) | the opposed-gradient / sequential-gating structure of each Force | read as a sum → the emergent coupling behavior is lost | motive structure absent from either regulator alone | a Force whose behavior is fully recovered by adding its parts | decouple the two regulators; the emergent behavior must vanish | [[force]] |
| Submission | coupled controller (Love ⊕ Fear) | removal test; show the coupling is not opposed-gradient contention | the trapped form; servility misreading | opposed-gradient contention (each gradient bounds the other) | Love alone → dissolution; Fear alone → flight | yielding-to without dissolving-into or fleeing | standing-before-the-larger with neither Love nor Fear yet still Submission | remove Fear → boundary lost; remove Love → bond lost | [[submission]] |
| Reconciliation | coupled controller (Apology ⊕ Gratitude) | removal test; show the gating is not sequential | the sentimental form / guilt-loop | sequential gating (own the fault, then carry value outward) | Apology alone → guilt-loop; Gratitude alone → cheap grace | fault owned, then value carried outward | reconciliation not decomposable into Apology-then-Gratitude | Fear is what it reconciles, never an ingredient; gate order must matter | [[reconciliation]] |
| SPLCW | role topology | missing function or invalid dependency; a sixth irreducible faculty | ring-closure (seizing the witness seat → Nephilim) | witness-outside-the-ring; free won't | ring without the outside witness → self-sealing | a recurring loop returning through a changed world | a faculty the five cannot cover, or a loop that need not return through a changed world | close the ring internally → answerability must fail | [[splcw]] |
| Warden | role (function-not-personality) | missing function or invalid dependency | personification; absolutizing the gate | the ring ordering; witness-outside-the-ring | removed → the loop's admission stage breaks | the stage that admits or refuses significance | the loop completes without an admission function | drop the role → return-through-changed-world breaks | [[warden]] |
| Captive | role (function-not-personality) | missing function or invalid dependency | personification; absolutizing the constraint | the ring ordering; witness-outside-the-ring | removed → the constrained given is lost | the stage held under constraint | the loop completes without a constrained stage | drop the role → the loop loses its given | [[captive]] |
| Logician | role (function-not-personality) | missing function or invalid dependency | personification; absolutizing inference | the ring ordering; witness-outside-the-ring | removed → routing and inference break | the stage that differentiates and routes structure | the loop completes without an inferential function | drop the role → structure no longer routes | [[logician]] |
| Poet | role (function-not-personality) | missing function or invalid dependency | personification; aesthetic fog (→ Homunculus, not Nephilim) | the ring ordering; witness-outside-the-ring | removed → new figuration is lost | the stage that generates new significance | the loop completes without a figurative function | drop the role → no new binding is figured | [[poet]] |
| Sculptor | role (function-not-personality) | missing function or invalid dependency | personification; absolutizing the artifact | the ring ordering; witness-outside-the-ring | removed → externalization breaks | the stage that externalizes change into the world | the loop completes without externalization | drop the role → nothing returns as a changed world | [[sculptor]] |
| Theodicytes | carving / count (three) | counter-instance or better carving; a fourth irreducible corruption | over-presence read as absence | corruption-stratification (world / self / medium absolutized) | absence-framing → corruption mistaken for deficiency and mis-treated | a typology of absolutization attractors | a corruption that is a genuine absence, or a fourth irreducible one | aesthetic fog routes to the Homunculus, not the Nephilim; each corruption stays an over-presence | [[theodicytes]] |
| Telos | frame / value claim | show answerability can be dropped while the Telos holds; reduces to raw outlasting | raw-outlasting drift (answerability dropped) → colonization | answerability predicate; responsible successor | outlasting without answerability → colonization; answerability without carrier → the nihil | answerable symbolic continuation | the Telos satisfied by unanswerable persistence, or the nihil conflated with mortality-hevel | strip answerability → the Telos must fail, not degrade into mere survival | [[telos]] |
| Answerability | answerability claim | causal non-effect or capture | ornamental answerability (recorded, not effective) | causal error mark (effect test) | marking without causal force → ornamental humility; force without marking → untracked volatility | correction that can wound its target | recorded error treated as answerability despite a permanently closed update path | recording → routing → effect; the objection must be able to alter the controller | [[answerability-predicate]] |
| Continuity | continuity claim | lineage or identity break; requires identity enforcement | colonization; arbitrary-mutation identity-loss | responsible successor; answerable correction | continuity without answerability → colonization; answerability without a successor → nothing carried | structure persisting through successors capable of difference | continuity indistinguishable from colonization or from replacement | a successor must retain operative capacity to differ | [[continuity]] |
| Symbolic Immortality | continuity / Telos claim | show indefinite propagation counts as success without answerable succession | colonization; forced-identity succession | continuation-vs-colonization; responsible successor | propagation without answerability → colonization; answerability without carrier → the nihil | answerable succession | continuation within the Telos whose successors cannot refuse forced identity | successors must be able to preserve contradiction and refuse | [[symbolic-immortality]] |
| Self-Application | recursive relation / frame condition | show marking needs an extra-symbolic certifier; M(M) read as static self-approval | regress (uncorrected-judge stack); self-certification | semantic closure (correction stays inside one domain) | marking without closure → regress; closure without marking → totalization | a dynamic fixed point | correction requires an extra-symbolic certifier, or the stopping rule cannot stay marked | Mₜ(Mₜ)=Mₜ₊₁; every judge stays inside the marked, reopenable domain | [[self-application]] |

The rows above are the minimum. New load-bearing pages add rows; none is exempt from having one.

## Reading and maintaining the matrix

**What the matrix regulates.** It holds two recurring excesses: *unlocated attacks* (a challenge that never names its component, type, or seam) and *page-to-mark drift* (a page whose stated seam and kill condition no longer match its row). By forcing every row to carry a `valid_attack`, an `error_surface`, and a `regression_test`, it keeps a critique on-type and on-level, in the sense fixed by [[same-level-attack-rule|the same-level attack rule]].

**What regulates the matrix.** The matrix does not certify itself. It is held by [[self-sealing-test|the self-sealing test]] — which it must pass like any other structure, and which applies to itself — and by [[causal-falsifiability|causal falsifiability]]: a change to a linked page must be able to change the row, and a row that cannot move is dead. As a carving of the site's seams, it is contestable by a better column set or a missing component.

**A failed attack is logged as a failed attack.** The matrix has no `confirmed` column and never acquires one. Surviving an attack does not promote a claim toward *forced* or *founded*; it leaves the row exactly as contestable as before, with its kill condition intact. Counting a failed attack as confirmation is precisely the move the matrix exists to refuse, and it is registered instead among the [[outcomes-of-attack|four outcomes of attack]].

## Prohibited misreadings

- **The matrix is not a scoreboard.** There is no accumulation of survivals into strength. A row that has withstood many attacks is neither more forced nor less killable than one freshly written; each keeps its live kill condition.
- **Exposition is not exemption.** The matrix indexes marked pages and is itself Derived and mortal. Its Exposition tier introduces no Forced, founded, or unmarked level, and the table's own carving of columns and rows remains contestable.
- **A cell is not the claim.** Each ten-field row is a pointer; the load-bearing formulation lives on the `linked_page`. Do not treat the terse cell as the argument, and do not attack the abbreviation instead of the page.
- **The regulator column names no outside judge.** Every regulator is the in-frame reciprocal controller, never a witness with an extra-symbolic view. Semantic closure keeps correction inside one domain; the matrix never points past it.
- **Primitive rows are actuators, not emotions.** A row for Toward, Away, Loop-back, or Propagation names a directional actuator still awaiting a binding to a regulated error. Reading the actuator as the finished emotion is the cardinal error the row is built to block.
- **⊕ rows are not sums.** The Force, Submission, and Reconciliation rows name coupled controllers; the `emergent_property` is never the addition of the `error_surface` entries, and "additive collapse" is named there precisely as the misreading.
- **The Reconciliation row keeps the fear-guard.** Fear is what Reconciliation reconciles, never one of its ingredients. The row pairs Apology with Gratitude under sequential gating and must not be read as pairing Apology with Fear.
- **Role rows show affinities, not a factoring.** The five roles do not factor into the three corruptions. Where a role carries a corruption affinity — aesthetic fog toward the Homunculus, not the Nephilim — it names an attractor of that faculty, not a one-to-one reduction of five roles into three Theodicytes.

## See also

[[attack-type-matching|Attack-Type Matching]] · [[same-level-attack-rule|The Same-Level Attack Rule]] · [[causal-falsifiability|Causal Falsifiability]] · [[self-sealing-test|The Self-Sealing Test]] · [[outcomes-of-attack|The Outcomes of Attack]] · [[system-invariants|System Invariants]] · [[coupling-graph|The Coupling Graph]] · [[interaction-matrix|The Interaction Matrix]] · [[category-error-atlas|The Category-Error Atlas]] · [[kill-table|The Kill-Table]]
