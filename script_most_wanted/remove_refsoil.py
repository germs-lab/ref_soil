#!/usr/bin/python
#usage : python remove_refsoil.py refsoil_emp_id.txt 100most_abundant_final.txt

import sys
dict = {}
for line in open(sys.argv[1],'r'):
    dict[line.strip()]=line.strip()

for line in open(sys.argv[2],'r'):
    spl = line.strip().split('\t')
    if not dict.has_key(spl[1]):
        print line.strip()
