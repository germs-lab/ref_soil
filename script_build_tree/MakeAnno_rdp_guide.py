#!/usr/bin/python
#usage: python MakeAnno_rdp_guide.py guidefile outputfile
#example: python MakeAnno_rdp_guide.py RefSoil_Guide_uniq.txt RefSoil_anno.txt

import sys,os
import modules
filein = sys.argv[1]
fileout = sys.argv[2]

full_path = os.path.realpath(__file__)
filedefault = os.path.dirname(full_path)+"/DefaultAnnoNoRing.txt"

deread = open(filedefault,'r')
fwrite = open(fileout,'w')

#write default
for line in deread:
    fwrite.write(line)
fwrite.write('\n')

# Make tax table from guide file
Tax = modules.TaxTable_from_guide(filein)

# class color assignment
classColor = modules.AssignColor(Tax)
KingdomColor = [["Bacteria",'#EE6A50'],["Archaea",'#9ACD32']]

# Write annotation
for item in classColor:
    fwrite.write(item[0]+'\t'+"annotation"+'\t'+"*:"+item[0]+'\n')
    fwrite.write(item[0]+'\t'+"annotation"+'\t'+item[0]+'\n')
    fwrite.write(item[0]+'\t'+"annotation_background_color"+'\t'+item[1]+'\n')
    fwrite.write(item[0]+'\t'+"clade_marker_color"+'\t'+item[1]+'\n')
    fwrite.write(item[0]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
    fwrite.write(item[0]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
