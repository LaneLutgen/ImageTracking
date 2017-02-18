'''
Created on Feb 18, 2017

@author: Lane
'''

import numpy as np
import cv2

#Main
cap = cv2.VideoCapture(0)
cv2.namedWindow("Video")
cv2.namedWindow("Edge Detection")
cv2.namedWindow("Threshold")

status, img = cap.read()

height = len(img)
width = len(img[0])

grayscale = np.zeros((height, width, 3), np.uint8)
floating = np.zeros((height, width, 3), np.float32)
cloneImage = None
difference = np.zeros((height, width, 3), np.uint8)

grayThreshold = 200;

while True:
    #Read the frame
    status, img = cap.read()
    
    #Brighten image
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv

    h, s, v = cv2.split(hsv)
    v += 255
    final_hsv = cv2.merge((h, s, v))

    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    
    #Capture current image state
    cloneImage = img
    
    #Show all the windows
    cv2.imshow("Video", img)
    
    #Blur Image
    blur = cv2.blur(img,(5,5))

    #Calculate the running average
    cv2.accumulateWeighted(blur, floating, 0.5, mask=None)
    
    #Numpy array to store 8 bit weighted image
    conversion = np.zeros((height, width, 3), np.uint8)
    
    #Swap running average to same format as frame
    cv2.convertScaleAbs(floating, conversion)
    
    #Take the difference between current and previous image
    difference = cv2.absdiff(cloneImage, conversion)
    
    #Grayscale difference image
    grayscale = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
    
    #Show image with edge detection
    cv2.imshow("Edge Detection", grayscale)
    
    blur2 = cv2.blur(grayscale,(5,5))
    
    #Threshold the image
    ret,thresh = cv2.threshold(blur2, 25, 255, cv2.THRESH_BINARY_INV)
    
    cv2.imshow("Threshold", thresh)
    
    #Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()