#!/usr/bin/python
#this script find full taxonomy from file of tax ID
#usage: python id_to_tax.py id_file.txt > full_tax.txt
import sys
import taxonomy_finder

for line in open(sys.argv[1],'r'):
    print line.strip() + "\t" + taxonomy_finder.from_id(line.strip())
    
