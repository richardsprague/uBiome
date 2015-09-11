# scratch file: I use this as an interactive terminal when I'm just "playing around"
# Should only keep stuff here in a single session.
# Okay to delete anything in here after the session is finished.
.myuBiomePath = "OneDrive/Projects/"
# set the root path for either Mac or Windows
if(Sys.info()["sysname"]=="Darwin") kRootPath=paste0("~/",.myuBiomePath) else kRootPath=paste0(paste0("c:/Users/",Sys.info()["login"]),"/",.myuBiomePath)

setwd(paste0(kRootPath,"uBiome"))

setwd("Data/sprague data")
allSprague <- read.csv("spragueResultsThruJun2015.csv")

allGenus <- allSprague[allSprague$tax_rank=="genus",]
allPhylum<-allSprague[allSprague$tax_rank=="phylum",]
allSpecies<-allSprague[allSprague$tax_rank=="species",]
require("vegan")

sapply(allSprague[,-(1:2)],fisher.alpha)
allSamples <- allGenus[,-(1:2)] # vector with just the genus vectors

require("ggplot2")
dV <- sapply(allSamples,fisher.alpha) #diversity vector
plot(dV,xaxt="n",main="Genus Diversity")
axis(1,1:8,labels=names(dV))

names(dV)<-c(as.Date("2014-5-23"),as.Date("2014-6-10"),as.Date("2014-10-23"),as.Date("2015-1-15"),as.Date("2015-2-20"),as.Date("2015-4-20"),as.Date("2015-4-27"),as.Date("2015-6-15"))
g<-names(allSprague)

dP <- sapply(allPhylum[-(1:2),-(1:2)],diversity)  #everything but the top 2 Phyla
dPDates<-as.Date(names(dV))
plot(dP~dPDates,main="Phylum Diversity (non-Major)",xlab="",ylab="diversity",xaxt="n")
axis(1,at=dPDates,labels=g[-(1:2)],las=2)

g<-names(allSprague)

# genus Fisher-Alpha diversity
dG <- sapply(allGenus[,-(1:2)],fisher.alpha)  
plot(dG~dPDates,main="Genus Diversity",xlab="",ylab="Fisher-Alpha Diversity",xaxt="n")
axis(1,at=dPDates,labels=g[-(1:2)],las=2)
abline(lm(dG~dPDates),col="red")

#genus diversity
dG <- sapply(allGenus[,-(1:2)],diversity,index="invsimpson")  
plot(dG~dPDates,main="Genus Diversity",xlab="",ylab="Inv Simpson Diversity",xaxt="n")
axis(1,at=dPDates,labels=g[-(1:2)],las=2)
abline(lm(dG~dPDates),col="red")

g<-names(allSprague)
#Phyla diversity
dP <- sapply(allPhylum[,-(1:2)],diversity,index="invsimpson")  
plot(dP~dPDates,main="Phylum Diversity",xlab="",ylab="Inv Simpson Diversity",xaxt="n")
axis(1,at=dPDates,labels=g[-(1:2)],las=2)
abline(lm(dP~dPDates),col="red")


#species diversity
dS <- sapply(allSpecies[,-(1:2)],fisher.alpha)
plot(dS~dPDates,main="Species Diversity",xlab="",ylab="Fisher-Alpha Diversity",xaxt="n")
axis(1,at=dPDates,labels=g[-(1:2)],las=2)
abline(lm(dS~dPDates),col="red")

names(dV)<-c(as.Date("2014-5-23"),as.Date("2014-6-10"),as.Date("2014-10-23"),as.Date("2015-1-15"),as.Date("2015-2-20"),as.Date("2015-4-20"),as.Date("2015-4-27"),as.Date("2015-6-15"))


plot(sapply(allSprague[-(1:3),-(1:2)],fisher.alpha),ylab="Diversity",xaxt="n",main="All Diversity")
axis(1,1:8,labels=names(dV))

