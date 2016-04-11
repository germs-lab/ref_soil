#!python
"""
parse_gold_html.py
Created by Erick Cardenas on 10.15.2014.
"""

# load some packages
try:
    import sys
    from bs4 import *
    import html5lib
    from optparse import OptionParser
    
except:
     import_exception = """ Could not load some modules """
     print import_exception 
     sys.exit(3)

usage= """
Need to run it like this:

python parse_gold_html.py
-i <input file in html format>
-o <output file>
"""

# add arguments to the parser
parser = OptionParser(usage)
parser.add_option('-i', dest='input_file', type=str, help='Input file (required)', default=None)
             
parser.add_option('-o', dest='output_file', type=str, help='Output file (required)', default=None)
               
          
def parse_gold_html(file_handle):
    # Create empty dictionary for results
    collection = {}

    # Parse html into Beautioful soup searchable document
    soup = BeautifulSoup(file_handle)
    file_handle.close()

    # Find Project data
    table0 = soup.find('div', id="ProjectInformation")
    # Get Gold ID
    Gold_ID = table0.findAll('tr')[1].findAll('td')[1].get_text()
    Gold_ID = Gold_ID.replace(u'\xa0',u'')
    Gold_ID = str(Gold_ID)
    Gold_ID = Gold_ID.lstrip('\n').rstrip('\n')
    collection["Gold_ID"] = Gold_ID


    # Get Organism information table
    table1 = soup.find('div', id="OrganismInformation")
    ## Get organism name
    org_name = str(table1.findAll('tr')[1].findAll('td')[1].get_text())
    org_name = org_name.lstrip('\n').rstrip('\n')
    collection["Organism"] = org_name

    ## Get organism NCBI Kingdom
    kingdom = table1.findAll('tr')[27].findAll('td')[1].get_text()
    kingdom = kingdom.replace(u'\xa0',u'')
    kingdom = str(kingdom)
    kingdom = kingdom.lstrip('\n').rstrip('\n')
    collection["Kingdom"] = kingdom
    ##If kingdom is Virus, then get order
    if kingdom == 'Viruses':
        NCBI_order = table1.findAll('tr')[30].findAll('td')[1].get_text()
        NCBI_order = NCBI_order.replace(u'\xa0',u'')
        NCBI_order = str(NCBI_order)
        NCBI_order = NCBI_order.lstrip('\n').rstrip('\n')
    else:
        NCBI_order = table1.findAll('tr')[28].findAll('td')[1].get_text()
        NCBI_order = NCBI_order.replace(u'\xa0',u'')
        NCBI_order = str(NCBI_order)
        NCBI_order = NCBI_order.lstrip('\n').rstrip('\n')
    collection ["Phyla-Order"] = NCBI_order


    # Get isolation information
    ## Get isolation ecosystem category
    try:
        isolation_ecosystem_category = (table1.findAll('tr')[36].findAll('td')[1].get_text())
        isolation_ecosystem_category = isolation_ecosystem_category.replace(u'\xa0',u'')
        isolation_ecosystem_category = str(isolation_ecosystem_category)
        isolation_ecosystem_category = isolation_ecosystem_category.lstrip('\n').rstrip('\n')
        ## Check for no results
        if len(isolation_ecosystem_category) == 0:
            isolation_ecosystem_category = 'none'
        collection["Isolation_ecosystem_category"] = isolation_ecosystem_category
    except IndexError:
        isolation_ecosystem_category = 'none'

    ## Get isolation ecosystem type
    isolation_ecosystem_type = (table1.findAll('tr')[37].findAll('td')[1].get_text())
    isolation_ecosystem_type = isolation_ecosystem_type.replace(u'\xa0',u'')
    isolation_ecosystem_type = str(isolation_ecosystem_type)
    isolation_ecosystem_type = isolation_ecosystem_type.lstrip('\n').rstrip('\n')
    ## Check for no results
    if len(isolation_ecosystem_type) == 0:
        isolation_ecosystem_type = 'none'
    collection["Isolation_ecosystem_type"] = isolation_ecosystem_type 

    # Find metadata table
    table2 = soup.find('div', id="OrganismMetadata")
    ## Get habitat information
    habitat = table2.findAll('tr')[20].findAll('td')[1].get_text()
    habitat = habitat.replace(u'\xa0',u'')
    habitat = str(habitat) 
    habitat =  habitat.replace('\t', '')
    habitat =  habitat.replace('\r', '')
    habitat =  habitat.rstrip('\n').lstrip('\n')
    habitat =  habitat.replace('\n\n', '-')
    ## Check for no results
    if len(habitat) == 0:
        habitat = 'none'
    collection["Known_habitats"] = habitat
    #print collection
    return collection


def main(argv):
    (opts, args) = parser.parse_args()
   
    # initialize the input and output file
    input_file = opts.input_file
    output_file = opts.output_file

    output_handle = open(output_file, "w")
    try:
        input_handle = open (input_file, 'r')
    except:
            print "count not open file " + input_file        

    # Parse html
    results = parse_gold_html(input_handle)

    # Print to output
    for key in results.iterkeys():
        output_handle.write('%s\t' %key)
    output_handle.write('\n')
    for value in results.itervalues():
        output_handle.write('%s\t' %value)
    output_handle.write('\n')

    output_handle.close()
    input_handle.close()        
    

# the main function 
main(sys.argv[1:])    


