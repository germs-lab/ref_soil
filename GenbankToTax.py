#!/usr/bin/python
# python GenbankToTax.py input.gbk

import sys

fread = open(sys.argv[1])

line = fread.readline()
line = fread.readline()
line = fread.readline()
line = fread.readline()
tempcol = line.strip().split('     ')
print tempcol

for line in fread:
    if ("taxon:" in line):
        tempcol = line.strip().split(":")
        print tempcol[1][:-1]
        break
