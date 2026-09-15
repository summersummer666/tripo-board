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
assert d['collected_at'].split(' Asia/Shanghai')[0] in re.search(r'<!--UPDATED_START-->(.*?)<!--UPDATED_END-->',s,re.S)[1], 'Capture timestamp mismatch'
ads=json.loads(re.search(r'const ADS = (.*?);\s*/\*ADS_END\*/',s,re.S)[1])
assert len(ads)==len(set(a['fb'] for a in ads))
for a in ads:
 r=by_id[a['fb']]
 for k,source in [('v','duplicates'),('started','started'),('ended','ended'),('live','live'),('days','days'),('video','video'),('thumb','thumbnail')]:assert a[k]==r[source],(a['fb'],k)
 assert unescape(a['hook'])==r['title']
 assert a['thumb']
summary=re.search(r'<!--STATS_START-->(.*?)<!--STATS_END-->',s,re.S)[1]
assert f'<b>{len(rows)}</b>' in summary and f'<b>{len(ads)}</b>' in summary
assert f'<b>{sum(r["live"] for r in rows)}</b>' in summary
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
