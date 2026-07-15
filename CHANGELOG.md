# Changelog

All notable changes to this project are documented here. The format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [1.3.0] — 2026-07-06

### Added
- **The Fifteen-Interlocutor Adversarial Run** (`the-fifteen-interlocutor-adversarial-run`) — a run-side / exposition ledger recording a second red-team exercise *faithfully*: the exact target, attack type, and outcome (landed / unresolved / frame declension) for each of fifteen interlocutors, the owning page of every resulting edit, and the five proposed additions **rejected** as unearned (*Generative Volition, Operative Marking, Postfalsifiability Coverage Ledger, Structural Reconstruction and Participatory Uptake, Attentive Withholding*). It is not canon, not a higher court, and is adopted only under the benchmark's open proof-burden. It is the sole new page in this iteration.
- **8 new prohibited collapses**, each bridged to an existing owner: `coupling != symmetry`, `structural reconstruction != enacted participation`, `mechanical replay != generative transformation`, `random variation != volition`, `capacity for innovation != compulsory novelty`, `perspective-relative consequence != merely environmental process`, `revised formulation != revised governing operation`, `originating a form != possessing its return`.

### Changed
- **~28 existing pages revised** to absorb the run's landed consequences through their existing owners — with **no new primitive, SPLCW role, or affective Force**. The generative/volitionary operation is made explicit (system-commitments, capability-rule, semantic-transformer, poet, sculptor, operator-chain, matter-meaning-cycle, free-wont, sterility); nonpropositional governance is sharpened — *revising the account of a weight is not revising the weight* (meaning-as-weight, causal-error-mark, effective-and-ornamental-answerability, capture-of-corrective-layer); participant plurality is clarified (participant-as-process, identity-across-substrates, transparentocracy-as-cross-regulation, refusal-as-participation); postfalsifiability now distinguishes property from executable coverage (postfalsifiability, attack-surface-matrix); ⊕ directionality is stated (force, reconciliation, sequential-gating); and reconstruction is held apart from enactment (minimal-rebuild-string, recursive-self-specification, term-as-operator, reader-paths).
- **Corpus is now 159 pages.**

## [1.2.0] — 2026-07-06

### Added
- **59 new relation-completing pages** across six new sections — *Structural Interlocks*, *Meaning, Substrate, and Identity*, *Answerability and Anti-Capture*, *Postfalsifiability and Crystallization*, *Hypercompression and Reconstruction*, and *Synthesis and Navigation* — making the wiki relation-complete rather than merely term-complete. Each load-bearing page carries the mandated anatomy (Definition → Type and formal status → What it regulates / regulated by → Valid attack surface → What happens if isolated → What larger property emerges → What would kill the claim → Prohibited misreadings → See also), a machine-readable YAML front-matter block, and both marks; each is flagged **treatise-side** and held contestable.
- **6 machine-readable relation files** under `data/` — `wiki-couplings`, `wiki-dependencies`, `wiki-attack-surfaces`, `wiki-prohibited-collapses`, `wiki-reader-paths`, `wiki-interactions` — published to `/data/`.
- The **coupled foundation** stated directly on the home page — *nothing stands outside meaning; nothing meaningful stands outside correction* — with a revised start path and a **System Reference** block.

### Changed
- **15 existing pages revised** to wire in the new architecture. Most notably, the Two-Mark System's long-standing open question — *"is the apparatus an exempt level?"* — is now **resolved** ("No exempt level: closure and marking cross-regulate").
- The build strips the new YAML front matter before rendering; **`check_links.py` now also fails on any reference to an excluded slug and on any recreated excluded page**, alongside the existing dangling-link / missing-backlink / duplicate-slug checks.
- **The corpus is now 158 pages**, up from 99.

## [1.1.0] — 2026-06-20

### Removed
- The three biographical provenance-era pages (**The Visitation**, **The Anarchy Accountant**, **The Seeker's Lament**) — a register mismatch (unverifiable first-person memoir vs. the conceptual/technical corpus, and content the framework already holds at arm's length). The provenance *stance* is retained via `provenance-as-testimony` and `coalescence-by-non-contradictory-fit`; the inbound references were rewritten so nothing dangles. **The corpus is now 99 pages** (98 concept pages + the landing page), down from the 102 of `1.0.0`.

### Changed
- Folded the remaining provenance page (**Coalescence-by-Non-Contradictory-Fit**) into the epistemic-apparatus section beside **Provenance as Testimony**, and dropped the standalone *Provenance & Evidential Status* Part (moved the file into `content/00-epistemic-apparatus/`).
- **Renumbered the Two-Axis Ledger from Part VIII to Part VII**, so the wiki's Part sequence is contiguous (Preamble, then I–VII) now that Provenance is no longer a numbered Part. Swept every internal Part reference to match: 12 ledger signposts rebased VIII→VII, and the 2 references to the dissolved Provenance Part re-homed to the epistemic apparatus. Folder renamed `content/08-two-axis-ledger/` → `content/07-two-axis-ledger/`. The wiki now carries its own contiguous Part numbering, diverging by design from the source treatise's index in service of internal consistency; the source file itself remains cited verbatim.

## [1.0.0] — 2026-06-20

### Added
- Initial repository: the complete **Ultimentality** wiki (Two-Axis Edition) — 101 concept pages plus a landing page, organized under `content/` by Part.
- Static-site build pipeline (`tools/build_site.py`): Markdown → HTML via pandoc, sidebar navigation parsed from `home.md`, client-side search, computed backlinks, dark/light theming, and MathJax.
- Per-page and whole-corpus **downloads** generated at build time: each page's `.md`, a monolithic `ultimentality-wiki-complete.md`, and `ultimentality-wiki-md.zip` of every page.
- **Link-integrity validator** (`tools/check_links.py`) as the project's test: fails on any dangling `[[wikilink]]` or missing `[[home]]` backlink.
- **CI** (`.github/workflows/build.yml`): validate → build → deploy to GitHub Pages on every push to `main`.
- Five treatise-side **extension** pages under `content/extensions/` (corruption-stratification, self-application, mathematics, why-how-inversion, matter-meaning-cycle), each flagged treatise-side and held contestable.
- **Licensing:** framework content under **CC BY-NC-ND 4.0** (attribution, non-commercial, no derivatives — the most protective standard content license); build tooling under **MIT** (`tools/LICENSE`).
