# Header file for everything related to uBiome analysis and publishing
# You should be able to run all scripts in either Windows or Mac
# You should be able to restart R, from a clean environment, and get the same results.
# 
# Assumptions:
# current directory is uBiome
# subdirectories include:
# Data 
# sources
# doc


.myuBiomePath = "OneDrive/Projects/"
# set the root path for either Mac or Windows
if(Sys.info()["sysname"]=="Darwin") kRootPath=paste0("~/",.myuBiomePath) else kRootPath=paste0(paste0("c:/Users/",Sys.info()["login"]),"/",.myuBiomePath)

setwd(paste0(kRootPath,"uBiome"))

# load the uBiome utilities
source("sources/uBiomeCompare.R")

# Now load all the sprague data
setwd("Data")



