#!/usr/bin/python
# This script make annotation file
#python add_kingdom.py RefSoil_v1.txt Annotation.txt
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

# Write annotation
for i in range(len(Tax)):
    tempColor = "k"
    kingColor = "k"
    for j in range(len(classColor)):
        if (classColor[j][0]==Tax[i][1]):
            tempColor = classColor[j][1]
    if (Tax[i][0] == KingdomColor[0][0]):
        kingColor = KingdomColor[0][1]
    elif(Tax[i][0] == KingdomColor[1][0]):
        kingColor = KingdomColor[1][1]
    if (Tax[i][5] != ""):
        fwrite.write(Tax[i][7]+'\t'+"annotation_background_color"+'\t'+tempColor+'\n')
        #fwrite.write(Tax[i][7]+'\t'+"annotation"+'\t'+tempColor+'\n')
        fwrite.write(Tax[i][7]+'\t'+"ring_width"+'\t'+"1"+'\t'+"4"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"ring_height"+'\t'+"1"+'\t'+"0.35"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"ring_color"+'\t'+"1"+'\t'+kingColor+'\n')
 
