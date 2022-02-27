import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0) # number represents webcam number 1

# common procedure for hands
mpHands = mp.solutions.hands

# this class only uses rgb images
hands = mpHands.Hands()


while True:
    success, img = cap.read()
    
    # convert webcam image to rgb
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    cv2.imshow("Image", img)
    cv2.waitKey(1) 
