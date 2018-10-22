#code to show only skin  color  trial and error
import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv",hsv)
    low_skin=np.array([0,30,60])
    up_skin=np.array([20,150,255])
    mask=cv2.inRange(hsv,low_skin,up_skin)
    cv2.imwrite("oomask.png",mask)
    
    pic = cv2.imread('oomask.png')
    img=cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(img,127,255,0)
    _,contours,_= cv2.findContours(thresh,1,2)
    print ("number of con= %d"%len(contours))

    cv2.drawContours(frame,contours,-1,(0,0,255),2)#-1 to draw all contours

    cv2.imshow('img2',frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
