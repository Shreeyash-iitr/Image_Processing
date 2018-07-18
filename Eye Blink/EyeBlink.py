from scipy.spatial import distance
from imutils import face_utils
import numpy
import imutils
import dlib
import cv2

def calculate_EAR(pnts):
    A = distance.euclidean(pnts[1], pnts[5])
    B = distance.euclidean(pnts[2], pnts[4])
    C = distance.euclidean(pnts[0], pnts[3])
    EAR = (A + B)/(2*C)
    return EAR

close = cv2.imread('closed_eye.jpg')
close = imutils.resize(close, width=500)
close_gray = cv2.cvtColor(close, cv2.COLOR_BGR2GRAY)

open = cv2.imread('open_eye.jpg')
open = imutils.resize(open, width=500)
open_gray = cv2.cvtColor(open, cv2.COLOR_BGR2GRAY)


img = open.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


detector = dlib.get_frontal_face_detector()
rects = detector(img_gray, 1)
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

(lstart, lend) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rstart, rend) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

for (i, rect) in enumerate(rects):
    pnts = predictor(img_gray, rect)
    pnts = face_utils.shape_to_np(pnts)
    left_eye_pnts = pnts[lstart:lend]
    right_eye_pnts = pnts[rstart:rend]
    EAR_right = calculate_EAR(right_eye_pnts)
    EAR_left = calculate_EAR(left_eye_pnts)
    EAR_avg = (EAR_left + EAR_right)/2.0
    for (x, y) in right_eye_pnts:
        cv2.circle(img, (x,y), 2, (255,0,0), -1)
    for (x, y) in left_eye_pnts:
        cv2.circle(img, (x,y), 2, (0,255,0), -1)
    print(EAR_left, EAR_right, EAR_avg)
    if(EAR_avg < 0.15):
        cv2.putText(img, "Blink", (20,30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255), 2)
    else:
        cv2.putText(img, "Open", (20, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)



cv2.imshow('open', img)
cv2.imwrite('result_open.jpg', img)
cv2.waitKey()