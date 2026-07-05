# Changelog

All notable changes to this project are documented here. The format loosely follows [Keep a Changelog](https://keepachangelog.com/).

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
