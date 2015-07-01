# scratch file: I use this as an interactive terminal when I'm just "playing around"
# Should only keep stuff here in a single session.
# Okay to delete anything in here after the session is finished.
.myuBiomePath = "OneDrive/Projects/"
# set the root path for either Mac or Windows
if(Sys.info()["sysname"]=="Darwin") kRootPath=paste0("~/",.myuBiomePath) else kRootPath=paste0(paste0("c:/Users/",Sys.info()["login"]),"/",.myuBiomePath)

setwd(paste0(kRootPath,"uBiome"))

# load the uBiome utilities
source("sources/uBiomeCompare.R")

# Now load all the sprague data
setwd("Data/sprague data")


a<-c("b1","b2","b3","b4")
aranks<-c("species","phylum","phylum","species")
acounts1<-c(76,77,78,79)
acounts2<-c(86,87,88,89)

rik<-data.frame(a,aranks,acounts1,acounts2)
names(rik)<-c("tax_name","tax_rank","sample_count1","sample_count2")

# count of all species in sample 2:
rik[rik$tax_rank=="species",][paste0("sample_count",2)]

rik[rik$sample_count2,]
rik$sample_count2

test<-function(...){
        for (i in list(...)){
                cat(i)
        }
}

# return just the organisms in sample data frames.
# enter as many data frames as you like
samplesCountsOf<-function(...) {
        x <- 0
        funArgs <- list(...)
        cat("length=",length(funArgs))
        if (length(funArgs)==0){
                x<-NULL
        } else if (length(funArgs)==1){
                x<-funArgs[[1]]$tax_name
        } else {
                x<-c(funArgs[[1]]$tax_name,samplesCountsOf(funArgs[[-1]]))
        }
      
    #    for(sample in list(...) ){
    #            x <- c(x,sample$count_norm)           
     #   }
       # x[order(x)]
    
    x
}


