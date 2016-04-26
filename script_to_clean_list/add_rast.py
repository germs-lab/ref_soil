#!/usr/bin/python
# usage: python add_rast.py id_map.txt rastID_to_ncbiACC.txt RefSoil_v1.base.txt > supplemental_table1_RefSoil_v1.txt

import sys
idmap = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    idmap[spl[0]]=spl[1]

rast = {}
for line in open(sys.argv[2],'r'):
    if (line[:3]=="Ref"):
        continue
    spl = line.strip().split('\t')
    if (rast.has_key(spl[0])):
        temp = rast[spl[0]]
        temp.append(spl[2])
        rast[spl[0]]=temp
    else:
        rast[spl[0]]=[spl[2]]

for line in open(sys.argv[3],'r'):
    if (line[:2]=="id"):
        print '\t'.join(["RefSoil ID","NCBI ID","Taxon ID","Kingdom","Phylum","Class","Order","Family","Genus","Species","Organism","RAST ID"])
        continue
    spl = line.strip().split('\t')
    rastid = ""
    if(rast.has_key(spl[0])):
        rastid = ','.join(rast[spl[0]])
    for i in range(6,13):
        if(spl[i]=="null"):
            spl[i]=""
    print '\t'.join([idmap[spl[0]],spl[2],spl[3],spl[6],spl[7],spl[8],spl[9],spl[10],spl[11],spl[12],spl[5],rastid])
