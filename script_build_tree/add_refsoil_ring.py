#!/usr/bin/python
#usage: python add_refsoil_ring.py refsoilguide output
#example: python add_refsoil_ring.py RefSoil_Guide_uniq.txt add_ring_step3.txt
import sys,os
import modules

filein = sys.argv[1]
fileout = sys.argv[2]

fread = open(filein,'r')
fwrite = open(fileout,'w')

for line in fread:
    fwrite.write(line.strip()+'\t'+"ring_width"+'\t'+"2"+'\t'+"1"+'\n')
    fwrite.write(line.strip()+'\t'+"ring_height"+'\t'+"2"+'\t'+"1"+'\n')
    fwrite.write(line.strip()+'\t'+"ring_color"+'\t'+"2"+'\t'+'#EE6A50'+'\n')
