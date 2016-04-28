#!/usr/bin/python
# this script find abundance in EMP each phylum
# usage: python count_abun_emp.py summary taxonomy repset > abun_phylum

import sys
import read_rdp_taxonomy

sread = open(sys.argv[1],'r')
sum = {}
flag = 0
for line in sread:
    if flag == 0:
        if (line[:21] == "Counts/sample detail:"):
            flag = 1
        continue

    spl = line.strip().split(':')
    sum[spl[0].strip()]=spl[1].strip()
sread.close()

tread = open(sys.argv[2],'r')
tax = {}
for line in tread:
    temp = read_rdp_taxonomy.table(line)
    tax[temp[0]]=temp[2]
tread.close()

repread = open(sys.argv[3],'r')
final = {}
for line in repread:
    if not (line[:1]=='>'):
        continue
    spl = line.strip().split(' ')
    temp = [spl[0][1:],tax[spl[0][1:]],sum[spl[0][1:]]]
    if (final.has_key(temp[1])):
        to = final[temp[1]]
        final[temp[1]] = to + float(temp[2])
    else:
        final[temp[1]] = float(temp[2])

for item in final.items():
    print '\t'.join([item[0],str(item[1])])
        
