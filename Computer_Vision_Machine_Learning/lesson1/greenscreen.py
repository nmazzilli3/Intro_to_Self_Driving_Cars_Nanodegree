# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:33:39 2020

@author: nmazzilli24
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import cv2

# Read in the image
image = mpimg.imread('images/car_green_screen.jpg')

# Print out the image dimensions (height, width, and depth (color))
print('Image dimensions:', image.shape)

# Display the image
'''
plt.figure()
plt.title('Green Screen Original Image')
plt.imshow(image)
'''

# Define our color selection boundaries in RGB values
lower_green = np.array([0,180,0]) 
upper_green = np.array([100,255,100])


# Define the masked area
mask = cv2.inRange(image, lower_green, upper_green)

# Vizualize the mask
'''
plt.figure()
plt.title('Masked Image')
plt.imshow(mask, cmap='gray')
'''

# Mask the image to let the car show through
masked_image = np.copy(image)

masked_image[mask != 0] = [0, 0, 0]

# Display it!
'''
plt.figure()
plt.title('Masked Image Black Background')
plt.imshow(masked_image)
'''

background_image = mpimg.imread('images/sky.jpg')
'''
plt.figure()
plt.title('Sky Background')
plt.imshow(background_image)
'''

## TODO: Crop it or resize the background to be the right size (450x660)
# Hint: Make sure the dimensions are in the correct order!
background_image_y = background_image.shape[0]
background_image_x = background_image.shape[1]
'''
print(background_image_y)
print(background_image_x)
'''

image_y = 450
image_x = 660

# Define how many pixels to slice off the sides of the original image
row_crop = int((background_image_y-image_y)/2)
col_crop = int((background_image_x-image_x)/2)

# Using image slicing, subtract the row_crop from top/bottom and col_crop from left/right
'''
background_crop = background_image[row_crop:-row_crop, col_crop:-col_crop, :]
print(background_crop.shape[0])
print(background_crop.shape[1])
'''
resized = cv2.resize(background_image, (image_x,image_y), interpolation = cv2.INTER_AREA)
'''
print(resized.shape[0])
print(resized.shape[1])
plt.figure()
plt.title('Sky Background Cropped')
plt.imshow(resized)
'''
## TODO: Mask the cropped background so that the car area is blocked
# Hint: mask the opposite area of the previous image
lower_green = np.array([100,255,100])
upper_green = np.array([0,180,0]) 


# Define the masked area
## TODO: Display the background and make sure 
## TODO: Add the two images together to create a complete image!
# complete_image = masked_image + crop_background
bg_masked_image = np.copy(resized)

bg_masked_image[mask == 0] = [0, 0, 0]


complete_image = bg_masked_image + masked_image
plt.figure()
plt.title('Sky Background Cropped With Car')
plt.imshow(complete_image)