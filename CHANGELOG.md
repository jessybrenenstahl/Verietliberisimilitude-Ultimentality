# Changelog

All notable changes to this project are documented here. The format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [1.0.0] — 2026-06-20

### Added
- Initial repository: the complete **Ultimentality** wiki (Two-Axis Edition) — 101 concept pages plus a landing page, organized under `content/` by Part.
- Static-site build pipeline (`tools/build_site.py`): Markdown → HTML via pandoc, sidebar navigation parsed from `home.md`, client-side search, computed backlinks, dark/light theming, and MathJax.
- Per-page and whole-corpus **downloads** generated at build time: each page's `.md`, a monolithic `ultimentality-wiki-complete.md`, and `ultimentality-wiki-md.zip` of every page.
- **Link-integrity validator** (`tools/check_links.py`) as the project's test: fails on any dangling `[[wikilink]]` or missing `[[home]]` backlink.
- **CI** (`.github/workflows/build.yml`): validate → build → deploy to GitHub Pages on every push to `main`.
- Five treatise-side **extension** pages under `content/extensions/` (corruption-stratification, self-application, mathematics, why-how-inversion, matter-meaning-cycle), each flagged treatise-side and held contestable.
