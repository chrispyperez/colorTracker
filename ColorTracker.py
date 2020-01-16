import cv2
import numpy as np

cap = cv2.VideoCapture('https://192.168.1.218:8080/video')

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
        # green = np.uint8([[[0,255,0 ]]])
        # hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
        # print hsv_green
        # [[[ 60 255 255]]]
        #choose[H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively.

    lower_bound = np.array([50,50,50]) # Mix of Blue and Green bounds, lower bound of green
    upper_bound = np.array([130,255,255]) #upper bound of blue

    # # define range of green color in HSV
    # lower_green = np.array([50,50,50])
    # upper_green = np.array([110,255,255])


    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_bound, upper_bound)


    # mask = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()