import numpy as np
import cv2 
pic = cv2.imread('omask.png')
img=cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img,127,255,0)
_,contours,_= cv2.findContours(thresh,1,2)
print ("number of con= %d"%len(contours))

cv2.drawContours(pic,contours,-1,(0,0,255),2)#-1 to draw all contours

cv2.imshow('img2',pic)

if cv2.waitKey(25) & 0xFF==ord('q'):
    cv2.destroyAllWindows()

