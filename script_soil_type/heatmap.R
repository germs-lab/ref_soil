library(gplots) 
library(Heatplus)
library(vegan)
library(RColorBrewer)

data=as.matrix(read.table("soil_type_count.txt",header=TRUE,sep="\t",row.names=1))
colnames(data)[8] <- "Sand,Rock,Ice"
dataREL2=data*0
for(i in 1:dim(data)[1]){
	dataREL2[i,]=data[i,]/sum(data[i,])
}
sub <- dataREL2[rowSums(dataREL2)!="NaN",]
scaleyellowred <- colorRampPalette(c("lightyellow", "red"), space = "rgb")(100)
data.dist <- vegdist(sub,method="bray")
row.clus <- hclust(data.dist,"aver")
data.dist.g <- vegdist(t(sub), method = "bray")
col.clus <- hclust(data.dist.g, "aver")
pdf("supplementary_figure4_soil_type_heatmap.pdf",width=8,height=8)
heatmap.2(as.matrix(sub),Rowv = as.dendrogram(row.clus), Colv = as.dendrogram(col.clus), col = scaleyellowred,margins = c(11, 5), trace = "none", density.info = "none", lhei = c(2, 10),labRow="",key.xlab="Relative Abundance")
dev.off()