##Preparation script

setwd(dir = '/media/jonathan.torel-salat/LaCie/RNA-seq/rstudio/DESEQ2')
library(readr)
library(dplyr)
library(DESeq2)

##Chargement données

CA_data=read.csv(file = 'CA_counts.csv')
GM_data=read.csv(file = 'GM_counts.csv')
MS_data=read.csv(file = 'MS_counts.csv')
MT_data=read.csv(file = 'MT_counts.csv')
PS_data=read.csv(file = 'PS_counts.csv')
PV_data=read.csv(file = 'PV_counts.csv')


##CICER ARIETINUM ####################################################################

##Mise en forme données

countdata_CA=CA_data
row.names(countdata_CA)=CA_data[,1]
countdata_CA=countdata_CA[,2:7]

#ctest(nodule)=1ere colonne

countdata_CA_10DPI_alun=countdata_CA[,c(1,5)]
countdata_CA_10DPI_almult=countdata_CA[,c(2,6)]
countdata_CA_28DPI_alun=countdata_CA[,c(3,5)]
countdata_CA_28DPI_almult=countdata_CA[,c(4,6)]

coldata_CA_10DPI_alun=data.frame(condition=c('root','nodule'),row.names=names(countdata_CA_10DPI_alun))
coldata_CA_10DPI_almult=data.frame(condition=c('root','nodule'),row.names=names(countdata_CA_10DPI_almult))
coldata_CA_28DPI_alun=data.frame(condition=c('root','nodule'),row.names=names(countdata_CA_28DPI_alun))
coldata_CA_28DPI_almult=data.frame(condition=c('root','nodule'),row.names=names(countdata_CA_28DPI_almult))


##Debut DESEQ2

dds_CA_10DPI_alun=DESeqDataSetFromMatrix(countData=countdata_CA_10DPI_alun,colData = coldata_CA_10DPI_alun,design=~condition)
deseq_CA_10DPI_alun=DESeq(dds_CA_10DPI_alun)
res_CA_10DPI_alun=results(deseq_CA_10DPI_alun,name="condition_root_vs_nodule")
#resLFC_CA_10DPI_alun=lfcShrink(res_CA_10DPI_alun,coef="condition_root_vs_nodule")

dds_CA_10DPI_almult=DESeqDataSetFromMatrix(countData=countdata_CA_10DPI_almult,colData = coldata_CA_10DPI_almult,design=~condition)
deseq_CA_10DPI_almult=DESeq(dds_CA_10DPI_almult)
res_CA_10DPI_almult=results(deseq_CA_10DPI_almult,name="condition_root_vs_nodule")

dds_CA_28DPI_alun=DESeqDataSetFromMatrix(countData=countdata_CA_28DPI_alun,colData = coldata_CA_28DPI_alun,design=~condition)
deseq_CA_28DPI_alun=DESeq(dds_CA_28DPI_alun)
res_CA_28DPI_alun=results(deseq_CA_28DPI_alun,name="condition_root_vs_nodule")
#resLFC_CA_10DPI_alun=lfcShrink(res_CA_10DPI_alun,coef="condition_root_vs_nodule")

dds_CA_28DPI_almult=DESeqDataSetFromMatrix(countData=countdata_CA_28DPI_almult,colData = coldata_CA_28DPI_almult,design=~condition)
deseq_CA_28DPI_almult=DESeq(dds_CA_28DPI_almult)
res_CA_28DPI_almult=results(deseq_CA_28DPI_almult,name="condition_root_vs_nodule")



##RESULTS


sum(res_CA_10DPI_alun$pvalue<0.01,na.rm=TRUE) # 0
plotMA(res_CA_10DPI_alun)

sum(res_CA_10DPI_almult$pvalue<0.01,na.rm=TRUE) ## 0
plotMA(res_CA_10DPI_almult)

sum(res_CA_28DPI_alun$pvalue<0.01,na.rm=TRUE) # 34
plotMA(res_CA_28DPI_alun)

sum(res_CA_28DPI_almult$pvalue<0.01,na.rm=TRUE) ## 34
plotMA(res_CA_28DPI_almult)


##LISTE GENE/CONTIG SIGNIFICATIFS

resSig_CA_10DPI_alun=subset(res_CA_10DPI_alun,pvalue<0.1)
resSig_CA_10DPI_almult=subset(res_CA_10DPI_almult,pvalue<0.1)
resSig_CA_28DPI_alun=subset(res_CA_28DPI_alun,pvalue<0.01)
resSig_CA_28DPI_almult=subset(res_CA_28DPI_almult,pvalue<00.1)

