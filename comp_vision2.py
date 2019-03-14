# -*- coding: utf-8 -*-
"""
Created on Thu May 24 20:26:38 2018

@author: Ayush
"""

import cv2
import numpy as np
img=cv2.imread('bookpage.jpg')
img_g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img',img_g)
th = cv2.adaptiveThreshold(img_g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('img',th)
cv2.waitKey(0)
cv2.destroyAllWindows()