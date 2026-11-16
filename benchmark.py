"""Analytical verification of Pharmexia star-allele/phenotype assignment against PharmCAT v3.4.0 tables.
Oracle = exhaustive phase enumeration over PharmCAT named-allele definitions + PharmCAT phenotype lookup."""
import sys, json, itertools, pathlib, csv, collections
import os, importlib; sys.path.insert(0,'.'); import stubs; oncox=importlib.import_module(os.environ.get('PGX_MODULE','oncox'))
PC = pathlib.Path('/home/claude/pharmgkb/pharmcat/src/main/resources/org/pharmgkb/pharmcat')
GENES = ['CYP2C19','CYP2C9','TPMT','NUDT15','SLCO1B1']
RULES = json.load(open('data/star_allele_rules.json'))['genes']
DEFS = oncox.ALLELE_DEFINITIONS

def load(gene):
    tr=json.load(open(PC/f'definition/alleles/{gene}_translation.json'))
    ph=json.load(open(PC/f'phenotype/{gene}.json'))
    var=tr['variants']; pos_by_rs={v['rsid']:i for i,v in enumerate(var) if v.get('rsid')}
    alleles={}
    base_na=[na for na in tr['namedAlleles'] if na['name']=='*1'] or [na for na in tr['namedAlleles'] if na['reference']]
    baseline=[x if x is not None else var[i]['ref'] for i,x in enumerate(base_na[0]['alleles'])]
    for na in tr['namedAlleles']:
        alt=set()
        for i,x in enumerate(na['alleles']):
            if x is None: continue
            if baseline[i] not in set(x.split(' or ')): alt.add(i)
        core={idx for idx,v in enumerate(var) if v['position'] in set(na.get('corePositions') or [])}
        alleles[na['name']]=dict(alt=frozenset(alt&core) if core else frozenset(alt),ref=(na['name']=='*1'),sv=na['structuralVariant'])
    ptab={tuple(sorted(e['diplotypekey'].items())):e['generesult'] for e in ph['diplotypes']}
    return tr,var,pos_by_rs,alleles,ph['haplotypes'],ptab
DATA={g:load(g) for g in GENES}

TAG_USED=[False]
def hap_name(gene,S):
    """Name a panel-visible haplotype S (set of panel locus indices carrying alt). Uses PharmCAT core definitions;
    where an allele has additional core positions outside the panel, the panel locus acts as a tag SNP (flagged)."""
    _,_,pos_by_rs,alleles,_,_=DATA[gene]
    P={pos_by_rs[d['rsid']] for d in DEFS[gene]}
    S=frozenset(S)
    if not S: return '*1'
    cands=[(len(a['alt']),n) for n,a in alleles.items() if not a['sv'] and (a['alt']&P)==S and '.' not in n]
    if not cands: return None
    cands.sort(); 
    if len(cands)>1 and cands[0][0]==cands[1][0]: return None
    n=cands[0][1]
    if not alleles[n]['alt']<=P: TAG_USED[0]=True
    return n
def oracle(gene, geno):  # geno: {rsid: 0/1/2}
    tr,var,pos_by_rs,alleles,func,ptab=DATA[gene]
    loci=[pos_by_rs[r] for r in geno]; cn=[geno[r] for r in geno]
    het=[l for l,c in zip(loci,cn) if c==1]; hom=[l for l,c in zip(loci,cn) if c==2]
    outcomes=set(); dips=set(); TAG_USED[0]=False
    for assign in itertools.product([0,1],repeat=len(het)):
        h=[set(hom),set(hom)]
        for l,a in zip(het,assign): h[a].add(l)
        n=[hap_name(gene,s) for s in h]
        if None in n: outcomes.add('UNDEFINED'); continue
        c=collections.Counter(n); key=tuple(sorted(c.items()))
        outcomes.add(ptab.get(key,'NO_TABLE_ENTRY')); dips.add('/'.join(sorted(n)))
    if len(outcomes)==1 and 'UNDEFINED' not in outcomes and 'NO_TABLE_ENTRY' not in outcomes:
        return 'DETERMINATE',next(iter(outcomes)),sorted(dips)+(['(tag-SNP assumption)'] if TAG_USED[0] else [])
    return 'AMBIGUOUS',sorted(outcomes),sorted(dips)

def run_pharmexia(gene, geno, alt_override=None):
    vs=[]
    for d in DEFS[gene]:
        r=d['rsid']
        if r not in geno: continue
        c=geno[r]
        vs.append(oncox.ObservedVariant(chrom=None,pos=None,ref=None,alt=(alt_override or {}).get(r,d['alt']),rsid=r,
            genotype={0:'0/0',1:'0/1',2:'1/1'}[c],genotype_code=c,gene=gene))
    a=oncox.assess_pharmacogenes(vs)[gene]
    ph=a.phenotype; 
    if ph: ph=ph.replace('Possible ','').replace(' (limited local panel)','')
    return dict(call=a.local_panel_call,phenotype=ph,confidence=a.call_confidence,ambiguous=a.ambiguous,coverage=a.coverage_complete)

