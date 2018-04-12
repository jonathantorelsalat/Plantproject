#!/bin/bash

/opt/STAR/bin/Linux_x86_64/STAR --runThreadN 40 --twopassMode Basic --outSAMstrandField intronMotif --outFilterMultimapNmax -1 --genomeDir /store/EQUIPES/PBI/Jonathan/cicer_arietinum/FASTQ/index --outSAMattributes All --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /store/EQUIPES/PBI/Jonathan/cicer_arietinum/FASTQ/STARout/CA_11to28DPI_almult --readFilesIn /store/EQUIPES/PBI/Jonathan/cicer_arietinum/FASTQ/cicer_ar_nod_11to28DPI_trimmed.fastq

/opt/STAR/bin/Linux_x86_64/STAR --runThreadN 40 --twopassMode Basic --outSAMstrandField intronMotif --outFilterMultimapNmax -1 --genomeDir /store/EQUIPES/PBI/Jonathan/cicer_arietinum/FASTQ/index --outSAMattributes All --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /store/EQUIPES/PBI/Jonathan/cicer_arietinum/FASTQ/STARout/CA_2to10DPI_almult --readFilesIn /store/EQUIPES/PBI/Jonathan/cicer_arietinum/FASTQ/cicer_ar_nod_2to10DPI_trimmed.fastq

/opt/STAR/bin/Linux_x86_64/STAR --runThreadN 40 --twopassMode Basic --outSAMstrandField intronMotif --outFilterMultimapNmax -1 --genomeDir /store/EQUIPES/PBI/Jonathan/cicer_arietinum/FASTQ/index --outSAMattributes All --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /store/EQUIPES/PBI/Jonathan/cicer_arietinum/FASTQ/STARout/CA_root_almult --readFilesIn /store/EQUIPES/PBI/Jonathan/cicer_arietinum/FASTQ/cicer_ar_root_trimmed.fastq

