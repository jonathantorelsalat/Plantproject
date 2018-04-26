##Traduire des seq ADN en seq peptidique
#input: fichier .fa
#Dictionnaire des codons

dico_codon={}
dico_codon['F']=['UUU','UUC']
dico_codon['L']=['UUA','UUG','CUU','CUC','CUA','CUG']
dico_codon['I']=['AUU','AUC','AUA']
dico_codon['M']=['AUG']
dico_codon['V']=['GUU','GUC','GUA','GUG']
dico_codon['S']=['UCU','UCC','UCA','UCG','AGU','AGC']
dico_codon['P']=['CCU','CCC','CCA','CCG']
dico_codon['T']=['ACU','ACC','ACA','ACG']
dico_codon['A']=['GCU','GCC','GCA','GCG']
dico_codon['Y']=['UAU','UAC']
dico_codon['Stop']=['UAA','UAG','UGA']
dico_codon['H']=['CAU','CAC']
dico_codon['G']=['CAA','CAG']
dico_codon['N']=['AAU','AAC']
dico_codon['K']=['AAA','AAG']
dico_codon['D']=['GAU','GAC']
dico_codon['E']=['GAA','GAG']
dico_codon['C']=['UGU','UGC']
dico_codon['W']=['UGG']
dico_codon['R']=['CGU','CGC','CGA','AGA','AGG']
dico_codon['G']=['GGU','GGC','GGA','GGG']




l_fichiers=[]
l_lines=[]

dico={}  #dico contenant toutes les infos de chaque contigs/peptides traduits


print("Début du script")

nb_fichier=input("Combien de fichiers à traduire ?")

sens_trad=input("Dans quel sens voulez-vous les traduire ? (f for forward , r for reverse, fr for both)")

if sens_trad in ['f','r','fr']:
	print("vous avez choisit",sens_trad)
else:
	print(sens_trad,"n'est pas un bon choix")
	sys.exit(0) ### Stoppe simplement l'exécution du programme.

print("Entrez les noms de fichiers à traduire (sans le .fa)")

for i in range(1,int(nb_fichier)+1):
	
	l_fichiers.append(input("Fichier "+str(i)+":"))

print("Voici la liste des fichiers à traduire",l_fichiers)



print("Chargeons les fichiers")
#sleep(10)


for i in l_fichiers:	
	dico_raw={}
	
	print("Chargement du fichier"+i+".fa")
	
	try:
		f = open(i+".fa", "r")
		dico_raw[i] = f.readlines()
		f.close()
	except:
		print("Le fichier n'a pu être chargé correctement. Vérifiez que le fichier existe 				bien et relancez votre programme.")
		sys.exit(0) ### Stoppe simplement l'exécution du programme.
		
	f_inter=[] #fichier de transition servant a supprimer les lignes vides 
	for lines in dico_raw[i]:
		if lines!="":
			if lines !="\n":
				f_inter.append(lines)
	dico_raw[i]=f_inter	# On réecrit le dico sans lignes vides
	
	f_inter=[] #seq inter pour enlever saut de ligne intempestifs au milieu d'une sequence
	new_seq=False #boleen qui permettra de coller les seq en cas de saut de ligne sauvage
	for lines in dico_raw[i]:
		if lines[0]==">": #si premier élément est un >
			new_seq=True   #début d'un nouveau codon
			f_inter.append(lines)
			
		if lines[0]!=">":
			if new_seq==False:
				f_inter[len(f_inter)-1]=f_inter[len(f_inter)-1]+lines#coller la ligne avec la precedente
				
			if new_seq==True: #si début d'une seq
				new_seq=False
				f_inter.append(lines)
				
				
	dico_raw[i]=f_inter	# On réecrit le dico sans sauts de lignes dans les seq


	print("Fichier chargé, début de la transcription")
	
	for plante in dico_raw: #pour chaque plante du dico contenant les lignes brutes
			
		dico[plante]={}
		for el in dico_raw[plante]: #pour chaque contig de chaque plante
			el=el.replace("\n","") #on enleve les sauts de lignes
			
			if el[0]==">": #si la ligne commence par un >
				
				el1=el[1:] #on le suppr
				dico[plante][el1]={} # et on définit le nom du contig comme clé
					
				
				
			else: #si pas de > (donc une sequence)
				
				rev="" #liste renversée
				rev_int="" #list reverse inter
				for lettre in el: #changement de brin
					if lettre=='a'or lettre=='A':
						rev_int=rev_int+"T"
					if lettre=='c'or lettre=='C':
						rev_int=rev_int+"G"
					if lettre=='g'or lettre=='G':
						rev_int=rev_int+"C"
					if lettre=='t' or lettre=='T':
						rev_int=rev_int+"A"
				for lettre in reversed(rev_int):
					rev=rev+lettre
				
					
				el=el.replace("T","U") #on transcrit
				rev=rev.replace("T","U")
				
								
				dico[plante][el1]["trans"]=el #et on stocke la sequence
				dico[plante][el1]["len"]=len(el) #ainsi que sa taille
				dico[plante][el1]["reverse"]=rev


