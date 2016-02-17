#!/usr/bin/python
#this script sperate RefSoil list into different domain
#usage: python split_domain.py RefSoil_v1.txt
import sys
fread = sys.argv[1]
bwrite = sys.argv[1]+".split.bacteria.txt"
awrite = sys.argv[1]+".split.archaea.txt"
fwrite = sys.argv[1]+".split.fungi.txt"

for line in fread:
    splt = line.strip().split("\t")
    if splt[6]=="Bacteria":
        bwrite.write(line.strip()+'\n')
    elif splt[6]=="Archaea":
        awrite.write(line.strip()+'\n')
    elif splt[6]=="Eukaryota":
        fwrite.write(line.strip()+'\n')
    else:
        print "unkown domain"
