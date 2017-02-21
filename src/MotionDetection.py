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
    
    #Brighten image by increasing V with the image in HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
    h, s, v = cv2.split(hsv)
    v += 255
    final_hsv = cv2.merge((h, s, v))

    #Convert back to BGR
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    
    #Capture current image state
    cloneImage = img
    
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
    
    img2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    ht, wt = thresh.shape
    min_x, min_y = wt, ht
    max_x = max_y = 0

    #For each contour keep track of min, max x and y values
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        min_x = min(x, min_x)
        max_x = max(x+w, max_x)
        min_y = min(y, min_y)
        max_y = max(y+h, max_y)
        #If bounding rectangle is larger than 75x75, draw it
        if w > 75 and h > 75:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0, 0, 255), 2)
        
    #Show frame with rectangles
    cv2.imshow("Video", img)
    
    #Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()