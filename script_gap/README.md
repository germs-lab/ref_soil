# find gap
## Calculate Gap
### build repset
```
blastn -db refsoil -query soil_repset.fna -evalue 1e-5 -out blast.out -outfmt 6
python cutoff.py blast.out > refsoil_similar.txt
cut -f1 refsoil_similar.txt > id_to_remove.txt
python build_repset.py id_to_remove.txt soil_repset.fna > gap_repset.fna
java -jar Xmx1g -jar classifier.jar classify -o gap_rdp_taxonomy.txt -h gap_rdp_hier.txt gap_repset.fna
```

### Calculate number of count for each phylum
```
python count_abun_emp.py summary taxonomy repset > abun_phylum.txt
```

### Calculate number of OTUs for each phylum
```
python count_tax_rdp.py taxonomy > numotu.txt
```

## You can use this to calculate for all EMP
### number of count for each phylum in EMP-Soil
```
python ../../ref_soil/script_gap/count_abun_emp.py ../soil_emp_table.summary ../soil_emp_rdp_tax/EMP_soil_RDP_taxonomy.txt ../soil_rep_set.fna > emp_soil_abun_phylum.txt
```
### number of OTUs for each phylum in EMP-soil
```
python ../../ref_soil/script_gap/count_tax_rdp.py ../soil_emp_rdp_tax/EMP_soil_RDP_taxonomy.txt > emp_soil_num_otu_phylum.txt
```
