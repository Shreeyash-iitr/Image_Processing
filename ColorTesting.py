import cv2
import numpy

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # THESE VALUES ARE FOR SKIN COLOUR DETECTION
    low = numpy.array([0, 20, 25])
    up = numpy.array([22, 255, 255])

    mask = cv2.inRange(hsv,low,up)

    cv2.imshow('mask',mask)
    cv2.imshow('original',hsv)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.release()




