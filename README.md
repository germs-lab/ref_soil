# RefSoil
Script for preparing input file.

##USAGE:
Assume you have installed git, GNU c complier(gcc)

$ git clone https://github.com/germs-lab/RefSoil

$ cd RefSoil

$ g++ NCBIinput.cpp -o NCBIinput

$ ./NCBIinput

You will see a file "refSeqListInputISNDC.txt" 

You can follow this tutorial to fetch genome fron NCBI and parse 16s

http://adina-howe.readthedocs.org/en/latest/ncbi/index.html

Here is useful command line.

Let me guess you are in the folder 'RefSoil'
Note: you should have installed 'python' and 'python-biopython'. 
$ cd ..

$ git clone https://github.com/adina/scripts-for-ngs2014.git

$ cp RefSoil/refSeqListInputISNDC.txt scripts-for-ngs2014

$ cd scripts-for-ngs2014

$ python fetch-genomes.py refSeqListInputISNDC.txt genbank-files

Now you will see around 1000 genes are downloaded.

To parse 16s,

$ for x in genbank-files/*; do python parse-genbank.py $x > $x.16S.fa; done