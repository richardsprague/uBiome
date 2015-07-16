
### uBiomeCompare.py
### lets you analyze your uBiome sample
###

__author__ = 'sprague'

import json
import csv





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

    def showContents(self):
        print("length=",len(self.sampleList))
        print("taxlist\n",self.taxranklist())

    def taxranklist(self, rank="species"):
        """ returns a list of all organisms in this sample that are species.
        """
        if self.taxRankList: # already computed, so don't recompute
            return self.taxRankList
        for organism in self.sampleList:
            self.taxRankList = self.taxRankList + [organism["tax_name"]]
        return self.taxRankList


    def countNormOf(self, taxName):
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


    def addCountsToList(self,organismList):
        """

        :rtype : list
        :param organismList: a  list of organism tax_names
        :param sample: a well-formed uBiome JSON-formatted sample
        :return: a list of dictionaries that includes the tax_name for the sample, plus its count_norm
        """
        if organismList == []:
            return []
        else:
            return [{"tax_name":organismList[0],"count_norm":self.countNormOf(organismList[0])}] +  self.addCountsToList(organismList[1:])

    def unique(self,sample2):
        """
        returns all organisms that are unique to sample 1
        :type sample2: object
        :param sample2:
        :return:
        """
        uniqueSet = set(self.taxranklist()) - set(sample2.taxranklist())
        listWithCounts = ubiomeAddCountsToList(list(uniqueSet),self.sampleList)
        returnSample=ubiomeDiffSample(listWithCounts)
        
        return returnSample

    def compareWith(self,sample2):
        """ returns a list of the difference between self and sample2
        """
        allOrganisms = set(self.taxranklist())+set(sample2.taxranklist())
        allOrganismsWithCounts = self.addCountsToList((allOrganisms))

    def writeCSV(self,filename):
        with open(filename,'w',newline='') as csvFile:
            print("Writing to",filename)
            ubiomeWriter = csv.DictWriter(csvFile,dialect='excel',fieldnames=self.sampleList[0].keys())
            ubiomeWriter.writeheader()
            for organism in self.sampleList:
                ubiomeWriter.writerow(organism)


class ubiomeDiffSample(ubiomeSample):
    def __init__(self,sampleList):
        self.sampleList = sampleList
        self.taxRankList = []



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
        unique=esample.unique(msample)
        print("len esample.unique",len(unique.sampleList))
        unique.writeCSV("esample.csv")



if __name__=="__main__":
    print("run uBiomeCompare.py")
    myApp = ubiomeApp()
    myApp.run()
else:
    print("uBiomeCompare loaded as a module")

