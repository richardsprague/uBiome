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


lapply(list("may","jun","oct"), function(M) M[grepl(bacteriaStr,M[[tax_name]]),]$count_norm)
lapply(list("may","jun","oct"), function(M) head(M))
sapply(c("may","jun","oct"), function(M) head(M))
