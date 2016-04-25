#!/usr/bin/python
#usage : python get_tax_most_abun.py 100_most_abun_id.txt taxonomyfile
import sys

dict = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split(':')
    dict[spl[0]]=spl[1].strip()

for line in open(sys.argv[2],'r'):
    spl = line.strip().split('\t')
    if (dict.has_key(spl[0])):
        out= [dict[spl[0]],line.strip()]
        print '\t'.join(out)
