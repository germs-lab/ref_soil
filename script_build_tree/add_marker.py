#!/usr/bin/python
# python add_marker.py sc_guide.txt
import sys

fread = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')

for line in fread:
    fwrite.write(line.strip()+'\t'+"clade_marker_shape"+'\t'+"*"+'\n')
    fwrite.write(line.strip()+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
    fwrite.write(line.strip()+'\t'+"clade_marker_color"+'\t'+"r"+'\n')
