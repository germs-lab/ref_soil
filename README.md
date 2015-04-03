# RefSoil
Script for preparing input file.

##USAGE:
Assume you have installed git, GNU c complier(gcc)

$ git clone https://github.com/germs-lab/RefSoil

$ cd RefSoil

$ g++ Fetchinput.cpp -o Fetchinput

$ ./Fetchinput RefSoilListJin.csv RefSoilListJin.txt

You will see a file "refSeqListJin.txt" 

You can follow this tutorial to fetch genome fron NCBI and parse 16s

http://adina-howe.readthedocs.org/en/latest/ncbi/index.html

Here is useful command line.

Let me guess you are in the folder 'RefSoil'
Note: you should have installed 'python' and 'python-biopython'. 
Note2: fetch-genomes2.py can fetch full-list of genbank

$ python fetch-genomes2.py RefSoilListJin.txt ../RefSoilgenbank

Now you will see around 1000 genes are downloaded.

To parse 16s,

$ for x in ../RefSoilgenbank/*; do python parse-genbank.py $x > ../RefSoil16s/$x.16S.fa; done

To get complete genome in fasta format

$ python fetch-genomes-fasta.py RefSoilListJin.txt ../RefSoilCompGenome