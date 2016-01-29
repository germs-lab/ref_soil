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
