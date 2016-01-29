#!/user/bin/python
import sys
for line in open(sys.argv[1],'r'):
    spl =  line.strip().split(',')
    for x in spl:
        print x
