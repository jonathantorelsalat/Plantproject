#!/bin/bash


/opt/STAR/bin/Linux_x86_64/STAR --runThreadN 20 --twopassMode Basic --outSAMstrandField intronMotif --outFilterMultimapNmax -1 --genomeDir /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/index --outSAMattributes All --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/STARout/nodule_21DAI_almult --readFilesIn /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/Phas_vulgaris_nod_21DAI.fastq 


/opt/STAR/bin/Linux_x86_64/STAR --runThreadN 20 --twopassMode Basic --outSAMstrandField intronMotif --outFilterMultimapNmax -1 --genomeDir /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/index --outSAMattributes All --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/STARout/root_almult --readFilesIn /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/Phas_vulgaris_root.fastq
