<div class="container-fluid main-container">

<div id="header">

#### *Richard Sprague <span class="citation">@sprague</span>* {.author}

#### *February 25, 2015* {.date}

</div>

The gut biome is interesting enough, but bacteria colonize just about
every part of the body, so recently I’ve been studying [my uBiome mouth
test
results](http://blog.richardsprague.com/2014/10/whats-in-my-microbiome.html).
The simple [GitHub RuBiome
utilities](https://github.com/richardsprague/uBiome) I use for analyzing
my gut will work for that too, so here’s a short example of how I did
it:

First I [loaded my uBiome
data](http://blog.richardsprague.com/2015/01/how-to-analyze-ubiome-sample-in-excel.html)
into two variables, one for each sample: June 2014 (`junMouth`) and the
other from October 2014 (`OctMouth`), after [a visit to my
dentist](http://blog.richardsprague.com/2014/10/why-review-dentists.html).

Let’s see which species are new in the later (October) sample:

``` {.r}
octToJunChange <- uBiome_sample_unique(OctMouth,junMouth)
```

    ##   count                        missing.tax_name
    ## 1  3640                  bacterium NLAE-zl-P562
    ## 2  2725                 Streptococcus sanguinis
    ## 3  2075               Capnocytophaga gingivalis
    ## 4  1969 Peptostreptococcus sp. oral clone FG014
    ## 5  1618                 Granulicatella adiacens

One of those species, *Streptococcus sanguinis* looks interesting.
[Wikipedia](https://en.wikipedia.org/wiki/Streptococcus_sanguinis) says
this:

> *S. sanguinis* is a normal inhabitant of the healthy human mouth where
> it is particularly found in dental plaque, where it modifies the
> environment to make it less hospitable for other strains of
> Streptococcus that cause cavities, such as Streptococcus mutans.

No cavities? Nice! More good news: this quick check confirms that I
don’t have any *S. mutans*:

``` {.r}
OctMouth[grepl("Streptococcus",OctMouth$tax_name),]$tax_name
```

    ## [1] Streptococcus                      Streptococcus pseudopneumoniae    
    ## [3] Streptococcus sanguinis            Streptococcus constellatus        
    ## [5] Streptococcus anginosus group      Streptococcus sp. oral clone GM006
    ## [7] Streptococcus thermophilus         Streptococcus oralis              
    ## [9] Streptococcus gordonii            
    ## 250 Levels: [Eubacterium] sulci ... Veillonellaceae

Then I look at the species that disappeared (went extinct) between the
two samples:

``` {.r}
junToOctChange <- uBiome_sample_unique(junMouth,OctMouth)
```

    ##   count                        missing.tax_name
    ## 1  6034                Capnocytophaga granulosa
    ## 2  4153 Peptostreptococcus sp. oral clone FL008
    ## 3  3375         Prevotella sp. oral clone ID019
    ## 4  2691                   Streptococcus rubneri
    ## 5  1571                       Prevotella buccae

Anything in the genus
[*Capnocytophaga*](https://en.wikipedia.org/wiki/Capnocytophaga) is an
opportunistic pathogen, so I say good riddance. Usually they’re fine,
but if your immune system dips they can turn bad.

[Streptococcus rubneri](http://www.ncbi.nlm.nih.gov/pubmed/23749274) was
discovered a couple years ago, so little is known about it.

[Prevotella buccae](https://microbewiki.kenyon.edu/index.php/Prevotella)
is more interesting. It seems to be implicated in periodontal disease
(yuk!) but that genus is involved too in breaking down proteins and
carbohydrates.

Hard to say what’s really going on. Meanwhile, here are the biggest
changes (increase) since the first sample:

``` {.r}
junToOctCompare <- uBiome_compare_samples(junMouth,OctMouth)
```

    ##                                  tax_name count_change
    ## 64         Streptococcus pseudopneumoniae        62007
    ## 68         Veillonella sp. oral taxon 780         8065
    ## 41                       Neisseria oralis         4693
    ## 2  Abiotrophia sp. oral clone P4PA_155 P1         2308
    ## 28                 Granulicatella elegans         1987

Whoah! That first one, *Streptococcus pseudopneumoniae*, looks nasty!
[Wikipedia](https://en.wikipedia.org/wiki/Streptococcus_pseudopneumoniae)
says it may cause pneumonia, though a recent medical journal says more
hopefully that it [“treads the fine line between commensal and
pathogen”](http://www.cmnewsletter.com/article/S0196-4399(14)00027-0/abstract?cc=y)

which is a scientific gobbleygook way of saying nobody has a clue. All
the more reason to keep testing, submitting, and getting more data. I
just sent two more kits to uBiome, and will let you know more as soon as
I get back the results.

</div>
