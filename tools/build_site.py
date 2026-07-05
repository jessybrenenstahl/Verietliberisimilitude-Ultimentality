#!/usr/bin/env python3
"""Build a static website from the Ultimentality markdown relicquary.

- Converts each .md -> .html via pandoc (gfm + tex math), resolving [[wikilinks]].
- Bespoke responsive template: sidebar nav (parsed from home.md), client-side
  search, computed backlinks, dark/light, MathJax.
- Output is a self-contained static site (no server runtime needed).
"""
import os, re, json, subprocess, shutil, html, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "site")
SITE_TITLE = "Ultimentality"
SITE_SUB = "A wiki of the framework"
SITE_DOMAIN = "ultimentality.relicquary.com"  # GitHub Pages custom domain; set "" to disable CNAME output

WIKILINK_ALIAS = re.compile(r"\[\[([^|\]]+)\|([^\]]+)\]\]")
WIKILINK_BARE  = re.compile(r"\[\[([^|\]]+)\]\]")
H1 = re.compile(r"^#\s+(.+?)\s*$", re.M)

def slug_to_href(slug):
    slug = slug.strip()
    return "index.html" if slug == "home" else f"{slug}.html"

def read_pages():
    pages = {}
    for dirpath, _dirs, files in os.walk(SRC):
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            slug = fn[:-3]
            raw = open(os.path.join(dirpath, fn), encoding="utf-8").read()
            m = H1.search(raw)
            title = m.group(1).strip() if m else slug
            pages[slug] = {"slug": slug, "title": title, "raw": raw}
    return pages

def link_targets(raw):
    t = set()
    for m in WIKILINK_ALIAS.finditer(raw):
        t.add(m.group(1).strip())
    for m in WIKILINK_BARE.finditer(raw):
        t.add(m.group(1).strip())
    return t

def resolve_wikilinks(raw):
    raw = WIKILINK_ALIAS.sub(lambda m: f"[{m.group(2).strip()}]({slug_to_href(m.group(1))})", raw)
    raw = WIKILINK_BARE.sub(lambda m: f"[{m.group(1).strip()}]({slug_to_href(m.group(1))})", raw)
    return raw

