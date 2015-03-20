# An analysis script to kickstart working with your uBiome files
# Before beginning: set your working directory to the location where your data is

setwd("/Users/sprague/OneDrive/Projects/Programming/uBiome/Data")
source("../sources/uBiomeCompare.R")
junMouth<-read.csv("junMouth.csv")
OctMouth<-read.csv("OctMouth.csv")

os<-OctMouth[OctMouth$tax_rank=="species",]
os<-os[order(os$tax_name),]
head(os$tax_name)
junMouth[grepl("Streptococcus",junMouth$tax_name),]$tax_name

jun[grepl("prausnitzii",jun$tax_name),]$count_norm

jan[grepl("aceto",jan$tax_name),]$count_norm


samples<-c(may, jun, oct, jan)
sapply(samples,function(x) x[grepl("prausnitzii",x[["tax_name"]]),])
sapply(samples,function(x) x["taxon"])

jun[grepl("prausnitzii",jun[["tax_name"]]),]

janGutPhyla<-jun[jun$tax_rank=="phylum",]

janGutPhyla<-jun[jun$tax_rank=="phylum",]

counts<-head(data.frame(janGutPhyla$count_norm/10000,janGutPhyla$tax_name),4)
names(counts)<-c("count_norm","tax_name")
barplot(as.matrix(counts),col=rainbow(5),legend.text=counts$tax_name)
sapply(samples,function(x) names(x))

t <- c(1,5,7,9,10)
barplot(as.matrix(t),legend.text=t, col=c("blue","green","red","orange","pink"))
barplot(junGutPhyla$count_norm,beside=FALSE)

js<-oct[which(oct$tax_rank=="species"),]$tax_name
js[order(js)]  # an alphabetized list of the species found
js[grepl("Bifi",js)] # all species that begin with "Bifi"

lapply(list("may","jun","oct"), function(M) M[grepl(bacteriaStr,M[[tax_name]]),]$count_norm)
lapply(list("may","jun","oct"), function(M) head(M))
sapply(c("may","jun","oct"), function(M) head(M))
