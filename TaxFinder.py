#!/usr/bin/python
# python TaxFinder.py test.txt result.txt
import sys
import re
fread = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')


for line in fread:
    taxID = line.split(".")[0]
    fwrite.write(taxID+";")
    lenID = len(taxID)
    lenCut = 169+lenID
    
    startK = line.find("TITLE=\"superkingdom\">")
    startK = startK + 21
    endK = line.find("</a", startK)
    if (endK == lenCut):
        fwrite.write("Null"+";")
    else:
        fwrite.write(line[startK:endK]+";")

    startP = line.find("TITLE=\"phylum\">")
    startP = startP + 15
    endP = line.find("</a", startP)
    if (endP == lenCut):
        fwrite.write("Null"+";")
    else:
        fwrite.write(line[startP:endP]+";")

    startC = line.find("TITLE=\"class\">")
    startC = startC + 14
    endC = line.find("</a", startC)
    if (endC == lenCut):
        fwrite.write("Null"+";")
    else:
        fwrite.write(line[startC:endC]+";")
    
    startO = line.find("TITLE=\"order\">")
    startO = startO + 14
    endO = line.find("</a", startO)
    if (endO == lenCut):
        fwrite.write("Null"+";")
    else:
        fwrite.write(line[startO:endO]+";")

    startF = line.find("TITLE=\"family\">")
    startF = startF + 15
    endF = line.find("</a", startF)
    if (endF == lenCut):
        fwrite.write("Null"+";")
    else:
        fwrite.write(line[startF:endF]+";")

    startG = line.find("TITLE=\"genus\">")
    startG = startG + 14
    endG = line.find("</a", startG)
    if (endG == lenCut):
        fwrite.write("Null"+";")
    else:
        fwrite.write(line[startG:endG]+";")

    startS = line.find("TITLE=\"species\">")
    startS = startS + 16
    endS = line.find("</a", startS)
    if (endS == lenCut):
        fwrite.write("Null"+'\n') 
    else:
        fwrite.write(line[startS:endS]+'\n')
