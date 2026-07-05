# Contributing

This repository is a **wiki-as-codebase**: the content *is* the source, and it is held to code-quality standards — structure, validation, and CI. Contributions follow the framework's own discipline.

## Adding or editing a page

1. Pages live in `content/<part>/…`, or `content/extensions/` for treatise-side additions. One concept per file; the filename is the **slug** and must be **unique across the whole tree**.
2. Start every page with the backlink line, a blank line, then the H1 title:

   ```
   [[home|← Ultimentality Wiki]]

   # The Page Title
   ```

3. Open with a **bold one-sentence lead** that defines the term in plain language *before* any notation. Use descriptive `##` sections.
4. Cross-link generously with `[[slug|Title]]`. Link only to slugs that exist somewhere in `content/`.
5. End with a **Formal status** blockquote and a **See also** line:

   ```
   ## Formal status

   > **E:** Derived, <FT|CV|AC> — <basis>. **A:** <mapping-accuracy aspiration>. **Provenance:** <canonical | treatise-side | seed>.

   ## See also
   [[slug|Title]] · [[slug|Title]] · …
   ```

## The marking discipline (non-negotiable)

- Every load-bearing claim carries **both** an epistemic (**E**) and an alethic (**A**) mark, kept independent. "Contestable" never means "probably wrong" or "merely optional."
- Flag provenance honestly: **canonical** (benchmark-fixed), **treatise-side** (scaffolding / extension), or **seed**.
- Do **not** promote a treatise-side or carving-tier claim to canonical/foundational — that is the framework's own forbidden move, the *textual Nephilim*. New pages default to **treatise-side / CV** unless they restate canonical content.
- Where a genuine tension is unresolved, mark it **Open** and leave it open; do not close it silently.

## Before you commit

Run the validator (CI enforces the same check):

```
make check      # tools/check_links.py — fails on any dangling [[wikilink]] or missing backlink
```

If you touched the pipeline or want to preview the site:

```
make build      # regenerates ./site
make serve      # build + serve at http://localhost:8000
```

`.github/workflows/build.yml` re-runs `check` + `build` and deploys to GitHub Pages on every push to `main`. Keep it green.

## If you add a page that should appear in navigation

Add its `[[slug|Title]]` under the appropriate `##` section in `content/home.md`. That single file drives the sidebar nav *and* the ordering of the monolithic `.md` export, so keeping it current keeps everything downstream in sync.
