#!/usr/bin/python

def table(line):
    noq = line.replace('"','').strip()
    spl = noq.split('\t')
    id = spl[0]
    domain = ""
    phylum = ""
    cla = ""
    order = ""
    family = ""
    genus = ""
    for i in range(1,len(spl)):
        if (spl[i] == "domain"):
            domain = spl[i-1]
        elif (spl[i] == "phylum"):
            phylum = spl[i-1]
        elif (spl[i] == "class"):
            cla = spl[i-1]
        elif (spl[i] == "order"):
            order = spl[i-1]
        elif (spl[i] == "family"):
            family = spl[i-1]
        elif (spl[i] == "genus"):
            genus = spl[i-1]
    temp = [id,domain,phylum,cla,order,family,genus]    
    return temp

def tax_table(filename):
    tax = []
    for line in open(filename,'r'):
        noq = line.replace('"','').strip()
        spl = noq.split('\t')
        id = spl[0]
        domain = ""
        phylum = ""
        cla = ""
        order = ""
        family = ""
        genus = ""
        for i in range(1,len(spl)):
            if (spl[i] == "domain"):
                domain = spl[i-1]
            elif (spl[i] == "phylum"):
                phylum = spl[i-1]
            elif (spl[i] == "class"):
                cla = spl[i-1]
            elif (spl[i] == "order"):
                order = spl[i-1]
            elif (spl[i] == "family"):
                family = spl[i-1]
            elif (spl[i] == "genus"):
                genus = spl[i-1]
        temp = [id,domain,phylum,cla,order,family,genus]
        tax.append(temp)
    return tax

def get_tax_dict(filename):
    tax = {}
    for line in open(filename,'r'):
        ta = table(line)
        temp = []
        for i in range(1,len(ta)):
            temp.append(ta[i])
        tax[ta[0]]=temp
    return tax
