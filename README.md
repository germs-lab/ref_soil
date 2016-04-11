# RefSoil
This repository provide the list of reference soil. (RefSoil_v1.txt)

### RefSoil_v1.txt
Each colume represents: uniq ID, chromosomes, version, taxon ID, Definition, Organism, Full taxonomy

RefSoil version 1 contains 928 genomes (888 bacteria, 34 archaea, 6 fungi) and 1070 chromosomes




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