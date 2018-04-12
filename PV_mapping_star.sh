#!/bin/bash


/opt/STAR/bin/Linux_x86_64/STAR --runThreadN 40 --outFilterMultimapNmax 1 --genomeDir /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/index --outSAMattributes All --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/STARout/nodule_21DAI --readFilesIn /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/Phas_vulgaris_nod_21DAI.fastq 


/opt/STAR/bin/Linux_x86_64/STAR --runThreadN 40 --outFilterMultimapNmax 1 --genomeDir /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/index --outSAMattributes All --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/STARout/root --readFilesIn /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/Phas_vulgaris_root.fastq
