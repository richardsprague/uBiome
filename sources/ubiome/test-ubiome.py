__author__ = 'sprague'

import unittest
import ubiome

pathPrefix="./testdata/"
may14 = ubiome.UbiomeSample(pathPrefix+"Sprague-ubiomeMay2014.json",name="May 2014")
jun14 = ubiome.UbiomeSample(pathPrefix+"sprague-uBiomeJun2014.json",name="Jun 2014")
oct14 = ubiome.UbiomeSample(pathPrefix+"Sprague-uBiomeOct2014.json",name="Oct 2014")
jan = ubiome.UbiomeSample(pathPrefix+"sprague-ubiomeJan2015x.json",name="Jan 2015")
feb = ubiome.UbiomeSample(pathPrefix+"sprague-ubiomeFeb2015.json",name="Feb 2015")

aprA = ubiome.UbiomeSample(pathPrefix+"sprague-ubiome-150421.json",name = "Apr21")
aprB = ubiome.UbiomeSample(pathPrefix+"sprague-ubiome-150428.json",name = "Apr28")
jul = ubiome.UbiomeSample(pathPrefix+"Sprague-ubiomeJul2015.json",name = "Jun 2015")
aug = ubiome.UbiomeSample(pathPrefix+"Sprague-ubiome-150815.json",name = "Aug 2015")


class MyTestCase(unittest.TestCase):

    def setUp(self):
        x = ubiome.UbiomeMultiSample(may14)
        x.merge(jun14)
        x.merge(oct14)
        x.merge(jan)
        x.merge(feb)
        x.merge(aprA)
        x.merge(aprB)
        x.merge(jul)
        x.merge(aug)
        self.sampleMultiSample = x

    # TODO  fix Ubiome.UbiomeMultiSample to handle first init properly
    # def test_multiSample_init(self):
    #     newMS = ubiome.UbiomeMultiSample()
    #     newMS.merge(jun14)
    #


    def test_unique(self):
        v = may14.unique(jun14)
        self.assertEqual(len(v.sampleList), 384)
    def test_compare_with(self):
        v = may14.compareWith(jun14)
        self.assertEqual(len(v.sampleList),139)

    def test_sampleList_count_norm_is_integer(self):
        v = may14.sampleList[1]['count_norm']
        self.assertIsInstance(v,int)

    def test_addCountsToList(self):
        v = may14.addCountsToList(["Roseburia","Akkermansia"])
        self.assertEqual(v,[{'tax_name': 'Roseburia', 'count_norm': 13554}, {'tax_name': 'Akkermansia', 'count_norm': 30960}])

    def test_CountNormOf(self):
        v = may14.countNormOf("Clostridiales")
        self.assertEqual(v,594169)

    def test_taxonOf(self):
        v = may14.taxonOf("Clostridiales")
        self.assertEqual(v,{'taxon': '186802', 'count': '150137', 'tax_rank': 'order', 'avg': None, 'tax_color': None, 'tax_name': 'Clostridiales', 'parent': '186801', 'count_norm': 594169})

    def test_sampleFullTaxListLength(self):
        self.assertEqual(len(self.sampleMultiSample.fullTaxList), 1039)
    def test_sampleTaxList(self):
        firstTenVals = [['tax_name', 'tax_rank'], ['Bacteria', 'superkingdom'], ['Firmicutes', 'phylum'], ['Clostridia', 'class'], ['Clostridiales', 'order'], ['Bacteroidetes/Chlorobi group', 'superphylum'], ['Bacteroidetes', 'phylum'], ['Bacteroidia', 'class'], ['Bacteroidales', 'order'], ['Ruminococcaceae', 'family']]
        self.assertEqual(firstTenVals,[self.sampleMultiSample.fullTaxList[i] for i in range(10)])

    def test_latestSample(self):
        latestSample = ['Aug 2015', 1000000, 642701, 622361, 622244, 184516, 184508, 184204, 184136, 307556]
        self.assertEqual(latestSample,[self.sampleMultiSample.samples[len(self.sampleMultiSample.samples)-1][i] for i in range(10)])



    def test_alltaxa_isList(self):
        self.assertEqual(len(self.sampleMultiSample.alltaxa()),1039)


    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
