import cv2
import imutils
from skimage import exposure
import numpy
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-q","--query",required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["query"])
ratio = (image.shape[0])/300
x = numpy.zeros((300, int(image.shape[1]/ratio)),dtype='uint8')
orig = image.copy()
image = imutils.resize(image, height=300)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)# remove noise preserving edges
edges = cv2.Canny(gray, 30, 200)      # experimental values
_, contours, _= cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key= cv2.contourArea, reverse=True)[:10]
screenCnt = None

for c in contours:
    peri = cv2.arcLength(c,closed= True)
    approx = cv2.approxPolyDP(c, 0.02*peri, closed=True)# approximate curve to be rectangle
    if len(approx) == 4:  # approx is collection of points
        screenCnt = approx
        break


cv2.drawContours(image, [screenCnt], -1, (0,255,0), 3)

pts = screenCnt.reshape(4,2)
rect = numpy.zeros((4,2), dtype='float32')

s = pts.sum(1)
rect[0] = pts[numpy.argmin(s)]
rect[2] = pts[numpy.argmax(s)]

diff = numpy.diff(pts,axis=1)
rect[1] = pts[numpy.argmin(diff)]
rect[3] = pts[numpy.argmax(diff)]

rect = rect*ratio

(tl, tr, br, bl) = rect
widthA = numpy.sqrt(((tl[0]-tr[0])**2)+((tl[1]-tr[1])**2))
widthB = numpy.sqrt(((br[0]-bl[0])**2)+((br[1]-bl[1])**2))
heightA = numpy.sqrt(((tl[0]-bl[0])**2)+((tl[1]-bl[1])**2))
heightB = numpy.sqrt(((tr[0]-br[0])**2)+((tr[1]-br[1])**2))

maxH = max(int(heightA),int(heightB))
maxW = max(int(widthA),int(widthB))
dst = numpy.array([[0,0], [maxW-1,0], [maxW-1, maxH-1], [0,maxH-1]],dtype='float32')

M = cv2.getPerspectiveTransform(rect, dst)
warp = cv2.warpPerspective(orig, M, (maxW,maxH))# change perspective
warp = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)
warp = exposure.rescale_intensity(warp, out_range=(0, 255))

(h, w) = warp.shape
(dX, dY) = (int(w*0.4),int(h*0.45))  # experimental values
crop = warp[10:dY, w-dX:w-10]        # experimental values
cv2.imwrite('cropped.png', crop)

cv2.imshow('screen',image)
cv2.imshow('original',orig)
cv2.imshow('edges', edges)
cv2.imshow('warp',imutils.resize(warp, height=300))
cv2.imshow('crop', imutils.resize(crop, height= 300))
cv2.waitKey()