#!/usr/bin/python
import sys
import genbank_get
import taxonomy_finder

fread = open(sys.argv[1],'r')
path = "../../refsoilgenbank_v1_29_2016/"
for line in fread:
    splt = line.strip().split(',')
    ld = ""
    ac = ""
    ti = ""
    name = ""
    ft = ""
    ld = splt[0]
    ac = line.strip()
    ti = genbank_get.taxon(path+splt[0]+'.gbk')
    name = genbank_get.organism(path+splt[0]+'.gbk')
    ft = taxonomy_finder.full(path+splt[0]+'.gbk')
    print ld + '\t' + ac + '\t' + ti + '\t' + name + '\t' + ft
