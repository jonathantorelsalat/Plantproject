#!/bin/bash

#tout trim à 300 (=/= on garde score >24)
fastx_trimmer -f 22 -l 300 -i cicer_ar_nod_2to10DPI.fastq -o cicer_ar_nod_2to10DPI_trimmed.fastq

fastx_trimmer -f 22 -l 300 -i cicer_ar_nod_11to28DPI.fastq -o cicer_ar_nod_11to28DPI_trimmed.fastq

fastx_trimmer -f 22 -l 300 -i cicer_ar_root.fastq -o cicer_ar_root_trimmed.fastq
