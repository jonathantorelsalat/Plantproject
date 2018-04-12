#!/bin/bash

#classique sans GTF
#/opt/STAR/bin/Linux_x86_64/STAR --runMode genomeGenerate --runThreadN 40 --limitGenomeGenerateRAM=120000000000 --genomeDir /store/EQUIPES/PBI/Jonathan/Medicago_sativa/FASTQ/index --genomeFastaFiles /store/EQUIPES/PBI/Jonathan/Medicago_sativa/FASTQ/Alfalfa_112K.fasta

#avec faux GTF

/opt/STAR/bin/Linux_x86_64/STAR --runMode genomeGenerate --runThreadN 40 --limitGenomeGenerateRAM=120000000000 --genomeDir /store/EQUIPES/PBI/Jonathan/Medicago_sativa/FASTQ/index_fakeGTF --genomeFastaFiles /store/EQUIPES/PBI/Jonathan/Medicago_sativa/FASTQ/Alfalfa_112K.fasta --sjdbGTFfile /store/EQUIPES/PBI/Jonathan/Medicago_sativa/fake_gtf/faux_GTF.gtf
