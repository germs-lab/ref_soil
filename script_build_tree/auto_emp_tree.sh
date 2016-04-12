python MakeAnno_rdp_guide.py EMP_soil_guide_uniq.txt EMP_soil_anno.txt
graphlan_annotate.py --annot EMP_soil_anno.txt EMP_soil_guide_uniq.txt EMP_step2.xml
python add_refsoil_ring.py RefSoil_guide_ar_bac.uniq.txt anno_step3.txt
graphlan_annotate.py --annot anno_step3.txt EMP_step2.xml EMP_step3.xml