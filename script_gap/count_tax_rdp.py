#!/usr/bin/python
# this script count otus by phylum from rdp taxonomy assignment
# usage: python count_tax_rdp.py rdp_taxonomy.txt

import sys
import read_rdp_taxonomy
dict = read_rdp_taxonomy.get_tax_dict(sys.argv[1])
print len(dict)