write.csv(resSig_CA_28DPI_alun,file="resSig_CA_28DPI_alun.csv")
write.csv(resSig_CA_28DPI_alun,file="resSig_CA_28DPI_almult.csv")
##MEDICAGO SATIVA ################################################################################################################################################



##Mise en forme données

countdata_MS=MS_data
row.names(countdata_MS)=MS_data[,1]
countdata_MS=countdata_MS[,2:13]

#ctest(nodule)=1ere colonne

countdata_MS_alun=countdata_MS[,c(1,3,5,7,9,11)]
countdata_MS_almult=countdata_MS[,c(2,4,6,8,10,12)]


#for (i in 1:112626) {  ##checking supplémentaire print les contig avec ggrosse diff entre nbr de read
 # a=(countdata_MS_alun[i,2]-countdata_MS_alun[i,3])
  #if (a > 500)  print(i+countdata_MS_alun[i,])
  
  #if (a<(-500)) print(i+countdata_MS_alun[i,])
#}
    


coldata_MS_alun=data.frame(condition=c('root','root','root','nodule','nodule','nodule'),row.names=names(countdata_MS_alun))
coldata_MS_almult=data.frame(condition=c('root','root','root','nodule','nodule','nodule'),row.names=names(countdata_MS_almult))



##Debut DESEQ2

dds_MS_alun=DESeqDataSetFromMatrix(countData=countdata_MS_alun,colData = coldata_MS_alun,design=~condition)
deseq_MS_alun=DESeq(dds_MS_alun)
res_MS_alun=results(deseq_MS_alun,name="condition_root_vs_nodule")
#resLFC_CA_10DPI_alun=lfcShrink(res_CA_10DPI_alun,coef="condition_root_vs_nodule")

dds_MS_almult=DESeqDataSetFromMatrix(countData=countdata_MS_almult,colData = coldata_MS_almult,design=~condition)
deseq_MS_almult=DESeq(dds_MS_almult)
res_MS_almult=results(deseq_MS_almult,name="condition_root_vs_nodule")

##RESULTS


sum(res_MS_alun$padj<0.01,na.rm=TRUE) # 17920
plotMA(res_MS_alun)

sum(res_MS_almult$padj<0.01,na.rm=TRUE) ## 39575
plotMA(res_MS_almult)


##LISTE GENE/CONTIG SIGNIFICATIFS

resSig_MS_alun=subset(res_MS_alun,padj<0.01)
resSig_MS_almult=subset(res_MS_almult,padj<0.01)

write.csv(resSig_MS_alun,file="resSig_MS_alun.csv")
write.csv(resSig_MS_almult,file="resSig_MS_almult.csv")
##### GLYCINE MAX ################################################################################################################################################################


##Mise en forme données

countdata_GM=GM_data
row.names(countdata_GM)=GM_data[,1]
countdata_GM=countdata_GM[,2:5]

#ctest(nodule)=derniere colonne

countdata_GM_alun=countdata_GM[,c(1,2)]
countdata_GM_almult=countdata_GM[,c(3,4)]

coldata_GM_alun=data.frame(condition=c('root','nodule'),row.names=names(countdata_GM_alun))
coldata_GM_almult=data.frame(condition=c('root','nodule'),row.names=names(countdata_GM_almult))

##Debut DESEQ2

dds_GM_alun=DESeqDataSetFromMatrix(countData=countdata_GM_alun,colData = coldata_GM_alun,design=~condition)
deseq_GM_alun=DESeq(dds_GM_alun)
res_GM_alun=results(deseq_GM_alun,name="condition_root_vs_nodule")
#resLFC_CA_10DPI_alun=lfcShrink(res_CA_10DPI_alun,coef="condition_root_vs_nodule")

dds_GM_almult=DESeqDataSetFromMatrix(countData=countdata_GM_almult,colData = coldata_GM_almult,design=~condition)
deseq_GM_almult=DESeq(dds_GM_almult)
res_GM_almult=results(deseq_GM_almult,name="condition_root_vs_nodule")

##RESULTS


sum(res_GM_alun$pvalue<0.01,na.rm=TRUE) # 516
plotMA(res_GM_alun)

sum(res_GM_almult$pvalue<0.01,na.rm=TRUE) ## 655
plotMA(res_GM_almult)


##LISTE GENE/CONTIG SIGNIFICATIFS

resSig_GM_alun=subset(res_GM_alun,pvalue<0.01) ## TOUJOURS CHECKER SI LOGFC EST DANS LE BON SENS !!!!!!!!!!!!!!!!!!!!!!!!!
resSig_GM_almult=subset(res_GM_almult,pvalue<0.01)

write.csv(resSig_GM_alun,file="resSig_GM_alun.csv")
write.csv(resSig_GM_almult,file="resSig_GM_almult.csv")

