#!/usr/bin/python
#python count_map.py summaryfile mapfile > output
import sys

sumread = open(sys.argv[1],'r')
mapread = open(sys.argv[2],'r')

#read summaryfile
dict = {}
line = sumread.next()
while (line.strip() != 'Counts/sample detail:'):
    line = sumread.next()
line = sumread.next()
for line in sumread:
    splt = line.strip().split(': ')
    dict[splt[0]]=splt[1]
sumread.close()
#read map
#ndict = {}
for line in mapread:
    splt = line.strip().split('\t')
    ids = splt[1].split(',')
    tsum = 0.0
    for x in ids:
        if(dict.has_key(x)):
            tnum = float(dict[x])
            tsum = tsum + tnum
    #ndict[splt[0]]=str(tsum)
    print splt[0]+'\t'+str(tsum)

