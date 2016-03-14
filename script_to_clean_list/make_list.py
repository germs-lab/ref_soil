#!/usr/bin/python
#usage: python make_list.py RefSoil_v1_chromosome.txt
import sys
import genbank_get
import taxonomy_finder

fread = open(sys.argv[1],'r')
path = "../../refsoilgenbank_vlist05/"
header = ["id","chromosom","version","taxon","definition","organism","kingdom","phylum","class","order","family","genus","species"]
print '\t'.join(header)
for line in fread:
    splt = line.strip().split(',')
    filename = path+splt[0]+'.gbk'
    ld = ""
    ac = ""
    vr = ""
    ti = ""
    de = ""
    name = ""
    ft = ""
    ld = splt[0]
    ac = line.strip()
    for x in splt:
        tempfilename = path+x+'.gbk'
        tempvr = genbank_get.version(tempfilename)
        if(vr == ""):
            vr = tempvr
        else:
            vr = vr + ',' + tempvr
    ti = genbank_get.taxon(filename)
    de = genbank_get.definition(filename)
    name = genbank_get.organism(filename)
    ft = taxonomy_finder.full(filename)
    print ld + '\t' + ac + '\t' + vr + '\t' +ti + '\t' + de + '\t' + name + '\t' + ft
