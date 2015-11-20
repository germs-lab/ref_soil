#!/usr/bin/python
# This script make annotation file
#python TreeAddTax.py RefSoilFullTax_w_id.txt Annot.step2.txt
import sys, os
import modules

full_path = os.path.realpath(__file__)
filedefault = os.path.dirname(full_path)+"/DefaultAnnoNoRing.txt"
deread = open(filedefault,'r')
fwrite = open(sys.argv[2],'w')

#write default
for line in deread:
    fwrite.write(line)
fwrite.write('\n')

#Make Tax table
Tax = modules.ReadRefSoilTax(sys.argv[1])

# class color assignment                                                              
classColor = modules.AssignColor2(Tax)
for i in range(len(Tax)):
    tempColor = "k"
    for j in range(len(classColor)):
        if (classColor[j][0]==Tax[i][2]):
            tempColor = classColor[j][1]
    NoDocTax = Tax[i][0].split('.')
    fwrite.write(NoDocTax[0]+'\t'+"annotation"+'\t'+Tax[i][2]+'\n')
    fwrite.write(NoDocTax[0]+'\t'+"annotation_background_color"+'\t'+tempColor+'\n')
    fwrite.write(NoDocTax[0]+'\t'+"clade_marker_color"+'\t'+tempColor+'\n')
    fwrite.write(NoDocTax[0]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
    fwrite.write(NoDocTax[0]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
