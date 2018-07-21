import cv2
import numpy

face_cascade = cv2.CascadeClassifier('/home/shreeyash/opencv-3.4.1/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/shreeyash/opencv-3.4.1/data/haarcascades/haarcascade_eye.xml')
blacky_cascade = cv2.CascadeClassifier('/home/shreeyash/PycharmProjects/untitled/Haar cascades/data/cascade_old.xml')
cap = cv2.VideoCapture(0)


while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    blacky = blacky_cascade.detectMultiScale(gray,7,7)
    for(bx, by, bw, bh) in blacky:
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, 'Blacky', (bx-bw, by-bh), font, 0.5, (0,255,0), 2, cv2.LINE_AA)
        cv2.rectangle(img, (bx, by), (bx+bw, by+bh),(0,0,255),2)
    """
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)
    """
    cv2.imshow('img', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()