##### PHAESOLUS VULGARIS ################################################################################################################################################################


##Mise en forme données

countdata_PV=PV_data
row.names(countdata_PV)=PV_data[,1]
countdata_PV=countdata_PV[,2:5]

#ctest(nodule)=derniere colonne

countdata_PV_alun=countdata_PV[,c(2,1)]
countdata_PV_almult=countdata_PV[,c(4,3)]

coldata_PV_alun=data.frame(condition=c('nodule','root'),row.names=names(countdata_PV_alun))
coldata_PV_almult=data.frame(condition=c('nodule','root'),row.names=names(countdata_PV_almult))

##Debut DESEQ2

dds_PV_alun=DESeqDataSetFromMatrix(countData=countdata_PV_alun,colData = coldata_PV_alun,design=~condition)
deseq_PV_alun=DESeq(dds_PV_alun)
res_PV_alun=results(deseq_PV_alun,name="condition_root_vs_nodule")
#resLFC_CA_10DPI_alun=lfcShrink(res_CA_10DPI_alun,coef="condition_root_vs_nodule")

dds_PV_almult=DESeqDataSetFromMatrix(countData=countdata_PV_almult,colData = coldata_PV_almult,design=~condition)
deseq_PV_almult=DESeq(dds_PV_almult)
res_PV_almult=results(deseq_PV_almult,name="condition_root_vs_nodule")

##RESULTS


sum(res_PV_alun$pvalue<0.01,na.rm=TRUE) # 403
plotMA(res_PV_alun)

sum(res_PV_almult$pvalue<0.01,na.rm=TRUE) ## 411
plotMA(res_PV_almult)


##LISTE GENE/CONTIG SIGNIFICATIFS

resSig_PV_alun=subset(res_PV_alun,pvalue<0.01) ## TOUJOURS CHECKER SI LOGFC EST DANS LE BON SENS !!!!!!!!!!!!!!!!!!!!!!!!!
resSig_PV_almult=subset(res_PV_almult,pvalue<0.01)



write.csv(resSig_PV_alun,file="resSig_PV_alun.csv")
write.csv(resSig_PV_almult,file="resSig_PV_almult.csv")







##### MEDICAGO TRUNCATULA ################################################################################################################################################################


##Mise en forme données

countdata_MT=MT_data
row.names(countdata_MT)=MT_data[,1]
countdata_MT=countdata_MT[,2:25]



#ctest(nodule)=derniere colonne

countdata_MT_polyA_alun=countdata_MT[,c(1:3,7:9)]
countdata_MT_ribo_alun=countdata_MT[,c(4:6,10:12)]
countdata_MT_polyA_almult=countdata_MT[,c(13:15,19:21)]
countdata_MT_ribo_almult=countdata_MT[,c(16:18,22:24)]


coldata_MT_polyA_alun=data.frame(condition=c('root','root','root','nodule','nodule','nodule'),row.names=names(countdata_MT_polyA_alun))
coldata_MT_polyA_almult=data.frame(condition=c('root','root','root','nodule','nodule','nodule'),row.names=names(countdata_MT_polyA_almult))
coldata_MT_ribo_alun=data.frame(condition=c('root','root','root','nodule','nodule','nodule'),row.names=names(countdata_MT_ribo_alun))
coldata_MT_ribo_almult=data.frame(condition=c('root','root','root','nodule','nodule','nodule'),row.names=names(countdata_MT_ribo_almult))


##Debut DESEQ2

dds_MT_polyA_alun=DESeqDataSetFromMatrix(countData=countdata_MT_polyA_alun,colData = coldata_MT_polyA_alun,design=~condition)
deseq_MT_polyA_alun=DESeq(dds_MT_polyA_alun)
res_MT_polyA_alun=results(deseq_MT_polyA_alun,name="condition_root_vs_nodule")
#resLFC_CA_10DPI_alun=lfcShrink(res_CA_10DPI_alun,coef="condition_root_vs_nodule")


dds_MT_polyA_almult=DESeqDataSetFromMatrix(countData=countdata_MT_polyA_almult,colData = coldata_MT_polyA_almult,design=~condition)
deseq_MT_polyA_almult=DESeq(dds_MT_polyA_almult)
res_MT_polyA_almult=results(deseq_MT_polyA_almult,name="condition_root_vs_nodule")
#resLFC_CA_10DPI_alun=lfcShrink(res_CA_10DPI_alun,coef="condition_root_vs_nodule")

dds_MT_ribo_alun=DESeqDataSetFromMatrix(countData=countdata_MT_ribo_alun,colData = coldata_MT_ribo_alun,design=~condition)
deseq_MT_ribo_alun=DESeq(dds_MT_ribo_alun)
res_MT_ribo_alun=results(deseq_MT_ribo_alun,name="condition_root_vs_nodule")
#resLFC_CA_10DPI_alun=lfcShrink(res_CA_10DPI_alun,coef="condition_root_vs_nodule")


