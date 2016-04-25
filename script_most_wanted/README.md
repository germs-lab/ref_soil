#most wanted
## most prevalence
```
python ../../ref_soil/script_most_wanted/nonzero.py ../soil_emp_table.biom > nonzero.out2
sort -n -r -k 2 nonzero.out2 |head -n 100 > 100_most_ubiq_id.txt
python get_most_ubiq_v2.py 100_most_ubiq_id.txt ../../emp/soil_emp_qiime_tax/SoilRepSet_tax_assignments.txt > 100_most_ubiq.txt
sort -k 1 -n -r 100_most_ubiq.txt >100_most_ubiq_sorted.txt
cut -f2 100_most_ubiq_sorted.txt > ubiq_id_to_blast.txt 
python subset_repset.py ubiq_id_to_blast.txt ../../emp/soil_rep_set.fna > ubiq_seq_to_blast.fna
blastn -db ../../emp/blast/DB/refsoil -query ubiq_seq_to_blast.fna -evalue 1e-5 -out ubiq.blast.out -outfmt 6
python ../script_soil_type/cutoff.py ubiq.blast.out > ubiq.over97.txt
cut -f1 ubiq.over97.txt > ubiq_id_to_remove.txt
python remove_refsoil.py ubiq_id_to_remove.txt 100_most_ubiq_sorted.txt > most_wanted_ubiq.txt
```

## most abun
```
tail -n 100 ../../emp/soil_emp_table.summary > 100_most_abun_id.txt
python get_tax_most_abun.py 100_most_abun_id.txt ../../emp/soil_emp_qiime_tax/SoilRepSet_tax_assignments.txt > 100_most_abun.txt
sort -n -r -k 1 100_most_abun.txt > 100_most_abun_sorted.txt
cut -f2 100_most_abun_sorted.txt > abun_id_to_blast.txt
python subset_repset.py abun_id_to_blast.txt ../../emp/soil_rep_set.fna > abun_seq_to_blast.fna
blastn -db ../../emp/blast/DB/refsoil -query abun_seq_to_blast.fna -evalue 1e-5 -out abun.blast.out -outfmt 6
python ../script_soil_type/cutoff.py abun.blast.out > abun.over97.txt
cut -f1 abun.over97.txt > abun_id_to_remove.txt
python remove_refsoil.py abun_id_to_remove.txt 100_most_abun_sorted.txt > most_wanted_abun.txt
```

## both abundance and prevalence
```
python both.py most_wanted_abun.txt most_wanted_ubiq.txt > most_wanted.txt
```