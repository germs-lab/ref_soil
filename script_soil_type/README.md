#soiltype

```
blastn -db DB/emp_soil -query RefSoil_ar_bac_16s.fa -evalue 1e-5 -out refsoil_empsoil_blast_e5.out -outfmt 6
python cutoff.py refsoil_empsoil_blast_e5.out > refsoil_emp_blast.result.txt
cut -f2 refsoil_emp_blast.result.txt |sort|uniq > uniqID.txt
biom subset-table -i ../soil_emp_table.biom -a observation -s uniqID.txt -o subset_table.biom
biom convert -i subset_table.biom -o subset_table.txt --to-tsv
python soil_type.py SampleSoilOrders.unix.fix.txt subset_table.txt > soil_type_count.txt
```