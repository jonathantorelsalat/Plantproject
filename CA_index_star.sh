#!/bin/bash

#classique sans GTF

/opt/STAR/bin/Linux_x86_64/STAR --runMode genomeGenerate --runThreadN 40 --limitGenomeGenerateRAM=120000000000 --genomeDir //store/EQUIPES/PBI/Jonathan/cicer_arietinum/FASTQ/index --genomeFastaFiles /store/EQUIPES/PBI/Jonathan/cicer_arietinum/Transcriptome/C_arietinum_transcriptome_majuscules.fa
