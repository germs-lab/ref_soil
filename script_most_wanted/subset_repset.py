#!/usr/bin/pyton
#usage: python subset_repset.py id_to_add rep_set.fa
import sys

dict = {}
for line in open(sys.argv[1],'r'):
    dict[line.strip()]= line.strip()

fread = open(sys.argv[2],'r')
flag = 0
seq = []
for line in fread:
    if line[:1]==">":
        flag = 0
        seq.append(line.strip())
        if dict.has_key(line.split(' ')[0][1:]):
            flag = 1
    if flag == 1:
        print line.strip()
