"""Release integrity checks. Validates artifacts, not LLM behavior or platform runtime."""
import argparse, hashlib, json, re, sys, zipfile
from pathlib import Path
from build import flatten

BASE=Path(__file__).resolve().parents[1]; CORE=BASE/'xjtlu-major-advisor'; VERSION='0.1.2-rc1'; DATA_VERSION='0.1.0-rc1'

def main():
    errors=[]; checks=[]
    def check(label,condition,detail=''):
        checks.append({'check':label,'passed':bool(condition),'detail':detail})
        if not condition: errors.append(label+': '+detail)
    cat=json.loads((BASE/'maintenance/catalog.json').read_text(encoding='utf-8'))
    idx=json.loads((CORE/'references/major-index.json').read_text(encoding='utf-8'))
    sources=json.loads((CORE/'references/source-register.json').read_text(encoding='utf-8'))['sources']
    sourceids={s['source_id'] for s in sources}
    ids=[e['major_id'] for e in cat['majors']]
    check('stable_unique_ids',len(ids)==len(set(ids)))
    check('catalog_index_identity',set(ids)=={e['major_id'] for e in idx['majors']})
    profiles={p.stem for p in (CORE/'references/majors').glob('*.md')}
    check('no_missing_or_orphan_profiles',profiles==set(ids),str(sorted(profiles^set(ids))))
    check('source_ids_unique',len(sources)==len(sourceids))
    check('directory_count_dynamic',cat['directory_count']==len(ids)==idx['directory_count'])
    check('default_personal_eligibility_pending',all(e['eligibility_status']=='pending_verification' for e in cat['majors']))
    for e in cat['majors']:
        p=CORE/'references/majors'/f'{e["major_id"]}.md'; txt=p.read_text(encoding='utf-8')
        check('profile_identity:'+e['major_id'],e['major_id'] in txt and e['official_name'] in txt and DATA_VERSION in txt)
        check('registered_source:'+e['major_id'],e['source_id'] in sourceids and e['url'] in txt)
        courses=[c for y in e['courses'] for v in y['categories'].values() for c in v]
        check('course_transfer:'+e['major_id'],all(c in txt for c in courses),f'{len(courses)} course list entries')
        check('similar_profile:'+e['major_id'],e['similar_id'] in profiles)
    # All actual relative markdown links in source; templates may contain labelled slots.
    badlinks=[]; scanned=0
    for p in BASE.rglob('*.md'):
        if 'dist' in p.relative_to(BASE).parts or 'build-staging' in p.parts: continue
        txt=p.read_text(encoding='utf-8'); scanned+=1
        for label,raw in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',txt):
            if re.match(r'https?://|mailto:|#|codex:',raw): continue
            if any(c in raw for c in '{}<>') or raw.startswith('['): continue
            target=raw.split('#')[0].split(' "')[0]
            if target and not (p.parent/target).exists(): badlinks.append(f'{p.relative_to(BASE)} -> {raw}')
    check('relative_links',not badlinks,'; '.join(badlinks))
    bundles=json.loads((BASE/'adapters/doubao/generated-manifest.json').read_text(encoding='utf-8'))
    check('doubao_version',bundles['version']==VERSION)
    check('doubao_catalog_exact_coverage',{e['major_id'] for e in bundles['majors']}==set(ids) and len(bundles['majors'])==len(ids))
    for e in bundles['majors']:
        src=CORE/e['source_file']; dst=BASE/'adapters/doubao/uploads'/e['group_file']
        check('doubao_source_hash:'+e['major_id'],hashlib.sha256(src.read_bytes()).hexdigest()==e['source_sha256'])
        check('doubao_full_profile:'+e['major_id'],flatten(src.read_text(encoding='utf-8')) in dst.read_text(encoding='utf-8'))
    for p in (BASE/'adapters/doubao/uploads').rglob('*.md'):
        check('txt_equivalence:'+p.name,p.with_suffix('.txt').read_bytes()==p.read_bytes())
    blocked=[]; secret_hits=[]; archivecounts={}
    expected=sum(1 for p in CORE.rglob('*') if p.is_file())
    for p in sorted((BASE/'dist').glob(f'*-{VERSION}.zip')):
        with zipfile.ZipFile(p) as z:
            check('zip_integrity:'+p.name,z.testzip() is None)
            names=z.namelist(); archivecounts[p.name]=len(names)
            for n in names:
                if n.startswith('/') or '..' in Path(n).parts or '\\' in n: blocked.append(p.name+':'+n)
            if '-source-' in p.name: continue
            for n in names:
                if any(t in n.split('/') for t in ('tests','maintenance','__pycache__','.env')) or n.endswith(('.py','.html','.pyc')) or 'fictional-policy' in n: blocked.append(p.name+':'+n)
                if n.endswith(('.md','.txt','.json')):
                    txt=z.read(n).decode('utf-8')
                    if re.search(r'(?<![\w-])sk-[A-Za-z0-9]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|[A-Z]:\\Users\\',txt): secret_hits.append(p.name+':'+n)
            if '-traework-' in p.name or '-workbuddy-' in p.name: check('root_skill:'+p.name,'SKILL.md' in names and len(names)==expected)
            if '-core-' in p.name: check('core_layout','xjtlu-major-advisor/SKILL.md' in names)
            if '-chatgpt-' in p.name: check('plugin_layout','.codex-plugin/plugin.json' in names and 'skills/xjtlu-major-advisor/SKILL.md' in names)
            prefix='skills/xjtlu-major-advisor/' if '-chatgpt-' in p.name else ('xjtlu-major-advisor/' if '-core-' in p.name else '')
            if '-doubao-' not in p.name:
                mismatches=[]
                for f in CORE.rglob('*'):
                    if not f.is_file() or (f.name=='SKILL.md' and '-workbuddy-' in p.name): continue
                    key=prefix+f.relative_to(CORE).as_posix()
                    if key not in names or z.read(key)!=f.read_bytes(): mismatches.append(key)
                check('package_core_identity:'+p.name,not mismatches,', '.join(mismatches))
    check('no_forbidden_student_files_or_archive_paths',not blocked,'; '.join(blocked))
    check('no_key_or_private_path_patterns',not secret_hits,'; '.join(secret_hits))
    # Authorship and synthetic-data labeling are also reviewed by a human-readable audit.
    check('minimum_example_reports',len(list((BASE/'examples').glob('*/report.md')))>=2)
    result={'version':VERSION,'date':'2026-09-19','kind':'static_artifact_validation','passed':not errors,'checks':checks,'counts':{'checks':len(checks),'failed':len(errors),'profiles':len(profiles),'sources':len(sources),'markdown_scanned':scanned,'archives':archivecounts},'limits':['Pattern scans cannot prove absence of all possible personal data; provenance and manual review required.','No platform runtime or actual student counseling claim.']}
    out=BASE/'validation/static-results.json'; out.parent.mkdir(exist_ok=True); out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result['counts'],ensure_ascii=False)); print('\n'.join(errors) if errors else 'PASS')
    return 1 if errors else 0

if __name__=='__main__': sys.exit(main())
