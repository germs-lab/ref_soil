# Compare to RefSeq
---
## get taxonomy from RefSoil
```
for x in *.gbk;do python /mnt/data3/jin_refseq/release74/dev/ncbi_tools/genbank_to_taxon.py $x;done > RefSoil_bac_tax.txt
cat RefSoil_bac_tax.txt|cut -f2|sort|uniq > RefSoil_bac_uniq_tax.txt
python /mnt/data3/jin_refseq/release74/dev/taxonomy_finder/id_to_tax.py RefSoil_bac_uniq_tax.txt > RefSoil_Full_taxonomy.txt
```
## get taxonomy from RefSeq
```    
for x in *.gbff ;do python /mnt/data3/jin_refseq/release74/dev/ncbi_tools/genbank_to_taxon.py $x;done > bacteria.tax.txt
cat bacteria.tax.txt|cut -f2|sort|uniq > RefSeq_bac_uniq_tax.txt
python /mnt/data3/jin_refseq/release74/dev/taxonomy_finder/id_to_tax.py RefSeq_bac_uniq_tax.txt > RefSeq_Full_taxonomy.txt
```
