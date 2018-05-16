import cv2
import numpy   
import urllib

url='http://192.168.0.105:8080/shot.jpg'
while True:
    imgresp = urllib.request.urlopen(url)
    imgNP = numpy.array(bytearray(imgresp.read()),dtype=numpy.uint8)
    track = cv2.imdecode(imgNP,-1)

    # track = cv2.imread('track2.jpg')
    #cv2.namedWindow('thresh', cv2.WINDOW_NORMAL)
    gray = cv2.cvtColor(track,cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
    thresh = cv2.resize(thresh1,(200,400))
    dst = [80, 160, 240, 320]

    for row in dst:
        count = 0
        for col in range(0, 200):
            if all([thresh[row][col] == 0, count == 0]):
                x1 = col
                count = 1

            elif all([thresh[row][col] == 255, count == 1]):
                x2 = col - 1
                k=9


                break
        if all([count == 1,k==9]):
            cv2.circle(thresh, ((x1 + x2) // 2, row), 5, (255, 0, 0), -1)

    for row in dst:
        cv2.circle(thresh, (200, row), 5, (0, 255, 0), -1)

    cv2.imshow('thresh', thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

