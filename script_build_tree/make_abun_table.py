#!/usr/bin/python
# python make_abun_table.py soil_type_count.txt refsoil_emp_blast.out.txt > soil_type_abun.txt

import sys

dict = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    dict[spl[0]]=line.strip()
temp = ["otu","taxID","Andisols","Gelisols","Vertisols","Mollisols","Inceptisols","Alfisols","Ultisols","Sand,Rock,Ice","Entisols"]
print '\t'.join(temp)
for line in open(sys.argv[2],'r'):
    spl = line.strip().split('\t')
    if (dict.has_key(spl[1])):
        temp = [spl[0],dict[spl[1]]]
        print '\t'.join(temp)
