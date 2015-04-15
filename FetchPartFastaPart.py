#!/usr/bin/python

import urllib2
import os
import sys
import time

if len(sys.argv) != 3:
    print "USAGE: fetch_genome.py <genome_id_list> <out_dir>"
    sys.exit(1)

url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={0}&seq_start={1}&seq_stop={2}&rettype=fasta&retmode=text"

if os.path.exists(sys.argv[2]):
	print "path exists"
else :	
	os.mkdir(sys.argv[2])

for id in open(sys.argv[1]):
    id = id.strip()
    line = id
    if id == "":
        continue

    words = line.split(',')
    id = words[0]
    s1 = url_template.format(words[0],words[1],words[2])

    sys.stdout.write("Fetching %s..." % id)
    sys.stdout.flush()
    gbk_out_file = os.path.join(sys.argv[2], id + ".fa")
    if os.path.exists(gbk_out_file):
        print "already fetched"

    open(gbk_out_file, "w").write(urllib2.urlopen(s1).read())
    print "Done"
    time.sleep(1.0/3)

