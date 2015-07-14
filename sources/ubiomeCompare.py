
### uBiomeCompare.py
### lets you analyze your uBiome sample
###

__author__ = 'sprague'

import json



class ubiomeSample():
    """ class representation of a well-formed uBiome sample

    """
    def __init__(self,fname):
        """ initialize with a string representing the path to a uBiome-formatted JSON file
        """
        jsonFile = open(fname)
        sourceJson = json.load(jsonFile)
        self.sampleList = sourceJson["ubiome_bacteriacounts"]
        self.taxRankList = []

    def taxranklist(self, rank="species"):
        """ returns a list of all organisms in this sample that are species.
        """
        if self.taxRankList: # already computed, so don't recompute
            return self.taxRankList
        for organism in self.sampleList:
            self.taxRankList = self.taxRankList + [organism["tax_name"]]


    def ubiomeCountNormOf(self, taxName):
        """
        returns the count_norm of a given taxName for a sample
        :param taxName: string representation of a uBiome tax_name
        :param sample:
        :return:
        """
        for organism in self.sampleList:
            if organism["tax_name"]==taxName:
                assert isinstance(organism, dict)
                return int(organism["count_norm"])


    def ubiomeAddCountsToList(self,organismList):
        """

        :rtype : list
        :param organismList: a  list of organism tax_names
        :param sample: a well-formed uBiome JSON-formatted sample
        :return: a list of dictionaries that includes the tax_name for the sample, plus its count_norm
        """
        if organismList == []:
            return []
        else:
            return [{"tax_name":organismList[0],"count_norm":self.ubiomeCountNormOf(organismList[0])}] +  self.ubiomeAddCountsToList(organismList[1:])

    def ubiomeUnique(self,sample2):
        """
        returns all organisms that are unique to sample 1
        :type sample2: object
        :param sample2:
        :return:
        """
        uniqueSet = set(self.taxranklist()) - set(sample2.taxranklist())
        listWithCounts = ubiomeAddCountsToList(list(uniqueSet),self.sampleList)
        return listWithCounts

# def taxRankOf(ubiomeJSONCounts,rank="species"):
#     for i in ubiomeJSONCounts:
#         if i["tax_rank"] == rank:
#                 print(i["tax_name"])
#     return 25

def taxRankList(ubiomeJSON,rank="species"):
    """
    Returns a list of all tax_names in uBiomeJSONCounts
    :param ubiomeJSON: JSON-formatted list of dictionaries, each of which contains info about an organism
    :param rank: botanical rank (i.e. kingdom, phylum, class, order, family, genus, species)
    :return: list
    """
    if ubiomeJSON==[]:
        return []
    else:
        return [ubiomeJSON[0]["tax_name"]] + taxRankList(ubiomeJSON[1:],rank)



def ubiomeCountNormOf(taxName, sample):
    """
    returns the count_norm of a given taxName for a sample
    :param taxName: string representation of a uBiome tax_name
    :param sample:
    :return:
    """
    for organism in sample:
        if organism["tax_name"]==taxName:
            assert isinstance(organism, dict)
            return int(organism["count_norm"])


def ubiomeAddCountsToList(organismList,sample):
    """

    :rtype : list
    :param organismList: a  list of organism tax_names
    :param sample: a well-formed uBiome JSON-formatted sample
    :return: a list of dictionaries that includes the tax_name for the sample, plus its count_norm
    """
    if organismList == []:
        return []
    else:
        return [{"tax_name":organismList[0],"count_norm":ubiomeCountNormOf(organismList[0],sample)}] +  ubiomeAddCountsToList(organismList[1:],sample)


def ubiomeCompareSamples(sample1,sample2):
    """
    returns a list of organisms from sample1 and the relative amounts compared to sample2. Positive numbers indicate more in sample 1
    :param sample1: list from the uBiome JSON-formatted sample
    :param sample2: list from the uBiome JSON-formatted sample
    :return:
    """
    return "still working on implementation"

def ubiomeUnique(sample1,sample2):
    """
    returns all organisms that are unique to sample 1
    :param sample1:
    :param sample2:
    :return:
    """
    uniqueSet = set(sample1) - set(sample2)
    listWithCounts = ubiomeAddCountsToList(list(uniqueSet),sample1)
    return listWithCounts

# sample JSON object pulled straight from uBiome

#jsonFile = open("../Data/others/elijah.json")
#elijah=json.load(jsonFile)



## Python sets:
## a - b
## a | b
## a & b
## a ^ b  # in a or b but not both

class ubiomeApp():
    def run(self):
        msample = ubiomeSample("../Data/sprague data/Sprague-ubiomeMay2014.json")
        m = msample.sampleList
        esample = ubiomeSample("../Data/others/elijah.json")
        e = esample.sampleList
        el=taxRankList(e)
        ml=taxRankList(m)
        elSet=set(el)
        mlSet = set(ml)
        c=ubiomeAddCountsToList(el,e)

#elcounts=ubiomeAddCountsToList(el,el)


        commonElijahMay = mlSet & elSet
        uniqueElijah = elSet - mlSet

        ecounts= ubiomeAddCountsToList(list(uniqueElijah),e)
        esample.taxranklist()
        print("ecounts=",len(ecounts))
        print("countnorm=",esample.ubiomeCountNormOf("Bacteria"))
  #      esample.ubiomeUnique(msample)

#ml=taxRankList(mayy)
#mlSet = set(ml)

if __name__=="__main__":
    print("run uBiomeCompare.py")
    myApp = ubiomeApp()
    myApp.run()
else:
    print("uBiomeCompare loaded as a module")

#ubiomeUnique(e,m)