python make_anno_refsoil.py bacteria.txt anno.step2.txt
graphlan_annotate.py --annot anno.step2.txt RefSoil_bac_ali.tree step2.xml
python add_kingdom.py bacteria.txt anno.step3.txt
graphlan_annotate.py --annot anno.step3.txt step2.xml step3.xml
python add_legend.py bacteria.txt anno.step4.txt
graphlan_annotate.py --annot anno.step4.txt step3.xml step4.xml
python make_abun_table.py soil_type_count.txt refsoil_emp_blast.out.txt > soil_type_abun.txt
python add_ring_soil_type.py soil_type_abun.txt anno.step5.txt
graphlan_annotate.py --annot anno.step5.txt step4.xml step5.xml
graphlan.py step5.xml step5.png --dpi 300 --size 15 --pad 0.6 --external_legends