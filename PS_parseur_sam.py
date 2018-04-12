import re 

li=['0952','3917']

for i in li:
	print("chargement dataSRR169"+i+"_trimmed_almult_forparseur.sam")
	### On vérifie que l'ouverture du fichier se passe correctement :
	try:
		f = open("/store/EQUIPES/PBI/Jonathan/custom_parseur/MS/SRR169"+i+"_trimmed_almult_forparseur.sam", "r")
		lines = f.readlines()
		f.close()
	except:
		print("Le fichier n'a pu être chargé correctement. Vérifiez que le fichier existe bien et relancez votre programme.")
		sys.exit(0) ### Stoppe simplement l'exécution du programme.

	Al_un = open("/store/EQUIPES/PBI/Jonathan/custom_parseur/MS/SRR169"+i+"_align_un.txt", "w")
	Al_mult = open("/store/EQUIPES/PBI/Jonathan/custom_parseur/MS/SRR169"+i+"_align_mult.txt", "w")

	n=None
	cpt=1
	num_align=None

	for ligne in lines: 				#parcourt des lignes
	
		liste=ligne.split('\t') 		#on stocke la ligne dans une liste

		if n==liste[2]:				#si on reste sur un contig deja listé
			cpt=cpt +1  			#on up le compteur
		else: 					# sinon
			if n is None:			#si contig non defini (1ere ligne)
				n=liste[2]		 #on définit le contig
				num_align=liste[11]
			else: 				#si changement de contig

			




				if num_align=='NH:i:1': 	#si alignement unique
					Al_un.write(n+"\t"+str(cpt)+"\n")	 #on écrit 
					Al_mult.write(n+"\t"+str(cpt)+"\n")	 #on écrit
				else: 			#si alignement multiple 
					if num_align=='NH:i:0': 	#si alignement inexistant (absent dans SAM)
						Al_un.write(n+"\t"+str(0)+"\n")	 #on écrit 	
						Al_mult.write(n+"\t"+str(0)+"\n")	 #on écrit
					else: #si alignement multiple
						Al_mult.write(n+"\t"+str(cpt)+"\n")	 #on écrit

				n=liste[2]
				cpt=1
				print(liste[2])
				num_align=liste[11]

	
	
		
	
	if liste[11]=='NH:i:1': 	#dernier contig si alignement unique
		Al_un.write(liste[2]+"\t"+str(cpt)+"\n")


	Al_un.close()
	Al_mult.close()

	

