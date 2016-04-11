import sys


fp = open("list-of-multiples.txt", "w")
fp2 = open("list-of-genomes.cleaned.txt", "w")

for line in open(sys.argv[1]):
    dat = line.rstrip().split(',')
    if len(dat) > 1:
        fp.write('%s\n' % line.rstrip())
        for x in dat:
            if x != '-':
                fp2.write('%s\n' % x)
    else:
        fp2.write('%s\n' % line.rstrip())
