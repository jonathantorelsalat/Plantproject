#!/bin/bash

/opt/subread-1.5.2/bin/featureCounts -T 40 -a /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/FASTQ/Phaseolus_vulgaris.PhaVulg1_0.38.chr.gtf -o //store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/BAM/PV_counts.txt /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/BAM/nodule_21DAIAligned.sortedByCoord.out.bam  /store/EQUIPES/PBI/Jonathan/Phaseolus_vulgaris/BAM/rootAligned.sortedByCoord.out.bam
