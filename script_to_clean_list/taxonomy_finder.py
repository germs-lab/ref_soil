#!/usr/bin/python
import urllib
import cStringIO
import pycurl

def get_taxonomy(locus,taxon):
    flist = [locus,taxon]
    buf = cStringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=' + taxon)
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()

    x= buf.getvalue()
    dat = x.split('\n')

    for line in dat:
        if('<dd><a ALT' in line):
            taxID=""
            lenID = len(taxID)
            lenCut = 163+lenID
    
            startK = line.find("TITLE=\"superkingdom\">")
            startK = startK + 21
            endK = line.find("</a", startK)
            if (endK == lenCut):
                flist.append("null")
            else:
                flist.append(line[startK:endK])

            startP = line.find("TITLE=\"phylum\">")
            startP = startP + 15
            endP = line.find("</a", startP)
            if (endP == lenCut):
                flist.append("null")
            else:
                flist.append(line[startP:endP])

            startC = line.find("TITLE=\"class\">")
            startC = startC + 14
            endC = line.find("</a", startC)
            if (endC == lenCut):
                flist.append("null")
            else:
                flist.append(line[startC:endC])
    
            startO = line.find("TITLE=\"order\">")
            startO = startO + 14
            endO = line.find("</a", startO)
            if (endO == lenCut):
                flist.append("null")
            else:
                flist.append(line[startO:endO])

            startF = line.find("TITLE=\"family\">")
            startF = startF + 15
            endF = line.find("</a", startF)
            if (endF == lenCut):
                flist.append("null")
            else:
                flist.append(line[startF:endF])

            startG = line.find("TITLE=\"genus\">")
            startG = startG + 14
            endG = line.find("</a", startG)
            if (endG == lenCut):
                flist.append("null")
            else:
                flist.append(line[startG:endG])

            startS = line.find("TITLE=\"species\">")
            startS = startS + 16
            endS = line.find("</a", startS)
            if (endS == lenCut):
                flist.append("null")
            else:
                flist.append(line[startS:endS])
    return flist

def full(filename):
    fread = open(filename,'r')
    locus = ""
    taxon = ""
    flag = 0
    plasmid = 0
    full_tax = ""
    for gbline in fread:
        if ("LOCUS" in gbline):
            locus = gbline.strip().split(" ")[7]
        if ("DEFINITION" in gbline):
            if("plasmid" in gbline):
                   plasmid = 1
        if ("taxon:" in gbline) and flag == 0:
            taxon = gbline.strip().split(":")[1][:-1]
            flag = 1
        if (gbline.strip()[:2] == "//" and plasmid == 0):
            flist = get_taxonomy(locus,taxon)
            #full_tax = ""
            for item in flist:
                full_tax = full_tax + item+'\t'
            #print full_tax
            flag = 0
        elif (gbline.strip()[:2] == "//" and plasmid == 1):
            plasmid = 0

    return full_tax
