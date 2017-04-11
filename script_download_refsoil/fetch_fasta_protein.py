#!/usr/bin/python

import urllib2
import os
import sys
import time

if len(sys.argv) != 3:
    print "USAGE: fetch_fasta_part.py <genome_id_list> <out_dir>"
    sys.exit(1)

url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=%s&rettype=fasta_cds_aa&retmode=text"
#url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=fasta_cds_na&retmode=text"
#url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=%s&rettype=gbwithparts&retmode=text"

if os.path.exists(sys.argv[2]):
    print "path exists"
else :
    os.mkdir(sys.argv[2])

for id in open(sys.argv[1]):
    id = id.strip()
    if id == "":
        continue

    sys.stdout.write("Fetching %s..." % id)
    sys.stdout.flush()
    gbk_out_file = os.path.join(sys.argv[2], id + ".fa")

    if os.path.exists(gbk_out_file):
        print "already fetched"
    else :
        open(gbk_out_file, "w").write(urllib2.urlopen(url_template % id).read())
        
    print "Done"
    time.sleep(1.0/3)
