#!/usr/bin/python
#python get_emp_count.py count_map.txt RefSoil_guide_ar_bac.txt > refsoil_count.txt
import sys
dict = {}
for line in open(sys.argv[1]):
    splt = line.strip().split('\t')
    dict[splt[0]]=splt[1]

for line in open(sys.argv[2]):
    if(dict.has_key(line.strip())):
           print line.strip()+'\t'+dict[line.strip()]