rows=[]
# Scenario A: exhaustive panel genotype combinations, full coverage
for g in GENES:
    loci=[d['rsid'] for d in DEFS[g]]
    for combo in itertools.product([0,1,2],repeat=len(loci)):
        geno=dict(zip(loci,combo)); o=oracle(g,geno); p=run_pharmexia(g,geno)
        called=p['phenotype'] is not None
        if o[0]=='DETERMINATE':
            if all(c==0 for c in combo): cls='conservative_no_reference_call'
            elif called and p['phenotype']==o[1]: cls='concordant_call'
            elif called: cls='DISCORDANT_call'
            else: cls='conservative_inconclusive_determinable'
        else:
            cls='DISCORDANT_overcall' if called else 'concordant_inconclusive_ambiguous'
        rows.append(dict(scenario='A_panel_exhaustive',gene=g,genotype=';'.join(f'{k}={v}' for k,v in geno.items()),
            oracle_status=o[0],oracle_phenotype=o[1] if o[0]=='DETERMINATE' else '|'.join(o[1]),oracle_diplotype='|'.join(o[2]),
            pharmexia_call=p['call'],pharmexia_phenotype=p['phenotype'],pharmexia_confidence=p['confidence'],classification=cls))
# Scenario C: incomplete coverage (strict subsets of loci observed)
for g in GENES:
    loci=[d['rsid'] for d in DEFS[g]]
    if len(loci)<2: continue
    for k in range(1,len(loci)):
        for sub in itertools.combinations(loci,k):
            for combo in itertools.product([0,1,2],repeat=k):
                geno=dict(zip(sub,combo)); p=run_pharmexia(g,geno)
                rows.append(dict(scenario='C_incomplete_coverage',gene=g,genotype=';'.join(f'{a}={b}' for a,b in geno.items()),
                    oracle_status='n/a',oracle_phenotype='',oracle_diplotype='',pharmexia_call=p['call'],pharmexia_phenotype=p['phenotype'],
                    pharmexia_confidence=p['confidence'],classification='DISCORDANT_call_under_incomplete_coverage' if p['phenotype'] else 'concordant_inconclusive_incomplete'))
# Scenario D: unsupported alt allele at a panel locus
for g in GENES:
    loci=[d['rsid'] for d in DEFS[g]]
    for r in loci:
        geno={x:0 for x in loci}; geno[r]=1
        p=run_pharmexia(g,geno,alt_override={r:'N'})
        rows.append(dict(scenario='D_unsupported_alt',gene=g,genotype=';'.join(f'{a}={b}' for a,b in geno.items()),oracle_status='n/a',oracle_phenotype='',oracle_diplotype='',
            pharmexia_call=p['call'],pharmexia_phenotype=p['phenotype'],pharmexia_confidence=p['confidence'],
            classification='DISCORDANT_call_unsupported_alt' if p['phenotype'] else 'concordant_inconclusive_unsupported_alt'))
# Scenario B: allele catalogue coverage and hidden-allele simulation
B=[]
for g in GENES:
    tr,var,pos_by_rs,alleles,func,ptab=DATA[g]
    panel_pos={pos_by_rs[d['rsid']] for d in DEFS[g]}
    panel_names={d['allele'].replace('_component','') for d in DEFS[g]}
    for n,a in alleles.items():
        if a['ref'] or a['sv']: continue
        f=func.get(n,'Unknown')
        key=tuple(sorted({(('*1',1),(n,1))}))
        pk=tuple(sorted([('*1',1),(n,1)]))
        ph=ptab.get(pk)
        overlap=bool(a['alt']&panel_pos)
        # simulate sample *1/*n: panel genotype = het at panel positions in A(n)
        loci=[d['rsid'] for d in DEFS[g]]
        geno={r:(1 if pos_by_rs[r] in a['alt'] else 0) for r in loci}
        p=run_pharmexia(g,geno)
        if n in panel_names and len(a['alt']&panel_pos)==len(a['alt']): rep='represented'
        elif overlap: rep='partial_overlap'
        else: rep='not_represented'
        if p['phenotype'] is None: out='inconclusive'
        elif ph is None: out='call_vs_no_reference_phenotype'
        elif p['phenotype']==ph: out='call_matches'
        else: out='call_MISMATCH'
        B.append(dict(gene=g,allele=n,function=f,pharmcat_phenotype_1_n=ph,representation=rep,pharmexia_phenotype=p['phenotype'],pharmexia_outcome=out,pharmexia_call=p['call']))
json.dump(B,open('scenarioB.json','w'),indent=1)
with open('benchmark_results.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
cnt=collections.Counter((r['scenario'],r['classification']) for r in rows)
for k,v in sorted(cnt.items()): print(k,v)
print('total rows',len(rows))
print('--- scenario B (alleles with non-normal/uncertain function) ---')
bc=collections.Counter((b['gene'],b['representation'],b['pharmexia_outcome']) for b in B)
for k,v in sorted(bc.items()): print(k,v)
