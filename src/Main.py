'''
Created on Feb 14, 2017

@author: Lane
'''

import numpy as num
import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow("Video")

while True:
    #Read the frame
    status, img = cap.read()
    
    #Convert from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #Show all the windows
    cv2.imshow("Video", img)
    cv2.imshow("HSV", hsv)
    
    #Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
