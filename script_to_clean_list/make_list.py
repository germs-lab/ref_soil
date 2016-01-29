#!/usr/bin/python
import sys
import genbank_get
import taxonomy_finder

fread = open(sys.argv[1],'r')

for line in fread:
    splt = line.strip().split(',')
    ld = ""
    ac = ""
    ti = ""
    name = ""
    ft = ""
    ld = splt[0]
    ac = line.strip()
    
    print ld + '\t' + ac + '\t' + ti + '\t' + name + '\t' + ft
