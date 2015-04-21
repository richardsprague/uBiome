# scratch file: I use this as an interactive terminal when I'm just "playing around"
# Should only keep stuff here in a single session.
# Okay to delete anything in here after the session is finished.

uBiome_compare_samples(sally,jan)

pie(sally[sally$tax_rank=="phylum",]$count_norm/10000,labels=sally[sally$tax_rank=="phylum",]$tax_name,col=rainbow(5))
barplot(sally[sally$tax_rank=="phylum",]$count_norm/10000,names.arg=sally[sally$tax_rank=="phylum",]$tax_name,col=rainbow(5))


sally[sally$tax_rank=="phylum",]
jan[jan$tax_rank=="phylum",]

janFeb<-uBiome_compare_samples(jan,feb)


samples<-c(may, jun, oct, jan)
sapply(samples,function(x) x[grepl("prausnitzii",x[["tax_name"]]),])
sapply(samples,function(x) x["taxon"])

jun[grepl("prausnitzii",jun[["tax_name"]]),]

oct[grepl("lact",oct[["tax_name"]]),]

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