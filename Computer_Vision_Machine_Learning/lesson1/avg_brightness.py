# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:37:15 2020

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


# Testing average brightness levels
# Look at a number of different day and night images and think about 
# what average brightness value separates the two types of images

# As an example, a "night" image is loaded in and its avg brightness is displayed
image_num = 190
test_im = STANDARDIZED_LIST[image_num][0]

avg = helpers.avg_brightness(test_im)
print('Avg brightness: ' + str(avg))


day_highest_idx = 0
day_lowest_idx = 0 
day_max_brightness = 0
day_min_brightness = 1000 
night_highest_idx = 0
night_lowest_idx = 0 
night_max_brightness = 0
night_min_brightness = 1000 
for idx in range(len(STANDARDIZED_LIST)):
    test_im = STANDARDIZED_LIST[idx][0]
    selected_label = STANDARDIZED_LIST[idx][1]
    avg = helpers.avg_brightness(test_im)
    print('Avg brightness: ' + str(avg) + ' ' + 'And it is ' + str(selected_label))
    if selected_label == 1:
        if avg > day_max_brightness:
            day_max_brightness = avg 
            day_highest_idx = idx 
            
        if avg < day_min_brightness: 
            day_min_brightness = avg 
            day_lowest_idx = idx

    if selected_label == 0:
        if avg > night_max_brightness:
            night_max_brightness = avg 
            night_highest_idx = idx 
            
        if avg < night_min_brightness: 
            night_min_brightness = avg 
            night_lowest_idx = idx
            
print('For day max brightness was ' + str(day_max_brightness) + ' ' + 'at idx:' + str(day_highest_idx))
print()
print('For day min brightness was ' + str(day_min_brightness) + ' ' + 'at idx:' + str(day_lowest_idx))
print()
print('For night max brightness was ' + str(night_max_brightness) + ' ' + 'at idx:' + str(night_highest_idx))
print()
print('For night min brightness was ' + str(night_min_brightness) + ' ' + 'at idx:' + str(night_lowest_idx))