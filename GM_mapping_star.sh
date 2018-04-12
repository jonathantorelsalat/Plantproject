#!/bin/bash


/opt/STAR/bin/Linux_x86_64/STAR --runThreadN 40 --outFilterMultimapNmax 1 --genomeDir /store/EQUIPES/PBI/Jonathan/glycine_max/FASTQ/index --outSAMattributes All --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /store/EQUIPES/PBI/Jonathan/glycine_max/FASTQ/STARout/nodule_trimmed --readFilesIn /store/EQUIPES/PBI/Jonathan/glycine_max/FASTQ/glycine_max_nodule_trimmed.fastq 

/opt/STAR/bin/Linux_x86_64/STAR --runThreadN 40 --outFilterMultimapNmax 1 --genomeDir /store/EQUIPES/PBI/Jonathan/glycine_max/FASTQ/index --outSAMattributes All --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /store/EQUIPES/PBI/Jonathan/glycine_max/FASTQ/STARout/root_trimmed --readFilesIn /store/EQUIPES/PBI/Jonathan/glycine_max/FASTQ/glycine_max_root_trimmed.fastq 
