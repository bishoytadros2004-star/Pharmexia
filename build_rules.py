"""Build data/star_allele_rules.json for the panel from PharmCAT v3.4.0 phenotype tables."""
import json, pathlib
PC = pathlib.Path('/home/claude/pharmgkb/pharmcat/src/main/resources/org/pharmgkb/pharmcat')
PANEL = {  # gene: (reference, [(allele, rsid, alt, callable)])
 'CYP2C19': ('*1',[('*2','rs4244285','A',True),('*3','rs4986893','A',True),('*17','rs12248560','T',True),('*4','rs28399504','G',True)]),
 'CYP2C9':  ('*1',[('*2','rs1799853','T',True),('*3','rs1057910','C',True)]),
 'TPMT':    ('*1',[('*2','rs1800462','C',True),('*3B_component','rs1800460','A',False),('*3C_component','rs1142345','G',False)]),
 'NUDT15':  ('*1',[('*3','rs116855232','T',True)]),
 'SLCO1B1': ('*1',[('*5','rs4149056','C',True)]),
}
PCNAME = {'*3B_component':'*3B','*3C_component':'*3C'}
CPIC = {'CYP2C19':'CPIC_CLOPIDOGREL','CYP2C9':'CPIC_WARFARIN','TPMT':'CPIC_THIOPURINES','NUDT15':'CPIC_THIOPURINES','SLCO1B1':'CPIC_STATINS'}
def pheno_table(gene):
    d=json.load(open(PC/f'phenotype/{gene}.json'))
    t={}
    for e in d['diplotypes']:
        key=tuple(sorted(e['diplotypekey'].items()))
        t[key]=e['generesult']
    return d,t
out={'schema_version':'2.0-pharmcat3.4.0-reference','genes':{},'source_layers':[
  {'name':'PharmCAT phenotype tables','version':'v3.4.0 (ClinPGx data 2026-07-13)','url':'https://github.com/PharmGKB/PharmCAT'},
  {'name':'CPIC guidelines','url':'https://cpicpgx.org/guidelines/'}]}
for gene,(ref,als) in PANEL.items():
    d,t=pheno_table(gene)
    alleles={}
    for a,rs,alt,call in als:
        pc=PCNAME.get(a,a)
        func=d['haplotypes'].get(pc,'Unknown')
        notes=[] if call else [f'{pc} is defined by {rs} alone only when the other TPMT*3 locus is reference; with both loci heterozygous, *1/*3A and *3B/*3C cannot be distinguished without phase, so no standalone call is made.']
        alleles[a]=dict(rsid=rs,alt=alt,callable=call,function=func,notes=notes,sources=[{'label':'PharmCAT/CPIC','url':'https://cpicpgx.org/'}])
    dp={}
    callable_=[a for a,_,_,c in als if c]
    for a in callable_:
        for pair in ((ref,a),(a,a)):
            if pair[0]==pair[1]: key=((pair[0],2),)
            else: key=tuple(sorted([(pair[0],1),(pair[1],1)]))
            ph=t.get(key)
            lab='/'.join(sorted(pair)) if False else (pair[0]+'/'+pair[1] if pair[0]<=pair[1] else pair[1]+'/'+pair[0])
            if ph: dp[lab]=ph
    out['genes'][gene]=dict(reference_allele=ref,required_loci=[rs for _,rs,_,_ in als],
        calling_strategy='single_nonreference_locus_only',allow_reference_call=False,
        confidence_categories={'supported':'LIMITED_PANEL_SUPPORTED','inconclusive':'INCONCLUSIVE'},
        alleles=alleles,diplotype_phenotypes=dp,
        limitations=[f'{gene}: only the panel alleles listed are detected; absence of a panel allele does not establish *1/*1.'],
        sources=[{'label':CPIC[gene],'url':'https://cpicpgx.org/guidelines/'}])
pathlib.Path('data').mkdir(exist_ok=True)
json.dump(out,open('data/star_allele_rules.json','w'),indent=2)
for g,v in out['genes'].items(): print(g,v['diplotype_phenotypes'])
