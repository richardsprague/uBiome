
.myuBiomePath = "OneDrive/Projects/"
# set the root path for either Mac or Windows
if(Sys.info()["sysname"]=="Darwin") kRootPath=paste0("~/",.myuBiomePath) else kRootPath=paste0(paste0("c:/Users/",Sys.info()["login"]),"/",.myuBiomePath)

setwd(paste0(kRootPath,"uBiome"))
setwd("Data/sprague data")

allSprague <- read.csv("sprague-all-thru-nov03.csv")


allGenus <- allSprague[allSprague$tax_rank=="genus",]
allPhylum<-allSprague[allSprague$tax_rank=="phylum",]
allSpecies<-allSprague[allSprague$tax_rank=="species",]
allSamples <- allGenus[,-(1:2)] 
require("vegan",quietly=TRUE)
dV <- sapply(allSamples,fisher.alpha)
names(dV)<-c(as.Date("2014-5-23"),as.Date("2014-6-10"),as.Date("2014-10-23"),as.Date("2015-1-15"),as.Date("2015-2-20"),
             as.Date("2015-4-20"),
             as.Date("2015-4-27"),
             as.Date("2015-6-30"),
             as.Date("2015-8-15"),
             as.Date("2015-9-15"),
             as.Date("2015-9-16"),
             as.Date("2015-10-6"),
             as.Date("2015-10-13"),
             as.Date("2015-10-18"),
             as.Date("2015-10-19"),
             as.Date("2015-10-20"),
             as.Date("2015-10-21"),
             as.Date("2015-10-26"),
             as.Date("2015-11-03")
             
)

g<-names(allSprague)
dPDates<-as.Date(names(dV))

myDiversity<-read.csv("alpha.csv")

# both are calculated at Genus
# dV is Fisher Alpha diversity
# dG is Inv Simpson diversity

#genus diversity
# dG <- sapply(allGenus[,-(1:2)],diversity,index="invsimpson")  
# plot(dG~dPDates,main="Genus Diversity",xlab="",ylab="Inv Simpson Diversity",xaxt="n")
# axis(1,at=dPDates,labels=g[-(1:2)],las=2)
# abline(lm(dG~dPDates),col="red")

alphaSimpson<-data.frame(as.Date(dPDates),dV*10,dG*10,myDiversity$uBiome)
names(alphaSimpson)<-c("Date","FisherAlpha","InvSimpson","uBiome")
#alphaSimpson$Date<-as.Date(dPDates)
sinceOct <- alphaSimpson[alphaSimpson$Date>as.Date("2015-10-01"),]

divPlot <-ggplot(sinceOct, aes(Date)) +
        ylab("Diversity") + 
        theme(legend.title=element_blank()) +
        geom_line(aes(y=uBiome, colour = "uBiome"),size=2) +
        geom_line(aes(y=InvSimpson, colour = "invSimpson")) +
        geom_line(aes(y=FisherAlpha, colour = "FisherAlpha")) +
                  geom_point(aes(y=uBiome)) +
        geom_point(aes(y=FisherAlpha)) +
        geom_point(aes(y=InvSimpson))
 
divPlot

divPlotAll <-ggplot(alphaSimpson, aes(Date)) +
        ylab("Diversity") + 
        theme(legend.title=element_blank()) +
        geom_line(aes(y=uBiome, colour = "uBiome"),size=2) +
        geom_line(aes(y=InvSimpson, colour = "invSimpson")) +
        geom_line(aes(y=FisherAlpha, colour = "FisherAlpha")) +
        geom_point(aes(y=uBiome)) +
        geom_point(aes(y=FisherAlpha)) +
        geom_point(aes(y=InvSimpson))

divPlotAll


# 
# qplot(as.Date(row.names(sinceOct)),sinceOct$dG, geom="line")
# 
# 
# qpoints(sinceOct$dV~as.Date(row.names(sinceOct)))

