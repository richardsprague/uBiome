#!/usr/bin/env python
# ### ubiome.py
### lets you analyze your uBiome sample
###
### works from the command line in either Python 2.7+ or Python 3+
### %python ubiome

from __future__ import print_function, division
__author__ = 'sprague'


import json
import csv
import sys

from argparse import ArgumentParser

#todo add __repl__ and __str__ to classes



class UbiomeTaxa():
    '''Abstracts the keys from the uBiome JSON file, making it easier to update if the format changes.
    Normally a SampleList looks like this:
    [dict1, dict2, dict3, dict4, ... dictN]

    where dict is something like this:
    {'parent': '2', 'count': '157391', 'count_norm': 622877, 'taxon': '1239',
        'tax_name': 'Firmicutes', 'tax_rank': 'phylum', 'tax_color': '5E6591', 'avg': None}

    a UbiomeTaxonomy object lets you do this:
    >>>a = UbiomeTaxa({'parent': '2', 'count': '157391', 'count_norm': 622877, 'taxon': '1239',\
        'tax_name': 'Firmicutes', 'tax_rank': 'phylum', 'tax_color': '5E6591', 'avg': None})

    >>>a.parent
    '2'
    >>>a.count_norm
    157391

    # but you're not allowed to set a new value for these attributes
    '''
    def __init__(self, ubiomeDict):
        assert(isinstance(ubiomeDict,dict))
        self._parent = ubiomeDict.get('parent',"unknown parent")
        #self._count = int(ubiomeDict.get('count')) #,"unknown count"))
        try: self._count = int(ubiomeDict.get('count'))
        except TypeError:
            self._count = "unknown count"

        try: self._count_norm = int(ubiomeDict.get('count_norm'))
        except TypeError:
            self._count_norm = "unknown count_norm"
        #self._count_norm=int(ubiomeDict.get('count_norm')) #,"unknown count_norm"))
        self._taxon = ubiomeDict.get('taxon',"unknown taxon")
        self._tax_name = ubiomeDict.get('tax_name',"unknown tax_name")
        self._tax_rank = ubiomeDict.get('tax_rank', "unknown tax_rank")
        self._avg = ubiomeDict.get('avg',"unknown avg")
        self._tax_color = ubiomeDict.get('tax_color',"unknown tax_color")

    def __repr__(self):
        return "<ubiome.ubiome.ubiomeDict: "+self.tax_name + ">"

    @property
    def dictForm(self):
        ''' returns taxa as a dict, for compatibility with the original JSON
        :return:dict
        '''
        return {"tax_name":self.tax_name,"taxon":self.taxon,"parent":self.parent,\
                "count":self.count,"count_norm":self.count_norm,"tax_rank":self.tax_rank, "avg":self.avg,"tax_color":self.tax_color}
    @property
    def parent(self):
        return self._parent
    @property
    def count(self):
            if type(self._count) == int:
                return self._count
            try:
                self._count = int(self._count)
            except ValueError:
                assert("bad value for count")
            return self._count

    @property
    def percent(self):
        ''' convert count_norm to percentage of sample

        :return: float
        '''
        return round(self.count_norm/10000,4)
    @property
    def taxon(self):
        return self._taxon
    @property
    def tax_color(self):
        return self._tax_color

    @property
    def avg(self):
        return self._avg

    @property
    def count_norm(self):
        return self._count_norm
    @property
    def tax_name(self):
        return self._tax_name
    @property
    def tax_rank(self):
        return self._tax_rank







# A sampleList is a list of dictionaries, each of which is a field from the standard uBiome JSON taxonomy
# _taxalist is the same thing, only made of elements of class UbiomeTaxa

class UbiomeSample():
    """ class representation of a well-formed uBiome sample

    """

    def __init__(self,fname=[],name=[]):
        """ initialize with a string representing the path to a uBiome-formatted JSON file
        If no name, just instantiate an object; you can read the contents later using readJSONFile or readCSVFile
        """
        if fname:
            self.readJSONfile(fname)
        else:
            #self.sampleList = []
            self._taxaList = []
        self._taxnamelist=[]
        if not name:
            self.name = fname
        else:
            self.name = name

    @property
    def taxaList(self):
        """ list of all taxa in this sample, represented as a list made of UbiomeTaxa

        :return: list
        """
        return self._taxaList


    def set_taxaList_JSON(self,sourceJson):
        allDicts = sourceJson["ubiome_bacteriacounts"] # a list of dicts
        newDicts = []
        for taxa_dict in allDicts:
            taxa_dict['count_norm']=int(taxa_dict['count_norm'])
            newDicts+=[taxa_dict]
        self._taxaList = [UbiomeTaxa(taxDict) for taxDict in newDicts ]

    def readJSONfile(self,fname):
        """ read a JSON file of the uBiome taxonomy (the one you get from downloading from the uBiome web site)
        :param fname: string
        :return:
        """
        import os
        #print("current directory = ", os.getcwd())
        jsonFile = open(fname)
        sourceJson = json.load(jsonFile)
        self.set_taxaList_JSON(sourceJson)

    def readCSVfile(self,fname):
        """
        read a CSV-formatted version of the uBiome taxonomy data.
        :param fname:
        :return:
        """
        csvFile = open(fname)
        sourceCSV = csv.DictReader(csvFile)
        header = sourceCSV.fieldnames
        for row in sourceCSV:
            self.taxaList+=[UbiomeTaxa(row)]