def md_to_html(md):
    p = subprocess.run(
        ["pandoc", "-f", "gfm+tex_math_dollars", "-t", "html", "--no-highlight"],
        input=md, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(p.stderr)
    return p.stdout

def plain_text(raw):
    t = resolve_wikilinks(raw)
    t = re.sub(r"`{1,3}[^`]*`{1,3}", " ", t)
    t = re.sub(r"[#>*_|\-\[\]()]", " ", t)
    t = re.sub(r"https?://\S+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def parse_nav(home_raw):
    """Return [(section_title, [(slug,label),...]), ...] from home.md order."""
    nav, cur = [], None
    for line in home_raw.splitlines():
        h = re.match(r"^##\s+(.+?)\s*$", line)
        if h:
            cur = (h.group(1).strip(), [])
            nav.append(cur)
            continue
        if cur is None:
            continue
        for m in WIKILINK_ALIAS.finditer(line):
            slug, label = m.group(1).strip(), m.group(2).strip()
            if slug == "home":
                continue
            if slug not in [s for s, _ in cur[1]]:
                cur[1].append((slug, label))
    return nav

CSS = r"""
:root{
  --bg:#0e1116;--panel:#161b22;--panel2:#1c2230;--text:#d7dde6;--muted:#9aa6b2;
  --link:#7cc7ff;--link2:#a6e3a1;--border:#2a313c;--accent:#8b5cf6;--code:#0b0e13;
  --maxw:820px;
}
@media (prefers-color-scheme: light){
  :root{--bg:#fbfbfd;--panel:#f3f4f7;--panel2:#eceef3;--text:#1c2230;--muted:#5b6675;
    --link:#0969da;--link2:#1a7f37;--border:#e1e4ea;--accent:#6d28d9;--code:#f3f4f7;}
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);
  font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;}
a{color:var(--link);text-decoration:none}
a:hover{text-decoration:underline}
.layout{display:flex;min-height:100vh}
.sidebar{width:300px;flex:0 0 300px;background:var(--panel);border-right:1px solid var(--border);
  height:100vh;position:sticky;top:0;overflow-y:auto;padding:18px 14px 60px}
.brand{display:block;font-weight:700;font-size:20px;color:var(--text);letter-spacing:.2px}
.brand small{display:block;font-weight:400;font-size:12px;color:var(--muted);margin-top:2px}
.search{width:100%;margin:14px 0 8px;padding:9px 11px;border-radius:9px;border:1px solid var(--border);
  background:var(--panel2);color:var(--text);font-size:14px}
#results{list-style:none;margin:0 0 6px;padding:0}
#results li{padding:6px 8px;border-radius:7px}
#results li:hover{background:var(--panel2)}
#results a{display:block}
#results .rtxt{display:block;color:var(--muted);font-size:12px;line-height:1.4;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
nav.toc{margin-top:6px}
nav.toc .sec{margin:14px 0 4px;font-size:11px;text-transform:uppercase;letter-spacing:.08em;
  color:var(--muted);font-weight:700}
nav.toc ul{list-style:none;margin:0 0 6px;padding:0}
nav.toc li{margin:1px 0}
nav.toc a{display:block;padding:4px 8px;border-radius:6px;color:var(--text);font-size:13.5px}
nav.toc a:hover{background:var(--panel2);text-decoration:none}
nav.toc a.active{background:var(--accent);color:#fff}
.main{flex:1;min-width:0;display:flex;justify-content:center;padding:34px 26px 90px}
.content{width:100%;max-width:var(--maxw)}
.crumb{color:var(--muted);font-size:13px;margin-bottom:10px}
.content h1{font-size:30px;line-height:1.2;margin:.2em 0 .5em}
.content h2{font-size:21px;margin-top:1.7em;padding-bottom:.25em;border-bottom:1px solid var(--border)}
.content h3{font-size:17px;margin-top:1.4em}
.content blockquote{margin:1em 0;padding:.6em 1em;border-left:3px solid var(--accent);
  background:var(--panel);border-radius:0 8px 8px 0;color:var(--text)}
.content blockquote em{color:var(--muted)}
.content code{background:var(--code);padding:.12em .4em;border-radius:5px;font-size:.9em;
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.content pre{background:var(--code);padding:14px;border-radius:10px;overflow:auto;border:1px solid var(--border)}
.content pre code{background:none;padding:0}
.content table{border-collapse:collapse;width:100%;margin:1em 0;font-size:14.5px;display:block;overflow-x:auto}
.content th,.content td{border:1px solid var(--border);padding:7px 10px;text-align:left;vertical-align:top}
.content th{background:var(--panel2)}
.content hr{border:none;border-top:1px solid var(--border);margin:2em 0}
.backlinks{margin-top:48px;padding-top:16px;border-top:1px solid var(--border)}
.backlinks h2{font-size:14px;border:none;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.backlinks ul{padding-left:18px;margin:.4em 0;color:var(--muted)}
.downloads{margin-top:40px;padding-top:16px;border-top:1px solid var(--border);
  display:flex;flex-wrap:wrap;align-items:center;gap:10px;font-size:13px}
.downloads .dl-h{color:var(--muted);text-transform:uppercase;letter-spacing:.06em;font-weight:700;font-size:11px}
.downloads a{display:inline-block;padding:6px 11px;border:1px solid var(--border);border-radius:8px;
  background:var(--panel);color:var(--link)}
.downloads a:hover{background:var(--panel2);text-decoration:none}
.topbar{display:none}
.menu-toggle{display:none}
@media (max-width:880px){
  .sidebar{position:fixed;z-index:40;transform:translateX(-100%);transition:transform .2s ease;
    box-shadow:0 0 40px rgba(0,0,0,.5)}
  body.nav-open .sidebar{transform:translateX(0)}
  .topbar{display:flex;align-items:center;gap:12px;position:sticky;top:0;z-index:30;
    background:var(--panel);border-bottom:1px solid var(--border);padding:10px 14px}
  .menu-toggle{display:inline-flex;background:var(--panel2);border:1px solid var(--border);
    color:var(--text);border-radius:8px;padding:7px 11px;font-size:16px;cursor:pointer}
  .topbar .t{font-weight:700}
  .main{padding:18px 16px 80px}
  .scrim{display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:35}
  body.nav-open .scrim{display:block}
}
"""

APP_JS = r"""
let IDX=[];
fetch('search.json').then(r=>r.json()).then(d=>{IDX=d});
const box=document.getElementById('search');
const res=document.getElementById('results');
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
if(box){box.addEventListener('input',()=>{
  const q=box.value.trim().toLowerCase();
  if(!q){res.innerHTML='';return}
  const hits=IDX.map(p=>{
    const t=p.title.toLowerCase(),x=p.text.toLowerCase();
    let s=-1;
    if(t.includes(q))s=0; else {const i=x.indexOf(q); if(i>=0)s=1+i/10000;}
    return {p,s};
  }).filter(o=>o.s>=0).sort((a,b)=>a.s-b.s).slice(0,12);
  res.innerHTML=hits.map(({p})=>`<li><a href="${p.href}">${esc(p.title)}</a><span class="rtxt">${esc(p.text.slice(0,90))}</span></li>`).join('');
});}
const mt=document.getElementById('mt'),scrim=document.getElementById('scrim');
if(mt)mt.addEventListener('click',()=>document.body.classList.toggle('nav-open'));
if(scrim)scrim.addEventListener('click',()=>document.body.classList.remove('nav-open'));
"""

def render_nav(nav, active):
    out = ['<nav class="toc">']
    out.append(f'<a class="brand" href="index.html">{html.escape(SITE_TITLE)}<small>{html.escape(SITE_SUB)}</small></a>')
    out.append('<input id="search" class="search" type="search" placeholder="Search the wiki…" autocomplete="off">')
    out.append('<ul id="results"></ul>')
    for sec, items in nav:
        out.append(f'<div class="sec">{html.escape(sec)}</div><ul>')
        for slug, label in items:
            cls = ' class="active"' if slug == active else ''
            out.append(f'<li><a{cls} href="{slug_to_href(slug)}">{html.escape(label)}</a></li>')
        out.append('</ul>')
    out.append('</nav>')
    return "\n".join(out)

PAGE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · {site}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="style.css">
<script>window.MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}}}};</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head><body>
<div class="topbar"><button id="mt" class="menu-toggle" aria-label="Menu">☰</button><span class="t">{site}</span></div>
<div class="scrim" id="scrim"></div>
<div class="layout">
<aside class="sidebar">{nav}</aside>
<div class="main"><article class="content">{crumb}{body}{backlinks}{downloads}</article></div>
</div>
<script src="app.js"></script>
</body></html>
"""

def downloads_footer(slug):
    name = f"{slug}.md"
    return (
        '<footer class="downloads"><span class="dl-h">Download</span>'
        f'<a href="relics/{name}" download="{name}">This page (.md)</a>'
        '<a href="ultimentality-wiki-complete.md" download="ultimentality-wiki-complete.md">Full corpus (one .md)</a>'
        '<a href="ultimentality-wiki-md.zip" download="ultimentality-wiki-md.zip">All pages (.zip)</a>'
        '</footer>'
    )

def build_monolith(pages, nav):
    parts = ["# Ultimentality — Complete Wiki\n",
             "> The entire Ultimentality wiki as a single Markdown document. "
             "Cross-references use double-bracket `[[wikilinks]]`; "
             "every load-bearing claim carries its dual epistemic (E) / alethic (A) marks.\n",
             "\n## Contents\n", "\n**Home**\n"]
    nav_slugs = []
    for sec, items in nav:
        parts.append(f"\n**{sec}**\n")
        for slug, label in items:
            parts.append(f"- {label}")
            nav_slugs.append(slug)
    leftover = [s for s in sorted(pages) if s != "home" and s not in nav_slugs]
    if leftover:
        parts.append("\n**Other pages**\n")
        for s in leftover:
            parts.append(f"- {pages[s]['title']}")
    order = ["home"] + nav_slugs + leftover

    def prep(md):
        md = re.sub(r'^\[\[home\|[^\]]*\]\]\s*\n+', '', md)          # strip the home backlink line
        md = re.sub(r'(?m)^(#{1,5})(\s)', lambda m: '#' * (len(m.group(1)) + 1) + m.group(2), md)  # demote +1
        return md.strip()

    seen = set()
    for slug in order:
        if slug in seen or slug not in pages:
            continue
        seen.add(slug)
        parts.append("\n\n---\n\n" + prep(pages[slug]["raw"]))
    return "\n".join(parts) + "\n"

def main():
    os.makedirs(OUT, exist_ok=True)
    # clean ONLY generated artifacts; preserve .git, README, CNAME, etc.
    KEEP = {".git", "README.md", "CNAME", ".gitignore"}
    GEN = {"style.css", "app.js", "search.json", ".nojekyll", "relics",
           "ultimentality-wiki-complete.md", "ultimentality-wiki-md.zip"}
    for fn in os.listdir(OUT):
        if fn in KEEP:
            continue
        if fn.endswith(".html") or fn in GEN:
            p = os.path.join(OUT, fn)
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    pages = read_pages()
    if "home" not in pages:
        raise SystemExit("home.md missing")
    nav = parse_nav(pages["home"]["raw"])

    # link graph for backlinks
    graph = {s: link_targets(p["raw"]) for s, p in pages.items()}
    backlinks = {s: [] for s in pages}
    for src, tgts in graph.items():
        for t in tgts:
            if t in backlinks and t != src:
                backlinks[t].append(src)

    search = []
    for slug, p in pages.items():
        body = md_to_html(resolve_wikilinks(p["raw"]))
        # drop the leading "[[home]]" backlink line + duplicate H1 handled by content
        title = p["title"]
        crumb = "" if slug == "home" else f'<div class="crumb"><a href="index.html">Home</a> / {html.escape(title)}</div>'
        bl = sorted(set(backlinks.get(slug, [])))
        if bl and slug != "home":
            items = "".join(
                f'<li><a href="{slug_to_href(b)}">{html.escape(pages[b]["title"])}</a></li>' for b in bl)
            blhtml = f'<div class="backlinks"><h2>Linked from ({len(bl)})</h2><ul>{items}</ul></div>'
        else:
            blhtml = ""
        desc = plain_text(p["raw"])[:150]
        out_html = PAGE.format(title=html.escape(title), site=html.escape(SITE_TITLE),
                               desc=html.escape(desc), nav=render_nav(nav, slug),
                               crumb=crumb, body=body, backlinks=blhtml,
                               downloads=downloads_footer(slug))
        fname = "index.html" if slug == "home" else f"{slug}.html"
        open(os.path.join(OUT, fname), "w", encoding="utf-8").write(out_html)
        # also emit home.html alias so [[home]] -> home.html resolves
        if slug == "home":
            open(os.path.join(OUT, "home.html"), "w", encoding="utf-8").write(out_html)
        search.append({"slug": slug, "title": title, "href": fname, "text": plain_text(p["raw"])[:400]})

    open(os.path.join(OUT, "search.json"), "w", encoding="utf-8").write(json.dumps(search, ensure_ascii=False))
    open(os.path.join(OUT, "style.css"), "w", encoding="utf-8").write(CSS)
    open(os.path.join(OUT, "app.js"), "w", encoding="utf-8").write(APP_JS)
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    if SITE_DOMAIN:
        open(os.path.join(OUT, "CNAME"), "w").write(SITE_DOMAIN)
    # keep the markdown relics in-repo for provenance
    relics = os.path.join(OUT, "relics")
    os.makedirs(relics, exist_ok=True)
    for dirpath, _dirs, files in os.walk(SRC):
        for fn in files:
            if fn.endswith(".md"):
                shutil.copy(os.path.join(dirpath, fn), os.path.join(relics, fn))
    # monolithic single-file corpus
    open(os.path.join(OUT, "ultimentality-wiki-complete.md"), "w", encoding="utf-8").write(
        build_monolith(pages, nav))
    # zip of every page's .md
    with zipfile.ZipFile(os.path.join(OUT, "ultimentality-wiki-md.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, _dirs, files in os.walk(SRC):
            for fn in sorted(files):
                if fn.endswith(".md"):
                    full = os.path.join(dirpath, fn)
                    rel = os.path.relpath(full, SRC)
                    z.write(full, arcname=os.path.join("ultimentality-wiki", rel))
    print(f"built {len(pages)} pages -> {OUT}")
    print("files:", len([f for f in os.listdir(OUT) if f.endswith('.html')]), "html")

if __name__ == "__main__":
    main()
