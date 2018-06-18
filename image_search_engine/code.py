import cv2                               # OpenCV image processing library
from imutils.paths import list_images    # library by adrian for simple functions like rotating image etc.
import argparse                          # lib. for argument parsing from terminal
import pickle                            # lib. for reading/writing python structures in bit array
import numpy
import os                                # used for operating system functions like getting directory path

class Searcher:
    def __init__(self,index):
        self.index = index

    def chi2_distance(self,histA, histB, eps = 1e-10):
        d = 0.5*numpy.sum([((a-b)**2)/(a+b+eps) for (a,b) in zip(histA, histB)])
        return d


    def search(self, queryfeatures):
        results = {}
        for (k, features) in self.index.items():
            d = self.chi2_distance(features, queryfeatures)
            results[k] = d
        results = sorted([(v,k) for (k,v) in results.items()])
        return results


class RGBHistogram:
    def __init__(self,bins):
        self.bins = bins

    def describe(self,image):
        hist = cv2.calcHist([image],[0,1,2],None,self.bins,[0,256,0,256,0,256])
        hist = cv2.normalize(hist, hist)
        return hist.flatten()

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required= True)
ap.add_argument("-i","--index", required=True)

args = vars(ap.parse_args())

index = pickle.loads(open(args["index"],"rb").read())
searcher = Searcher(index)
desc = RGBHistogram([8,8,8])

""" ============Run Only Once===============
for imagePath in list_images(args["dataset"]):
    k = imagePath[imagePath.rfind("/")+ 1:]
    image = cv2.imread(imagePath)
    feature = desc.describe(image)
    index[k] = feature

f = open(args["index"],"wb")
f.write(pickle.dumps(index))
f.close()
print("[INFO] done...indexeed {} images".format(len(index)))
"""

for (query, queryfeatures) in index.items():
    results = searcher.search(queryfeatures)
    path = os.path.join(args["dataset"],query)
    queryImage = cv2.imread(path)
    cv2.imshow("Query", queryImage)
    print("query : {}",format(query))
    montageA = numpy.zeros((166*5, 400, 3), dtype = "uint8")
    montageB = numpy.zeros((166*5, 400, 3), dtype="uint8")
    for j in range(0,10):
        (score, imageName) = results[j]
        path = os.path.join(args["dataset"],imageName)
        result = cv2.imread(path)
        print("\t{}. {} : {:.3f}".format(j+1, imageName, score))
        if j<5:
            montageA[j*166:(j+1)*166,:] = result
        else:
            montageB[(j-5)*166:(j-5+1)*166,:] = result

    cv2.imshow("Results 1-5",montageA)
    cv2.imshow("Results 6-10",montageB)
    cv2.waitKey()


#####==================python code.py --dataset images --index index===================TO RUN##########