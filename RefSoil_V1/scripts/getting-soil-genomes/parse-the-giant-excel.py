import sys

for n, line in enumerate(open(sys.argv[1], 'rU')):
    if n < 2:
        continue
    else:
        dat = line.rstrip().split('\t')
        if len(dat) == 36:
            strain = dat[9]
            strain = strain.replace('"', '')
            print strain
