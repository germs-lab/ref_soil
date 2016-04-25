#!/usr/bin/python
#usage: python get_most_ubiq_v2.py 100most_ubiq_id.txt ../Soil_EMP_taxonomy/JavaNewSoilRepSet_tax_assignments.txt
import sys

tax_dict = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split(' ')
    tax_dict[spl[0]]=spl[1]

for line in open(sys.argv[2]):
    spl = line.strip().split('\t')
    if(tax_dict.has_key(spl[0])):
        out = [tax_dict[spl[0]],line.strip()]
        print '\t'.join(out)

