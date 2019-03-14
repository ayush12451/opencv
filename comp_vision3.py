# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:42:37 2018

@author: Ayush
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    laplasian=cv2.Laplacian(frame,cv2.CV_64F)
    can=cv2.Canny(gray,100,100)
    cv2.imshow('org',gray)
    cv2.imshow('lap',laplasian)
    
    cv2.imshow('can',can)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()