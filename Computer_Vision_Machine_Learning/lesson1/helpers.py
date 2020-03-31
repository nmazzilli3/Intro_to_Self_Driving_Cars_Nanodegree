# Helper functions

import os
import glob # library for loading images from a directory
import matplotlib.image as mpimg
import cv2
import numpy as np
import matplotlib.pyplot as plt



# This function loads in images and their labels and places them in a list
# The list contains all images and their associated labels
# For example, after data is loaded, im_list[0][:] will be the first image-label pair in the list
def load_dataset(image_dir):
    
    # Populate this empty image list
    im_list = []
    image_types = ["day", "night"]
    
    # Iterate through each color folder
    for im_type in image_types:
        
        # Iterate through each image file in each image_type folder
        # glob reads in any image with the extension "image_dir/im_type/*"
        for file in glob.glob(os.path.join(image_dir, im_type, "*")):
            
            # Read in the image
            im = mpimg.imread(file)
            
            # Check if the image exists/if it's been correctly read-in
            if not im is None:
                # Append the image, and it's type (red, green, yellow) to the image list
                im_list.append((im, im_type))

    return im_list


def standardize_input(image):
    
    ## TODO: Resize image so that all "standard" images are the same size 600x1100 (hxw) 
    image_x = 1100 
    image_y = 600
    standard_im = cv2.resize(image, (image_x,image_y), interpolation = cv2.INTER_AREA)

    
    return standard_im

def encode(label):
        
    numerical_val = 0
    ## TODO: complete the code to produce a numerical label
    if label == 'day':
        numerical_val = 1
    
    return numerical_val


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

def avg_brightness(rgb_image):
    
    # Convert image to HSV
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

    # Add up all the pixel values in the V channel
    sum_brightness = np.sum(hsv[:,:,2])

    
    ## TODO: Calculate the average brightness using the area of the image
    # and the sum calculated above
    avg = sum_brightness/(600*1100)
    
    return avg

# This function should take in RGB image input
def estimate_label(rgb_image):
    
    avg_v = avg_brightness_hsv(rgb_image,'v')
    ## TODO: extract average brightness feature from an RGB image 
    # Use the avg brightness feature to predict a label (0, 1)
    predicted_label = 0 #night
    threshold_h = 120
    threshold_l = 92
    s_avg_day = 53.8
    s_avg_nite = 103.9
    h_avg_day = 67.1
    h_avg_nite = 45.9
    r_avg_day = 121.7
    r_avg_nite =67.8
    r_std_day = 20.9 
    r_std_nite = 36.3
    g_avg_day = 124.9
    g_avg_nite = 52.1
    g_std_day = 25.2
    g_std_nite = 28.3
    b_avg_day = 126.7
    b_avg_nite = 40.8
    v_avg_day = 137
    
    #Check to see if r or g is within std dev of sample 
    
    
  ## TODO: Return the predicted_label (0 or 1) based on whether the avg is 
    # above or below the threshold
    if avg_v > threshold_h: 
        predicted_label = 1
    elif  avg_v > threshold_l :
        r_avg = mean_rgb(rgb_image,'r')
        g_avg = mean_rgb(rgb_image,'g')
        b_avg = mean_rgb(rgb_image,'b')
        h_avg = mean_hsv(rgb_image,'h')
        s_avg = mean_hsv(rgb_image,'s')
        #Need another value to compare too close 
        #Check to see if r or g is within std dev of sample 
        r_in_range = r_avg >= r_avg_day
        g_in_range = g_avg < 90
        b_in_range = b_avg < 85
        h_in_range = h_avg >= h_avg_nite
        #print(str(r_avg) + ' ' + str(g_avg) + ' ' + str(b_avg) + ' ' + str(h_avg) + ' ' + str(avg_v))

        if  b_in_range or g_in_range:
            predicted_label = 0
        else:
            predicted_label = 1
    else: 
        predicted_label = 0
        
        
    
    return predicted_label    

def hsv_histograms(rgb_image):
    # Convert to HSV
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

    # Create color channel histograms
    h_hist = np.histogram(hsv[:,:,0], bins=32, range=(0, 180))
    s_hist = np.histogram(hsv[:,:,1], bins=32, range=(0, 256))
    v_hist = np.histogram(hsv[:,:,2], bins=32, range=(0, 256))
    
    # Generating bin centers
    bin_edges = h_hist[1]
    bin_centers = (bin_edges[1:]  + bin_edges[0:len(bin_edges)-1])/2

    # Plot a figure with all three histograms
    fig = plt.figure(figsize=(12,3))
    plt.subplot(131)
    plt.bar(bin_centers, h_hist[0])
    plt.xlim(0, 180)
    plt.title('H Histogram')
    plt.subplot(132)
    plt.bar(bin_centers, s_hist[0])
    plt.xlim(0, 256)
    plt.title('S Histogram')
    plt.subplot(133)
    plt.bar(bin_centers, v_hist[0])
    plt.xlim(0, 256)
    plt.title('V Histogram')
    
    return h_hist, s_hist, v_hist

