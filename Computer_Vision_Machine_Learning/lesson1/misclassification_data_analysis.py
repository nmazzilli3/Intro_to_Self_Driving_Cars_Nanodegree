# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:07:51 2020

@author: nmazzilli24
"""

import cv2 # computer vision library
import helpers

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd

#Create data dictionary 

#We need image, selected label, RGB averares, RGB min/max, HSV averges, min,max
# Image data directories
image_dir_training = "day_night_images/training/"
image_dir_test = "day_night_images/test/"

# Using the load_dataset function in helpers.py
# Load training data
IMAGE_LIST = helpers.load_dataset(image_dir_training)

# Standardize all training images
STANDARDIZED_LIST = helpers.standardize(IMAGE_LIST)

#default_data['item3'] = 3
#default_data.update({'item3': 3})
image_num = 0
test_im = STANDARDIZED_LIST[image_num][0]
selected_label = STANDARDIZED_LIST[image_num][1]
pred_label = helpers.estimate_label(test_im)
r_avg = helpers.avg_brightness_rgb(test_im,'r')
g_avg = helpers.avg_brightness_rgb(test_im,'g')
b_avg = helpers.avg_brightness_rgb(test_im,'b')
r_mean = helpers.mean_rgb(test_im,'r')
g_mean = helpers.mean_rgb(test_im,'g')
b_mean = helpers.mean_rgb(test_im,'b')
r_min = helpers.min_rgb(test_im,'r')
r_max = helpers.max_rgb(test_im,'r')
g_min = helpers.min_rgb(test_im,'g')
g_max = helpers.max_rgb(test_im,'g')
b_min = helpers.min_rgb(test_im,'b')
b_max = helpers.max_rgb(test_im,'b')
#Now HSV Data
h_avg = helpers.avg_brightness_hsv(test_im,'h')
s_avg = helpers.avg_brightness_hsv(test_im,'s')
v_avg = helpers.avg_brightness_hsv(test_im,'v')
h_mean = helpers.mean_hsv(test_im,'h')
s_mean = helpers.mean_hsv(test_im,'s')
v_mean = helpers.mean_hsv(test_im,'v')
h_min = helpers.min_hsv(test_im,'h')
h_max = helpers.max_hsv(test_im,'h')
s_min = helpers.min_hsv(test_im,'s')
s_max = helpers.max_hsv(test_im,'s')
v_min = helpers.min_hsv(test_im,'v')
v_max = helpers.max_hsv(test_im,'v')
'''
df2 = pd.DataFrame([selected_label,pred_label,r_avg,r_mean,h_avg,h_mean], 
                    columns = ['selected_label','pred_label','r_avg','r_mean','v_avg','v_mean'])
df2
'''

df = pd.DataFrame(columns=['selected_label', 'pred_label', 'r_avg','r_min','r_max','g_avg','g_min','g_max','b_avg','b_min','b_max'
                           ,'h_avg','h_min','h_max','s_avg','s_min','s_max','v_avg','v_min','v_max'])

for idx in range(len(STANDARDIZED_LIST)):
    test_im = STANDARDIZED_LIST[idx][0]
    selected_label = STANDARDIZED_LIST[idx][1]
    pred_label = helpers.estimate_label(test_im)
    r_avg = helpers.avg_brightness_rgb(test_im,'r')
    g_avg = helpers.avg_brightness_rgb(test_im,'g')
    b_avg = helpers.avg_brightness_rgb(test_im,'b')
    r_mean = helpers.mean_rgb(test_im,'r')
    g_mean = helpers.mean_rgb(test_im,'g')
    b_mean = helpers.mean_rgb(test_im,'b')
    r_min = helpers.min_rgb(test_im,'r')
    r_max = helpers.max_rgb(test_im,'r')
    g_min = helpers.min_rgb(test_im,'g')
    g_max = helpers.max_rgb(test_im,'g')
    b_min = helpers.min_rgb(test_im,'b')
    b_max = helpers.max_rgb(test_im,'b')
    #Now HSV Data
    h_avg = helpers.avg_brightness_hsv(test_im,'h')
    s_avg = helpers.avg_brightness_hsv(test_im,'s')
    v_avg = helpers.avg_brightness_hsv(test_im,'v')
    h_mean = helpers.mean_hsv(test_im,'h')
    s_mean = helpers.mean_hsv(test_im,'s')
    v_mean = helpers.mean_hsv(test_im,'v')
    h_min = helpers.min_hsv(test_im,'h')
    h_max = helpers.max_hsv(test_im,'h')
    s_min = helpers.min_hsv(test_im,'s')
    s_max = helpers.max_hsv(test_im,'s')
    v_min = helpers.min_hsv(test_im,'v')
    v_max = helpers.max_hsv(test_im,'v')
    df2 = pd.DataFrame([[selected_label,pred_label,r_avg,r_min,r_max,g_avg,g_min,g_max,b_avg,b_min,b_max,h_avg,h_min,h_max,s_avg,s_min,s_max,v_avg,v_min,v_max]], 
                       columns=['selected_label', 'pred_label', 'r_avg','r_min','r_max','g_avg','g_min','g_max','b_avg','b_min','b_max'
                           ,'h_avg','h_min','h_max','s_avg','s_min','s_max','v_avg','v_min','v_max'])
    
    #df.loc[idx] = selected_label + pred_label + r_avg + r_min + r_max + g_avg + g_min + g_max + b_avg + b_min + b_max + h_avg + h_min + h_max + s_avg + s_min + s_max + v_avg + v_min + v_max
    df = df.append(df2)

'''
df = pd.DataFrame({"selected_label":[selected_label], 
                         "pred_label":[pred_label],
                         "r_avg":[r_avg],
                         "r_mean":[r_mean],
                         "v_avg":[v_avg],
                         "v_mean":[v_mean]}) 



image_num = 200
test_im = STANDARDIZED_LIST[image_num][0]
selected_label = STANDARDIZED_LIST[image_num][1]
print(selected_label)
print()
pred_label = helpers.estimate_label(test_im)
r_avg = helpers.avg_brightness_rgb(test_im,'r')
g_avg = helpers.avg_brightness_rgb(test_im,'g')
b_avg = helpers.avg_brightness_rgb(test_im,'b')
r_mean = helpers.mean_rgb(test_im,'r')
g_mean = helpers.mean_rgb(test_im,'g')
b_mean = helpers.mean_rgb(test_im,'b')
r_min = helpers.min_rgb(test_im,'r')
r_max = helpers.max_rgb(test_im,'r')
g_min = helpers.min_rgb(test_im,'g')
g_max = helpers.max_rgb(test_im,'g')
b_min = helpers.min_rgb(test_im,'b')
b_max = helpers.max_rgb(test_im,'b')
#Now HSV Data
h_avg = helpers.avg_brightness_hsv(test_im,'h')
s_avg = helpers.avg_brightness_hsv(test_im,'s')
v_avg = helpers.avg_brightness_hsv(test_im,'v')
h_mean = helpers.mean_hsv(test_im,'h')
s_mean = helpers.mean_hsv(test_im,'s')
v_mean = helpers.mean_hsv(test_im,'v')
h_min = helpers.min_hsv(test_im,'h')
h_max = helpers.max_hsv(test_im,'h')
s_min = helpers.min_hsv(test_im,'s')
s_max = helpers.max_hsv(test_im,'s')
v_min = helpers.min_hsv(test_im,'v')

df1 = pd.DataFrame({"selected_label":[selected_label], 
                         "pred_label":[pred_label],
                         "r_avg":[r_avg],
                         "r_mean":[r_mean],
                         "v_avg":[v_avg],
                         "v_mean":[v_mean]})
df.append(df1)
'''
#pd.set_option("display.max_rows", None, "display.max_columns", None)

df.to_excel("output.xlsx") 