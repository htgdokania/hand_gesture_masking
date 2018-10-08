#code to show only skin  color  trial and error
import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    low_skin=np.array([0,30,60])
    up_skin=np.array([20,150,255])
    mask=cv2.inRange(hsv,low_skin,up_skin)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    blur=cv2.GaussianBlur(mask,(15,15),0)

##    cv2.imshow('res',result)
##    cv2.imshow('frame',frame)
##    cv2.imshow('mask',mask)
    cv2.imshow('blur',blur)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
