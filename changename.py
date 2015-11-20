#!/usr/bin/python
# python changename.py input
import sys
fread = open(sys.argv[1],'r')

temp = []
for line in fread:
    temp.append(line.strip())

fread.close()
fwrite = open(sys.argv[1],'w')
for i in range(len(temp)):
    if(temp[i][:1]=='>'):
        filename = sys.argv[1].split('/')
        thisname = filename[len(filename)-1][:-2].split('.')
        fwrite.write('>'+thisname+' '+temp[i][1:]+' 16S rRNA gene'+'\n')
    else :
        fwrite.write(temp[i]+'\n')
