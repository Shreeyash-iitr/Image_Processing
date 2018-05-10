import cv2                       #importing openCV

import numpy                     #importing numpy

# Here we are interested in making a program which can convert RGB image to gray_scale image.
# We could have used cv2.cvtColor() but we are interested in making the function itself.


img = cv2.imread('src.JPG')
#  reading source image from computer

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#  just to match function's output with our output image

temp = numpy.zeros((img.shape[0], img.shape[1]), numpy.uint8)
#  creating an image array of size equal to source image {img}. img.shape[0] and img.shape[1] gives no. of rows
#  and columns  in source image. Every pixel is initialised with zero.

for row in range(0,img.shape[0]):
    for col in range(0,img.shape[1]):
        temp[row][col] = (0.299*img[row][col][2]) + (0.587*img[row][col][1]) + (0.114*img[row][col][0])
        # 0.587, 0.114, 0.299 are multipliers for different colors chosen according to eye color sensitivity
        # note that 0.587+0.114+0.299 = 1

        # temp[row][col] = (0.333333 * img[row][col][2]) + (0.333333 * img[row][col][1]) + (0.333333 * img[row][col][0])
        # try this also where equal weightage of RGB colors is taken.

cv2.imshow('gray', gray)
cv2.imshow('temp', temp)
# comparing two outputs

cv2.waitKey()


