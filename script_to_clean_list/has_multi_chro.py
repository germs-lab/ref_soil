#!/usr/bin/python
import sys
import genbank_get

fread = open(sys.argv[1],'r')
for line in fread:
    filename = "../../refsoilgenbank_v1_29_2016/"+line.strip()+".gbk"
    if(genbank_get.has_chromosome(filename)):
        print line.strip()#, genbank_get.has_chromosome(filename)
