import cv2
# this is to import OpenCV

img1 = cv2.imread('eb2.JPG')                          # Reading image file from computer

img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)             # Converting image to gray_scale

cv2.imshow('original',img)                            # Showing original grayscale image

for x in range(0,img.shape[0]):                       # for loop traversing through each row and column of image
    for y in range(0,img.shape[1]):
        img[x][y]+=653                                # Adding any scalar value to each pixel


cv2.imshow('+257',img)
cv2.imwrite('+257.JPG',img)                           # saving final image
cv2.waitKey()
