#!/usr/bin/env python

import sys
import re
import os
import ijson

if len(sys.argv) < 2:
	print "USAGE:  refsoil_annotation_parser.py <subsystem_ontology.json> <subsystem_annotation_binding_file1> <subsystem_annotation_binding_file2> <...>"
	sys.exit(1)

 
## read in subsystem ontology json file and find all level1 and level2. put them into seperate lists
def get_l1(ss_ontology):
	for item in ijson.items(open(ss_ontology), ''):
		l1 = []
		for x in item["data"]:
			if "level1" in x and x["level1"] not in l1:
				l1.append(x["level1"])
		return l1			

def get_l2(ss_ontology):
	for item in ijson.items(open(ss_ontology), ''):
		l2 = []
		for x in item["data"]:
			if "level2" in x and x["level2"] not in l2:
				l2.append(x["level2"])
		return l2	

## parse EC from rast annotation file, fill in NA if non-exist
def get_ec(description):
	l_ec = []
	n = description.count('(EC')	
	if n == 0:
		l_ec = ["NA"]
	elif n >= 1:
		for i in range(1, n+1):
			ec = desc.split('(EC')[-i].replace(')', '')
			ec = re.split(" |,|_", ec)[-1].replace('-', '0')
			l_ec.append(ec)
	return l_ec

## parse TC from rast annotation file, fill in NA if non-exist
def get_tc(description):
	l_tc = []
	n = description.count('(TC')	
	if n == 0:
		l_tc = ["NA"]
	elif n >= 1:
		for i in range(1, n+1):
			tc = desc.split('(TC')[-i].replace(')', '')
			tc = re.split(" |,|_", tc)[-1].replace('-', '0')
			l_tc.append(tc)
	return l_tc

def search(dataToSearch, searchFor):
	for i in dataToSearch:
		if searchFor in i:
			return searchFor
	else:
		return "NA"

## subsystem ontology file
ontology = sys.argv[1]
## all rast annoation files
files = sys.argv[2:]

## read in and create a dictionary for the subsystem onotology file. Create level1 and level2 lists to search in.
L1 = get_l1(ontology)
L2 = get_l2(ontology)

for f in files:
	for lines in open(f, 'rU'):
		line = lines.strip().split('\t')
		fig_id = line[2].split("|")[1]
		TaxID = fig_id.split(".")[0]
		gene = line[0]
		desc = line[1]
		EC = get_ec(desc)
		TC = get_tc(desc)
		if len(line) == 5:
			col4 = line[3]
			T1 = search(L1, col4)
			col5 = line[4]
			T2 = search(L2, col5)
			print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (fig_id, TaxID, gene, desc, EC, TC, T1, T2)	
		elif len(line) == 4:
			col4 = line[3]
			T1 = search(L1, col4)
			T2 = search(L2, col4)
			print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (fig_id, TaxID, gene, desc, EC, TC, T1, T2)	
		elif len(line) == 3:
			T1 = "NA"
			T2 = "NA"
			print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (fig_id, TaxID, gene, desc, EC, TC, T1, T2)	

