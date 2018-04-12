import re 

li=['2to10DPI','11to28DPI','root']

for i in li:

	### On vérifie que l'ouverture du fichier se passe correctement :
	try:
		f = open("/store/EQUIPES/PBI/Jonathan/custom_parseur/CA/CA_"+i+"_almult_forparseur.sam", "r")
		lines = f.readlines()
		f.close()
	except:
		print("Le fichier n'a pu être chargé correctement. Vérifiez que le fichier existe bien et relancez votre programme.")
		sys.exit(0) ### Stoppe simplement l'exécution du programme.

	Al_un = open("/store/EQUIPES/PBI/Jonathan/custom_parseur/CA/CA_"+i+"_align_un.txt", "w")
	Al_mult = open("/store/EQUIPES/PBI/Jonathan/custom_parseur/CA/CA_"+i+"_align_mult.txt", "w")

	n=None
	cpt_mult=0
	cpt_un=0
	num_align=None

	for ligne in lines: 				#parcourt des lignes
	
		liste=ligne.split('\t') 		#on stocke la ligne dans une liste

		if n==liste[2]: 
			num_align=liste[11]			#si on reste sur un contig deja listé
			if num_align=='NH:i:1':
				cpt_un=cpt_un+1
				cpt_mult=cpt_mult+1
				   				
			else:
				cpt_mult=cpt_mult+1  			#on up le compteur
				
		else: 					# sinon
			if n is None:			#si contig non defini (1ere ligne)
				n=liste[2]		 #on définit le contig
				num_align=liste[11]
				if num_align=='NH:i:1':
					cpt_un=cpt_un+1
					cpt_mult=cpt_mult+1
					   				
				else:
					cpt_mult=cpt_mult+1
					
			else: 				#si changement de contig
				print("on a change de contig, on écrit les resultst"+str(cpt_un)+str(cpt_mult))
				Al_un.write(n+"\t"+str(cpt_un)+"\n")	 #on écrit 
				Al_mult.write(n+"\t"+str(cpt_mult)+"\n")	 #on écrit

				n=liste[2]
				cpt_un=0
				cpt_mult=0
				print(liste[2])
				num_align=liste[11]			#si on reste sur un contig deja listé
				if num_align=='NH:i:1':
					cpt_un=cpt_un+1
					cpt_mult=cpt_mult+1
					   				
				else:
					cpt_mult=cpt_mult+1  			#on up le compteur
					
				
				
				
				
		

	
	
		
	print("fin du fichier on écrit result")
	Al_un.write(n+"\t"+str(cpt_un)+"\n")	 #on écrit 
	Al_mult.write(n+"\t"+str(cpt_mult)+"\n")	 #on écrit


	Al_un.close()
	Al_mult.close()
	


	

