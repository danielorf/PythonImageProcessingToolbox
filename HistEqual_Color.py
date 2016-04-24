# Histogram Equalization
#   https://en.wikipedia.org/wiki/Histogram_equalization
#   http://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html

import numpy as np
import cv2
import os

rootdir = 'input'
proc_dir = 'processed'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print file

        img = cv2.imread(os.path.join(subdir, file))

        img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        y, cb, cr = cv2.split(img)
        y_e = cv2.equalizeHist(y)
        img = cv2.merge((y_e, cb, cr))
        img = cv2.cvtColor(img, cv2.COLOR_YCR_CB2BGR)

        print_name = "%s" %(file)
        print_name = "%s\%s" %(proc_dir,print_name)
        print_name = print_name.lower()

        cv2.imwrite(print_name, img)
        
        print print_name