# todo make explicit return values
    def prettyPrint(self):
        """
        print a nice ascii table of the sample
        :return: prettytable
        """
        try:
            __import__("prettytable")
        except ImportError:
            #print("no prettyprint available")
            pTable = "Tax_Name\tTax_Rank\tCount_Norm\n"
            for tax in self.taxaList:
                pTable+=tax.tax_name+"\t"+tax.tax_rank + "\t" + str(tax.percent) + "\n"
            return pTable
        else:
            import prettytable
            uniqueTable = prettytable.PrettyTable(["Tax_Name","Tax_Rank","Count_Norm"])
            # for i in self.sampleList:
            #     uniqueTable.add_row([i["tax_name"],i["tax_rank"],i["count_norm"]])
            for i in self._taxaList:
                uniqueTable.add_row([i.tax_name,i.tax_rank,i.count_norm])
            #print(uniqueTable)
            return uniqueTable


    def sort(self,sortBy="tax_name"):
        """
        sort the sample (mutably) by sortBy (which is any of the JSON headers)
        :param str sortBy: any of the valid JSON headers
        :return: bool
        """
        #self._taxaList = sorted(self._taxaList,key=lambda k:k.__getattribute__(sortBy),reverse=True)
        self._taxaList = sorted(self._taxaList,key=lambda k:getattr(k,sortBy),reverse=True)
        return True



    def showContents(self):
        """ display the highlights of this sample (useful for debugging)

        :return:
        """
        l = len(self.taxaList)
        print("length=",l)
        i=0
        while l>10&i<10:
            print(self._taxaList[i])
            l=l-1
            i+=1


    def taxnames(self):
        """ returns a list of all organisms in this sample
        :return: list
        """
        if self._taxnamelist: # already computed, so don't recompute
            return self._taxnamelist
        for taxon in self.taxaList:
            self._taxnamelist = self._taxnamelist + [[taxon.tax_name,taxon.tax_rank]]
        return self._taxnamelist


    def diversity(self, rank="species"):
        """ uses Simpson index: http://codegolf.stackexchange.com/questions/53455/simpson-diversity-index
        :return int
        """
        l = len(self.taxaList)
        s = [(taxa.tax_name,int(taxa.count_norm)) for taxa in self.taxaList if taxa.tax_rank == rank]
        # N = sum(n for (t,n) in s )
        eT, eN =  list(zip(*s))
        d = 1 - sum([eN[i]*(eN[i]-1) for i,j in enumerate(eN)])/(sum(eN)*(sum(eN)-1))
        return d # sum(s[i%l]<>s[i/l]for i in range(l*l))/(l-1.)/l


    def taxaField(self,taxName, field):
        ''' look up taxName in _taxaList and return its attribute corresponding to 'field'
        :param taxName:
        :return:
        '''
        for taxa in self.taxaList:
            if taxa.tax_name == taxName:
                return getattr(taxa,field)



    def countNormOf(self, taxName):
        """
        returns the count_norm of a given taxName for a sample
        :param taxName: string representation of a uBiome tax_name
        :return:
        """
        return self.taxaField(taxName,'count_norm')

    def taxonOf(self,taxName):
        return self.taxaField(taxName,'dictForm')

    def unique(self,sample2):
        """
        returns all organisms that are unique to sample 1
        :type sample2: UbiomeSample
        :param sample2:
        :return: UBiomeDiffSample
        """
        uniqueList = []
        for taxon1 in self.taxaList:

            t=[tax for tax in sample2.taxaList if tax.tax_name == taxon1.tax_name]
            if not t: # not found sample2, so add to the return list
              uniqueList = [UbiomeTaxa({"tax_name":taxon1.tax_name,
               "count_norm":taxon1.count_norm,
               "tax_rank":taxon1.tax_rank,
               "taxon":taxon1.taxon
               })] + uniqueList
        return UbiomeDiffSample(uniqueList)


    def addCountsToList(self,taxonList):
        """ given a list of taxa, return another list, of dicts, that contain the same taxa and their corresponding count_norm
        :param taxonList: list # contains taxnames
        :return:
        """
        if not taxonList:
            return []
        else:
            return [{"tax_name":taxonList[0],"count_norm":self.countNormOf(taxonList[0])}] +\
                   self.addCountsToList(taxonList[1:])



    # def compareWith_old(self,sample2):
    #     """ compare the current sample with sample2 and return a uBiomeDiffSample object of the differences
    #
    #     :param sample2: UbiomeSample
    #     :return: UBiomeDiffSample
    #     """
    #
    #     taxList = []
    #     for taxon1 in self.sampleList:
    #         t=sample2.taxonOf(taxon1["tax_name"])
    #         if t: #found this taxon in sample2
    #             countDiff = int(taxon1["count_norm"]) - int(t["count_norm"])
    #             taxList = [{"tax_name":taxon1["tax_name"],\
    #                         "taxon":taxon1["taxon"],
    #                         "count_norm":countDiff,"tax_rank":taxon1["tax_rank"]}] + taxList
    #     diffSample = UbiomeDiffSample(taxList)
    #     return diffSample

    def compareWith(self,sample2):
        """ compare the current sample with sample2 and return a uBiomeDiffSample object of the differences

        :param sample2: UbiomeSample
        :return: UBiomeDiffSample
        """

        taxList = []
        for taxon1 in self.taxaList:


            if sample2.taxonOf(taxon1.tax_name): #found this taxon in sample2
                t=[tax for tax in sample2.taxaList if tax.tax_name == taxon1.tax_name][0]
                countDiff = taxon1.count_norm - t.count_norm
                taxList = [UbiomeTaxa({"tax_name":taxon1.tax_name,\
                                       "taxon":taxon1.taxon,\
                                      "count_norm":countDiff,\
                                      "tax_rank":taxon1.tax_rank})] + taxList
        diffSample = UbiomeDiffSample(taxList)
        return diffSample

    def writeCSV(self,filename):
        """ write contents of the current sample to a CSV file.  If filename=sys.stdout, just display it

        :param filename:
        :return:
        """
        sampleList = [{"tax_name":tax.tax_name,\
                            "count_norm":tax.count_norm,\
                            "percent":tax.percent,\
                            "tax_rank":tax.tax_rank,\
                            "taxon": tax.taxon
                            } for tax in self._taxaList]
        if filename==sys.stdout:
            ubiomeWriter = csv.DictWriter(sys.stdout,dialect='excel',fieldnames=sampleList[0].keys())
            #print('writing to csv')
            ubiomeWriter.writeheader()
            for organism in sampleList:
                ubiomeWriter.writerow(organism)
        else:
            with open(filename,'w') as csvFile:
                #print('writing to csv')
                ubiomeWriter = csv.DictWriter(csvFile,dialect='excel',fieldnames=sampleList[0].keys())
                ubiomeWriter.writeheader()
                for organism in sampleList:
                    ubiomeWriter.writerow(organism)