def avg_brightness_rgb(rgb_image,rgb_char):
    
    # Convert image to HSV
    area = 600*1100

    if rgb_char == 'r' or rgb_char == 'R':
        # Add up all the pixel values in the R channel
        r = np.sum(rgb_image[:,:,0])
        average = r/area
    elif rgb_char == 'g' or rgb_char == 'G':
        g = np.sum(rgb_image[:,:,1])
        average = g/area
    elif rgb_char == 'b' or rgb_char == 'B': 
        b = np.sum(rgb_image[:,:,2])
        average = b/area
    else:
        average = None
        
    return average 

def mean_rgb(rgb_image,rgb_char):
    
    if rgb_char == 'r' or rgb_char == 'R':
        # Add up all the pixel values in the R channel
        return_val = np.mean(rgb_image[:,:,0])
    elif rgb_char == 'g' or rgb_char == 'G':
        return_val = np.mean(rgb_image[:,:,1])
    elif rgb_char == 'b' or rgb_char == 'B': 
        return_val = np.mean(rgb_image[:,:,2])
    else:
        return_val = None
        
    return return_val 

def min_rgb(rgb_image,rgb_char):
    
    if rgb_char == 'r' or rgb_char == 'R':
        # Add up all the pixel values in the R channel
        return_val = np.min(rgb_image[:,:,0])
    elif rgb_char == 'g' or rgb_char == 'G':
        return_val = np.min(rgb_image[:,:,1])
    elif rgb_char == 'b' or rgb_char == 'B': 
        return_val = np.min(rgb_image[:,:,2])
    else:
        return_val = None
        
    return return_val 

def max_rgb(rgb_image,rgb_char):
    
    if rgb_char == 'r' or rgb_char == 'R':
        # Add up all the pixel values in the R channel
        return_val = np.max(rgb_image[:,:,0])
    elif rgb_char == 'g' or rgb_char == 'G':
        return_val = np.max(rgb_image[:,:,1])
    elif rgb_char == 'b' or rgb_char == 'B': 
        return_val = np.max(rgb_image[:,:,2])
    else:
        return_val = None
        
    return return_val 
'''
    ## TODO: set the value of a threshold that will separate day and night images
    
    
    
    area = 600*1100 
    r_avg = r/area
    g_avg = g/area
    b_avg = b/area 
    
    print('The V Channel avg is ' + str(avg) + ' ' + 'The R Chan avg is: ' + str(r_avg) 
          + ' ' + 'The G chan avg is: ' + str(g_avg) + ' ' + 'The B Chan avg is: ' + str(b_avg))
  
'''    

def avg_brightness_hsv(rgb_image,hsv_char):
    
    # Convert image to HSV
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    area = 600*1100

    if hsv_char == 'h' or hsv_char == 'H':
        # Add up all the pixel values in the R channel
        val = np.sum(hsv[:,:,0])
        average = val/area
    elif hsv_char == 's' or hsv_char == 'S':
        val = np.sum(hsv[:,:,1])
        average = val/area
    elif hsv_char == 'v' or hsv_char == 'V': 
        val = np.sum(hsv[:,:,2])
        average = val/area
    else:
        average = None
        
    return average 

def mean_hsv(rgb_image,hsv_char):
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    if hsv_char == 'h' or hsv_char == 'H':
        # Add up all the pixel values in the R channel
        return_val = np.mean(hsv[:,:,0])
    elif hsv_char == 's' or hsv_char == 'S':
        return_val = np.mean(hsv[:,:,1])
    elif hsv_char == 'v' or hsv_char == 'V':
        return_val = np.mean(hsv[:,:,2])
    else:
        return_val = None
        
    return return_val 

def min_hsv(rgb_image,hsv_char):
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)    
    if hsv_char == 'h' or hsv_char == 'H':
        # Add up all the pixel values in the R channel
        return_val = np.min(hsv[:,:,0])
    elif hsv_char == 's' or hsv_char == 'S':
        return_val = np.min(hsv[:,:,1])
    elif hsv_char == 'v' or hsv_char == 'V':
        return_val = np.min(hsv[:,:,2])
    else:
        return_val = None
        
    return return_val 

def max_hsv(rgb_image,hsv_char):
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)   
    if hsv_char == 'h' or hsv_char == 'H':
        # Add up all the pixel values in the R channel
        return_val = np.max(hsv[:,:,0])
    elif hsv_char == 's' or hsv_char == 'S':
        return_val = np.max(hsv[:,:,1])
    elif hsv_char == 'v' or hsv_char == 'V':
        return_val = np.max(hsv[:,:,2])
    else:
        return_val = None
        
    return return_val 