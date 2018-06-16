import cv2
import numpy

A = cv2.imread('apple.png')
B = cv2.imread('orange.png')

G = A.copy()
#G=cv2.cvtColor(G,cv2.COLOR_BGR2GRAY)
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

G = B.copy()
#G=cv2.cvtColor(G,cv2.COLOR_BGR2GRAY)
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i],dstsize= (gpA[i-1].shape[1],gpA[i-1].shape[0]))
    #L = gpA[i-1]-GE
    L = cv2.subtract(gpA[i - 1], GE)
    lpA.append(L)


lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i],dstsize= (gpB[i-1].shape[1],gpB[i-1].shape[0]))
    #L = gpB[i-1]-GE
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

LS = []
for la,lb in zip(lpA,lpB):
    r,c,d = la.shape
    ls = numpy.hstack((la[:,0:c//2],lb[:,c//2:]))
    LS.append(ls)

ls_ = LS[0]

for i in range(1,6):
    ls_ = cv2.pyrUp(ls_,dstsize=(LS[i].shape[1],LS[i].shape[0]))
    cv2.imshow('ls_', ls_)
    ls_ = ls_+LS[i]
    jls_ = cv2.add(ls_,LS[i])
    #cv2.imshow('LS[i]', LS[i])
    #cv2.imshow('test', ls_)
    cv2.waitKey()





cv2.waitKey()