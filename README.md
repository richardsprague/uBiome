
---
# Getting Started#
Log into your [uBiome account](http://beta.ubiome.com)
Select "Raw Taxonomy", like this:

![Alt text](/images/ScreenShot Raw Taxonomy.jpg)

you'll see a screen that looks something like this:

![Alt text](/images/uBiome json screenshot.png)

From inside your browser, Save As.. to a filename ending with '.json'.

From R, set the working directory to the location where you saved the uBiome file.

Now do this:

    install.packages("jsonlite")
    library("jsonlite")
    convert_json_files_to_csv()

Now every .json file in that directory will be converted to .csv

# uBiome Tools
useful tools for manipulating uBiome information

Some of the scripts require you to first [install R] (http://www.r-project.org).

[__uBiome_compare_samples__](./compareSamples.md)
Given two samples, output all the differences, including the difference in count_norm

[__uBiome_sample_unique__](findUnique.md)
Given two samples, output which rows are the uniquely found in one but not the other.

[__convert_json_files_to_csv__](convertJsonToCSV.md)
