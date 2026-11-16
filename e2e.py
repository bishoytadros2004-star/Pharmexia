import sys, json, pathlib, io, contextlib
sys.path.insert(0,'.'); import stubs, oncox
svc=oncox.AnalysisService()
def V(rs,c,gene=None):
    d=[x for g,ds in oncox.ALLELE_DEFINITIONS.items() for x in ds if x['rsid']==rs][0]
    g=[g for g,ds in oncox.ALLELE_DEFINITIONS.items() if d in ds][0]
    return oncox.ObservedVariant(chrom=None,pos=None,ref=None,alt=d['alt'],rsid=rs,genotype={0:'0/0',1:'0/1',2:'1/1'}[c],genotype_code=c,gene=g)
def panel(gene,**kv):
    return [V(d['rsid'],kv.get(d['rsid'],0)) for d in oncox.ALLELE_DEFINITIONS[gene]]
cases={
 'CYP2C19 all-reference, clopidogrel':(panel('CYP2C19'),['clopidogrel']),
 'CYP2C19 *2/*2, clopidogrel':(panel('CYP2C19',rs4244285=2),['clopidogrel']),
 'CYP2C19 *2 het + *17 het (unphased), clopidogrel':(panel('CYP2C19',rs4244285=1,rs12248560=1),['clopidogrel']),
 'CYP2C19 *2 het with rs4986893 missing, clopidogrel':([V('rs4244285',1),V('rs12248560',0)],['clopidogrel']),
 'TPMT rs1800460+rs1142345 het (3A vs 3B/3C), azathioprine':(panel('TPMT',rs1800460=1,rs1142345=1),['azathioprine']),
 'TPMT *1/*2 + NUDT15 *1/*3, mercaptopurine':(panel('TPMT',rs1800462=1)+panel('NUDT15',rs116855232=1),['mercaptopurine']),
 'CYP2C9 *1/*3 + VKORC1 A/A, warfarin':(panel('CYP2C9',rs1057910=1)+[V('rs9923231',2)],['warfarin']),
 'SLCO1B1 rs4149056 het, simvastatin':(panel('SLCO1B1',rs4149056=1),['simvastatin']),
}
for name,(vs,drugs) in cases.items():
    with contextlib.redirect_stdout(io.StringIO()):
        r=svc.analyze_variants(vs,selected_drugs=drugs)
    print('##',name,'| overall:',r.overall_category)
    for f in r.findings:
        print('  ',f.drug,f.gene,'|',f.category,f.result_kind,'| dip:',f.diplotype,'| pheno:',f.phenotype,'| clin_grade:',f.clinical_grade)
        print('     rec:',(f.recommendation or '')[:150].replace('\n',' '))
    for g,a in r.gene_assessments.items():
        if a.observed_target_loci: print('   gene',g,a.local_panel_call,a.phenotype,a.call_confidence,'ambiguous' if a.ambiguous else '')
