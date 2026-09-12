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

def _expand_couplings(pages, root):
    targets=[page for page in pages.values() if COUPLINGS_MARKER in page['raw']]
    if not targets:
        return
    rows=json.loads((Path(root)/'data/wiki-couplings.json').read_text())
    table=coupling_table(rows,pages)
    for page in targets:
        page['raw']=page['raw'].replace(COUPLINGS_MARKER,table)

# All formats use the same expanded raw page: HTML, standalone Markdown, monolith, ZIP.
def data_tables(pages, root):
    root=Path(root)
    def cell(value):return str(value).replace('|','&#124;').replace('\n',' ')
    def ref(slug):return f"[[{slug}|{pages[slug]['title']}]]" if slug in pages else cell(slug)
    def table(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join('---' for _ in headers)+'|']+['| '+' | '.join(row)+' |' for row in rows])
    result={}
    def needed(kind):return any(f'<!-- GENERATED:{kind} -->' in p['raw'] for p in pages.values())
    if needed('attacks'):
        rows=json.loads((root/'data/wiki-attack-surfaces.json').read_text())
        result['attacks']=table(['Page','Status','Challenge','Revision condition','Executable test references'],[[ref(x['component']),cell(x['claim_type']),cell(x['valid_attack']),cell(x['kill_condition']),cell(', '.join(map(str,x['tests']))) if x['tests'] else 'Not registered'] for x in rows])
    if needed('interactions'):
        rows=json.loads((root/'data/wiki-interactions.json').read_text())
        result['interactions']=table(['Source','Relation','Target'],[[ref(x['source']),cell(x['relation']),ref(x['target'])] for x in rows])
    if needed('collapses'):
        rows=json.loads((root/'data/wiki-prohibited-collapses.json').read_text())
        result['collapses']=table(['Distinguish','From','Mistaken inference','Source'],[[cell(x['a']),cell(x['b']),cell(x['damage']),ref(x['bridge'])] for x in rows])
    return result

def expand_references(pages,root):
    _expand_couplings(pages,root)
    for kind,table in data_tables(pages,root).items():
        for page in pages.values():page['raw']=page['raw'].replace(f'<!-- GENERATED:{kind} -->',table)