class UbiomeDiffSample(UbiomeSample):
    """ same as regular uBiome sampleList, except count_norm is a delta, not an absolute number.

    """
    def __init__(self,taxaList):
        self.sampleList = [{"tax_name":tax.tax_name,\
                            "count_norm":tax.count_norm,\
                            "percent":tax.percent,\
                            "tax_rank":tax.tax_rank,\
                            "taxon": tax.taxon
                            } for tax in taxaList]
        self._taxaList = taxaList



class ubiomeApp():
    """
    app-ified version to make testing easier.
    """
    def __init__(self,fname1,fname2):
        self.sample1 = UbiomeSample(fname1)
        self.sample2 = UbiomeSample(fname2)



    def testUnique(self):
        unique=self.sample1.unique(self.sample2)
        return len(unique.sampleList)
        #print("len esample.unique",len(unique.sampleList))
        #unique.writeCSV("sample1Unique.csv")

    def runUnique(self):
        unique=self.sample1.unique(self.sample2)
        #print("len esample.unique",len(unique.sampleList))
        unique.writeCSV(sys.stdout)

    def testCompare(self):
        compare=self.sample1.compareWith(self.sample2)
        #compare.writeCSV("sample1Compare.csv")
        return compare

    def runCompare(self):
        compare=self.sample1.compareWith(self.sample2)
        compare.writeCSV(sys.stdout)
        compare.prettyPrint()
        return compare



if __name__=="__main__":
    #print("run uBiomeCompare.py")
    #import doctest


    parser = ArgumentParser()
    parser.add_argument("-c","--compare",help="Compare sample1 with with sample2")
    parser.add_argument("-u","--unique",help="Find items in sample1 not in sample2")
    #parser.add_argument("-d","--debug",help="turn on debug mode to run tests")
    parser.add_argument("sample2",help="sample you are comparing to")
    args = parser.parse_args()

    if not(args):
        print("type ubiomecompare -h for help")
        quit()
    if args.compare:
        #print("Compare Sample 1 Args=",args.compare,args.sample2)
        a=args.compare
        b=args.sample2
    if args.unique:
        #print("Unique Sample 1",args.unique,args.sample2)
        a=args.unique
        b=args.sample2

   # a = "../Data/sprague data/Sprague-ubiomeMay2014.json"
   # b = "../Data/sprague data/Sprague-uBiomeJun2014.json"
    myApp = ubiomeApp(a,b)
    if args.unique:
        myApp.runUnique()
    if args.compare:
        myApp.runCompare()


else:
    print("uBiome loaded as a module")

