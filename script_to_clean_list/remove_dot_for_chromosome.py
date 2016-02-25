#!/usr/bin/python
import sys

fread = open(sys.argv[1],'r')
for line in fread:
    lists = ""
    splt = line.strip().split(',')
    for ids in splt:
        id = ids.split('.')
        templist = id[0]
        if(lists == ""):
            lists = templist
        else:
            lists = lists+','+templist
    print lists
