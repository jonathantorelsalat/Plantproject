#!/bin/bash

/opt/STAR/bin/Linux_x86_64/STAR --runMode genomeGenerate --runThreadN 40 --genomeDir /store/EQUIPES/PBI/Jonathan/glycine_max/FASTQ/index --genomeFastaFiles /store/EQUIPES/PBI/Jonathan/glycine_max/FASTQ/Glycine_max.Glycine_max_v2.0.dna.chr.fa  --sjdbGTFfile /store/EQUIPES/PBI/Jonathan/glycine_max/annotation/Glycine_max.Glycine_max_v2.0.38.gtf --sjdbOverhang 33
