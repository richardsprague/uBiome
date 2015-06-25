# An analysis script to kickstart working with your uBiome files
# Load this first to get all the data I currently know about.

# Before beginning: set your working directory to the location where your data is

# Load universal header file
source("../uBiome.R")

# read Richard Sprague gut data
may<-read.csv("sprague data/sprague-uBiomeMay2014.csv")
jun<-read.csv("sprague data/sprague-uBiomeJun2014.csv")
oct<-read.csv("sprague data/sprague-uBiomeOct2014.csv")
jan<-read.csv("sprague data/sprague-ubiomeJan2015x.csv")
feb<-read.csv("sprague data/sprague-ubiomeFeb2015.csv")

# compare my trip to Belize
# positive numbers mean more because i went to Belize
janFeb<-uBiome_compare_samples(jan,feb)
janFebGenus<-uBiome_compare_samples(jan,feb,"genus")
#write.csv(janFebGenus,"belizeTripGenus.csv")

newAfterBelizeGenus<-uBiome_sample_unique(feb,jan,"genus")  # found in feb, but not jan
extinctAfterBelize<-uBiome_sample_unique(jan,feb,"genus")

# get Richard Sprague mouth data for two months
junMouth<-read.csv("junMouth.csv")
OctMouth<-read.csv("OctMouth.csv")


#data for June has weird headings, so this section makes the names consistent
junNames<-names(jun)
junNamesS<-strsplit(junNames,"\\.")
names(junNamesS)<-NULL
junNamesT<-sapply(junNamesS,function(x){x[2]})
names(jun)<-junNamesT

rm(junNames)
rm(junNamesT)
rm(junNamesS)

# read other people's data

# /Users/sprague/OneDrive/Projects/Programming/uBiome/Data/
elijah<-read.csv("elijah.csv")
sally<-read.csv("sallyjamesSept2014.csv")
user1<-read.csv("user1-uBiomeOct.csv")


# os<-OctMouth[OctMouth$tax_rank=="species",]
# os<-os[order(os$tax_name),]
# head(os$tax_name)
# junMouth[grepl("Streptococcus",junMouth$tax_name),]$tax_name
# 
# jun[grepl("prausnitzii",jun$tax_name),]$count_norm
# 
# jan[grepl("aceto",jan$tax_name),]$count_norm
# 
