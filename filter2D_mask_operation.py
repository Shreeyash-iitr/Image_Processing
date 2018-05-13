
# here we are interested in method by which we put mask on image.
# mask is actually a matrix which is multiplied to image for various functions like edge detection, smoothening etc.


import cv2
# importing opencv

import numpy
# importing numpy

from PIL import Image
#importing PIL.Image

img = cv2.imread('src.JPG')
# reading image from computer

res = numpy.zeros((img.shape[0], img.shape[1], 3),numpy.uint8)
# making a numpy image object of same size as img


temp = numpy.zeros((img.shape[0]+2, img.shape[1]+2,3), numpy.uint8)
for row in range(0, img.shape[0]):
    for col in range(0, img.shape[1]):
        for color in range(0,3):
            temp[row + 1][col + 1][color] = img[row][col][color]

      #  for color in range(0, 3):
# making an image temp same as img having two extra(at boundaries) row and column initialized with zero



for i in range(1, temp.shape[0]-1):
    for j in range(1, temp.shape[1]-1):
        for k in range(0,3):
            res[i-1][j-1][k] = ((5*temp[i][j][k]) - (temp[i-1][j][k] + temp[i+1][j][k] + temp[i][j-1][k] + temp[i][j+1][k]))
            print(res[i-1][j-1][k])
            # multiplying mask matrix to get new image
#      mask =     [0  -1   0
#                 -1   5  -1
#                  0  -1   0]



kernf = numpy.zeros([3,3])
kernf[0,1] = -1
kernf[1,2] = -1
kernf[1,0] = -1
kernf[2,1] = -1
kernf[1,1] = 5
print(kernf)
func = cv2.filter2D(img,-1,kernf)
# to match our output image with cv2.filter2D function's output image



cv2.imshow('original', img)
cv2.imshow('kernf',func)
cv2.imshow('masked.JPG', res)
cv2.waitKey()


# result is almost same as functions output except at some pixels. The mask I used here is used for smoothening.







