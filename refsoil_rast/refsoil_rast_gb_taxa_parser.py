#!/usr/bin/env python
## author: Adina Howe, Fan Yang

import sys 
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

#This uses Biopython to parse the genbank file, and link the results to rast ID for RefSoil
'''
record.annotations         record.letter_annotations
record.dbxrefs             record.lower
record.description         record.name
record.features            record.reverse_complement
record.format              record.seq
record.id                  record.upper
'''
'''
annoations:
{'comment': 'Upstream region of a putative chromosomal mobile element flanking T\nn1546::IS1251 in Enterococcus faecium, containing IS1216V and a\ntruncated IS3-like element.\nMethod: conceptual translation.', 'sequence_version': 1, 'source': 'Enterococcus faecium', 'taxonomy': ['Bacteria', 'Firmicutes', 'Bacilli', 'Lactobacillales', 'Enterococcaceae', 'Enterococcus'], 'data_file_division': 'BCT', 'keywords': [''], 'references': [Reference(title='Identification of chromosomal mobile element conferring high-level vancomycin resistance in Enterococcus faecium', ...)], 'accessions': ['AAB00676'], 'db_source': 'locus ENETRANSPO accession L40841.1', 'date': '23-MAY-1996', 'organism': 'Enterococcus faecium', 'gi': '807609'}
'''

if len(sys.argv) == 1:
	sys.exit("USAGE: %s <path/to/genbank_file1> <path/to/genbank_file2> <...>" % sys.argv[0])
 
def get_info(genbank_file):
    l_to_print = []
    ## obtain rast id from the full input file path: eg. /mnt/data3/jin_rast/RAST_RefSoilv1/999891.7/genbank_file
    rast_id = genbank_file.strip().split("/")[5]
    l_to_print.append(rast_id)
    ## get genbank record
    for record in list(SeqIO.parse(genbank_file, 'genbank')):
        l_to_print.append(record.id)
        l_to_print.append(record.description)
        l_to_print.append(record.annotations['organism'])
        for taxa in record.annotations['taxonomy']:
            l_to_print.append(taxa)
    return '\t'.join(l_to_print)

genbank_files = sys.argv[1:]

for f in genbank_files:
    info = get_info(f)
    print info
