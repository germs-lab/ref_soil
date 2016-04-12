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
    fwrite.write(line.strip()+'\t'+"ring_width"+'\t'+"1"+'\t'+"1"+'\n')
    fwrite.write(line.strip()+'\t'+"ring_height"+'\t'+"1"+'\t'+"0.35"+'\n')
    fwrite.write(line.strip()+'\t'+"ring_color"+'\t'+"1"+'\t'+'#EE6A50'+'\n')
