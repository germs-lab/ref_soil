# Build 16s tree
Basic of Graphlan(installation and tutorial) is available [Here](https://github.com/germs-lab/dev/tree/master/GraphlanInput).

## Build 16s tree from 16s rRNA gene sequences
You need 16s file, here is the description how to get 16s sequences. https://github.com/germs-lab/ref_soil

### Step1: build tree file from 16s rRNA gene sequences
#### Alignment using infernal with RDP's bacterial model
```
$ ~/infernal-1.1.1-linux-intel-gcc/binaries/cmalign bacteria_model.cm RefSoil16sGenbank_HMM_clean.fa > RefSoil_bac_ali.sto
$ ~/infernal-1.1.1-linux-intel-gcc/binaries/esl-reformat afa RefSoil_bac_ali.sto > RefSoil_bac_ali.afa
```
#### Build tree using Fasttree
```
$ wget http://www.microbesonline.org/fasttree/FastTree
$ chmod +x FastTree
$ ./FastTree -nt < RefSoil_bac_ali.afa > RefSoil_bac.tree
```
### Step2: make annotation file, visualizing
#### Add color for phylum
```
python split_domain.py ../../ref_soil/RefSoil_v1.txt
python make_anno_refsoil.py RefSoil_v1.txt.split.bacteria.txt anno.step2.txt
graphlan_annotate.py --annot anno.step2.txt RefSoil_bac.tree step2.xml
```
#### This step add first ring
```
python add_kingdom.py RefSoil_v1.txt.split.bacteria.txt anno.step3.txt
graphlan_annotate.py --annot anno.step3.txt step2.xml step3.xml
```
#### This step add legend
```
python add_legend.py RefSoil_v1.txt.split.bacteria.txt anno.step4.txt
graphlan_annotate.py --annot anno.step4.txt step3.xml step4.xml
```
#### Add soil type
```
python make_abun_table.py soil_type_count.txt refsoil_emp_blast.out.txt > soil_type_abun.txt
python add_ring_soil_type.py soil_type_abun.txt anno.step5.txt
graphlan_annotate.py --annot anno.step5.txt step4.xml step5.xml
```
#### Finally generate tree figure
```
graphlan.py step5.xml step5.png --dpi 300 --size 15 --pad 0.6 --external_legends
```

## Build tree by using RDP classifier
Running RDP classifier
```
java -Xmx1g -jar ~/RDPTools/classifier.jar classify -o EMP_soil_RDP_taxonomy.txt -h EMP_soil_RDP_hier.txt JavaNewSoilRepSet.fna
java -Xmx1g -jar ~/RDPTools/classifier.jar classify -o RefSoil_RDP_taxonomy.txt -h RefSoil\
_RDP_hier.txt RefSoil_ar_bac_16s.txt
```
You will have Taxonomy file

Then, make guide file
```
python rdp_to_guide.py EMP_soil_RDP_taxonomy.txt EMP_soil_map.txt > EMP_soil_guide.txt
sort EMP_soil_guide.txt|uniq > EMP_soil_guide_uniq.txt
python rdp_to_guide.py RefSoil_RDP_taxonomy.txt RefSoil_map.txt > RefSoil_guide_ar_bac.txt
sort RefSoil_guide_ar_bac.txt |uniq > RefSoil_guide_ar_bac.uniq.txt
```
You are ready to draw tree

step1: plain tree
```
graphlan.py EMP_soil_guide_uniq.txt EMP.step1.png --dpi 300 --size 15 --pad 0.6
```
step2: add color for phylum
Make annotation file
```
python MakeAnno_rdp_guide.py EMP_soil_guide_uniq.txt EMP_soil_anno.txt
graphlan_annotate.py --annot EMP_soil_anno.txt EMP_soil_guide_uniq.txt EMP_step2.xml
graphlan.py EMP_step2.xml EMP.step2.png --dpi 300 --size 15 --pad 0.6
```
step3: add refsoil ring
```
python add_refsoil_ring.py RefSoil_guide_ar_bac.txt anno_step3.txt
graphlan_annotate.py --annot anno_step3.txt EMP_step2.xml EMP_step3.xml
graphlan.py EMP_step3.xml EMP_step3.png --dpi 300 --size 15 --pad 0.6
```
step4: add single cell ring
```
python Guide_Add_Ring_SingleCell.py /mnt/data2/jin_emp/emp/Dev/GraphlanInput/singlecell.unix.txt anno_step4.txt
graphlan_annotate.py --annot anno_step4.txt EMP_step3.xml EMP_step4.xml
graphlan.py EMP_step4.xml EMP.step4.png --dpi 300 --size 15 --pad 0.6
```
step5: add abundance ring
count using map
```
python count_map.py summaryfile mapfile > output
```
get count for refsoil
```
python get_emp_count.py EMP_count.txt RefSoil_guide_ar_bac.txt > refsoil_count.txt
```
make annotation
```
python MakeAnno_EMP_abundance.py EMP_count.txt anno.emp.count.txt
graphlan_annotate.py --annot anno.emp.count.txt EMP_step4.xml EMP_step5.xml
graphlan.py EMP_step5.xml EMP_step5.png --dpi 300 --size 15 --pad 0.6 --external_legends
```
to get count for singlecell
```
python /mnt/data2/jin_emp/emp/Dev/GraphlanInput/get_emp_count.py sc_guide_map.txt /mnt/data2/jin_emp/emp/soil_emp_rdp_tax/EMP_count.txt sc_guide.txt
```
