# RefSoil
Script to get 16s tree from  RefSoil-DB amd RefSeq-DB

1. If you want to build tree file from RefSoil-DB, use genbank-file to get 16s
2. If you want to build tree file from RefSoil-DB, use HMM to get 16s
3. If you want to build tree file from RefSeq-DB, use HMM to get 16s

##USAGE:
Assume you have installed git, GNU c complier(gcc)
```
$ git clone https://github.com/germs-lab/RefSoil
$ cd RefSoil
```
1. Build tree file from RefSoil-DB, Use genbank to get 16s
----------
### Prepare List
```
$ g++ Fetchinput.cpp -o Fetchinput
$ ./Fetchinput RefSoilList_bac_w_nameV9_17_2015unix.csv RefSoilList.txt
```
You will see a file "RefSoilList.txt" 

### Download Genbank file


You can follow this tutorial to fetch genome fron NCBI and parse 16s

http://adina-howe.readthedocs.org/en/latest/ncbi/index.html

Here is useful command line.

Let me guess you are in the folder 'RefSoil'
Note: you should have installed 'python' and 'python-biopython'. 
Note2: fetch-genomes2.py can fetch full-list of genbank
```
$ python fetch-genomes2.py RefSoilList.txt ../RefSoilgenbankV9_17_2015
```
Now you will see around 1000 genes are downloaded.

### Parse 16s

To parse 16s,
```
$ for x in ../RefSoilgenbankV9_17_2015/*; do python parse-genbank.py $x > $x.16S.fa; done
```
Let's move 16s.fa files into another folder
```
$ mkdir ../RefSoil16s

$ mv ../RefSoilgenbankV9_17_2015/*.16S.fa ../RefSoil16s
```
### Treatment of file size 0


If some of the 16s file contains nothing, you may want to run HMMer to find 16s in the genome

#### First, Sort file by case
case1: don't need to work more
case2: need to work more
```
$ g++ FileSort.cc -o FileSort

$ ./FileSort RefSoilListJinUnix.csv ../RefSoil16s case1 case2
```
#### Second, Make list for download
```
$ g++ getFileList.cpp -o getFileList 

$ ./getFileList case2 ListOfFile.txt
```
Note, Fetchinput make list from file, getFileList make list from folder

#### Third, download complete genome
To get complete genome in fasta format
```
$ python fetch-genomes-fasta.py ListOfFile.txt FullGenomeForHMM
```
(Option)If you want to download complete gonome for all RefSoil, you can try.
```
$ python fetch-genomes-fasta.py RefSoilListJin.txt ../RefSoilCompGenome
```
#### Fourth, Run HMM(this is 16s hmm Vs RefSeq bacteria DB)
```
$ hmmsearch ssu.hmm /mnt/data1/jin/DBRefSeqBacFna/bacteria.fna > RefSeqHMM16s.output
```
#### GetResultHMM
```
$ g++ GetResultHMM.cpp -o GetResultHMM

$ ./GetResultHMM RefSeq16sHMM.output RefSeq16sHMM.txt
```
#### FetchPartFastaPart.py
```
$ python FetchPartFastaPart.py RefSeq16sHMM.txt RefSeq16s
```
#### After this, you will need, 
ChangeName.cpp
This will be described later

#### Finally, let's merge 16s Files into one
```
$ g++ MergeFiles.cpp -o MergeFiles

$ ./MergeFiles ../RefSoil16s RefSoil16s.fa
```
### Clustalo
```
$ clustalo -i RefSoil16s.fa --guidetree-out=RefSoil16s.dnd
```
You will get tree file : RefSoil16s.dnd

2. Build tree file from RefSoil-DB, Use HMM to get 16s
------
### get list
```
$ g++ Fetchinput.cpp -o Fetchinput

$ ./Fetchinput RefSoilList_bac_w_nameV9_17_2015unix.csv RefSoilList.txt
```
You will see a file "RefSoilList.txt"

### Download complete genome
```
$ python fetch-genomes-fasta.py RefSoilList.txt ../RefSoilFastaV9_17_2015
```
### merge file
```
$ cat ../RefSoilFastaV9_17_2015/*.fa > RefSoilFasta.fa
```
### HMM
```
$ hmmsearch ssu.hmm RefSoilFasta.fa > RefSoilHMM16sFasta.output
```
Note: if you don't have	hmmer, install (apt-get	install	hmmer)
### Get result from HMM
```
$ g++ GetResultHMM.cpp -o GetResultHMM

$ ./GetResultHMM RefSoilHMM16sFasta.output RefSoil16sHMMfasta.txt
```
### Fetch 16s seq
```
$ python FetchPartFastaPart.py RefSoil16sHMMfasta.txt RefSoil16sFasta
```
### Merge 16s seq
```
$ cat RefSoil16sFasta/*.fa > RefSoil16sHMMFasta.fa
```
### replace : into space
```
$ sed s/:/' '/ RefSoil16sHMMFasta.fa > RefSoil16sHMMFastaNS.fa
```
### Clustalo
```
$ clustalo -i RefSoil16sHMMFastaNS.fa --guidetree-out=RefSoil16sHMMFastaNS.dnd
```

3. Build tree file from RefSeq-DB, Use	HMM to get 16s
------
### Donwload RefSeq DB

### Make one file
```
$ g++ MergeFiles.cpp -o MergeFiles

$ ./MergeFiles ../RefSeqbac RefSeqbac.fa
```
### HMM
```
$ hmmsearch ssu.hmm ../RefSeqbac/RefSeqbac.fa > RefSeqbac16s.output
```
Note: if you don't have hmmer, install (apt-get install hmmer)
### Get result from HMM
```
$ g++ GetResultHMM.cpp -o GetResultHMM

$ ./GetResultHMM RefSeqbac16s.output RefSeqbac16sHMM.txt
```
### Fetch 16s seq
```
$ python FetchPartFastaPart.py RefSeqbac16sHMM.txt RefSeqbac16s
```
### Merge 16s
```
$ g++ MergeFiles.cpp -o MergeFiles

$ ./MergeFiles RefSeqbac16s RefSeqbac16s.fa
```
### clustalo
```
$ clustalo -i RefSeqbac16s.fa --guildetree-out=RefSeqbac16s.dnd
```
