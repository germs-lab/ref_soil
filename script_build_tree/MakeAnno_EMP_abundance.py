#!/usr/bin/python
# python MakeAnno_EMP_abundance.py EMP_count.txt anno.emp.count.txt

import sys,os
import modules
import math
Abunin = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')
log = 1
for line in Abunin:
    tempCol = line.strip().split('\t')
    fwrite.write(tempCol[0]+'\t'+"ring_width"+'\t'+"9"+'\t'+"1"+'\n')
    height = tempCol[1]
    if(log == 1):
        x = math.log(float(height),10)
        height = str(x)
    fwrite.write(tempCol[0]+'\t'+"ring_height"+'\t'+"9"+'\t'+height+'\n')
    fwrite.write(tempCol[0]+'\t'+"ring_color"+'\t'+"9"+'\t'+"g"+'\n')
