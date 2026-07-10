#!/usr/bin/env python3
"""Link-integrity validator for the Ultimentality content tree — the project's test.

Fails (exit 1) if any page contains a [[wikilink]] whose target slug does not
exist anywhere under content/, if any page (other than the home landing) is
missing its [[home|…]] backlink, if two pages share a slug, or if any page
recreates or links to an excluded (deliberately removed) proposal slug. Run via
`make check` or in CI.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "content")
WIKILINK = re.compile(r"\[\[([^|\]]+)(?:\|[^\]]+)?\]\]")

# Deliberately removed proposals — must never be recreated as pages or linked to.
EXCLUDED = {
    "ultimatum-to-mentality",
    "ultimentality-and-ultimatality",
    "human-and-artificial-descriptive-symmetry",
    "distributed-participant",
    "witness-independence",
    "local-sincerity-global-telos",
    "pathologies-of-isolation",
}


def collect_pages():
    """slug -> absolute path, walking content/ recursively."""
    pages = {}
    for dirpath, _dirs, files in os.walk(SRC):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            slug = fn[:-3]
            if slug in EXCLUDED:
                raise SystemExit(
                    f"excluded proposal recreated as a page: {os.path.join(dirpath, fn)}"
                )
            if slug in pages:
                raise SystemExit(
                    f"duplicate slug '{slug}': {pages[slug]} and {os.path.join(dirpath, fn)}"
                )
            pages[slug] = os.path.join(dirpath, fn)
    return pages


def main():
    if not os.path.isdir(SRC):
        raise SystemExit(f"content directory not found: {SRC}")
    pages = collect_pages()
    errors = []
    for slug, path in sorted(pages.items()):
        raw = open(path, encoding="utf-8").read()
        rel = os.path.relpath(path, ROOT)
        for m in WIKILINK.finditer(raw):
            target = m.group(1).strip()
            if target in EXCLUDED:
                errors.append(f"{rel}: references excluded slug [[{target}]]")
            elif target not in pages:
                errors.append(f"{rel}: dangling wikilink [[{target}]]")
        if slug != "home" and not re.search(r"\[\[home\|", raw):
            errors.append(f"{rel}: missing [[home|…]] backlink")

    if errors:
        print(f"FAIL: {len(errors)} issue(s) in {len(pages)} pages:")
        for e in errors[:200]:
            print("  - " + e)
        sys.exit(1)

    print(f"OK: {len(pages)} pages; every wikilink resolves and every page has a backlink.")


if __name__ == "__main__":
    main()
