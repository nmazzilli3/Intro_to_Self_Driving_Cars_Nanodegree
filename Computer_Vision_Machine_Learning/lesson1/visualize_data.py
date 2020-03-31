# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:08:29 2020

@author: nmazzilli24
"""

#zip to tar in jupter !tar chvfz notebook.tar.gz *

import cv2 # computer vision library
import helpers

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

'''

Training and Testing Data¶
The 200 day/night images are separated into training and testing datasets.

60% of these images are training images, for you to use as you create a classifier.
40% are test images, which will be used to test the accuracy of your classifier.
First, we set some variables to keep track of some where our images are stored:

image_dir_training: the directory where our training image data is stored
image_dir_test: the directory where our test image data is stored

'''
# Image data directories
image_dir_training = "day_night_images/training/"
image_dir_test = "day_night_images/test/"

'''
Load the datasets¶
These first few lines of code will load the training day/night images and store all of them in a variable, IMAGE_LIST. This list contains the images and their associated label ("day" or "night").

For example, the first image-label pair in IMAGE_LIST can be accessed by index: IMAGE_LIST[0][:].

'''

# Using the load_dataset function in helpers.py
# Load training data
IMAGE_LIST = helpers.load_dataset(image_dir_training)

# Select an image and its label by list index
image_index = 200
selected_image = IMAGE_LIST[image_index][0]
selected_label = IMAGE_LIST[image_index][1]

# Display image and data about it
plt.figure()
plt.imshow(selected_image)
print("Shape: "+str(selected_image.shape))
print("Label: " + str(selected_label))
hsv = cv2.cvtColor(selected_image, cv2.COLOR_RGB2HSV)
#access https://stackoverflow.com/questions/52352947/how-can-i-read-rgb-or-hsv-values-of-image-on-python-opencv
print(selected_image[300][300])
print(hsv[300][300])

print()
image_index1 = 1
selected_image = IMAGE_LIST[image_index1][0]
selected_label = IMAGE_LIST[image_index1][1]

# Display image and data about it
plt.figure()
plt.imshow(selected_image)
print("Shape: "+str(selected_image.shape))
print("Label: " + str(selected_label))
hsv = cv2.cvtColor(selected_image, cv2.COLOR_RGB2HSV)
#access https://stackoverflow.com/questions/52352947/how-can-i-read-rgb-or-hsv-values-of-image-on-python-opencv
print(selected_image[300][300])
print(hsv[300][300])
print()

# Isolate RGB channels
r = selected_image[:,:,0]
g = selected_image[:,:,1]
b = selected_image[:,:,2]

# Visualize the individual color channels
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))
ax1.set_title('R channel')
ax1.imshow(r, cmap='gray')
ax2.set_title('G channel')
ax2.imshow(g, cmap='gray')
ax3.set_title('B channel')
ax3.imshow(b, cmap='gray')

hsv = cv2.cvtColor(selected_image, cv2.COLOR_RGB2HSV)

# HSV channels
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

# Visualize the individual color channels

f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))
ax1.set_title('H channel')
ax1.imshow(h, cmap='gray')
ax2.set_title('S channel')
ax2.imshow(s, cmap='gray')
ax3.set_title('V channel')
ax3.imshow(v, cmap='gray')