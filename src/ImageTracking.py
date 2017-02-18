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
minR = 0
maxR = 0
minG = 0
maxG = 0
minB = 0
maxB = 0

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
        print("HSV Value")
        print(hsvValue) 
        print("BGR Value")
        print(bgrValue) 
        print("Min HSV")
        print(minHSV)
        print("Max HSV")
        print(maxHSV) 
        print("Min BGR")
        print(minBGR)
        print("Max BGR")
        print(maxBGR)
  
def adjust_min_r(value):
    global minR
    minR = value
    
def adjust_min_g(value):
    global minG
    minG = value
    
def adjust_min_b(value):
    global minB
    minB = value
    
def adjust_max_r(value):
    global maxR
    maxR = value
    
def adjust_max_g(value):
    global maxG
    maxG = value
    
def adjust_max_b(value):
    global maxB
    maxB = value
    
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
cv2.createTrackbar("Min R", "Video", 0, 255, adjust_min_r)
cv2.createTrackbar("Max R", "Video", 0, 255, adjust_max_r)
cv2.createTrackbar("Min G", "Video", 0, 255, adjust_min_g)
cv2.createTrackbar("Max G", "Video", 0, 255, adjust_max_g)
cv2.createTrackbar("Min B", "Video", 0, 255, adjust_min_b)
cv2.createTrackbar("Max B", "Video", 0, 255, adjust_max_b)
cv2.createTrackbar("Erosion/Dilation", "Video", 50, 100, erosion)

while True:
    #Read the frame
    status, img = cap.read()
    
    #Convert from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #Get a grayscale frame from the tracked color
    minBGR = np.array([minB, minG, minR])
    maxBGR = np.array([maxB, maxG, maxR])
    
    
    mask = cv2.inRange(hsv, minBGR, maxBGR)
    
    kernel = np.ones((5,5), np.uint8)
    if erosionVal < 50:
        mask = cv2.erode(mask, kernel, iterations=(50 - erosionVal))
    elif erosionVal > 50:
        mask = cv2.dilate(mask, kernel, iterations=(erosionVal - 50))  
    
    #Show all the windows
    cv2.imshow("Video", img)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Tracking Window", mask)
    
    if x_coor != 0 and y_coor != 0:
        hsvValue = hsv[y_coor, x_coor]
        bgrValue = img[y_coor, x_coor]
    
    #Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
