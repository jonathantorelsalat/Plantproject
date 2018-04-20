#Verifions que tout les peptides ont été blastés 

#param
import os

FichList = [ f for f in os.listdir('.') if os.path.isfile(os.path.join('.',f)) ]
l_fichiers=[]
l_lines=[]
dico_rawd={}
dico_contig={}
dico_blast={}
liste_contig_manquant=[]


#chargeons tout les fichiers (à proposer au choix utilisateurs)

print("Début du script")

nb_fichier=input("Combien de fichiers à vérifier ?")


print("Entrez les noms de fichiers  à vérifier (sans le .fa)")

for i in range(1,int(nb_fichier)+1):
	
	l_fichiers.append(input("Fichier "+str(i)+":"))

print("Voici la liste des fichiers à vérifier",l_fichiers)


print("Chargeons les fichiers")





for i in l_fichiers:
	
	

	print("Chargement du fichier"+i+".fa")
	
	try:
		l_lines.append("lines_"+str(i))
		f = open(i+".fa", "r")
		dico_rawd[i] = f.readlines()
		f.close()
	except:
		print("Le fichier n'a pu être chargé correctement. Vérifiez que le fichier existe 				bien et relancez votre programme.")
		sys.exit(0) ### Stoppe simplement l'exécution du programme.

	print("Fichier chargé, début stockage des noms de peptides")
	
	for plante in dico_rawd:
		
		dico_contig[plante]=[]
		for el in dico_rawd[plante]:
			
			
			if el[0]==">":
				el=el.replace(">","")
				dico_contig[plante].append(el)
			
print("ouverture du fichier de résultat: summary_res_blast.txt")

summary = open("summary_res_blast.txt", "w")
					
print("Début comparaison")
for plante in dico_contig:
	liste_blast=[]
	print("Début de la verification des peptides de "+plante)
	for el in FichList:
		if plante+"_vs" in el:
			taille=len(el)
			if el[taille-6]==".":
				if el[taille-5]=="b":
					if el[taille-4]=="l":						
						if el[taille-3]=="a":
							if el[taille-2]=="s" :
								if el[taille-1]=="t":
									liste_blast.append(el)	
	
	print("Voici la liste des blast concernés pour la vérification")	
	print(liste_blast)
	
	for f_blast in liste_blast:
		print("Chargement de "+f_blast)

		try:
			f = open(f_blast, "r")
			f_lignes = f.readlines()
			f.close()
		except:
			print("Le fichier n'a pu être chargé correctement. Vérifiez que le fichier existe bien et relancez votre programme.")
			sys.exit(0) ### Stoppe simplement l'exécution du programme.

		print("Chargement fichier terminé, début de la comparaison")
		for el in dico_contig[plante]:
			if ("# Query: "+el) not in f_lignes:
				print("lui pas en commun")
				print(el)
				liste_contig_manquant.append(el)
	
		print("Fin de comparaison entre "+plante+" et "+f_blast+" début écriture résultat")
		summary.write("Vérification de "+plante+" dans le fichier "+f_blast+" listes des peptides manquant: "+"\n"+liste_contig_manquant+"\n")


		
	
	
		









summary.close()







print("fin")



