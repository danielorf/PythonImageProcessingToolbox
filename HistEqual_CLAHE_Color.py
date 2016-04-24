# Contrast Limited Adaptive Histogram Equalization
#   https://en.wikipedia.org/wiki/Adaptive_histogram_equalization
#   http://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html

import numpy as np
import cv2
import os

rootdir = 'input'
proc_dir = 'processed'

cLimit = 1.5  #Threshold for contrast limiting
tileGridSizeX = 8  # Size of grid for histogram equalization. Input image will be divided into equally sized rectangular tiles. tileGridSize defines the number of tiles in row and column.
tileGridSizeY = 8

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print file

        img = cv2.imread(os.path.join(subdir, file))

        img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        y, cb, cr = cv2.split(img)
        clahe = cv2.createCLAHE(clipLimit=cLimit, tileGridSize=(tileGridSizeX,tileGridSizeY))
        y_c = clahe.apply(y)
        img = cv2.merge((y_c, cb, cr))
        img = cv2.cvtColor(img, cv2.COLOR_YCR_CB2BGR)


        print_name = "%s" %(file)
        print_name = "%s\%s" %(proc_dir,print_name)
        print_name = print_name.lower()

        cv2.imwrite(print_name, img)
        
        print print_name



