#!/usr/bin/python

import urllib2
import os
import sys
import time

if len(sys.argv) != 3:
    print "USAGE: fetch_genome.py <genome_id_list> <out_dir>"
    sys.exit(1)

url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=fasta&retmode=text"

os.mkdir(sys.argv[2])

l_failed = []

def get_fasta(id):
    data = urllib2.urlopen(url_template % id).read()
    return data




for id in open(sys.argv[1]):
    id = id.strip()
    if id == "":
        continue

    sys.stdout.write("Fetching %s..." % id)
    sys.stdout.flush()
    gbk_out_file = os.path.join(sys.argv[2], id + ".fa")
    if os.path.exists(gbk_out_file):
        print "already fetched"
    try:
        data = urllib2.urlopen(url_template % id).read()
        open(gbk_out_file, "w").write(get_fasta(id))
        print "Done"
    except:      
        l_failed.append(id)
        print "Failed"
    time.sleep(1.0/3)

l_failed_twice = []

for id in l_failed:
    id = id.strip()
    if id == "":
        continue
    sys.stdout.write("Retrying fetching %s..." % id)
    sys.stdout.flush()
    gbk_out_file = os.path.join(sys.argv[2], id + ".fa")
    try:
        data = urllib2.urlopen(url_template % id).read()
        open(gbk_out_file, "w").write(get_fasta(id))
        print "Done"
    except:
        l_failed_twice.append(id)
        print "Failed"
    print "Done"
    time.sleep(1.0/3)


fp_fail = open("genomes-download-failed.txt", "w")
for failed_id in l_failed_twice:
    fp_fail.write('%s\n' % failed_id)

