#!/bin/bash

#classique sans GTF

/opt/STAR/bin/Linux_x86_64/STAR --runMode genomeGenerate --runThreadN 40 --limitGenomeGenerateRAM=120000000000 --genomeDir /store/EQUIPES/PBI/Jonathan/Pisum_sativum/FASTQpe/index --genomeFastaFiles /store/EQUIPES/PBI/Jonathan/Pisum_sativum/transcriptome/PS_contigs_ref.fa

