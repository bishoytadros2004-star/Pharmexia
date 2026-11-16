import json, pathlib, sys, io, contextlib, os, importlib
sys.path.insert(0,'.'); import stubs; oncox=importlib.import_module(os.environ.get('PGX_MODULE','oncox'))
PC=pathlib.Path('/home/claude/pharmgkb/pharmcat/src/main/resources/org/pharmgkb/pharmcat/definition/alleles')
pos={}
for g in ['CYP2C19','CYP2C9','TPMT','NUDT15','SLCO1B1','VKORC1']:
    tr=json.load(open(PC/f'{g}_translation.json'))
    for v in tr['variants']:
        if v.get('rsid'): pos[v['rsid']]=(v['chromosome'],v['position'],v['ref'],v['alts'][0] if v['alts'] else None,v['rsid'])
SAMPLES={
 'S01_normal_reference_all_panel':{},
 'S02_cyp2c19_poor_2_2':{'rs4244285':'1/1'},
 'S03_cyp2c19_rapid_1_17_cyp2c9_im_1_3':{'rs12248560':'0/1','rs1057910':'0/1','rs9923231':'0/1'},
 'S04_thiopurine_tpmt2_nudt15_3_het':{'rs1800462':'0/1','rs116855232':'0/1'},
 'S05_tpmt_ambiguous_3A_or_3B3C':{'rs1800460':'0/1','rs1142345':'0/1'},
 'S06_slco1b1_decreased':{'rs4149056':'0/1'},
 'S07_cyp2c19_4_het':{'rs28399504':'0/1'},
 'S08_cyp2c19_4B_or_4A17_unphased':{'rs12248560':'0/1','rs28399504':'0/1'},
}
panel=[d['rsid'] for g,ds in oncox.ALLELE_DEFINITIONS.items() if g in('CYP2C19','CYP2C9','TPMT','NUDT15','SLCO1B1','VKORC1') for d in ds]
def chrom_key(c): return int(c[3:])
rows=sorted([pos[r] for r in panel],key=lambda x:(chrom_key(x[0]),x[1]))
for name,gt in SAMPLES.items():
    L=['##fileformat=VCFv4.2','##reference=GRCh38','##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">','#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t'+name]
    for c,p,ref,alt,rs in rows:
        L.append(f'{c}\t{p}\t{rs}\t{ref}\t{alt}\t.\tPASS\t.\tGT\t{gt.get(rs,"0/0")}')
    pathlib.Path(f'test_files_v210/{name}.vcf').write_text('\n'.join(L)+'\n')
# CSV equivalent for S02
import csv
with open('test_files_v210/S02_cyp2c19_poor_2_2.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['rsid','ref','alt','genotype','sample_id'])
    for r in panel: w.writerow([r,pos[r][2],pos[r][3],SAMPLES['S02_cyp2c19_poor_2_2'].get(r,'0/0'),'S02'])
print(len(rows),'panel loci:',[r[4] for r in rows])
svc=oncox.AnalysisService()
drugs=['clopidogrel','warfarin','azathioprine','simvastatin']
for name in SAMPLES:
    with contextlib.redirect_stdout(io.StringIO()):
        r=svc.analyze_file(pathlib.Path(f'test_files_v210/{name}.vcf'),selected_drugs=drugs)
    print('##',name,'overall',r.overall_category,'valid',r.validation.is_valid if hasattr(r.validation,'is_valid') else '')
    for f in r.findings: print('   ',f.drug,f.category,f.result_kind,f.diplotype,f.phenotype)
with contextlib.redirect_stdout(io.StringIO()):
    r=svc.analyze_file(pathlib.Path('test_files_v210/S02_cyp2c19_poor_2_2.csv'),selected_drugs=['clopidogrel'])
print('CSV S02:',[(f.drug,f.category,f.diplotype,f.phenotype) for f in r.findings])
