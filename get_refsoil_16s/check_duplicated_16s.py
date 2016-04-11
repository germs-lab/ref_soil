#!/usr/bin/python
#usage: python check_duplicated_16s.py RefSoil_v1_chromosome.txt merged16s.fa 
import sys

# read chromosome list
chdic = {}
rlist = open(sys.argv[1])
for line in rlist:
    splt = line.strip().split(',')
    if (len(splt)==1):
        chdic[splt[0]]="null"
    else:
        temp = ""
        for i in range(1,len(splt)):
            if temp == "":
                temp = splt[i]
            else:
                temp = temp + ',' +splt[i]
        chdic[splt[0]] = temp
#print chdic
rlist.close()
# make a set
listdic = {}
list = open(sys.argv[2])
for line in list:
    if(line[:1]==">"):
        ids = line.strip().split(" ")[0][1:]
        if (chdic.has_key(ids)):
            listdic[ids] = ids
        else:
            for x in chdic.items():
                if(ids in x):
                    listdic[ids]=x[0]
list.close()
#print listdic
#exit(0)
# read merged file
fread = open(sys.argv[2])
flag = 0
for line in fread:
    if(line[:1]==">"):
        flag = 0
        ids = line.strip().split(" ")[0][1:]
        if (chdic.has_key(ids)):
            # if only one chromosome, write 
            if(chdic[ids]=="null"):
                print line.strip()
                flag = 1
                del chdic[ids]
            else:
                print line.strip()
                flag = 1
                del chdic[ids]

    else:
        if(flag == 1):
            print line.strip()
#print chdic

"""
        else:
            # if multiple chromosome, check if the first one has 16s 
            #print "non leading chromosome"
            if(listdic.has_key(ids)):
                print "has key"
                if not (chdic.has_key(listdic[ids])):
                    print line.strip()
                    flag = 1
                       
            else:
                print "no key"
"""

                
