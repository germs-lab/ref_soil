#!/usr/bin/python
import sys
fread = open(sys.argv[1],'r')
fread.next()
fwritebac = open(sys.argv[1]+'.bacteria.txt','w')
fwritear = open(sys.argv[1]+'.archaea.txt','w')
fwritefun = open(sys.argv[1]+'.fungi.txt','w')
for line in fread:
    splt = line.strip().split('\t')
    ids = splt[2].split(',')
    if splt[6]=="Bacteria":
        for i in ids:
            fwritebac.write(i+'\n')
    elif splt[6]=="Archaea":
        for i in ids:
            fwritear.write(i+'\n')
    elif splt[6]=="Eukaryota":
        for i in ids:
            fwritefun.write(i+'\n')
    else:
        print "unkown domain"

