#!/usr/bin/python
# This script make annotation file
#python MakeAnno_RefSoil_legend.py RefSoil_v1.txt.split.bacteria.txt legend.txt
# print Legends part may not useful
import sys, os
import modules
filein = sys.argv[1]
fileout = sys.argv[2]
full_path = os.path.realpath(__file__)

fwrite = open(fileout,'w')

#Make Tax table using RefSoil_v1
Tax = modules.TaxTable_from_RefSoil(filein)

# class color assignment
#classColor = modules.AssignColor(Tax)
classColor = modules.assigned_phylum_color(Tax)
KingdomColor = [["Bacteria",'#EE6A50'],["Archaea",'#9ACD32']]

#print legend
for i in classColor:
    fwrite.write(i[0]+'\t'+"annotation"+'\t'+"*:"+i[0]+'\n')
    fwrite.write(i[0]+'\t'+"annotation_background_color"+'\t'+i[1]+'\n')
    fwrite.write(i[0]+'\t'+"clade_marker_color"+'\t'+i[1]+'\n')
    fwrite.write(i[0]+'\t'+"annotation_legend_font_size"+'\t'+"2"+'\n')
