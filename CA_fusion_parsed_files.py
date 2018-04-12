import re 
import time


li=['2to10DPI','11to28DPI','root']

liste_nomcontig=[]

dictionnaire={} #contiendra toutes les valeurs de tout les fichiers

nbfichier=1
nom_des_fichiers=['Contigs/genes number']


la=['un','mult']
for setfile in li:
	for nfile in la:

		liste_fichier=[]
		liste_comptage=[]
		
		print("ouverture de CA_"+setfile+"_align_"+nfile+".txt")

		f = open("CA_"+setfile+"_align_"+nfile+".txt", "r")
		nom_des_fichiers.append("CA_"+setfile+"_align_"+nfile+".txt")


		lines = f.readlines()
		f.close()

		for ligne in lines:
			liste=ligne.split('\t')
			liste_fichier.append(liste[0])
			liste_comptage.append(liste[1])
				
		max_contig=83405

		

		for i in range(83405):
			liste_nomcontig.append("CONTIG"+str(i+1))

	
		
		
		j=0


		taille_max=len(liste_fichier)

		if liste_fichier[taille_max-1]!=("CONTIG"+str(max_contig)):
			liste_fichier.append("CONTIG"+str(max_contig))
			fake_end=True
		else: fake_end=False

		for i in range(83405):


			valueinterm=liste_fichier[j]
			

			if liste_nomcontig[i]==valueinterm:
				j=j+1
			else:
	
				liste_fichier.insert(i,liste_nomcontig[i])
				liste_comptage.insert(i,"0"+"\n")
				j=j+1
		if fake_end==True:
			liste_comptage.insert(max_contig,0)

		

		dictionnaire[0]=liste_nomcontig
		dictionnaire[nbfichier]=liste_comptage
	
		nbfichier=nbfichier+1

print("debut ecriture")

out=open("CA_counts.txt","w")


for i in range(len(nom_des_fichiers)):
	out.write(nom_des_fichiers[i]+"\t")
out.write("\n")

for i in range(max_contig):
	for k in range(len(dictionnaire)):
		dictionnaire[k][i]=str(dictionnaire[k][i]).replace("\n","")
		out.write(dictionnaire[k][i]+"\t")
	out.write("\n")


out.close()




print("fin")






