print("Fin de la transcription de toutes les données et début de la traduction")

for plante in dico: #pour chaque plantes dans le dico
	print ("Début de la traduction de "+plante)
	for el in dico[plante]: #pour chaque contig de plante
		seq=dico[plante][el]["trans"]  #on définit la seq ADN
		max_len=0
		orf_max_len=""
		cdna_max_seq=[]
		if sens_trad=="f":
			seq=dico[plante][el]["trans"]  #on définit la seq ADN
			liste_orf_f=['f1','f2','f3']   #ADN orf 1 /2 /3
			liste_orf_f_trad=['f1_trad','f2_trad','f3_trad'] # ARN orf 1/2/3
			liste_cdna_f=['f1_cdna','f2_cdna','f3_cdna'] # max cdna orf 1/2/3
			liste_len_cdna=['f1_len_cdna','f2_len_cdna','f3_len_cdna'] #taille cdna orf 1/2/3
		if sens_trad=="r":
			seq=dico[plante][el]["reverse"]  #on définit la seq ADN
			liste_orf_f=['r1','r2','r3']   #ADN orf 1 /2 /3
			liste_orf_f_trad=['r1_trad','r2_trad','r3_trad'] # ARN orf 1/2/3
			liste_cdna_f=['r1_cdna','r2_cdna','r3_cdna'] # max cdna orf 1/2/3
			liste_len_cdna=['r1_len_cdna','r2_len_cdna','r3_len_cdna'] #taille cdna orf 1/2/3
		
		
		if sens_trad=='f' or sens_trad=='r':	
			for i in range(0,3): #pour chaque orf forward
				#on définit les clé du dico
				dico[plante][el][liste_orf_f[i]]=[]  #ADN orf 1/2/3
				dico[plante][el][liste_orf_f_trad[i]]=[] # ARN orf 1/2/3
				dico[plante][el][liste_cdna_f[i]]=[] #Cdna orf 1/2/3
				j=i
				while i<(len(seq)-2): 		#on parcourt la séquence
					dico[plante][el][liste_orf_f[j]].append(seq[i]+seq[i+1]+seq[i+2]) # on crée les triplets (codons)
					i=i+3
				for triplet in dico[plante][el][liste_orf_f[j]]: #on check les triplet et on attribue un nom d'ac aminé
					for codon in dico_codon:
						if triplet in dico_codon[codon]:
							dico[plante][el][liste_orf_f_trad[j]].append(codon) #on crée la seq peptidique
				
				seq_inter=[] #seq en cours
				seq_inter2=[]  #seq intermediaire qui stock la plus grd seq
				cdna_ouvert=False #booleen si dans seq codante ou pas
				cpt_cdna=0   #compteur pour traiter dernier codon
				
				for cdna in dico[plante][el][liste_orf_f_trad[j]]:
					
					cpt_cdna=cpt_cdna+1					
						
					if cdna =='Stop': #on rencontre un codon stop
						
						if cdna_ouvert == True: #si seq était ouverte
							
							cdna_ouvert = False
							
							
							if len(seq_inter)>len(seq_inter2): #si la new sequence est plus grde que sequence codante precedente
								seq_inter2=seq_inter #on remplace
								
						seq_inter=[] #on refresh	
								
								
					else: #si ni stop
						if cdna == 'M': #on rencontre un codon start
							if cdna_ouvert == False:  #si pas dans une sequence codante
								cdna_ouvert=True  #on commence la seq
						if cdna_ouvert == True: #et qu'on est dans une sequence codante
							seq_inter.append(cdna) #on add le codon
					if cpt_cdna==len(dico[plante][el][liste_orf_f_trad[j]]): #dernier codon
						
						
						if len(seq_inter)>len(seq_inter2): #si la new sequence est plus grde que sequence codante precedente
							seq_inter2=seq_inter #on remplace
					dico[plante][el][liste_cdna_f[j]]=seq_inter2
				dico[plante][el][liste_len_cdna[j]]=len(seq_inter2)
				if len(seq_inter2)> max_len:
					max_len=len(seq_inter2)
					orf_max_len=liste_orf_f[j]
					cdna_max_seq=seq_inter2
					
							
		if sens_trad=='fr':	##SI REVERSE ET FORWARD
			for n in range(0,2):
				if n ==0:
					seq=dico[plante][el]["trans"]  #on définit la seq ADN
					liste_orf_f=['f1','f2','f3']   #ADN orf 1 /2 /3
					liste_orf_f_trad=['f1_trad','f2_trad','f3_trad'] # ARN orf 1/2/3
					liste_cdna_f=['f1_cdna','f2_cdna','f3_cdna'] # max cdna orf 1/2/3
					liste_len_cdna=['f1_len_cdna','f2_len_cdna','f3_len_cdna'] #taille cdna orf 1/2/3
				if n ==1:
					seq=dico[plante][el]["reverse"]  #on définit la seq ADN
					liste_orf_f=['r1','r2','r3']   #ADN orf 1 /2 /3
					liste_orf_f_trad=['r1_trad','r2_trad','r3_trad'] # ARN orf 1/2/3
					liste_cdna_f=['r1_cdna','r2_cdna','r3_cdna'] # max cdna orf 1/2/3
					liste_len_cdna=['r1_len_cdna','r2_len_cdna','r3_len_cdna'] #taille cdna orf 1/2/3
									
				for i in range(0,3): #pour chaque orf forward
					#on définit les clé du dico
					dico[plante][el][liste_orf_f[i]]=[]  #ADN orf 1/2/3
					dico[plante][el][liste_orf_f_trad[i]]=[] # ARN orf 1/2/3
					dico[plante][el][liste_cdna_f[i]]=[] #Cdna orf 1/2/3
					j=i
					while i<(len(seq)-2): 		#on parcourt la séquence
						dico[plante][el][liste_orf_f[j]].append(seq[i]+seq[i+1]+seq[i+2]) # on crée les triplets (codons)
						i=i+3
					for triplet in dico[plante][el][liste_orf_f[j]]: #on check les triplet et on attribue un nom d'ac aminé
						for codon in dico_codon:
							if triplet in dico_codon[codon]:
								dico[plante][el][liste_orf_f_trad[j]].append(codon) #on crée la seq peptidique
					
					seq_inter=[] #seq en cours
					seq_inter2=[]  #seq intermediaire qui stock la plus grd seq
					cdna_ouvert=False #booleen si dans seq codante ou pas
					cpt_cdna=0   #compteur pour traiter dernier codon
					
					for cdna in dico[plante][el][liste_orf_f_trad[j]]:
						
						cpt_cdna=cpt_cdna+1					
							
						if cdna =='Stop': #on rencontre un codon stop
							
							if cdna_ouvert == True: #si seq était ouverte
								
								cdna_ouvert = False
								
								
								if len(seq_inter)>len(seq_inter2): #si la new sequence est plus grde que sequence codante precedente
									seq_inter2=seq_inter #on remplace
									
							seq_inter=[] #on refresh	
									
									
						else: #si ni stop
							if cdna == 'M': #on rencontre un codon start
								if cdna_ouvert == False:  #si pas dans une sequence codante
									cdna_ouvert=True  #on commence la seq
							if cdna_ouvert == True: #et qu'on est dans une sequence codante
								seq_inter.append(cdna) #on add le codon
						if cpt_cdna==len(dico[plante][el][liste_orf_f_trad[j]]): #dernier codon
							
							
							if len(seq_inter)>len(seq_inter2): #si la new sequence est plus grde que sequence codante precedente
								seq_inter2=seq_inter #on remplace
						dico[plante][el][liste_cdna_f[j]]=seq_inter2
					dico[plante][el][liste_len_cdna[j]]=len(seq_inter2)
					if len(seq_inter2)> max_len:
						max_len=len(seq_inter2)
						orf_max_len=liste_orf_f[j]
						cdna_max_seq=seq_inter2
					
					
					
					
					
					
		dico[plante][el]["cdna_max_seq"]=cdna_max_seq	
		dico[plante][el]['cdna_max_len']=max_len
		dico[plante][el]['orf_max_len']=orf_max_len #indique quel sens/orf contient le plus grand cnda (f1 / f2 / f3)
		
