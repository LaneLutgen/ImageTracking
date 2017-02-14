'''
Created on Feb 14, 2017

@author: Lane
'''

import numpy as num
import cv2


x_coor = 0
y_coor = 0
    
def mouseCall(evt, x, y, flags, pic):
    global x_coor
    global y_coor
    if evt == cv2.EVENT_LBUTTONDOWN:
        print("Coordinates set")
        x_coor = x
        y_coor = y
        print("X: %d" % x_coor)
        print("Y: %d" % y_coor)
        
        
#Main
cap = cv2.VideoCapture(0)
cv2.namedWindow("Video")
cv2.namedWindow("HSV")

#Set mouse callback function
cv2.setMouseCallback("HSV", mouseCall, None)

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
