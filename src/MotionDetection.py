'''
Created on Feb 18, 2017

@author: Lane
'''

import numpy as np
import cv2

#Main
cap = cv2.VideoCapture(0)
cv2.namedWindow("Video")
cv2.namedWindow("Thresh")

status, img = cap.read()

height = len(img)
width = len(img[0])

grayscale = np.zeros((height, width, 3), np.uint8)
floating = np.zeros((height, width, 3), np.float32)
cloneImage = None
difference = np.zeros((height, width, 3), np.uint8)

while True:
    #Read the frame
    status, img = cap.read()
    
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
    
    cv2.imshow("Thresh", grayscale)
    
    #Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()