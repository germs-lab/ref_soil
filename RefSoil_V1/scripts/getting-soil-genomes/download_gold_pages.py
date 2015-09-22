#!/usr/bin/python

import sys
import urllib2
import time
import difflib

# Inputs
filelist = open(sys.argv[1],'r')

# Parse list of Gold ids
list_of_gold_ids = []
for line in filelist:
    line = line.strip('\n')
    line0 = str(line)
    list_of_gold_ids.append(line0)
#print list_of_gold_ids

GOLD_base = "https://gold.jgi-psf.org/projects?id="

def write_html(html_text, file_name):
    try:
        output_handle = open(file_name,"w")
    except:
        "couldn't open file " + file_name
    
    output_handle.write(html_text)
    output_handle.close()
    return
    

    
# find all gh families
#for fam in Families.keys():
#    for i in range(1,Families[fam]+1):
#        link = CAZY_base + fam + str(i) + "_all.html"
#        html_old = ""
#        for j in range(0,10001,1000):
#            download_link = link + "?debut_PRINC=" + str(j) + "#pagination_PRINC"
#            html = None
#            try :
#                response = urllib2.urlopen(download_link)
#                html = response.read()
#                
#            except ValueError:
#                print "couldn't download file "  + download_link
#            if html:
#                seq=difflib.SequenceMatcher(a=html, b=html_old)
#                ratio = seq.real_quick_ratio()
#                cazy_file = "CAZy" + "_" + fam + str(i) + "_" + "page" + str(j) + ".html"
#                if ratio != 1.0:
#                    write_html(html, cazy_file)
#                else:
#                    break
#                html_old = html
#            time.sleep(1)
        
    
# find gold webpages
for gold in list_of_gold_ids:
    link = GOLD_base + str(gold)
    html_old = ""
    download_link = link 
    html = None
    try :
        response = urllib2.urlopen(download_link)
        html = response.read()
    except ValueError:
        print "couldn't download file "  + download_link
    if html:
        seq = difflib.SequenceMatcher(a=html, b=html_old)
        ratio = seq.real_quick_ratio()
        gold_file = "GOLD" + "_" + gold + ".html"
        if ratio != 1.0:
            write_html(html, gold_file)
    else:
        break
    html_old = html
    time.sleep(2)
    
