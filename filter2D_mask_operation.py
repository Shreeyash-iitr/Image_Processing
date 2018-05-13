
# here we are interested in method by which we put mask on image.
# mask is actually a matrix which is multiplied to image for various functions like edge detection, smoothening etc.


import cv2
# importing opencv

import numpy
# importing numpy

img = cv2.imread('src.JPG')
# reading image from computer

res = numpy.zeros((img.shape[0], img.shape[1], 3),numpy.uint64)
# making a numpy image object of same size as img


temp = numpy.zeros((img.shape[0]+2, img.shape[1]*3+6), numpy.uint8)
for row in range(0, img.shape[0]):
    for col in range(0, img.shape[1]*3):
        temp[row + 1][col + 3] = img[row][col]

      #  for color in range(0, 3):

# making an image temp same as img having two extra(at boundaries) row and column initialized with zero

for i in range(1, temp.shape[0]-1):
    for j in range(1, temp.shape[1]-1):
        for k in range(0,3):
            #res[i-1][j-1][k] = \
            print(temp[i][j][k] - temp[i-1][j][k] - temp[i+1][j][k] - temp[i][j-1][k] - temp[i][j+1][k])
# multiplying mask matrix to get new image
#      mask =     [0  -1   0
#                 -1   5  -1
#                  0  -1   0]

#cv2.imshow('original', img)
#cv2.imshow('temp',temp)
#cv2.imshow('masked.JPG', res)
#cv2.waitKey()







