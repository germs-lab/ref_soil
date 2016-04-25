#!/usr/bin/python
# python MakeAnno_EMP_abundance.py EMP_count.txt anno.emp.count.txt

import sys,os
import modules
import math
Abunin = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')
log = 1
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
    
    fwrite.write(item[0]+'\t'+"ring_width"+'\t'+"1"+'\t'+"1"+'\n')
    fwrite.write(item[0]+'\t'+"ring_height"+'\t'+"1"+'\t'+str(height)+'\n')
    fwrite.write(item[0]+'\t'+"ring_color"+'\t'+"1"+'\t'+"g"+'\n')
    fwrite.write(item[0]+'\t'+"ring_alpha"+'\t'+"1"+'\t'+str(alpha)+'\n')

    fwrite.write(item[0]+'\t'+"ring_color"+'\t'+"4"+'\t'+"#FFFFFF"+'\n')

fwrite.write("ring_internal_separator_thickness"+'\t'+"1"+'\t'+"0.5"+'\n')
fwrite.write("ring_separator_color"+'\t'+"2"+'\t'+"#888888"+'\n')
fwrite.write("ring_internal_separator_thickness"+'\t'+"2"+'\t'+"0.5"+'\n')
fwrite.write("ring_separator_color"+'\t'+"2"+'\t'+"#888888"+'\n')
fwrite.write("ring_internal_separator_thickness"+'\t'+"3"+'\t'+"0.5"+'\n')
fwrite.write("ring_separator_color"+'\t'+"2"+'\t'+"#888888"+'\n')
fwrite.write("ring_internal_separator_thickness"+'\t'+"4"+'\t'+"0.5"+'\n')
fwrite.write("ring_separator_color"+'\t'+"2"+'\t'+"#888888"+'\n')

fwrite.write("ring_label"+'\t'+"1"+'\t'+"Abundance"+'\n')
fwrite.write("ring_label_color"+'\t'+"1"+'\t'+"#000000"+'\n')
fwrite.write("ring_label_font_size"+'\t'+"1"+'\t'+"20"+'\n')
fwrite.write("ring_label"+'\t'+"2"+'\t'+"RefSoil"+'\n')
fwrite.write("ring_label_color"+'\t'+"2"+'\t'+"#000000"+'\n')
fwrite.write("ring_label_font_size"+'\t'+"2"+'\t'+"20"+'\n')
fwrite.write("ring_label"+'\t'+"3"+'\t'+"Single Cell"+'\n')
fwrite.write("ring_label_color"+'\t'+"3"+'\t'+"#000000"+'\n')
fwrite.write("ring_label_font_size"+'\t'+"3"+'\t'+"20"+'\n')
