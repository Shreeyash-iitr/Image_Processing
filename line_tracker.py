import cv2
t1 = cv2.getTickCount()
x1=0
x2=0
track = cv2.imread('track3.jpg')
cv2.namedWindow('thresh', cv2.WINDOW_NORMAL)
ret, thresh = cv2.threshold(track, 50, 255, cv2.THRESH_BINARY)
dst = [653,1306,1959,2612]
pix = 0
for row in dst:
    count = 0
    for col in range(0, 1836):
        if all([thresh[row][col][0] == 0, count == 0]):
            x1 = col
            count = 1
            #col=col+10

        elif all([thresh[row][col][0] == 255, count == 1]):
            x2 = col - 1

            break
    if (count==1):
        cv2.circle(thresh, ((x1 + x2) // 2, row), 50, (255, 0, 0), -1)



for row in dst:
    cv2.circle(thresh, (918, row), 50, (0, 255, 0), -1)


cv2.imshow('thresh', thresh)
t2= cv2.getTickCount()
print((t2-t1)/cv2.getTickFrequency())

cv2.waitKey()