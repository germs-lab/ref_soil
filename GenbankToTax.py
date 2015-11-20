#!/usr/bin/python
# python GenbankToTax.py input.gbk

import sys

fread = open(sys.argv[1])

filename = sys.argv[1].split('/')
print filename

for line in fread:
    if ("taxon:" in line):
        tempcol = line.strip().split(":")
        print tempcol[1][:-1]
        break
