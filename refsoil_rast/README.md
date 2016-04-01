# This folder includes subsystem ontology file, scripts and procedures to process RAST annotations for RefSoil

1. Extract RAST annotation from individual RAST annotation file:   
    ```
    python refsoil_annotation_parser.py subsystem_ontology.txt PATH/TO/RAST_RefSoilv1/*/Subsystems/bindings.plus.SS_categories
    ```

2. Some RefSoil ID include multiple genbank files. Each genbank file is annotated by RAST separately and assigned with a unique RAST ID. We can extract organism taxonomy and link the RAST ID with NCBI accession number from individual genbank file:  
    ```
    python refsoil_rast_gb_taxa_parser.py PATH/TO/RAST_RefSoilv1/*/genbank_file
    ```

3. Follow procedures in "rast_annotation_process.R" to organize and combine data, and create plot and tables. 
