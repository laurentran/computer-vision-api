
import os, pprint


class ImageLibrary():
    """
    Helper class 
    """
    def __init__(self, 
                 positive_images_loc=None,
                 negative_images_loc=None, 
                 ):

        self.allData = {}

        for image in os.listdir(positive_images_loc):
            self.allData[positive_images_loc+"/"+image] = {'positive':True}

        for image in os.listdir(negative_images_loc):
            self.allData[negative_images_loc+"/"+image] = {'positive':False}

    def printDataSet(self, dataSet=None):
        """
        Print Data set
        """
        if dataSet == None:
            dataSet = self.allData

        pprint.pprint(dataSet)


    def populateStatInfo(self):
        """
        Example of how to populate more data
        """
        for image in self.allData.keys():
            self.allData[image]['stat'] = os.lstat(image)

    def getAllPositiveDataKeys(self):

        tmpData = []
        for image in self.allData.keys():
            if self.allData[image]['positive']:
                tmpData.append(image)

        return tmpData

    def getAllNegativeDataKeys(self):

        tmpData = []
        for image in self.allData.keys():
            if not self.allData[image]['positive']:
                tmpData.append(image)

        return tmpData

if __name__ == '__main__':

    positive_images_loc = "../positive_images"
    negative_images_loc = "../negative_images"

    myImageLib = ImageLibrary(positive_images_loc, negative_images_loc)

    myImageLib.populateStatInfo()
    
    myImageLib.printDataSet()

