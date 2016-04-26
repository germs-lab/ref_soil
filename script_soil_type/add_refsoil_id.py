#!/usr/bin/python
# usage: python add_refsoil_id.py id_map.unix.txt blast.result taxonomy soil_type_count.txt > supplementary_table_soil_type.txt

import sys
import read_rdp_taxonomy
ids = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    ids[spl[0]] = spl[1]

dict = {}
for line in open(sys.argv[2],'r'):
    spl = line.strip().split('\t')
    if (dict.has_key(spl[1])):
        temp = dict[spl[1]]
        temp.append(ids[spl[0]])
        dict[spl[1]]=temp
    else:
        dict[spl[1]]=[ids[spl[0]]]

tax = read_rdp_taxonomy.get_tax_dict(sys.argv[3])

for line in open(sys.argv[4],'r'):
    spl = line.strip().split('\t')
    if not (dict.has_key(spl[0])):
        continue
    temp = [spl[0],','.join(dict[spl[0]])]
    temp.append(tax[spl[0]][1])
    for i in range(1,len(spl)):
        temp.append(spl[i])
    print '\t'.join(temp)
