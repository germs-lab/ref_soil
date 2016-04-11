# Build 16s tree
Basic of Graphlan(install and tutorial) is available [Here](https://github.com/germs-lab/dev/tree/master/GraphlanInput).

## Build 16s tree from 16s rRNA gene sequences
You need 16s file, here is the description how to get 16s sequences. https://github.com/germs-lab/ref_soil

### step1: build tree file from 16s rRNA gene sequences
#### Alignment using infernal with RDP's bacterial model
```
$ ~/infernal-1.1.1-linux-intel-gcc/binaries/cmalign bacteria_model.cm RefSoil16sGenbank_HMM_clean.fa > RefSoil_bac_ali.sto
$ ~/infernal-1.1.1-linux-intel-gcc/binaries/esl-reformat afa RefSoil_bac_ali.sto > RefSoil_bac_ali.afa
```
#### build tree using Fasttree
```
$ wget http://www.microbesonline.org/fasttree/FastTree
$ chmod 655 FastTree
$ ./FastTree -nt < RefSoil_bac_ali.afa > RefSoil_bac.tree
```
### Step2: make annotation file, visualizing
#### add color for phylum
```
python ../../dev/GraphlanInput/make_anno_refsoil.py RefSoil_v1.txt.split.bacteria.txt anno.step2.txt
graphlan_annotate.py --annot anno.step2.txt RefSoil_bac.tree step2.xml
```
####This step add first ring
```
python ../../dev/GraphlanInput/add_kingdom.py RefSoil_v1.txt.split.bacteria.txt anno.step3.txt
graphlan_annotate.py --annot anno.step3.txt step2.xml step3.xml
```
####This step add legend
```
python ../../dev/GraphlanInput/add_legend.py RefSoil_v1.txt.split.bacteria.txt anno.step4.txt
graphlan_annotate.py --annot anno.step4.txt step3.xml step4.xml
```
####add soil type
```
python ../dev/emp_tools/make_abun_table.py soil_type_count.txt refsoil_emp_blast.out.txt > soil_type_abun.txt
python ../../dev/GraphlanInput/add_ring_soil_type.py soil_type_abun.txt anno.step5.txt
graphlan_annotate.py --annot anno.step5.txt step4.xml step5.xml
```
#### Finally generate tree figure
```
graphlan.py step5.xml step5.png --dpi 300 --size 15 --pad 0.6 --external_legends
```