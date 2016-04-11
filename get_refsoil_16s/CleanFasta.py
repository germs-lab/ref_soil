#!/usr/bin/python
# python CleanFasta.py input output
import sys

fread = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')
flag = 0
seq = ""
for line in fread:
    TempLine = line.strip()
    if(TempLine == ""):
        continue
    if(TempLine[:1]== '>'):
        if(flag == 0):
            fwrite.write(TempLine+'\n')
            flag = 1
        else:
            fwrite.write(seq+'\n')
            seq =""
            fwrite.write(TempLine+'\n')
    else:
        seq = seq + TempLine
fwrite.write(seq+'\n')
