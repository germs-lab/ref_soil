#!/usr/bin/python
#usage: python soil_type_anova_input.py SampleSoilOrders.unix.fix.txt subset_table.txt > anova_input.txt

import sys

typeread = open(sys.argv[1],'r')
samread = open(sys.argv[2],'r')
type = {}
for line in typeread:
    spl = line.strip().split('\t')
    type[spl[0]]=spl[5]
typeread.close()

line = samread.next()
line = samread.next().strip().split('\t')
sample = []
for x in line:
    sample.append(x)

for line in samread:
    spl = line.strip().split('\t')
    for i in range(1,len(spl)):
        key = sample[i]
        if (type.has_key(key)):
            if not spl[i]=="0.0":
                print spl[0],type[key],spl[i]
