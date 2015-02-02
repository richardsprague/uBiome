# Find Unique Items in Two Samples #

Be sure your working directory is set to the location of your data.

If your samples are kept in the following CSV files:
```
may
jun
```
Then run the following function in R:
```
uBiome_sample_unique(may,jun,"species")
```
and R will return a list of ways in which the two samples are unique.
 For example:
 ```
   missing.count_norm            missing.tax_name
1              74140        Bacteroides plebeius
2               9914      Parabacteroides merdae
3               8295 Bifidobacterium tsurumiense
4               6906        Roseburia sp. 11SE38
5               4452 Bacteroidales bacterium ph8
6               3977       Bilophila wadsworthia
>
 ``` 
