"""Render reference tables from their maintained data, without inferring doctrine."""
import json
from pathlib import Path

COUPLINGS_MARKER = '<!-- GENERATED:couplings -->'

def coupling_table(rows, pages):
    def ref(slug):
        if slug not in pages:
            raise ValueError(f'Coupling references unknown page: {slug}')
        return f"[[{slug}|{pages[slug]['title']}]]"
    def cell(value):
        return str(value).replace('|', '&#124;').replace('\n', ' ')
    lines=['| Component | Relation | Component | Emergent property | Source pages |',
           '|---|---|---|---|---|']
    for row in rows:
        left=ref(row['source']); right=ref(row['target'])
        evidence=' · '.join(ref(slug) for slug in row['evidence_pages'])
        lines.append(f"| {left} | {cell(row['relation'])} | {right} | {cell(row['emergent_property'])} | {evidence} |")
    return '\n'.join(lines)

def expand_references(pages, root):
    targets=[page for page in pages.values() if COUPLINGS_MARKER in page['raw']]
    if not targets:
        return
    rows=json.loads((Path(root)/'data/wiki-couplings.json').read_text())
    table=coupling_table(rows,pages)
    for page in targets:
        page['raw']=page['raw'].replace(COUPLINGS_MARKER,table)
