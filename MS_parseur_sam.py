import re 
print("checking liste")

###li_init=['25','26','27','31','32','33']

li=['25','26','27','31','32','33']


print("liste acquise")


for i in li:

	print("Chargement fichier SRR18238"+i)

	try:
		f = open("SRR18238"+i+"_trimmed_star_almult_forparseur.sam", "r")
		lines = f.readlines()
		f.close()
	except:
		print("Le fichier n'a pu être chargé correctement. Vérifiez que le fichier existe 				bien et relancez votre programme.")
		sys.exit(0) ### Stoppe simplement l'exécution du programme.



	
	### On vérifie que l'ouverture du fichier se passe correctement :
	
	print("Début comptage du fichier")	
	
	Al_un = open("SRR18238"+i+"_align_un.txt", "w")
	Al_mult = open("SRR18238"+i+"_align_mult.txt", "w")

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
				print("nhi1 deja connu"+str(cpt_un))   				
			else:
				cpt_mult=cpt_mult+1  			#on up le compteur
				print("nhimult deja connu"+str(cpt_un))
		else: 					# sinon
			if n is None:			#si contig non defini (1ere ligne)
				n=liste[2]		 #on définit le contig
				num_align=liste[11]
				if num_align=='NH:i:1':
					cpt_un=cpt_un+1
					cpt_mult=cpt_mult+1
					print("nhi1 non connu"+str(cpt_un))   				
				else:
					cpt_mult=cpt_mult+1
					print("nhimult non connu"+str(cpt_un))
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
					print("nhi1 nouveaucontig")   				
				else:
					cpt_mult=cpt_mult+1  			#on up le compteur
					print("nhimult nouveau contig")
				
				
				
				
		print(liste[11])

	
	
		
	print("fin du fichier on écrit result")
	Al_un.write(n+"\t"+str(cpt_un)+"\n")	 #on écrit 
	Al_mult.write(n+"\t"+str(cpt_mult)+"\n")	 #on écrit


	Al_un.close()
	Al_mult.close()
	

