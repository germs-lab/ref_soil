#!/usr/bin/python
#usage: python Guide_Add_Ring_SingleCell.py taxonomyFile outputFile
#python Guide_Add_Ring_SingleCell.py singlecell.unix.txt anno.SingleCell.Ring.txt

import sys, os
import modules

filein = sys.argv[1]
fileout = sys.argv[2]



fread = open(filein,'r')
fwrite = open(fileout,'w')


#Make singlecell table
AbunTable = []
Sep = "\t"
AbunTable = modules.ReadTableSep(filein,Sep)

for i in range(len(AbunTable)):
    fwrite.write(AbunTable[i][12]+'\t'+"ring_width"+'\t'+"2"+'\t'+"1"+'\n')
    fwrite.write(AbunTable[i][12]+'\t'+"ring_height"+'\t'+"2"+'\t'+"0.35"+'\n')
    fwrite.write(AbunTable[i][12]+'\t'+"ring_color"+'\t'+"2"+'\t'+"b"+'\n')
