
may<-read.csv("sprague-uBiomeJun2014.csv")
may$ubiome_bacteriacounts.tax_name
may$ubiome_bacteriacounts.tax_rank=="species"
may_species <- may[may$ubiome_bacteriacounts.tax_rank=="species",]
head(may$ubiome_bacteriacounts.tax_rank)
summary(may[may$ubiome_bacteriacounts.tax_rank,])