dds_MT_ribo_almult=DESeqDataSetFromMatrix(countData=countdata_MT_ribo_almult,colData = coldata_MT_ribo_almult,design=~condition)
deseq_MT_ribo_almult=DESeq(dds_MT_ribo_almult)
res_MT_ribo_almult=results(deseq_MT_ribo_almult,name="condition_root_vs_nodule")
#resLFC_CA_10DPI_alun=lfcShrink(res_CA_10DPI_alun,coef="condition_root_vs_nodule")

##RESULTS


sum(res_MT_polyA_alun$padj<0.01,na.rm=TRUE) # 15228  PADJ !!!!!!!!!
plotMA(res_MT_polyA_alun)

sum(res_MT_polyA_almult$padj<0.01,na.rm=TRUE) # 16390  PADJ !!!!!!!!!
plotMA(res_MT_polyA_almult)

sum(res_MT_ribo_alun$padj<0.01,na.rm=TRUE) # 14921  PADJ !!!!!!!!!
plotMA(res_MT_ribo_alun)

sum(res_MT_ribo_almult$padj<0.01,na.rm=TRUE) # 15806  PADJ !!!!!!!!!
plotMA(res_MT_ribo_almult)


##LISTE GENE/CONTIG SIGNIFICATIFS

resSig_MT_polyA_alun=subset(res_MT_polyA_alun,padj<0.01) ## TOUJOURS CHECKER SI LOGFC EST DANS LE BON SENS !!!!!!!!!!!!!!!!!!!!!!!!!
resSig_MT_polyA_almult=subset(res_MT_polyA_almult,padj<0.01)

resSig_MT_ribo_alun=subset(res_MT_ribo_alun,padj<0.01) ## TOUJOURS CHECKER SI LOGFC EST DANS LE BON SENS !!!!!!!!!!!!!!!!!!!!!!!!!
resSig_MT_ribo_almult=subset(res_MT_ribo_almult,padj<0.01)


write.csv(resSig_MT_polyA_alun,file="resSig_MT_polyA_alun.csv")
write.csv(resSig_MT_polyA_almult,file="resSig_MT_polyA_almult.csv")

write.csv(resSig_MT_ribo_alun,file="resSig_MT_ribo_alun.csv")
write.csv(resSig_MT_ribo_almult,file="resSig_MT_ribo_almult.csv")


##### PISUM SATIVUM ################################################################################################################################################################


##Mise en forme données

countdata_PS=PS_data
row.names(countdata_PS)=PS_data[,1]
countdata_PS=countdata_PS[,2:5]

#ctest(nodule)=derniere colonne

countdata_PS_alun=countdata_PS[,c(3,1)]
countdata_PS_almult=countdata_PS[,c(4,2)]

coldata_PS_alun=data.frame(condition=c('root','nodule'),row.names=names(countdata_PS_alun))
coldata_PS_almult=data.frame(condition=c('root','nodule'),row.names=names(countdata_PS_almult))

##Debut DESEQ2

dds_PS_alun=DESeqDataSetFromMatrix(countData=countdata_PS_alun,colData = coldata_PS_alun,design=~condition)
deseq_PS_alun=DESeq(dds_PS_alun)
res_PS_alun=results(deseq_PS_alun,name="condition_root_vs_nodule")
#resLFC_CA_10DPI_alun=lfcShrink(res_CA_10DPI_alun,coef="condition_root_vs_nodule")

dds_PS_almult=DESeqDataSetFromMatrix(countData=countdata_PS_almult,colData = coldata_PS_almult,design=~condition)
deseq_PS_almult=DESeq(dds_PS_almult)
res_PS_almult=results(deseq_PS_almult,name="condition_root_vs_nodule")

##RESULTS


sum(res_PS_alun$pvalue<0.01,na.rm=TRUE) # 969
plotMA(res_PS_alun)

sum(res_PS_almult$pvalue<0.01,na.rm=TRUE) ## 1045
plotMA(res_PS_almult)


##LISTE GENE/CONTIG SIGNIFICATIFS

resSig_PS_alun=subset(res_PS_alun,pvalue<0.01) ## TOUJOURS CHECKER SI LOGFC EST DANS LE BON SENS !!!!!!!!!!!!!!!!!!!!!!!!!
resSig_PS_almult=subset(res_PS_almult,pvalue<0.01)

write.csv(resSig_PS_alun,file="resSig_PS_alun.csv")
write.csv(resSig_PS_almult,file="resSig_PS_almult.csv")



