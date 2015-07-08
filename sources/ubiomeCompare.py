__author__ = 'sprague'

import json

# sample JSON object pulled straight from uBiome

jsonFile = open("../Data/others/elijah.json")
elijah=json.load(jsonFile)

with open("../Data/sprague data/Sprague-ubiomeMay2014.json") as jFile2:
    may = json.load(jFile2)

#mayy = may["ubiome_bacteriacounts"]

#e = json.loads(elijah)

b = elijah["ubiome_bacteriacounts"]

def taxRankOf(ubiomeJSONCounts=b,rank="species"):
    for i in ubiomeJSONCounts:
        if i["tax_rank"] == rank:
                print(i["tax_name"])
    return 25

def taxRankList(ubiomeJSONCounts=b,rank="species"):
    if ubiomeJSONCounts==[]:
        return []
    else:
        return [ubiomeJSONCounts[0]["tax_name"]] + taxRankList(ubiomeJSONCounts[1:],rank)


#taxRankList(mayy)

bl=taxRankList(b)
blSet=set(bl)
#ml=taxRankList(mayy)
#mlSet = set(ml)