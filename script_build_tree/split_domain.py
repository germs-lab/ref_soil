#!/usr/bin/python
#this script sperate RefSoil list into different domain
#usage: python split_domain.py RefSoil_v1.txt
import sys
fread = open(sys.argv[1],'r')
fread.next()
bwrite = open(sys.argv[1]+".split.bacteria.txt",'w')
awrite = open(sys.argv[1]+".split.archaea.txt",'w')
fwrite = open(sys.argv[1]+".split.fungi.txt",'w')

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
