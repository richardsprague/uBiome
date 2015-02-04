## Example file showing how I use these utilities
##
setwd("../Data") # set your working directory to the place where you keep your data.

source("../sources/uBiomeCompare.R")
may<-read.csv("sprague-uBiomeMay2014.csv")
jun<-read.csv("sprague-uBiomeJun2014.csv")

#data for June has weird headings, so this section makes the names consistent
junNames<-names(jun)
junNamesS<-strsplit(junNames,"\\.")
names(junNamesS)<-NULL
junNamesT<-sapply(junNamesS,function(x){x[2]})
names(jun)<-junNamesT

oct<-read.csv("sprague-uBiomeOct2014.csv")
names(jun)
names(oct)


# returns a dataframe showing how the two samples compare
# 
uBiome_compare_samples <- function(sample1,sample2,rank="species"){
        
        #pull out just the rows made of the tax rank of interest (usually "species")
        s1Rank <-sample1[sample1$tax_rank==rank,]
        s2Rank <-sample2[sample2$tax_rank==rank,]
        
        # which tax_rank (e.g. species) from sample 1 are still found in sample 2?
        s1_still_found<-which(s1Rank$tax_name %in% s2Rank$tax_name)
        s2_still_found<-which(s2Rank$tax_name %in% s1Rank$tax_name)
        
        s1_table<-s1Rank[s1_still_found,] # full table of all sample 1 species still found in sample 2
        s2_table<-s2Rank[s2_still_found,]
        #handy: note that rownames(s2_table) maintains references to the original row names from sample2
        
        s1_tA<-s1_table[order(s1_table$tax_name),] #alphabetized version of s1_table
        s2_tA<-s2_table[order(s2_table$tax_name),] #alphabetized version of s2_table
        
        change_s1_s2 <-data.frame(s1_tA$tax_name,s2_tA$count_norm - s1_tA$count_norm)
        
        change_s1_s2
}


maySpecies <-may[may$tax_rank=="species",]
octSpecies <-oct[oct$tax_rank=="species",]

#sort
msA<-maySpecies[order(maySpecies$tax_name),] #May species table alphabetized 
osA<-octSpecies[order(octSpecies$tax_name),] #Oct species table alphabetized 


# maySpecies %in% octSpecies
mayOctMatch<-match(maySpecies$tax_name,octSpecies$tax_name)

ms<-which(maySpecies$tax_name %in% octSpecies$tax_name)


os<-which(octSpecies$tax_name %in% maySpecies$tax_name)
maySpeciesstillInOct <-maySpecies$tax_name[ms] # names of all May species still found in Oct sample
mayt<-maySpecies[ms,] # full table of all May species still found in Oct
octt<-octSpecies[os,]
#important: note that rownnames(octt) maintains references to the original row names from oct
sapply(rownames(mayt),as.integer) #to convert to a vector, instead of char

maytA<-mayt[order(mayt$tax_name),] #alphabetized version of mayt
octtA<-octt[order(octt$tax_name),] #alphabetized version of octt

species_change_May_Oct <-data.frame(maytA$tax_name,octtA$count_norm - maytA$count_norm)

#write.csv(species_change_May_Oct,file="Sprague-uBiome change May-Oct.csv")
