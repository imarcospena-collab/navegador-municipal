"""Turn the workbook's Personas tab (readCells JSON saved to personas_read.json) into asp.json for the site.
Only rows for the 2028–2032 term with a status other than 'En el cargo' and a source are published."""
import json, re, unicodedata
def slug(s): s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn'); return re.sub(r'[^a-z0-9]+','-',s).strip('-')
ids={d['name']:d['id'] for d in json.load(open('data/data.json'))}
rows=json.load(open('data/personas_read.json'))['rows']; out={}
for k,r in rows.items():
    if k=='1' or len(r)<11: continue
    gl,_,_,_,per,name,party,_,st,date,src=r[:11]
    if per!='2028–2032' or st in (None,'En el cargo') or not src or gl not in ids: continue
    if isinstance(date,dict): date=date.get('date','')
    out.setdefault(ids[gl],[]).append({'name':name,'party':party or '','status':st,'date':date or '','src':src})
json.dump(out,open('data/asp.json','w'),ensure_ascii=False); print(sum(map(len,out.values())),'aspirantes')
