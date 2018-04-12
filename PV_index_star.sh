#!/bin/bash

/opt/STAR/bin/Linux_x86_64/STAR --runMode genomeGenerate --runThreadN 40 --genomeDir /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/index --genomeFastaFiles /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/genome/Phaseolus_vulgaris.PhaVulg1_0.dna.chr.fa  --sjdbGTFfile /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/annotation/Phaseolus_vulgaris.PhaVulg1_0.38.chr.gtf --sjdbOverhang 35
