
# Getting Started#
uBiome provides access to the raw data from your sample.
The tools here will make it easier to understand the information
in those data files.

Before you begin, you must:

1. Download your raw data from uBiome, in the form of JSON files (see below)
2. [Install R](http://www.r-project.org), the (free) open source
 scientific programming language
---
# Get the Data from uBiome #



Log into your [uBiome account](http://beta.ubiome.com)
Select "Raw Taxonomy", like this:

![Alt text](/images/ScreenShot Raw Taxonomy.jpg)

you'll see a screen that looks something like this:

![Alt text](/images/uBiome json screenshot.png)

From inside your browser, Save As.. to a filename ending with '.json'.

Launch R, then set the working directory to the location
where you saved the uBiome JSON file. For example:

```
setwd("/ubiome")  # enter the path for your directory here
```
(Note that everything after the '#' is a comment and doesn't need to be typed.

Now you are ready to begin using the tools. To load them, type:
```
source("uBiomeConvertToCSV.R") # or another filename, depending on which tool.
```

# uBiome Tools
useful tools for manipulating uBiome information


[__uBiome_compare_samples__](./compareSamples.md)
Given two samples, output all the differences, including the difference in count_norm

[__uBiome_sample_unique__](findUnique.md)
Given two samples, output which rows are the uniquely found in one but not the other.

[__convert_json_files_to_csv__](convertJsonToCSV.md) Convert all JSON files in a
directory to CSV files, suitable for reading in Excel or use with the other functions here.
