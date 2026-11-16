import csv, json, collections
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
G=['CYP2C19','CYP2C9','TPMT','NUDT15','SLCO1B1']
rows=[r for r in csv.DictReader(open('benchmark_results_v210.csv')) if r['scenario']=='A_panel_exhaustive']
cat={'concordant_call':'Phenotype call, concordant with reference','concordant_inconclusive_ambiguous':'Inconclusive; reference ambiguous or undefined','conservative_inconclusive_determinable':'Inconclusive by design (not callable, or unphased multi-locus)','conservative_no_reference_call':'Inconclusive; all panel loci reference (no "normal" call)'}
cols=['#1b6ca8','#9aa5b1','#e08e0b','#c9d6e3']
A={g:collections.Counter() for g in G}
for r in rows: A[r['gene']][r['classification']]+=1
B=[b for b in json.load(open('scenarioB_v210.json')) if '.' not in b['allele']]
def rel(f):
    f=str(f).lower()
    return ('no function' in f) or f=='0.0' or ('decreased' in f) or f in('0.5','0.25') or ('increased' in f)
B=[b for b in B if rel(b['function'])]
def bcat(b):
    if b['representation']=='not_represented': return 'nd'
    return {'call_matches':'ok','call_MISMATCH':'bad','inconclusive':'inc'}.get(b['pharmexia_outcome'],'ok')
BC={g:collections.Counter() for g in G}
for b in B: BC[b['gene']][bcat(b)]+=1
fig,ax=plt.subplots(1,2,figsize=(12.5,4.8),dpi=200)
left=[0]*len(G)
for k,c in zip(cat,cols):
    v=[A[g][k] for g in G]; ax[0].barh(G,v,left=left,color=c,label=cat[k],edgecolor='white'); left=[l+x for l,x in zip(left,v)]
ax[0].invert_yaxis(); ax[0].set_xlabel('Genotype combinations at panel loci (n)'); ax[0].set_title('A  Exhaustive panel genotypes (n = 123)',loc='left',fontsize=11,fontweight='bold')
ax[0].legend(fontsize=7.5,loc='lower right',frameon=False)
ax[0].text(0.99,0.02,'',transform=ax[0].transAxes)
k2=[('ok','Detected, phenotype concordant','#1b6ca8'),('inc','Detected, inconclusive by design','#e08e0b'),('bad','Detected, phenotype discordant','#b3261e'),('nd','Not detected, reported inconclusive','#9aa5b1')]
left=[0]*len(G)
for k,l,c in k2:
    v=[BC[g][k] for g in G]; ax[1].barh(G,v,left=left,color=c,label=l,edgecolor='white'); left=[a+b for a,b in zip(left,v)]
ax[1].invert_yaxis(); ax[1].set_xlabel('PharmCAT v3.4.0 named alleles with no, decreased or increased function (n)')
ax[1].set_title('B  Allele catalogue coverage (n = %d)'%len(B),loc='left',fontsize=11,fontweight='bold')
ax[1].legend(fontsize=7.5,loc='lower right',frameon=False)
for a in ax:
    for s in ('top','right'): a.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig('out/figure5_verification.png'); 
print({g:dict(A[g]) for g in G}); print({g:dict(BC[g]) for g in G}); print(len(B))
