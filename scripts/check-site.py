"""Check publishable static artifacts, internal links and core data invariants."""
import json,re,sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
class Page(HTMLParser):
 def __init__(self): super().__init__(); self.ids=[]; self.refs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  for key in ['href','src']:
   if key in a:self.refs.append(a[key])
  if 'style' in a:self.refs.extend(re.findall(r'url\([\'\"]?([^\)\'\"]+)',a['style']))
pages={p:Page() for p in DOCS.glob('*.html')}
errors=[]
for p,parser in pages.items():
 parser.feed(p.read_text(encoding='utf8'))
 if len(parser.ids)!=len(set(parser.ids)): errors.append(f'Duplicate IDs: {p.name}')
routes={'overview','atlas','questionnaire','observers','genesis','teacher','matrix','sources','about','main'}
for p,parser in pages.items():
 for ref in parser.refs:
  u=urlsplit(ref)
  if u.scheme or ref.startswith('//'):continue
  dest=(p.parent/unquote(u.path)).resolve() if u.path else p
  if dest.is_dir():dest=dest/'index.html'
  if not dest.is_relative_to(DOCS.resolve()):errors.append(f'Escaping public directory: {p.name}: {ref}');continue
  if not dest.exists():errors.append(f'Missing: {p.name}: {ref}');continue
  if u.fragment and dest in pages and not(dest.name=='index.html' and u.fragment in routes):
   if u.fragment not in pages[dest].ids:errors.append(f'Missing anchor: {p.name}: {ref}')
for p in DOCS.rglob('*'):
 if any(x in p.parts for x in ['.private','.git','node_modules']):errors.append(f'Private/build data in publication: {p}')
 if p.is_file() and p.suffix in ['.json','.html','.js','.md']:
  s=p.read_text(encoding='utf8')
  if re.search(r'gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{30,}',s):errors.append(f'Possible credential in public file: {p}')
 if p.is_file() and p.suffix=='.css':
  for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)',p.read_text(encoding='utf8')):
   u=urlsplit(ref)
   if not u.scheme and not ref.startswith('//') and not (p.parent/unquote(u.path)).is_file():errors.append(f'Missing CSS asset: {p.name}: {ref}')
q=json.loads((DOCS/'data/questionnaire.json').read_text(encoding='utf8'))
questions=[x for d in q['domains'] for x in d['questions']]
assert len(questions)==288 and len(q['lenses'])==12
assert len({x['id'] for x in questions})==288
assert len({x['prompt'] for x in questions})==288
demo=json.loads((DOCS/'data/demo-answers.json').read_text(encoding='utf8'))
assert len(demo['answers'])==48 and all(x['kind']=='simulated' for x in demo['answers'])
known_sources={s['id'] for s in json.loads((DOCS/'data/sources.json').read_text(encoding='utf8'))['sources']}
for x in demo['answers']:assert set(x['sourceRefs'])<=known_sources
atlas=json.loads((DOCS/'data/weaving-atlas.json').read_text(encoding='utf8'))
assert len(atlas['territories'])==100 and sum(t['quota'] for t in atlas['territories'])==100000
assert atlas['status']['generated']<=100000 and atlas['status']['checked']<=atlas['status']['generated']
assert atlas['status']['answered']<=atlas['status'].get('accepted',atlas['status']['checked'])
snapshot=DOCS/'data/weaving-status.json'
if snapshot.exists():
 current=json.loads(snapshot.read_text(encoding='utf8'))['counts']
 for key in ['planned','generated','checked','accepted','answered']:assert atlas['status'].get(key,0)==current[key],f'Atlas/snapshot mismatch: {key}'
result={'htmlPages':len(pages),'internalReferences':sum(len(p.refs) for p in pages.values()),'seedQuestions':288,'reflectionLenses':12,'demoAnswers':48,'territories':100,'plannedSlots':100000,'errors':errors}
print(json.dumps(result,indent=2))
sys.exit(bool(errors))
