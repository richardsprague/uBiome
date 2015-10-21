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



    def test_unique(self):
        v = may14.unique(jun14)
        self.assertEqual(len(v.sampleList), 384)
    def test_compare(self):
        v = may14.compareWith(jun14)
        self.assertEqual(len(v.sampleList),139)

    def test_sampleFullTaxListLength(self):
        self.assertEqual(len(self.sampleMultiSample.fullTaxList), 1039)
    def test_sampleTaxList(self):
        firstTenVals = [['tax_name', 'tax_rank'], ['Bacteria', 'superkingdom'], ['Firmicutes', 'phylum'], ['Clostridia', 'class'], ['Clostridiales', 'order'], ['Bacteroidetes/Chlorobi group', 'superphylum'], ['Bacteroidetes', 'phylum'], ['Bacteroidia', 'class'], ['Bacteroidales', 'order'], ['Ruminococcaceae', 'family']]
        self.assertEqual(firstTenVals,[self.sampleMultiSample.fullTaxList[i] for i in range(10)])

    def test_latestSample(self):
        latestSample = ['Aug 2015', 1000000, 642701, 622361, 622244, 184516, 184508, 184204, 184136, 307556]
        self.assertEqual(latestSample,[self.sampleMultiSample.samples[len(self.sampleMultiSample.samples)-1][i] for i in range(10)])



    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
