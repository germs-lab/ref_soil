#!/usr/bin/python
# python GenbankToTax.py input.gbk

import sys

fread = open(sys.argv[1],'r')

filename = sys.argv[1].split('/')
ID = filename[len(filename)-1][:-4]

for line in fread:
    if ("taxon:" in line):
        tempcol = line.strip().split(":")
        print ID+'\t'+tempcol[1][:-1]
        break
