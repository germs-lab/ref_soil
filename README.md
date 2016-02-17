# RefSoil
This repository provide the list of reference soil. (RefSoil_v1.txt)

### RefSoil_v1.txt
Each colume represents: uniq ID, chromosomes, version, taxon ID, Definition, Organism, Full taxonomy

RefSoil version 1 contains 928 genomes (888 bacteria, 34 archaea, 6 fungi) and 1070 chromosomes


##Script to get 16s tree for RefSoil-DB

This page describe the detail how to generate 16s tree of RefSeq: the tree is built using genbank file from RefSeq to retrive 16s. If 16s sequence is not present, HMM is used to find 16s sequence.

##required:
Assume you have installed git, GNU c complier(gcc)
```
$ git clone https://github.com/germs-lab/ref_soil.git
$ cd ref_soil
```
1. Build tree file from RefSoil-DB, Use genbank to get 16s
----------
This documentation shows building 16s tree for Bacteria.
### Prepare List
```
python get_list_for_download_from_RefSoil.py RefSoil_v1.txt
```
Then you will see three files: RefSoil_v1.txt.archaea.txt, RefSoil_v1.txt.bacteria.txt, RefSoil_v1.txt.fungi.txt

### Download Genbank file


You can follow this tutorial to fetch genome fron NCBI and parse 16s

http://adina-howe.readthedocs.org/en/latest/ncbi/index.html

Here is useful command line.

Let me guess you are in the folder 'RefSoil'

Note: you should have installed 'python' and 'python-biopython'. 

Note2: fetch-genomes2.py can fetch full-list of genbank
```
$ python fetch-genomes2.py RefSoil_v1.txt.bacteria.txt ../RefSoil_v1_bacteria
```
Now you will see 981 genbank files are downloaded.

### Parse 16s

To parse 16s,
```
$ for x in ../RefSoil_v1_bacteria/*.gbk; do python parse-genbank.py $x > $x.16S.fa; done
```
Let's move 16s.fa files into another folder
```
$ mkdir ../RefSoil16s

$ mv ../RefSoil_v1_bacteria/*.16S.fa ../RefSoil16s
```
### Treatment of file size 0


If some of the 16s file contains nothing, you may want to run HMMer to find 16s in the genome

#### First, Sort file by case
case1: don't need to work more
case2: need to work more
```
$ cat RefSoil_v1.txt|cut -f3 > RefSoil_v1_version.txt
$ g++ FileSort.cc -o FileSort
$ ./FileSort RefSoil_v1_version.txt ../RefSoil16s case1 case2
```

#### Now, merge file
```
cat ../RefSoil16s/*.fa > merged16s.fa
```

### check multiple chromosome
```
$ cat RefSoil_v1.txt|cut -f2 > RefSoil_v1_chromosome.txt
$ python check_duplicated_16s.py RefSoil_v1_chromosome.txt merged16s.fa > genbank_16s.fa
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
#### merge file
```
$ cat FullGenomeForHMM/*.fa > MissingFasta.fa
```
#### Fourth, Run HMM(this is 16s hmm Vs RefSeq bacteria DB)
```
$ hmmsearch ssu.hmm MissingFasta.fa > RefSoilHMM16s.output
```
#### GetResultHMM
```
$ g++ GetResultHMM.cpp -o GetResultHMM

$ ./GetResultHMM RefSoilHMM16s.output RefSoil16sHMM.txt
```
#### FetchPartFastaPart.py
```
$ python FetchPartFastaPart.py RefSoil16sHMM.txt RefSoil16s
```
#### change name and merge
```
$ for x in RefSoil16s/*; do python changename.py $x;done
$ cat RefSoil16s/*.fa > HMM16smerged.fa
```
#### Finally, let's merge 16s Files into one
```
$ cat genbank_16s.fa HMM16smerged.fa > RefSoil16sGenbank_HMM.fa
```
### make clean fasta
```
$ python CleanFasta.py RefSoil16sGenbank_HMM.fa RefSoil16sGenbank_HMM_clean.fa
```

### now make tree
```
$ cd ~
$ wget http://eddylab.org/infernal/infernal-1.1.1-linux-intel-gcc.tar.gz
$ tar xf infernal-1.1.1-linux-intel-gcc.tar.gz
```
back to original folder
```
$ ~/infernal-1.1.1-linux-intel-gcc/binaries/cmalign bacteria_model.cm RefSoil16sGenbank_HMM_clean.fa > RefSoil_bac_ali.sto
$ ~/infernal-1.1.1-linux-intel-gcc/binaries/esl-reformat afa RefSoil_bac_ali.sto > RefSoil_bac_ali.afa
```
Now build tree
```
$ wget http://www.microbesonline.org/fasttree/FastTree
$ chmod 655 FastTree
$ ./FastTree -nt < RefSoil_bac_ali.afa > RefSoil_bac.tree
```

### plot tree: Graphlan
step1: only tree
```
graphlan.py RefSoil_bac.tree step1.pn --dpi 300 --size 15 --pad 0.6
```
step2: add color for phylum
```
python MakeAnno_RefSoil_no_ring.py RefSoil_v1.txt.split.bacteria.txt RefSoil_bacAnno.txt
graphlan_annotate.py --annot RefSoil_bacAnno.txt RefSoil_bac.tree step2.xml
graphlan.py step2.xml step2.png --dpi 300 --size 15 --pad 0.6
```
##below here, not used

### Clustalo
```
$ clustalo -i RefSoil16sGenbank_HMM_clean.fa --guidetree-out=RefSoil16sGenbank_HMM.dnd
```
You will get tree file : RefSoil16s.dnd


## Find Tax information
```
for x in ../RefSoilgenbank_v11_17_2015/*;do python GenbankToTax.py $x;done > RefSoilTax.txt
python TaxFinder2.py RefSoilTax.txt RefSoilFullTax_w_id.txt
```

## below here about new id
uniq_id_remove_error.txt contains non-redundant ncbi id after remove error
id_for_download.txt contains all ncbi id for download genbank file


### below here is not used anymore
```
$ g++ Fetchinput.cpp -o Fetchinput
$ ./Fetchinput RefSoilList_bac_w_nameV11_17_2015.unix.csv RefSoilList.txt
```
You will see a file "RefSoilList.txt"