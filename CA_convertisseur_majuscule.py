f=open("C_arietinum_nodule_transcriptome_assembly.fasta","r")

fichier=f.read()
f.close()

fichier_maj=open("C_arietinum_transcriptome_majuscules.fa","w")

fichier_maj.write(fichier.upper())

fichier_maj.close()


