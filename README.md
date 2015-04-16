# RefSoil
Script to get 16s tree from  RefSoil-DB amd RefSeq-DB

1. If you want to build tree file from RefSoil-DB, use genbank-file to get 16s
2. If you want to build tree file from RefSoil-DB, use HMM to get 16s
3. If you want to build tree file from RefSeq-DB, use HMM to get 16s

##USAGE:
Assume you have installed git, GNU c complier(gcc)

$ git clone https://github.com/germs-lab/RefSoil

$ cd RefSoil

1. Build tree file from RefSoil-DB, Use genbank to get 16s
----------
### Prepare List

$ g++ Fetchinput.cpp -o Fetchinput

$ ./Fetchinput RefSoilListJinUnix.csv RefSoilListJin.txt

You will see a file "refSeqListJin.txt" 

### Download Genbank file


You can follow this tutorial to fetch genome fron NCBI and parse 16s

http://adina-howe.readthedocs.org/en/latest/ncbi/index.html

Here is useful command line.

Let me guess you are in the folder 'RefSoil'
Note: you should have installed 'python' and 'python-biopython'. 
Note2: fetch-genomes2.py can fetch full-list of genbank

$ python fetch-genomes2.py RefSoilListJin.txt ../RefSoilgenbank

Now you will see around 1000 genes are downloaded.

### Parse 16s

To parse 16s,

$ for x in ../RefSoilgenbank/*; do python parse-genbank.py $x > $x.16S.fa; done

Let's more 16s.fa files into another folder

$ mkdir ../RefSoil16s

$ mv ../RefSoilgenbank/*.16S.fa ../RefSoil16s

### Treatment of file size 0


If some of the 16s file contains nothing, you may want to run HMMer to find 16s in the genome

#### First, Sort file by case
case1: don't need to work more
case2: need to work more

$ g++ FileSort.cc -o FileSort

$ ./FileSort RefSoilListJinUnix.csv ../RefSoil16s case1 case2

#### Second, Make list for download

$ g++ getFileList.cpp -o getFileList 

$ ./getFileList case2 ListOfFile.txt

Note, Fetchinput make list from file, getFileList make list from folder

#### Third, download complete genome
To get complete genome in fasta format

$ python fetch-genomes-fasta.py ListOfFile.txt FullGenomeForHMM

(Option)If you want to download complete gonome for all RefSoil, you can try.

$ python fetch-genomes-fasta.py RefSoilListJin.txt ../RefSoilCompGenome

#### Fourth, Run HMM(this is 16s hmm Vs RefSeq bacteria DB)

$ hmmsearch ssu.hmm /mnt/data1/jin/DBRefSeqBacFna/bacteria.fna > RefSeqHMM16s.output

#### GetResultHMM
$ g++ GetResultHMM.cpp -o GetResultHMM

$ ./GetResultHMM RefSeq16sHMM.output RefSeq16sHMM.txt

#### FetchPartFastaPart.py

$ python FetchPartFastaPart.py RefSeq16sHMM.txt RefSeq16s

#### After this, you will need, 
ChangeName.cpp
This will be described later

#### Finally, let's merge 16s Files into one

$ g++ MergeFiles.cpp -o MergeFiles

$ ./MergeFiles ../RefSoil16s RefSoil16s.fa

### Clustalo

$ clustalo -i RefSoil16s.fa --guidetree-out=RefSoil16s.dnd

You will get tree file : RefSoil16s.dnd

2. Build tree file from RefSoil-DB, Use HMM to get 16s
------
### get list

### Download complete genome

### HMM

### Get result from HMM

### Fetch 16s seq

### Merge 16s seq

### Clustalo



3. Build tree file from RefSeq-DB, Use	HMM to get 16s
------
### Donwload RefSeq DB

### Make one file

### HMM

### Get result from HMM

### Fetch 16s seq

### Merge 16s

### clustalo


 
 what is RunA2.cpp ?
------
This is the file that help yuo run AMPHORA2 automatically

The RunA2.cpp need to run in the working directory under AMPHORA2 folder
Let me say you have this directory structure:
    RefSoilCompGenome
    AMPHORA2/Working
Then, the RunA2.cpp need to run under AMPHORA2/Working

$ g++ RunA2.cpp -o RunA2

$ ./RunA2 ../../RefSoilCompGenome