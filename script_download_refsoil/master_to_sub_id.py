#!/usr/bin/python
#usage: python master_to_sub_id.py master_id_list.txt > genome_id_list.txt
import urllib2
import os
import sys
import time

if len(sys.argv) != 2:
    print "USAGE: fetch_genome.py <genome_id_list>"
    sys.exit(1)

#url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=gb&retmode=text"
url_template = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=%s&rettype=gbwithparts&retmode=text"

for id in open(sys.argv[1]):
    id = id.strip()
    if id == "":
        continue

    gb = urllib2.urlopen(url_template % id).read()
    spl = gb.split('\n')
    for line in spl:
        if line[:3] == "WGS" and line[:4] != "WGS_":
            sp = line.split("         ")[1].split('-')
            if len(sp)>1 and sp[0][:2] != "NZ":
                id1 = sp[0]
                header = id1[:len(id1)-7]
                id1_num = int(id1[len(id1)-7:])
            
                id2 = sp[1]
                id2_num = int(id2[len(id2)-7:])
            
                for i in range(id1_num,id2_num+1):
                    print header + str(i)
    time.sleep(1.0/3)
