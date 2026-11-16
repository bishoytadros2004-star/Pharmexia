import sys, os, itertools, importlib, json; sys.path.insert(0,'.'); import stubs
oncox=importlib.import_module(os.environ.get('PGX_MODULE','oncox'))
FWD={'rs1800462':('C','G'),'rs1800460':('C','T'),'rs1142345':('T','C'),'rs9923231':('C','T')}
def run(gene,combo,loci,forward):
    vs=[]
    for r,c in zip(loci,combo):
        d=[x for x in oncox.ALLELE_DEFINITIONS[gene] if x['rsid']==r][0]
        ref,alt=(FWD[r] if (forward and r in FWD) else (None,d['alt']))
        vs.append(oncox.ObservedVariant(chrom=None,pos=None,ref=ref,alt=alt,rsid=r,genotype={0:'0/0',1:'0/1',2:'1/1'}[c],genotype_code=c,gene=gene))
    a=oncox.assess_pharmacogenes(vs)[gene]
    return (a.local_panel_call,a.phenotype,a.call_confidence,tuple(sorted(m.rsid for m in a.matched_alleles)))
tot=0;bad=0
for gene in ['TPMT','VKORC1']:
    loci=[d['rsid'] for d in oncox.ALLELE_DEFINITIONS[gene]]
    for combo in itertools.product([0,1,2],repeat=len(loci)):
        tot+=1
        if run(gene,combo,loci,True)!=run(gene,combo,loci,False): bad+=1
print(os.environ.get('PGX_MODULE','oncox'),'forward-vs-gene-strand scenarios:',tot,'discordant:',bad)
