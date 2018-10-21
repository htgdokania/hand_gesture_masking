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
    img=cv2.GaussianBlur(mask,(5,5),0)

##    img=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(img,127,255,0)
    _,contours,hierarchy = cv2.findContours(thresh,1,2)
    cnt = contours[5]
    M = cv2.moments(cnt)
    
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    print(box)
    cv2.drawContours(frame,[box],0,(0,0,255),2)

    cv2.imshow('mask',frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
