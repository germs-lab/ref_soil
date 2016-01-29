#!/usr/bin/python
import sys
import genbank_get

filename = sys.argv[1]
tax = genbank_get.taxon(filename)

print filename + '\t' + tax
