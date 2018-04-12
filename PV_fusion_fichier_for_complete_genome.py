chrom1= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.1.fa")
chrom2= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.2.fa")
chrom3= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.3.fa")
chrom4= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.4.fa")
chrom5= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.5.fa")
chrom6= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.6.fa")
chrom7= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.7.fa")
chrom8= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.8.fa")
chrom9= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.9.fa")
chrom10= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.10.fa")
chrom11= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.11.fa")


n = 0
for line in chrom1:
    n += 1
for line in chrom2:
    n += 1


for line in chrom3:
    n += 1
for line in chrom4:
    n += 1
for line in chrom5:
    n +=1
for line in chrom6:
    n += 1
for line in chrom7:
    n += 1
for line in chrom8:
    n += 1
for line in chrom9:
    n += 1
for line in chrom10:
    n += 1
for line in chrom11:
    n += 1

print (n)

chrom1= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.1.fa")
chrom2= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.2.fa")
chrom3= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.3.fa")
chrom4= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.4.fa")
chrom5= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.5.fa")
chrom6= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.6.fa")
chrom7= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.7.fa")
chrom8= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.8.fa")
chrom9= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.9.fa")
chrom10= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.10.fa")
chrom11= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chromosome.11.fa")



contenu_1=chrom1.read()
contenu_2=chrom2.read()
contenu_3=chrom3.read()
contenu_4=chrom4.read()
contenu_5=chrom5.read()
contenu_6=chrom6.read()
contenu_7=chrom7.read()
contenu_8=chrom8.read()
contenu_9=chrom9.read()
contenu_10=chrom10.read()
contenu_11=chrom11.read()


fichier_sortie=open("Phaseolus_vulgaris.PhaVulg1_0.dna.chr.fa","w") # ouverture en écriture du fichier résultat
fichier_sortie.write(contenu_1 + contenu_2+ contenu_3+ contenu_4+ contenu_5+ contenu_6+ contenu_7+ contenu_8+ contenu_9+ contenu_10+ contenu_11)

fichier_sortie.close()

chrom= open("Phaseolus_vulgaris.PhaVulg1_0.dna.chr.fa")






m=0
for line in chrom:
    m += 1

print (m)







































