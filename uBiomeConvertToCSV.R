# converts every json file in directory to a CSV file
# please run the following before using this function:
# install.packages("jsonlite")
# library("jsonlite")
convert_json_files_to_csv <- function( directory=getwd()){
  json_files_in_directory <- list.files(directory, full.name=TRUE,pattern="[[:alnum:]].json")
  for (i in json_files_in_directory){
    json_version <- fromJSON(i)  # returns as a list, so we must convert to a data frame 
    asFrame <- do.call("rbind",lapply(json_version,as.data.frame))
    fname <-strsplit(i,split=".json")
    csvName <- paste0(fname[[1]],".csv")
    cat("converting...",i," to ",csvName,"\n")
   # write.csv(asFrame,file=csvName)
  }
}