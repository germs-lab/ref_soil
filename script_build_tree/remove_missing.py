#!/usr/bin/python
#this code remove missing genome from splited file
#usage: python remove_missing.py missing.txt ../RefSoil_v1.txt.split.bacteria.txt > bacteria.txt

import sys
dict = {}
for line in open(sys.argv[1],'r'):
    dict[line.strip()]=line.strip()

for line in open(sys.argv[2],'r'):
    spl = line.strip().split('\t')
    if (dict.has_key(spl[0])):
        continue
    print line.strip()
