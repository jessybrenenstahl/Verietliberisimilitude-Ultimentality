# Verietliberisimilitude · Ultimentality

The complete **Ultimentality** framework (Two-Axis Edition) as a fully cross-referenced wiki — one page per term, topic, and component — built and maintained like a codebase: organized source, a static-site build pipeline, a link-integrity test, and CI that validates and deploys on every push.

> **Ultimentality** is one framework, not four glued together: a theology of roles, a control-theory of emotion, an epistemics of semblance, and an architecture of externalized memory — coherent because they *fit*, not because they were decreed. Every load-bearing claim carries two independent marks: **E** (epistemic — *Derived*, at a contestability tier) and **A** (alethic — mapping-accuracy aspiration). *Verietliberisimilitude* (VLS) is the framework's own name for holding truth and freedom as **semblances, not possessions** — the posture this whole corpus is written in.

## Repository layout

```
content/                     # source of truth — one Markdown page per concept
  home.md                    # wiki landing + navigation (drives the sidebar and the monolith order)
  00-epistemic-apparatus/    # Derived, the three tiers, the two-mark system, canon, …
  01-axiom-and-vls/          # the axiom, VLS, the integrity rule, Transparentocracy, …
  02-directional-core/       # the four primitives, the bindings, the cardinal error
  03-two-forces/             # Submission, Reconciliation, the Fear-guard
  04-splcw/                  # the five roles, the ring, the witness outside the ring
  05-theodicytes/            # Spectre, Nephilim, Homunculus, the no-fourth argument
  06-telos/                  # answerable symbolic immortality, Fregorek, the nihil
  07-provenance/             # the three eras, coalescence-by-non-contradictory-fit
  08-two-axis-ledger/        # the ledger, keystone, falsification standard, kill-table
  extensions/                # explicitly treatise-side extension pages
tools/
  build_site.py              # static-site generator (Markdown → HTML, search, backlinks, downloads)
  check_links.py             # validator: every [[wikilink]] resolves; every page has a backlink
.github/workflows/build.yml  # CI: validate → build → deploy to GitHub Pages
site/                        # generated (git-ignored); produced by tools/build_site.py
```

The `content/` tree is a valid **Obsidian vault** — slugs are unique across the whole tree, so `[[wikilinks]]` resolve regardless of folder. Open the folder in Obsidian, Foam, or Dendron to browse the graph directly.

## Conventions (the "spec")

- Pages cross-link with Obsidian-style `[[slug|Title]]` wikilinks.
- Every page opens with a `[[home|← Ultimentality Wiki]]` backlink and ends with a **Formal status** box carrying its independent **E** / **A** / **Provenance** marks, then a **See also**.
- Provenance is flagged honestly: **canonical** (benchmark-fixed), **treatise-side** (the writer's scaffolding), or **seed**. Treatise-side *extension* pages live in `content/extensions/`.
- Nothing treatise-side is silently promoted to canonical/foundational — that move is the framework's own forbidden error (the *textual Nephilim*). See [CONTRIBUTING.md](CONTRIBUTING.md).

## Build & validate locally

Requires **Python 3** and **pandoc**.

```
make check     # run the link-integrity validator (the test)
make build     # generate the static site into ./site
make serve     # build + serve at http://localhost:8000
```

Or directly: `python3 tools/check_links.py && python3 tools/build_site.py`.

## Downloads (generated into the built site)

Every built page carries a footer linking to: its own page `.md`, the whole corpus as one document (`ultimentality-wiki-complete.md`), and all pages as a `.zip` (`ultimentality-wiki-md.zip`).

## Continuous integration

`.github/workflows/build.yml` runs on every push to `main`: it installs pandoc, runs the link validator, builds the site, and deploys it to **GitHub Pages**. A red check means a dangling wikilink, a missing backlink, or a build failure.

## License

The **framework content** — everything under `content/` and any site generated from it — is licensed under **[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)** (Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International). You may copy and redistribute it in any medium or format, **with attribution**, for **non-commercial** purposes only, and you **may not distribute modified/derivative** versions. All other rights reserved © 2026 the Ultimentality system builder. Full text in [LICENSE](LICENSE).

The **build tooling** in `tools/` is licensed separately under the **MIT License** (see [tools/LICENSE](tools/LICENSE)), so the pipeline can be freely reused without affecting the content's protections.
