#code to show only skin  color  trial and error
import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
##    cv2.imshow('hsv',hsv)
    """type 1"""
##    low_red=np.array([0,20,70])
##    up_red=np.array([20,255,255])
    """type 2"""
    low_red=np.array([0,30,60])
    up_red=np.array([20,150,255])

    mask=cv2.inRange(hsv,low_red,up_red)
    result=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',result)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
