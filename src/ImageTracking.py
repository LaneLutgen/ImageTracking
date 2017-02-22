'''
Created on Feb 14, 2017

@author: Lane
'''

import numpy as np
import cv2

#Coordinates used for mouse click
x_coor = 0
y_coor = 0

#Height and width of the video feed
height = 0
width = 0

#Array to store HSV value from a click
hsvValue = np.array([0,0,0], dtype = "uint8")
bgrValue = np.array([0,0,0], dtype = "uint8")

minBGR = np.array([0,0,0], dtype = "uint8")
maxBGR = np.array([0,0,0], dtype = "uint8")

minHSV = np.array([0,0,0], dtype = "uint8")
maxHSV = np.array([0,0,0], dtype = "uint8")

#Globals for setting the min and max RGB values 
minH = 0
maxH = 0
minS = 0
maxS = 0
minV = 0
maxV = 0

#Value used for erosion and dilation
erosionVal = 50
    
def mouseCall(evt, x, y, flags, pic):
    global x_coor
    global y_coor
    global hsvValue
    global bgrValue
    global minHSV
    global maxHSV
    global minBGR
    global maxBGR
    if evt == cv2.EVENT_LBUTTONDOWN:
        x_coor = x
        y_coor = y 
        if x_coor != 0 and y_coor != 0:
            hsvValue = hsv[y_coor, x_coor]
        print("HSV Value")
        print(hsvValue) 
  
def adjust_min_h(value):
    global minH
    minH = value
    
def adjust_min_s(value):
    global minS
    minS = value
    
def adjust_min_v(value):
    global minV
    minV = value
    
def adjust_max_h(value):
    global maxH
    maxH = value
    
def adjust_max_s(value):
    global maxS
    maxS = value
    
def adjust_max_v(value):
    global maxV
    maxV = value
    
def erosion(value):
    global erosionVal
    erosionVal = value             
        
#Main
cap = cv2.VideoCapture(0)
cv2.namedWindow("Video")
cv2.namedWindow("HSV")
cv2.namedWindow("Tracking Window")

#Set mouse callback function
cv2.setMouseCallback("HSV", mouseCall, None)

#Create the sliders for mins and maxes
cv2.createTrackbar("Min H", "Video", 0, 180, adjust_min_h)
cv2.createTrackbar("Max H", "Video", 0, 180, adjust_max_h)
cv2.createTrackbar("Min S", "Video", 0, 255, adjust_min_s)
cv2.createTrackbar("Max S", "Video", 0, 255, adjust_max_s)
cv2.createTrackbar("Min V", "Video", 0, 255, adjust_min_v)
cv2.createTrackbar("Max V", "Video", 0, 255, adjust_max_v)
cv2.createTrackbar("Erosion", "Video", 50, 100, erosion)

while True:
    #Read the frame
    status, img = cap.read()
    
    #Convert from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #Get a grayscale frame from the tracked color
    minHSV = np.array([minH, minS, minV])
    maxHSV = np.array([maxH, maxS, maxV])
    
    mask = cv2.inRange(hsv, minHSV, maxHSV)
    
    kernel = np.ones((5,5), np.uint8)
    if erosionVal < 50:
        mask = cv2.erode(mask, kernel, iterations=(50 - erosionVal))
    elif erosionVal > 50:
        mask = cv2.dilate(mask, kernel, iterations=(erosionVal - 50))  
    
    #Show all the windows
    cv2.imshow("Video", img)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Tracking Window", mask)
    
    #Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
