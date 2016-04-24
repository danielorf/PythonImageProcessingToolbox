import numpy as np
import cv2
import os


img = cv2.imread('beaches4.jpg')
blur = cv2.bilateralFilter(img,9,75,75)

cv2.imshow('img',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
