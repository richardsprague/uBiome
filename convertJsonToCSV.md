#Convert JSON files to CSV#

From R, set the working directory to the location where you saved the uBiome file.

Now do this:
```
install.packages("jsonlite")
library("jsonlite")
convert_json_files_to_csv()
```
Now every .json file in that directory will be converted to .csv
