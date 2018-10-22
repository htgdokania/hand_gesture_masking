import numpy as np
import cv2 
pic = cv2.imread('mom2.png')
img=cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img,127,255,0)
_,contours,_ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print ("no. of conoturs detected =%d"%len(contours))
##print (contours)
##cnt = contours[0]
##M = cv2.moments(cnt)
##print( M )

##rect = cv2.minAreaRect(cnt)
##box = cv2.boxPoints(rect)
##box = np.int0(box)
##print(box)
##cv2.drawContours(pic,[box],0,(0,0,255),2)
####pic = cv2.polylines(pic,[box],1,(0,0,255),4)

cv2.imshow('img2',pic)

if cv2.waitKey(25) & 0xFF==ord('q'):
    cv2.destroyAllWindows()

