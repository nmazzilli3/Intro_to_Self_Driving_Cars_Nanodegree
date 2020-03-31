# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:16:29 2020

@author: nmazzilli24
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import cv2

# Read in the image
stop1 = mpimg.imread('images/stop_sign.jpg')

print('Image shape: ', stop1.shape)
plt.figure()
plt.title('Stop Sign 1 Image')
plt.imshow(stop1)

# Read in the image
stop2 = mpimg.imread('images/stop_sign2.jpg')

print('Image shape: ', stop2.shape)
plt.figure()
plt.title('Stop Sign 2 Image')
plt.imshow(stop2)

# To crop and image, you can use image slicing 
# which is just slicing off a portion of the image array

# Make a copy of the image to manipulate
image_crop = np.copy(stop2)

# Define how many pixels to slice off the sides of the original image
row_crop = 90
col_crop = 250

# Using image slicing, subtract the row_crop from top/bottom and col_crop from left/right
image_crop = stop2[row_crop:-row_crop, col_crop:-col_crop, :]
plt.figure()
plt.title('Stop Sign 2 Cropped Image')
plt.imshow(image_crop)

# Use OpenCV's resize function
standardized_im = cv2.resize(image_crop, (1389, 1500))

print('Image shape: ', standardized_im.shape)

# Plot the two images side by side
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
ax1.set_title('Stop sign 1')
ax1.imshow(stop1)
ax2.set_title('Standardized stop sign 2')
ax2.imshow(standardized_im)

# Sum all the red channel values and compare
red_sum1 = np.sum(stop1[:,:,0])
red_sum2 = np.sum(standardized_im[:,:,0])

print('Sum of all red pixel values in the first stop sign image: ', red_sum1)
print('Sum of red pixel values in the second, standardized image: ', red_sum2)

red_sum_orig = np.sum(stop2[:,:,0])

print('\nFor comparison, the sum of red pixels in the non-standardized image: ', red_sum_orig)

