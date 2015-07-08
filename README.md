
# Getting Started#
uBiome provides access to the raw data from your sample.
The tools here will make it easier to understand the information
in those data files.

Before you begin, you will need:

1. An account with http://ubiome.com
2. Access to [R](http://www.r-project.org), the (free) open source
 scientific programming language, available for Mac/Windows/Unix.

---

# Next #

Check out the [Beginners Guide](./docs/BeginnersGuide.md)  (better yet, check the [Hackers Guide](./docs/HackersGuide/hackersGuide-md/hackersGuide.md))

Download the [RuBiome source files](./sources) and copy to the directory of your choice.

Fire up R and run the program [uBiome.R](uBiome.R) to set the correct working directories.


---

# Bacteria to watch

I use [this Excel file](https://github.com/richardsprague/uBiome/blob/master/Data/sprague%20ubiome%20analysis%202015.xlsx) to analyze each of my samples.

Divided into "good" vs. "bad", though that is probably an imprecise distinction. Nevertheless it may be useful to watch these particular organisms when you are starting.

# uBiome Tools
useful tools for manipulating uBiome information


[__uBiome_compare_samples__](./compareSamples.md)
Given two samples, output all the differences, including the difference in count_norm

[__uBiome_sample_unique__](findUnique.md)
Given two samples, output which rows are the uniquely found in one but not the other.

[__convert_json_files_to_csv__](convertJsonToCSV.md) Convert all JSON files in a
directory to CSV files, suitable for reading in Excel or use with the other functions here.
