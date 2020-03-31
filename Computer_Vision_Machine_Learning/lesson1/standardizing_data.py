# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:59:27 2020

@author: nmazzilli24
"""

import cv2 # computer vision library
import helpers

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Image data directories
image_dir_training = "day_night_images/training/"
image_dir_test = "day_night_images/test/"

# Using the load_dataset function in helpers.py
# Load training data
IMAGE_LIST = helpers.load_dataset(image_dir_training)


'''
Input
It's important to make all your images the same size so that they can be sent through the same pipeline of classification steps! Every input image should be in the same format, of the same size, and so on.

TODO: Standardize the input images
Resize each image to the desired input size: 600x1100px (hxw).
'''

# This function should take in an RGB image and return a new, standardized version
def standardize_input(image):
    
    ## TODO: Resize image so that all "standard" images are the same size 600x1100 (hxw) 
    image_x = 1100 
    image_y = 600
    standard_im = cv2.resize(image, (image_x,image_y), interpolation = cv2.INTER_AREA)

    
    return standard_im

'''
TODO: Standardize the output
With each loaded image, you also need to specify the expected output. For this, use binary numerical values 0/1 = night/day.
'''

# Examples: 
# encode("day") should return: 1
# encode("night") should return: 0

def encode(label):
        
    numerical_val = 0
    ## TODO: complete the code to produce a numerical label
    if label == 'day':
        numerical_val = 1
    
    return numerical_val


'''
Construct a STANDARDIZED_LIST of input images and output labels.
This function takes in a list of image-label pairs and outputs a standardized list of resized images and numerical labels.

This uses the functions you defined above to standardize the input and output, so those functions must be complete for this standardization to work!
'''

def standardize(image_list):
    
    # Empty image data array
    standard_list = []

    # Iterate through all the image-label pairs
    for item in image_list:
        image = item[0]
        label = item[1]

        # Standardize the image
        standardized_im = standardize_input(image)

        # Create a numerical label
        binary_label = encode(label)    

        # Append the image, and it's one hot encoded label to the full, processed list of image data 
        standard_list.append((standardized_im, binary_label))
        
    return standard_list

# Standardize all training images
STANDARDIZED_LIST = standardize(IMAGE_LIST)

# Display a standardized image and its label

# Select an image by index
image_num = 0
selected_image = STANDARDIZED_LIST[image_num][0]
selected_label = STANDARDIZED_LIST[image_num][1]

# Display image and data about it
## TODO: Make sure the images have numerical labels and are of the same size
plt.imshow(selected_image)
print("Shape: "+str(selected_image.shape))
print("Label [1 = day, 0 = night]: " + str(selected_label))
