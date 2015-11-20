#!/usr/bin/python
# python GenbankToTax.py input.gbk output.txt

import sys

fread = open(sys.argv[1])
fwrite = open(sys.argv[2])
filename = sys.argv[1].split('/')
fwrite.write(filename[len(filename)-1][:-4]+'\t')

for line in fread:
    if ("taxon:" in line):
        tempcol = line.strip().split(":")
        fwrite.write(tempcol[1][:-1]+'\n')
        break
