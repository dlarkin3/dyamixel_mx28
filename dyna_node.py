#!/usr/bin/env python

import dynamixel_mx28 as dm28              
import cv2
import numpy as np
import time

dyna = dm28.dynamixel_mx28(dxl_id=3)

def nothing(x):
    pass    
    
cv2.namedWindow('image')
cv2.createTrackbar('Speed','image',1024,2047,nothing)
img = np.full((300,512,3), 55)
dyna.set_left_limit(3600)
dyna.set_right_limit(1500)
event = 0

def click_and_stop(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        print("================================================ TOGGLE BRAKE")
        dyna.toggle_brake()

while 1:
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break    
    cv2.setMouseCallback("image", click_and_stop)
        
    set_speed = cv2.getTrackbarPos('Speed','image')# - 255
    dyna.set_moving_speed(set_speed)
    time.sleep(0.1)
    
cv2.destroyAllWindows()    
