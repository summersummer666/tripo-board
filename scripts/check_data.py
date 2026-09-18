"""Verify published card counts and timestamps against the actual capture ledger."""
from pathlib import Path
import json,re
from html import unescape
from html.parser import HTMLParser
root=Path(__file__).resolve().parents[1]
s=(root/'index.html').read_text()
name=re.search(r'href="(ads-snapshot-[\d-]+\.json)"',s)[1]
d=json.loads((root/name).read_text()); rows=d['records']; by_id={r['id']:r for r in rows}
assert len(rows)==len(by_id),'Duplicate IDs in capture ledger'
capture_stamp=d['collected_at'].split(' Asia/Shanghai')[0]
assert capture_stamp in s, 'Full-ledger timestamp is not disclosed in the page'
ads=json.loads(re.search(r'const ADS = (.*?);\s*/\*ADS_END\*/',s,re.S)[1])
assert len(ads)==len(set(a['fb'] for a in ads))
for a in ads:
 r=by_id[a['fb']]
 for k,source in [('v','duplicates'),('started','started'),('ended','ended'),('live','live'),('days','days'),('video','video'),('thumb','thumbnail')]:assert a[k]==r[source],(a['fb'],k)
 assert unescape(a['hook'])==r['title']
 assert a['thumb']
summary=re.search(r'<!--STATS_START-->(.*?)<!--STATS_END-->',s,re.S)[1]
assert str(len(rows)) in summary, 'Full-ledger row count is not disclosed in the header'
top_path=root/'foreplay-top5-2026-09-18.json'
if top_path.exists():
 top=json.loads(top_path.read_text())
 assert top['window_start']=='2026-09-12' and top['window_end']=='2026-09-18'
 for brand in ['Suno','ElevenLabs','Bambu Lab 3D','ELEGOO','Creality']:
  cases=[x for x in top['cases'] if x['brand']==brand]
  assert 0 < len(cases) <= 5, (brand,len(cases))
  assert [x['duplicates'] for x in cases]==sorted((x['duplicates'] for x in cases),reverse=True),brand
  assert len({x['video'] or x['thumb'] for x in cases})==len(cases),brand
 assert '近 7 天' in s and top['checked_at'][:10] in s
class Links(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if 'id' in a:self.ids.append(a['id'])
  if t=='a':self.links.append(a.get('href',''))
l=Links();l.feed(s);assert len(l.ids)==len(set(l.ids)),'Duplicate HTML IDs'
for href in l.links:
 if href.startswith('#'):assert href[1:] in l.ids,href
 elif href and not href.startswith(('https:','http:','mailto:')) and '${' not in href:assert (root/href.split('#')[0]).exists(),href
assert '/Users/' not in s,'Local paths exposed'
print(f'PASS: {len(rows)} ledger rows, {len(ads)} cards, timestamp, links and IDs')
