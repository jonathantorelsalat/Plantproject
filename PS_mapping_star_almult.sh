#!/bin/bash

/opt/STAR/bin/Linux_x86_64/STAR --runThreadN 20 --twopassMode Basic --outSAMstrandField intronMotif --outFilterMultimapNmax -1 --genomeDir /store/EQUIPES/PBI/Jonathan/Pisum_sativum/FASTQpe/index --outSAMattributes All --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /store/EQUIPES/PBI/Jonathan/Pisum_sativum/FASTQpe/STARout/SRR1690952_trimmed_almult --readFilesIn /store/EQUIPES/PBI/Jonathan/Pisum_sativum/FASTQpe/SRR1690952_1_trimmed.fastq /store/EQUIPES/PBI/Jonathan/Pisum_sativum/FASTQpe/SRR1690952_2_trimmed.fastq

/opt/STAR/bin/Linux_x86_64/STAR --runThreadN 20 --twopassMode Basic --outSAMstrandField intronMotif --outFilterMultimapNmax -1 --genomeDir /store/EQUIPES/PBI/Jonathan/Pisum_sativum/FASTQpe/index --outSAMattributes All --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /store/EQUIPES/PBI/Jonathan/Pisum_sativum/FASTQpe/STARout/SRR1693197_trimmed_almult --readFilesIn /store/EQUIPES/PBI/Jonathan/Pisum_sativum/FASTQpe/SRR1693197_1_trimmed.fastq /store/EQUIPES/PBI/Jonathan/Pisum_sativum/FASTQpe/SRR1693197_2_trimmed.fastq



