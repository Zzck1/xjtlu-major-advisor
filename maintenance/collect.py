"""Maintainer-only public source collector. Python 3 standard library; no student dependency.
Usage: python maintenance/collect.py --cache /path/to/work/school-cache
Preserves raw public pages outside student distributions; never reads private student data.
"""
import argparse, concurrent.futures, hashlib, json, re, time, urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

class Node:
    def __init__(self, tag='', attrs=None, parent=None):
        self.tag, self.attrs, self.parent, self.children = tag, dict(attrs or []), parent, []
    def text(self):
        return re.sub(r'\s+', ' ', ''.join(x.text() if isinstance(x, Node) else x for x in self.children)).strip()
    def walk(self):
        yield self
        for x in self.children:
            if isinstance(x, Node): yield from x.walk()
    def has(self, cls): return cls in self.attrs.get('class','').split()

class Tree(HTMLParser):
    VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def __init__(self, data):
        super().__init__(convert_charrefs=True)
        self.root = Node('root'); self.current = self.root; self.feed(data)
    def handle_starttag(self, tag, attrs):
        n=Node(tag,attrs,self.current); self.current.children.append(n)
        if tag not in self.VOID: self.current=n
    def handle_endtag(self, tag):
        n=self.current
        while n.parent and n.tag != tag: n=n.parent
        if n.parent: self.current=n.parent
    def handle_data(self,data): self.current.children.append(data)

def fetch(url, path):
    for attempt in range(3):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (public education research)'})
            with urllib.request.urlopen(req,timeout=45) as r:
                raw=r.read(); final=r.url; status=r.status
            path.write_bytes(raw)
            return {'url':url,'final_url':final,'http_status':status,'bytes':len(raw), 'sha256':hashlib.sha256(raw).hexdigest(),'retrieved_at':datetime.now(timezone.utc).isoformat(),'status':'read'}
        except Exception as e:
            error=f'{type(e).__name__}: {e}'
            if attempt<2: time.sleep(attempt+1)
    return {'url':url,'status':'failed','error':error}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--cache',required=True); a=ap.parse_args()
    cache=Path(a.cache); cache.mkdir(parents=True,exist_ok=True)
    index_url='https://www.xjtlu.edu.cn/zh/study/undergraduate'
    index=fetch(index_url,cache/'undergraduate.html')
    if index['status']!='read': raise RuntimeError(index)
    tree=Tree((cache/'undergraduate.html').read_text(encoding='utf-8')).root
    cards=[n for n in tree.walk() if n.tag=='a' and n.has('study_item')]
    entries=[]
    for n in cards:
        slug=n.attrs['href'].rstrip('/').split('/')[-1]
        entries.append({'major_id':'xjtlu-'+slug,'official_name':n.attrs.get('data-title',n.text()),'url':n.attrs['href'],'directory_school_id':n.attrs.get('data-school'),'cache_file':slug+'.html'})
    if not entries or len({x['major_id'] for x in entries})!=len(entries): raise RuntimeError('Empty or duplicate directory')
    def job(e): return {**e,**fetch(e['url'],cache/e['cache_file'])}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(job,entries))
    (cache/'manifest.json').write_text(json.dumps({'directory':index,'entries':results},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'entries':len(results),'read':sum(e['status']=='read' for e in results),'failed':[e['major_id'] for e in results if e['status']!='read']},ensure_ascii=False))

if __name__=='__main__': main()
