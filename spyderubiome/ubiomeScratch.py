"""
Defines the function plotTaxa, that will draw a time-series plot of Richard Sprague's
entire microbiome results for a particular taxa.

For example,
>>>plotTaxa("Firmicutes")

draws a pretty chart of my Firmicutes results


"""

__author__ = 'sprague'

import matplotlib.pyplot as plt
import ubiome

class UbiomeApp():
    def __init__(self):
        may14 = ubiome.UbiomeSample("../Data/sprague data/Sprague-ubiomeMay2014.json",name="May 2014")
        jun14 = ubiome.UbiomeSample("../Data/sprague data/sprague-uBiomeJun2014.json",name="Jun 2014")
        oct14 = ubiome.UbiomeSample("../Data/sprague data/Sprague-uBiomeOct2014.json",name="Oct 2014")
        jan = ubiome.UbiomeSample("../Data/sprague data/sprague-ubiomeJan2015x.json",name="Jan 2015")
        feb = ubiome.UbiomeSample("../Data/sprague data/sprague-ubiomeFeb2015.json",name="Feb 2015")

        aprA = ubiome.UbiomeSample("../Data/sprague data/sprague-ubiome-150421.json",name = "Apr21")
        aprB = ubiome.UbiomeSample("../Data/sprague data/sprague-ubiome-150428.json",name = "Apr28")
        jul = ubiome.UbiomeSample("../Data/sprague data/Sprague-ubiomeJul2015.json",name = "Jun 2015")

        aprJulc = aprB.compareWith(jul)
        aprJulu = aprB.unique(jul)

        aprJulu.sort("count_norm")

        self.x = ubiome.UbiomeMultiSample(may14)
        self.x.merge(jun14)
        self.x.merge(oct14)
        self.x.merge(jan)
        self.x.merge(feb)
        self.x.merge(aprA)
        self.x.merge(aprB)
        self.x.merge(jul)




def nthElementEquals(searchList, searchTaxname):
    """returns the element of searchList that matches searchTaxname

    :param searchList: list
    :param searchTaxname: string
    :return: int
    """
    for i, taxa in enumerate(x.fullTaxList):
        taxname, taxrank = taxa
        if taxname == searchTaxname:
            return i
    return None

newApp = UbiomeApp()
x = newApp.x

import datetime

def plotTaxa(taxName):
    dates = [datetime.date(2014,5,20), datetime.date(2014,6,7), datetime.date(2014,10,20), datetime.date(2015,1,15), datetime.date(2015,2,15), datetime.date(2015,4,21), datetime.date(2015,4,28),datetime.date(2015,6,30)]
    cCounts = [int(sample[nthElementEquals(x.fullTaxList,taxName)])/10000 for i,sample in enumerate(x.samples)]
    plt.plot_date(dates,cCounts,'-')
    plt.ylabel("Percent of sample")
    plt.title(taxName)
    plt.show()


plotTaxa("Methanobrevibacter smithii")

