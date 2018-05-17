# Aim is to abstract data of green curve on graph in terms of its x and y co-ordinates.
import cv2
import numpy
cv2.namedWindow('graph',cv2.WINDOW_NORMAL)
cv2.namedWindow('thresh',cv2.WINDOW_NORMAL)
graph = cv2.imread('graph1.png')
temp = numpy.zeros((graph.shape[0],graph.shape[1],3),numpy.uint8)
for row in range(0,graph.shape[0]):
    for col in range(0,graph.shape[1]):
        if all([graph[row][col][1]>=60, graph[row][col][0]<120, graph[row][col][2]<120]):
            for k in range(0,3):
                temp[row][col][k]=graph[row][col][k]
        else:
            temp[row][col][0]= 255
            temp[row][col][1] = 255
            temp[row][col][2] = 255
        #if all([graph[row][col][1] <= 20, graph[row][col][0] < 20, graph[row][col][2] < 20]):
         #   for k in range(0,3):
          #      temp[row][col][k]=graph[row][col][k]

gray = cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

cv2.imshow('graph',graph)
cv2.line(thresh,(97,88),(107,95),(0,0,0),1)
cv2.line(thresh,(145,119),(155,145),(0,0,0),1)
cv2.line(thresh,(185,78),(188,88),(0,0,0),1)
cv2.line(thresh,(255,119),(263,139),(0,0,0),1)
cv2.line(thresh,(426,119),(435,143),(0,0,0),1)
en = 0
for col in range(76,469):
    for row in range(11,212):
        if thresh[row][col]==0:
            y=(-1.945*row)+201.4
            x=(0.010283*col)+27
            st='y= '+str(y)+ '  x= '+ str(x)
            print( st)
            break





cv2.imshow('thresh',thresh)

cv2.waitKey()
