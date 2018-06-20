import mahotas
import numpy
import argparse
import pickle
import glob
import cv2
from zernikemoments import ZernikeMoments

'''class ZernikeMoments:
    def __init__(self,radius):
        self.radius = radius
        #The larger the radius, the more pixels will be included in the computation.

    def describe(self, image):
        return mahotas.features.zernike_moments(image, self.radius)'''

#===========construct the argument parser and parse the arguments============
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--sprites", required=True)
ap.add_argument("-i", "--index",required= True)
args = vars(ap.parse_args())

desc = ZernikeMoments(21)  # radius 21 is experimental
index = {}

for spritepath in glob.glob(args["sprites"]+"/*.png"):
    pokemon = spritepath[spritepath.rfind("/")+ 1:].replace(".png","")
    image = cv2.imread(spritepath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.copyMakeBorder(image, 15, 15, 15, 15, cv2.BORDER_CONSTANT,value=255)
    thresh = cv2.bitwise_not(image)
    thresh[thresh> 0] = 255
    outline = numpy.zeros(image.shape, dtype="uint8")
    x, contours, y = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #print(contours)
    contours = sorted(contours, key = cv2.contourArea,reverse= True)[0]
    cv2.drawContours(outline, [contours], -1, 255, -1)
    moments = desc.describe(outline)
    index[pokemon] = moments


#========= Writing index in a file==================
f = open(args["index"],"wb")
f.write(pickle.dumps(index))
f.close()
