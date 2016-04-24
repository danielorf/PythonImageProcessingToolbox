# Bilateral Filter
#   https://en.wikipedia.org/wiki/Bilateral_filter
#   http://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html#bilateralfilter
#	http://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html

import numpy as np
import cv2
import os

rootdir = 'input'
proc_dir = 'processed'

filterDiameter = 9      # Diameter of each pixel neighborhood that is used during filtering. If it is non-positive, it is computed from sigmaSpace .
sigmaColor = 75         # Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood (see sigmaSpace ) will be mixed together, resulting in larger areas of semi-equal color.
sigmaSpace = 75         # Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough (see sigmaColor ). When d>0 , it specifies the neighborhood size regardless of sigmaSpace . Otherwise, d is proportional to sigmaSpace .

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print file

        img = cv2.imread(os.path.join(subdir, file))       
        blur = cv2.bilateralFilter(img,filterDiameter,sigmaColor,sigmaSpace)

        print_name = "%s" %(file)
        print_name = "%s\%s" %(proc_dir,print_name)
        print_name = print_name.lower()

        cv2.imwrite(print_name, blur)
        
        print print_name
