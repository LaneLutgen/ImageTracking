'''
Created on Feb 14, 2017

@author: Lane
'''

import numpy as np
import cv2

x_coor = 0
y_coor = 0
height = 0
width = 0
hsvValue = np.uint8([0,0,0]) 
    
def mouseCall(evt, x, y, flags, pic):
    global x_coor
    global y_coor
    if evt == cv2.EVENT_LBUTTONDOWN:
        x_coor = x
        y_coor = y    
  
def adjust_min_r(value):
    print("magic")
    
def adjust_min_g(value):
    print("magic")
    
def adjust_min_b(value):
    print("magic")
    
def adjust_max_r(value):
    print("magic")
    
def adjust_max_g(value):
    print("magic")
    
def adjust_max_b(value):
    print("magic")          
  
     
#Main
cap = cv2.VideoCapture(0)
cv2.namedWindow("Video")
cv2.namedWindow("HSV")

#Set mouse callback function
cv2.setMouseCallback("HSV", mouseCall, None)

#Create the sliders for mins and maxes
cv2.createTrackbar("Min R", "Video", 255, 255, adjust_min_r)
cv2.createTrackbar("Min G", "Video", 255, 255, adjust_min_g)
cv2.createTrackbar("Min B", "Video", 255, 255, adjust_min_b)
cv2.createTrackbar("Max R", "Video", 255, 255, adjust_max_r)
cv2.createTrackbar("Max G", "Video", 255, 255, adjust_max_g)
cv2.createTrackbar("Max B", "Video", 255, 255, adjust_max_b)

while True:
    #Read the frame
    status, img = cap.read()
    
    #Convert from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #Show all the windows
    cv2.imshow("Video", img)
    cv2.imshow("HSV", hsv)
    
    if x_coor != 0 and y_coor != 0:
        hsvValue = hsv[y_coor, x_coor]
    
    #Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
