#!/usr/bin/python
#usage: python nonzero.py biom > nonzero.out
from biom import load_table
from biom.table import Table
import numpy as np
import sys

table = load_table(sys.argv[1])
count = table.nonzero_counts('observation',True)
otuid = table.ids(axis='observation')
#print len(a)
#print len(b)
for i in range(0,len(count)):
    print otuid[i],count[i]
