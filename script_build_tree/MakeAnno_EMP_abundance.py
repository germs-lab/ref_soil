#!/usr/bin/python
# python MakeAnno_EMP_abundance.py EMP_count.txt anno.emp.count.txt

import sys,os
import modules
import math
Abunin = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')
log = 0
height = 1
dict = {}
for line in Abunin:
    tempCol = line.strip().split('\t')
    dict[tempCol[0]]=tempCol[1]

biggest = 0.0
for item in dict.items():
    if (log == 1):
        x = math.log(float(item[1]),10)
        dict[item[0]]=str(x)
    else:
        x = float(item[1])
    if (x > biggest):
        biggest = x

for item in dict.items():
    alpha = float(item[1])/biggest
    
    fwrite.write(item[0]+'\t'+"ring_width"+'\t'+"9"+'\t'+"1"+'\n')
    fwrite.write(item[0]+'\t'+"ring_height"+'\t'+"9"+'\t'+str(height)+'\n')
    fwrite.write(item[0]+'\t'+"ring_color"+'\t'+"9"+'\t'+"g"+'\n')
    fwrite.write(item[0]+'\t'+"ring_alpha"+'\t'+"9"+'\t'+str(alpha)+'\n')
