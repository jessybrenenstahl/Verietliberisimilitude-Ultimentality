"""Read the scalar/list subset used by this corpus, and derive navigation exports.
Not a general YAML parser or validator. Reads selected fields in the corpus's
supported syntax and ignores other fields; unsupported structures are not
guaranteed to be rejected.
"""
import ast,json,re
from pathlib import Path

def scalar(value):
    value=value.strip()
    if value.startswith(('"', "'")):
        return ast.literal_eval(value)
    return value

def items(value):
    # Commas inside quoted descriptions are not separators.
    parts=re.findall(r'''(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|[^,])+''',value[1:-1])
    return [scalar(x) for x in parts if x.strip()]

def metadata(raw):
    if not raw.startswith('---\n'): return {}
    front=raw.split('---',2)[1];result={}
    lines=front.splitlines()
    for i,line in enumerate(lines):
        m=re.match(r'^(slug|title|valid_attack|isolation_failure|kill_condition|prerequisites|regulates|regulated_by):\s*(.*)$',line)
        if not m: continue
        key,value=m.groups()
        if value.startswith('['):result[key]=items(value)
        elif value:result[key]=scalar(value)
        else:
            vals=[]
            for next_line in lines[i+1:]:
                match=re.match(r'^\s+-\s+(.*)$',next_line)
                if not match:break
                vals.append(scalar(match.group(1)))
            result[key]=vals
    tier=re.search(r'^  tier:\s*(.*)$',front,re.M)
    result['tier']=scalar(tier.group(1)) if tier else 'Unspecified'
    return result

def derived(root):
    root=Path(root);paths=sorted((root/'content').rglob('*.md'));slugs={p.stem for p in paths}
    old_path=root/'data/wiki-attack-surfaces.json'
    old={x['component']:x for x in json.loads(old_path.read_text())} if old_path.exists() else {}
    attacks=[];interactions=[];dependencies=[]
    for p in paths:
        m=metadata(p.read_text())
        if not m:continue
        slug=p.stem
        attacks.append(dict(component=slug,claim_type=m['tier'],valid_attack=m.get('valid_attack','Not specified'),invalid_attacks=[],regulator=m.get('regulated_by',[]),isolation_failure=m.get('isolation_failure','Not specified'),kill_condition=m.get('kill_condition','Not specified'),tests=old.get(slug,{}).get('tests',[])))
        for target in m.get('regulates',[]):interactions.append(dict(source=slug,target=target,relation='regulates',target_in_wiki=target in slugs))
        for source in m.get('regulated_by',[]):interactions.append(dict(source=source,target=slug,relation='regulates',target_in_wiki=True,source_in_wiki=source in slugs))
        for source in m.get('prerequisites',[]):dependencies.append(dict(source=source,target=slug,relation='prerequisite-of',in_wiki=source in slugs))
    unique={ (x['source'],x['target'],x['relation']):dict(source=x['source'],target=x['target'],relation=x['relation'],source_in_wiki=x['source'] in slugs,target_in_wiki=x['target'] in slugs) for x in interactions}
    return {'wiki-attack-surfaces.json':sorted(attacks,key=lambda x:x['component']),'wiki-interactions.json':[unique[k] for k in sorted(unique)],'wiki-dependencies.json':sorted(dependencies,key=lambda x:(x['source'],x['target']))}

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    for name,rows in derived(root).items():
        path=root/'data'/name;expected=json.dumps(rows,indent=2,ensure_ascii=False)+'\n'
        if args.check:
            if not path.exists() or path.read_text()!=expected:raise SystemExit('Stale metadata export: '+name+'; run python3 tools/source_metadata.py')
        else:path.write_text(expected)
    print('Structured source exports match.' if args.check else 'Structured source exports regenerated.')
