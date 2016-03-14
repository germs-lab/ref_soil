#!/usr/bin/python

def organism(genbankfile):
    organism = ""
    for line in open(genbankfile,'r'):
        if("organism=" in line):
            splt = line.strip().split("=")
            organism = splt[1][1:-1]
            break
    return organism

def taxon(genbankfile):
    taxon = ""
    for line in open(genbankfile,'r'):
        if("taxon:" in line):
            splt = line.strip().split(':')
            taxon = splt[1][:-1]
            break
    return taxon

def has_chromosome(genbankfile):
    has = False
    for line in open(genbankfile,'r'):
        if("chromosome=" in line):
            has = True
            break
    return has

def version(genbankfile):
    version = ""
    for line in open(genbankfile,'r'):
        if("VERSION" in line):
            splt = line.strip().split(' ')
            version = splt[5]
            break
    return version

def definition(genbankfile):
    definition = ""
    for line in open(genbankfile,'r'):
        if("DEFINITION" in line):
            splt = line.strip().split(' ')
            for i in range(1,len(splt)):
                if(definition == ""):
                    definition = splt[i]
                else:
                    definition = definition +' ' + splt[i]
            break
    return definition
