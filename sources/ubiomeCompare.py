__author__ = 'sprague'

import json

# sample JSON object pulled straight from uBiome

jsonFile = open("../Data/others/elijah.json")
elijah=json.load(jsonFile)

with open("../Data/sprague data/Sprague-ubiomeMay2014.json") as jFile2:
    may = json.load(jFile2)

m = may["ubiome_bacteriacounts"]

e = elijah["ubiome_bacteriacounts"]

def taxRankOf(ubiomeJSONCounts=e,rank="species"):
    for i in ubiomeJSONCounts:
        if i["tax_rank"] == rank:
                print(i["tax_name"])
    return 25

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



## Python sets:
## a - b
## a | b
## a & b
## a ^ b  # in a or b but not both

el=taxRankList(e)
ml=taxRankList(m)
elSet=set(el)
mlSet = set(ml)
c=ubiomeAddCountsToList(el,e)

#elcounts=ubiomeAddCountsToList(el,el)


commonElijahMay = mlSet & elSet
uniqueElijah = elSet - mlSet

ecounts= ubiomeAddCountsToList(list(uniqueElijah),e)

#ml=taxRankList(mayy)
#mlSet = set(ml)

if __name__=="__main__":
    print("run uBiomeCompare.py")
else:
    print("uBiomeCompare loaded as a module")

#ubiomeUnique(e,m)