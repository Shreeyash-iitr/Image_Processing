from scipy.spatial import distance as dist
import sys
sys.path.insert(0, '/home/shreeyash/PycharmProjects/untitled/Pokedex')
from zernikemoments import ZernikeMoments
import numpy
import argparse
import pickle
import cv2
import imutils


class Searcher:
    def __init__(self,index):
        self.index = index

    def search(self, queryfeatures):
        results = {}
        for (k,features) in self.index.items():
            d = dist.euclidean(queryfeatures, features)
            results[k] = d
        results = sorted([(v,k) for (k,v) in results.items()])
        return results

ap = argparse.ArgumentParser()
ap.add_argument("-","--index",required=True)
ap.add_argument("-q","--query",required=True, help="path to cropped query image")

args = vars(ap.parse_args())

with open(args["index"],'rb') as f:
    index = f.read()
index = pickle.loads(index)

image = cv2.imread(args["query"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = imutils.resize(image, width =64) #ques- why 64 and not 56?
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,7)
outline = numpy.zeros(image.shape, dtype='uint8')
_, cnts, _= cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key= cv2.contourArea, reverse=True)[0]
cv2.drawContours(outline, [cnts], -1, 255, -1)

desc = ZernikeMoments(21)
queryfeatures = desc.describe(outline)
searcher = Searcher(index)
result = searcher.search(queryfeatures)
print("That pokemon is : %s"% result[0][1].upper())
cv2.imshow('image', image)
cv2.waitKey()

#python CODE.py --index index.cpickle --query cropped.png
#That pokemon is : MAROWAK


