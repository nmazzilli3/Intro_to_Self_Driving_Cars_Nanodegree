# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:44:49 2020

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

# Standardize all training images
STANDARDIZED_LIST = helpers.standardize(IMAGE_LIST)

## Test out your code by calling the above function and seeing 
# how some of your training data is classified
correct = 0
for idx in range(len(STANDARDIZED_LIST)):
    test_im = STANDARDIZED_LIST[idx][0]
    selected_label = STANDARDIZED_LIST[idx][1]
    label = helpers.estimate_label(test_im)
    if selected_label == label:
        correct += 1 
        
print(correct/len(STANDARDIZED_LIST))

