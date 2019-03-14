# -*- coding: utf-8 -*-
"""
Created on Wed May 23 22:21:40 2018

@author: Ayush
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')                   for saving video
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #out.write(frame)
    th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    cv2.imshow('frame',th)
    cv2.imshow('frame1',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()