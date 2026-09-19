"""Extract public page facts for curator review; does not infer eligibility."""
import json, sys
from pathlib import Path
from collect import Tree

def extract(e, cache):
    if e['status']!='read': return {**e,'missing':['detail_page']}
    root=Tree((cache/e['cache_file']).read_text(encoding='utf-8')).root
    metadata_dates={}
    for n in root.walk():
        if n.tag=='script' and n.attrs.get('type')=='application/ld+json':
            try:
                schema=json.loads(''.join(c for c in n.children if isinstance(c,str)))
                for item in schema.get('@graph',[]):
                    if item.get('@type')=='WebPage':
                        metadata_dates={k:item.get(k) for k in ('datePublished','dateModified')}
            except (ValueError,TypeError): pass
    main=next((n for n in root.walk() if n.attrs.get('id')=='academics-content'),root)
    nodes=list(main.walk()); fields={}; sections={}
    for n in nodes:
        if n.has('right'):
            ds=[x for x in n.walk() if x.tag=='div' and x.has('link')]
            hs=[x.text() for x in n.walk() if x.tag=='h6']
            if ds and hs: fields[ds[0].text()]='；'.join(hs)
        if n.has('comment-content-container'):
            heads=[x.text() for x in n.walk() if x.tag in ('h2','h3')]
            if heads:
                ps=[x.text() for x in n.walk() if x.tag=='p' and x.text()]
                ls=[x.text() for x in n.walk() if x.tag=='li' and x.text()]
                sections[heads[0]]={'paragraphs':ps,'bullets':ls}
    header=next((n for n in nodes if n.has('header-section-navigation')),None)
    intro=[n.text() for n in header.walk() if n.tag=='p'] if header else []
    courses=[]
    for n in nodes:
        if n.has('accordion-item'):
            hs=[x.text() for x in n.walk() if x.tag=='h4']
            if not hs: continue
            body=next((x for x in n.walk() if x.has('accordion-body')),n)
            buckets={}; kind='未标明必选性质'
            for x in body.walk():
                if x.tag in ('h5','h6'): kind=x.text()
                if x.tag=='li': buckets.setdefault(kind,[]).append(x.text())
            notes=[x.text() for x in body.walk() if x.tag=='p' and (not x.parent or x.parent.tag!='li') and x.text()]
            ancestor=n.parent
            label='课程'
            while ancestor and ancestor!=main:
                headings=[x.text() for x in ancestor.walk() if x.tag=='h2' and not x.has('accordion-header')]
                if headings:
                    label=headings[0]; break
                ancestor=ancestor.parent
            courses.append({'pathway':label,'year':hs[0],'categories':buckets,'notes':notes})
    # Employment blocks sometimes use a different module wrapper.
    careers=[]
    for n in nodes:
        if n.tag in ('h2','h3') and any(t in n.text() for t in ('就业','职业发展','职业前景')):
            p=n.parent
            for _ in range(7):
                ps=[x.text() for x in p.walk() if x.tag in ('p','li') and x.text()]
                if ps: careers=ps; break
                if p.parent and p.parent!=main: p=p.parent
                else: break
    if not careers:
        careers=sections.get('就业',{}).get('paragraphs',[])
    missing=[]
    if not courses: missing.append('yearly_courses')
    if not fields.get('院系'): missing.append('school')
    if not fields.get('学习地点'): missing.append('location')
    if not careers: missing.append('career_text')
    missing+=['programme_selection_threshold','confirmed_cohort_curriculum']
    if not metadata_dates.get('datePublished'): missing.append('page_publication_date')
    return {**e,'page_title':next((n.text() for n in nodes if n.tag=='h1'),''),'fields':fields,'metadata_dates':metadata_dates,'intro':intro,'sections':sections,'courses':courses,'career_text':careers,'missing':missing}

if __name__=='__main__':
    cache=Path(sys.argv[1]); manifest=json.loads((cache/'manifest.json').read_text(encoding='utf-8'))
    data=[extract(e,cache) for e in manifest['entries']]
    (cache/'extracted.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    for i,e in enumerate(data):
        print(i,e['major_id'],e['official_name'],e.get('fields'),len(e.get('courses',[])),e['missing'])
