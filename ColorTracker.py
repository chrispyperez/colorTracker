import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('https://192.168.1.218:8080/video')
cap2 = cv2.VideoCapture('https://192.168.1.227:8080/video')

propID = cap.get(4)
print(propID)
while(1):

    # Take each frame
    retVal, frame = cap.read()
    retVal2, frame2 = cap2.read()
    # edges = cv2.Canny(frame,100,200)

    # plt.imshow(edges,cmap = 'gray')
    # plt.show()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
        # green = np.uint8([[[0,255,0 ]]])
        # hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
        # print hsv_green
        # [[[ 60 255 255]]]
        #choose[H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively.

    lower_bound = np.array([90,50,50]) 
    upper_bound = np.array([110,255,255]) 

    # # define range of green color in HSV
    # lower_green = np.array([50,50,50])
    # upper_green = np.array([110,255,255])


    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_bound, upper_bound)


    # mask = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    # cv2.imshow('frame',frame)
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 300,300)
    cv2.namedWindow('frame2', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame2', 300,300)
    cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('mask', 300,300)
    cv2.namedWindow('res', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('res', 300,300)

    cv2.imshow('frame2',frame2)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)


    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break
    elif k == ord('s'): #press s to take
        cv2.imwrite('test.png', res)




cap.release()
cv2.destroyAllWindows()