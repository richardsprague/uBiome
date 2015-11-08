#
# Generate a single spreadsheet of all my uBiome results (through Sept)
"""

This section is for brief in-app doc testing.

To run, type
python ubiomeCompare -c "../Data/sprague data/Sprague-ubiomeMay2014.json" "../Data/sprague data/Sprague-uBiomeJun2014.json"

>>> myApp.testUnique()
384
>>> v=myApp.testCompare()
>>> len(v.sampleList)
139
>>> testRikAll()
length of fullTaxList= 1062
[['tax_name', 'tax_rank'], ['Bacteria', 'superkingdom'], ['Firmicutes', 'phylum'], ['Clostridia', 'class'], ['Clostridiales', 'order'], ['Bacteroidetes/Chlorobi group', 'superphylum'], ['Bacteroidetes', 'phylum'], ['Bacteroidia', 'class'], ['Bacteroidales', 'order'], ['Ruminococcaceae', 'family']]
length of samples= 11
May 2014 ---> 1062
Jun 2014 ---> 1062
Oct 2014 ---> 1062
Jan 2015 ---> 1062
Feb 2015 ---> 1062
Apr21 ---> 1062
Apr28 ---> 1062
Jun 2015 ---> 1062
Aug 2015 ---> 1062
Sep 2015 ---> 1062
Sep 2015b ---> 1062
latest sample: ['Sep 2015b', 1000000, 651287, 626270, 625217, 249473, 249473, 247615, 247485, 195110]



>>> 5+5
10

"""
from __future__ import print_function
__author__ = 'sprague'

import ubiome
import sys
#import prettytable

pathPrefix="./ubiome/testdata/"
may14 = ubiome.UbiomeSample(pathPrefix+"Sprague-ubiomeMay2014.json",name="May 2014")
jun14 = ubiome.UbiomeSample(pathPrefix+"sprague-uBiomeJun2014.json",name="Jun 2014")
oct14 = ubiome.UbiomeSample(pathPrefix+"Sprague-uBiomeOct2014.json",name="Oct 2014")
s1 = ubiome.UbiomeSample(pathPrefix+"sample1.json",name="sample1")
s2 = ubiome.UbiomeSample(pathPrefix+"sample2.json",name="sample2")

v = ubiome.UbiomeMultiSample(may14)
v.merge(jun14)
v.merge(oct14)
def testRikAll():
    pathPrefix="../Data/sprague data/"
    may14 = ubiome.UbiomeSample(pathPrefix+"Sprague-ubiomeMay2014.json",name="May 2014")
    jun14 = ubiome.UbiomeSample(pathPrefix+"sprague-uBiomeJun2014.json",name="Jun 2014")
    oct14 = ubiome.UbiomeSample(pathPrefix+"Sprague-uBiomeOct2014.json",name="Oct 2014")
    jan = ubiome.UbiomeSample(pathPrefix+"sprague-ubiomeJan2015x.json",name="Jan 2015")
    feb = ubiome.UbiomeSample(pathPrefix+"sprague-ubiomeFeb2015.json",name="Feb 2015")

    aprA = ubiome.UbiomeSample(pathPrefix+"sprague-ubiome-150421.json",name = "Apr21")
    aprB = ubiome.UbiomeSample(pathPrefix+"sprague-ubiome-150428.json",name = "Apr28")
    jul = ubiome.UbiomeSample(pathPrefix+"Sprague-ubiomeJul2015.json",name = "Jun 2015")
    aug = ubiome.UbiomeSample(pathPrefix+"Sprague-ubiome-150815.json",name = "Aug 2015")
    sep15 = ubiome.UbiomeSample(pathPrefix+"sprague-ubiome-150915.json",name = "Sep 2015")
    sep15b = ubiome.UbiomeSample(pathPrefix+"sprague-ubiome-150915b.json",name = "Sep 2015b")
#    aprJulc = aprB.compareWith(jul)
 #   aprJulu = aprB.unique(jul)

 #   aprJulu.sort("count_norm")
 #   aprJuluPretty = aprJulu.prettyPrint()

    #aprJulu.writeCSV(sys.stdout)
    #aprJulu.prettyPrint()

    x = ubiome.UbiomeMultiSample(may14)
    x.merge(jun14)
    #x.merge(oct14)
    # x.merge(jan)
    # x.merge(feb)
    # x.merge(aprA)
    # x.merge(aprB)
    #x.merge(jul)
    x.merge(aug)
    #x.merge(sep15)
    # x.merge(sep15b)
    # #x.writeCSV(sys.stdout)
    x.showContents()
    #x.writeCSV("spragueResultsThruSepb.csv")

DEBUG = True


if DEBUG:
    #myApp.testUnique()
    #v = myApp.testCompare(myApp.esample,myApp.msample)
    import doctest
    myApp = ubiome.ubiomeApp( "../Data/sprague data/Sprague-ubiomeMay2014.json" , "../Data/sprague data/Sprague-uBiomeJun2014.json")
#    testRikAll()
#    doctest.testmod()
    print("all tests successful")

print("starting program now")


myApp = ubiome.ubiomeApp( "../Data/sprague data/Sprague-ubiomeMay2014.json" , "../Data/sprague data/Sprague-uBiomeJun2014.json")


#myApp.sample1.showContents()
sample1=myApp.sample1
sample2=myApp.sample2

#sample2.unique(sample1).showContents()
sample1.compareWith(sample2)

a = ubiome.UbiomeTaxa({'parent': '2', 'count': '157391', 'count_norm': 622877, 'taxon': '1239',\
        'tax_name': 'Firmicutes', 'tax_rank': 'phylum', 'tax_color': '5E6591', 'avg': None})


c = s1.unique(s2)
#c.showContents()
print("s1.unique(s2)=\n",c.prettyPrint())

d = s2.unique(s1)
print("s2.unique(s1)=\n",d.prettyPrint())
#d.showContents()

e = s1.compareWith(s2)
#e.showContents()
print("s1.compareWith(s2)\n",e.prettyPrint())
#
# uniqueTable = prettytable.PrettyTable(["Tax_Name","Tax_Rank","Count_Norm"])
# for i in aprJulu.sampleList:
#     uniqueTable.add_row([i["tax_name"],i["tax_rank"],i["count_norm"]])
#
# print(uniqueTable)


testRikAll()
