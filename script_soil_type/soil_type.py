#!/usr/bin/python
# usage: python soil_type.py SampleSoilOrders.unix.fix.txt subset_table.txt > soil_type_count.txt
import sys

typeread = open(sys.argv[1],'r')
samread = open(sys.argv[2],'r')
type = {}
for line in typeread:
    spl = line.strip().split('\t')
    type[spl[0]]=spl[5]
typeread.close()
#print len(type)
line = samread.next()
line = samread.next().strip().split('\t')
sample = []
for x in line:
    sample.append(x)
temp = {"Vertisols":0.0,"Alfisols":0.0,"Andisols":0.0,"Mollisols":0.0,"Gelisols"\
:0.0,"Sand,Rock,Ice":0.0,"Inceptisols":0.0,"Entisols":0.0,"Ultisols":0.0}
templist = []
templist.append("otu")
for x in temp.keys():
    templist.append(x)
print '\t'.join(templist)
for line in samread:
    spl = line.strip().split('\t')
    temp = {"Vertisols":0.0,"Alfisols":0.0,"Andisols":0.0,"Mollisols":0.0,"Gelisols":0.0,"Sand,Rock,Ice":0.0,"Inceptisols":0.0,"Entisols":0.0,"Ultisols":0.0}
    for i in range(1,len(spl)):
        key = sample[i]
        if (type.has_key(key)):
            num = temp[type[key]]
            temp[type[key]] = num + float(spl[i])
    templist=[]
    templist.append(spl[0])
    for x in temp.items():
        templist.append(str(x[1]))
    print '\t'.join(templist)

