#!/usr/bin/python

import sys

li = open(sys.argv[2],'r')
dictionary = {}
for line in li:
    splt = line.strip().split('.')
    dictionary[splt[0]]= splt[0]

li.close()

com = open(sys.argv[1],'r')
for line in com:
    if (dictionary.has_key(line.strip())):
        print line.strip() +" yes"
    else :
        print line.strip()
