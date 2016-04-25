python make_anno_refsoil.py bacteria.txt anno.step2.txt
graphlan_annotate.py --annot anno.step2.txt RefSoil_bac_ali.tree step2.xml
python add_kingdom.py bacteria.txt anno.step3.txt
graphlan_annotate.py --annot anno.step3.txt step2.xml step3.xml
python add_legend.py bacteria.txt anno.step4.txt
graphlan_annotate.py --annot anno.step4.txt step3.xml step4.xml
graphlan.py step4.xml step4.png --dpi 300 --size 15 --pad 0.6
#graphlan.py step4.xml step4.png --dpi 300 --size 15 --pad 0.6 --external_legends