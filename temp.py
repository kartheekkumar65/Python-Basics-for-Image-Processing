# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2           # The OpenCV library for opening and saving images
import numpy as np   # Array manipulations and other math stuff
from matplotlib import pyplot as plt # plotting graphs
import matplotlib
import matplotlib.image as mpimg

img = mpimg.imread('cameraman.tif')
imgplot = plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


# Lets make some operations and save the results

# change the data type of the image
img2 = img.astype('float64')

# Convert to normalized floating point
out = (img2 - np.min(img2))/(np.max(img2) - np.min(img2) )
img_org = out.copy();

# increase the pixel intensity values in the image
out = out + 0.5
out[out > 1.0] = 1

out_img = np.uint8(out*255)

imgplot = plt.imshow(cv2.cvtColor(out_img, cv2.COLOR_BGR2RGB))
plt.show()

# write the image to memory
#cv2.imwrite('cameraman_bright.png',out_img)