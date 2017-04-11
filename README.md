# RefSoil
This repository provide the list of reference soil. (RefSoil_v1.txt)

### RefSoil_v1.txt
Each colume represents: uniq ID, chromosomes, version, taxon ID, Definition, Organism, Full taxonomy

RefSoil version 1 contains 928 genomes (888 bacteria, 34 archaea, 6 fungi) and 1070 chromosomes

## How to download RefSoil database
### Download from figshare
Probably the easiest way is the go to the following link to download file
https://figshare.com/articles/RefSoil_Database/4362812

### Download using script
You can also download from NCBI using list of ID and given script bellow.

First, clone this repository
```
git clone https://github.com/germs-lab/ref_soil.git
```

#### Download Genbank format
```
python script_download_refsoil/fetch_genbank.py script_download_refsoil/refsoil_id.txt refsoil_genbank
```

#### Download full genome nucleotide sequence in FASTA format
```
python script_download_refsoil/fetch_fasta_genome.py script_download_refsoil/refsoil_id.txt refsoil_full_genome_fasta
```

#### Download CDS nucleotide in FASTA format
```
python script_download_refsoil/fetch_fasta_cds.py script_download_refsoil/refsoil_id.txt refsoil_cds_fasta
```

#### Download protein sequence in FASTA format
```
python script_download_refsoil/fetch_fasta_protein.py script_download_refsoil/refsoil_id.txt refsoil_protein_fasta
```

## List of the script
[Get 16s rRNA gene sequences](https://github.com/germs-lab/ref_soil/tree/master/get_refsoil_16s)

[Build 16s rRNA gene tree](https://github.com/germs-lab/ref_soil/tree/master/script_build_tree)

[RAST analysis](https://github.com/germs-lab/ref_soil/tree/master/refsoil_rast)

[Compare RefSeq](https://github.com/germs-lab/ref_soil/tree/master/compare_refseq)