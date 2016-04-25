python MakeAnno_rdp_guide.py EMP_soil_guide_uniq.txt EMP_soil_anno.txt
graphlan_annotate.py --annot EMP_soil_anno.txt EMP_soil_guide_uniq.txt EMP_step2.xml
python add_refsoil_ring.py RefSoil_guide_ar_bac.uniq.txt anno_step3.txt
graphlan_annotate.py --annot anno_step3.txt EMP_step2.xml EMP_step3.xml
python Guide_Add_Ring_SingleCell.py singlecell.unix.txt anno_step4.txt
graphlan_annotate.py --annot anno_step4.txt EMP_step3.xml EMP_step4.xml
python get_emp_count.py EMP_count.txt RefSoil_guide_ar_bac.uniq.txt > refsoil_count.txt
python MakeAnno_EMP_abundance.py EMP_count.txt anno.emp.count.txt
graphlan_annotate.py --annot anno.emp.count.txt EMP_step4.xml EMP_step5.xml
graphlan.py EMP_step5.xml EMP_step5.png --dpi 300 --size 15 --pad 0.6
#graphlan.py EMP_step5.xml EMP_step5.png --dpi 300 --size 15 --pad 0.6 --external_legends
