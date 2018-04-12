#!/bin/bash

/opt/STAR/bin/Linux_x86_64/STAR --runMode genomeGenerate --runThreadN 40 --genomeDir /store/EQUIPES/PBI/Jonathan/Medicago_truncatula/FASTQpe/index --genomeFastaFiles /store/EQUIPES/PBI/Jonathan/Medicago_truncatula/FASTQpe/med_truncatula.fa  --sjdbGTFfile /store/EQUIPES/PBI/Jonathan/Medicago_truncatula/FASTQpe/Medicago_truncatula.MedtrA17_4.0.38.chr.gtf --sjdbOverhang 49
