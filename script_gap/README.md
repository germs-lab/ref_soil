# find gap

## build repset
```
blastn -db refsoil -query soil_repset.fna -evalue 1e-5 -out blast.out -outfmt 6
python cutoff.py blast.out > refsoil_similar.txt
cut -f1 refsoil_similar.txt > id_to_remove.txt
python build_repset.py id_to_remove.txt soil_repset.fna > gap_repset.fna
java -jar Xmx1g -jar classifier.jar classify -o gap_rdp_taxonomy.txt -h gap_rdp_hier.txt gap_repset.fna
```
