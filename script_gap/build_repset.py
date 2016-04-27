#!/usr/bin/python
# usage: python build_repset.py in_to_remove.txt repset.fna > new_repset.fna

import sys

dict = {}
idread = open(sys.argv[1],'r')
for line in idread:
    dict[line.strip()]=line.strip()
idread.close()

fread = open(sys.argv[2],'r')
flag = 0
for line in fread:
    spl = line.strip().split(' ')
    if (line[:1] == ">"):
        if not (dict.has_key(spl[0][1:])):
            print line.strip()
            flag = 1
        else:
            flag = 0
    elif (line[:1] != ">" and flag == 1):
        print line.strip()
    elif (line[:1] != ">" and flag == 0):
        continue
