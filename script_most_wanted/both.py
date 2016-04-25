#!/usr/bin/python
#usage: python both.py file1 file2

import sys

dict = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    dict[spl[1]]=spl[0]

for line in open(sys.argv[2],'r'):
    spl = line.strip().split('\t')
    if (dict.has_key(spl[1])):
        print dict[spl[1]]+'\t'+line.strip()
