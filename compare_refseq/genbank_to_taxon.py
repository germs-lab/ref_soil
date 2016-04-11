#!/usr/bin/python
import sys


fread = open(sys.argv[1],'r')
locus = ""
flag = 0
for gbline in fread:
    if ("LOCUS" in gbline):
        locus = gbline.strip().split(" ")[7]
    if("taxon:" in gbline and flag == 0):
        organism = gbline.strip().split(":")[1][:-1]
        flag = 1
    if(gbline.strip()[:2] == "//" ):
        print locus+"\t"+organism
        locus = ""
        organism = ""
        flag = 0
