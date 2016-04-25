#!/usr/bin/python
# This script make annotation file
#python MakeAnno_RefSoil_no_ring.py RefSoil_v1.txt Annotation.txt
# print Legends part may not useful
import sys, os
import modules
filein = sys.argv[1]
fileout = sys.argv[2]
full_path = os.path.realpath(__file__)
filedefault = os.path.dirname(full_path)+"/default_refsoil.txt"

deread = open(filedefault,'r')
fwrite = open(fileout,'w')

#write default
for line in deread:
    fwrite.write(line)
fwrite.write('\n')

#Make Tax table using RefSoil_v1
Tax = modules.TaxTable_from_RefSoil(filein)

# class color assignment
#classColor = modules.AssignColor(Tax)
classColor = modules.assigned_phylum_color_le(Tax)
KingdomColor = [["Bacteria",'#EE6A50'],["Archaea",'#9ACD32']]
dict = {}
# Write annotation
for i in range(len(Tax)):
    tempColor = "k"
    kingColor = "k"
    temple = "A"
    for j in range(len(classColor)):
        if (classColor[j][0]==Tax[i][1]):
            tempColor = classColor[j][1]
            temple = classColor[j][2]
    if (Tax[i][0] == KingdomColor[0][0]):
        kingColor = KingdomColor[0][1]
    elif(Tax[i][0] == KingdomColor[1][0]):
        kingColor = KingdomColor[1][1]
    if (Tax[i][5] != ""):
        #fwrite.write(Tax[i][7]+'\t'+"annotation_background_color"+'\t'+tempColor+'\n')
        #fwrite.write(Tax[i][7]+'\t'+"annotation"+'\t'+tempColor+'\n')
        #fwrite.write(Tax[i][7]+'\t'+"annotation"+'\t'+temple+":"+Tax[i][1]+'\n')
        fwrite.write(Tax[i][7]+'\t'+"clade_marker_color"+'\t'+tempColor+'\n')
        fwrite.write(Tax[i][7]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
        #fwrite.write(Tax[i][7]+'\t'+"ring_width"+'\t'+"1"+'\t'+"4"+'\n')
        #fwrite.write(Tax[i][7]+'\t'+"ring_height"+'\t'+"1"+'\t'+"0.35"+'\n')
        #fwrite.write(Tax[i][7]+'\t'+"ring_color"+'\t'+"1"+'\t'+kingColor+'\n')
        if not (dict.has_key(Tax[i][1])):
            dict[Tax[i][1]]=[temple,Tax[i][7]]
for item in dict.items():
    fwrite.write(item[1][1]+'\t'+"annotation"+'\t'+item[1][0]+":"+item[0]+'\n')
    fwrite.write(item[1][1]+'\t'+"annotation_font_size"+'\t'+"20"+'\n')
