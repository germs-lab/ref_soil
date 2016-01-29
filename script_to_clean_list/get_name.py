#!/usr/bin/python

import sys
import genbank_get

filename = sys.argv[1]
name = genbank_get.organism(filename)
print filename + '\t' + name