print("Début d'écriture des fichiers de sortie")


for plante in dico:
	print("Début d'écriture du summary de "+plante)
	res=open(plante+"_cdna_summary.txt","w")
	res.write("Peptide name"+"\t"+"taille contig"+"\t"+"taille peptide"+"\t"+"max length cDNA"+"\t"+"sens"+sens_trad+"\t"+"% de recouvrement"+"\n")
	
	
	for contig in dico[plante]:
		res.write(contig+"\t"+str(dico[plante][contig]["len"])+"\t"+str(int(dico[plante][contig]["len"]/3))+"\t"+str(dico[plante][contig]["cdna_max_len"])+"\t"+dico[plante][contig]["orf_max_len"]+"\t"+str(100*dico[plante][contig]["cdna_max_len"]/int(dico[plante][contig]["len"]/3))+"\n")
	res.close()
	
	print("Début d'écriture des cDNA de "+plante)
	res2=open(plante+"_cdna.txt","w")
	
	for contig in dico[plante]:
					
		res2.write(contig+"\n"+str(''.join(dico[plante][contig]["cdna_max_seq"]))+"\n")
	res2.close()
	
	
print ("End of translate.")
	

## TEST AFFICHAGE CDNA DE TAILLE MAX

#for plante in dico:
#	for contig in dico[plante]:
#		print(contig,dico[plante][contig]["cdna_max_len"],dico[plante][contig]["orf_max_len"])
#		print(dico[plante][contig]["cdna_max_seq"])
