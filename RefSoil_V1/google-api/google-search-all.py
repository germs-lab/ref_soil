#!/usr/bin/python2.4
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Custom Search.

Command-line application that does a search based on previous code by Joe Gregorio (Google).
"""

__author__ = 'adina@iastate.edu (Adina Howe)'

import pprint, sys

from apiclient.discovery import build

def main():

  # Reads in list of strains of interest
  l = []
  for line in open(sys.argv[1]):
      l.append(line.rstrip())
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.


  for each in l:
      query_string = str(each) 
      print query_string
      service = build("customsearch", "v1", developerKey="")
      res = service.cse().list(q=query_string, exactTerms="soil OR root OR rhizosphere OR sludge OR sand OR mud OR rhizome OR sediment OR nodule", cx='007338222879492932262:fn39gax5y9y',c2coff=1).execute()
      file_out_name = query_string.translate(None, "?.!/;:,")
      fp = open('_'.join(file_out_name.split(' ')) + '.test', 'w')
      if res.has_key("items"):
        for n, x in enumerate(res["items"]):
          url = x["formattedUrl"].encode('utf-8')
          snippet = x["snippet"].encode('utf-8')
          fp.write('Result Entry %s\n' % str(n))
          fp.write('%s' % '-'*100)
          fp.write('\n')
          fp.write('%s\n' % x["displayLink"].encode('utf-8'))
          fp.write('%s\n' % x["title"].encode('utf-8'))
          fp.write('%s\n' % x["link"].encode('utf-8'))
          fp.write('%s\n' % snippet)
          fp.write('\n')
        fp.close()
      else:
        fp.write("No items found.\n")
        fp.close()
        continue

  

if __name__ == '__main__':
  main()
