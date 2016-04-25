#!/usr/bin/python
#usage: python add_refsoil_ring.py refsoilguide output
#example: python add_refsoil_ring.py RefSoil_Guide_uniq.txt add_ring_step3.txt
import sys,os
import modules

filein = sys.argv[1]
fileout = sys.argv[2]

fread = open(filein,'r')
fwrite = open(fileout,'w')
Tax = modules.TaxTable_from_guide(filein)
col = modules.assigned_phylum_color_le(Tax)
dict = {}
#print col
for i in range(len(col)):
    if not (dict.has_key(col[i][0])):
        dict[col[i][0]] = [col[i][1],col[i][2]]

for item in dict.items():
    fwrite.write(item[0]+'\t'+"annotation"+'\t'+item[1][1]+":"+item[0]+'\n')
    fwrite.write(item[0]+'\t'+"annotation_background_color"+'\t'+item[1][0]+'\n')
    fwrite.write(item[0]+'\t'+"annotation_font_size"+'\t'+"25"+'\n')
        
for line in fread:
    fwrite.write(line.strip()+'\t'+"ring_width"+'\t'+"2"+'\t'+"1"+'\n')
    fwrite.write(line.strip()+'\t'+"ring_height"+'\t'+"2"+'\t'+"1"+'\n')
    fwrite.write(line.strip()+'\t'+"ring_color"+'\t'+"2"+'\t'+'#EE6A50'+'\n')
