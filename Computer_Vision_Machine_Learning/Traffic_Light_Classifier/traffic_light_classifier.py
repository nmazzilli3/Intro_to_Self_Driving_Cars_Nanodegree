# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:02:59 2020

@author: nmazzilli24
"""

'''
Traffic Light Classifier
In this project, you’ll use your knowledge of computer vision techniques to build a classifier for images of traffic lights! You'll be given a dataset of traffic light images in which one of three lights is illuminated: red, yellow, or green.

In this notebook, you'll pre-process these images, extract features that will help us distinguish the different types of images, and use those features to classify the traffic light images into three classes: red, yellow, or green. The tasks will be broken down into a few sections:

Loading and visualizing the data. The first step in any classification task is to be familiar with your data; you'll need to load in the images of traffic lights and visualize them!

Pre-processing. The input images and output labels need to be standardized. This way, you can analyze all the input images using the same classification pipeline, and you know what output to expect when you eventually classify a new image.

Feature extraction. Next, you'll extract some features from each image that will help distinguish and eventually classify these images.

Classification and visualizing error. Finally, you'll write one function that uses your features to classify any traffic light image. This function will take in an image and output a label. You'll also be given code to determine the accuracy of your classification model.

Evaluate your model. To pass this project, your classifier must be >90% accurate and never classify any red lights as green; it's likely that you'll need to improve the accuracy of your classifier by changing existing features or adding new features. I'd also encourage you to try to get as close to 100% accuracy as possible!

Here are some sample images from the dataset (from left to right: red, green, and yellow traffic lights):
    
'''

'''
Here's what you need to know to complete the project:¶
Some template code has already been provided for you, but you'll need to implement additional code steps to successfully complete this project. Any code that is required to pass this project is marked with '(IMPLEMENTATION)' in the header. There are also a couple of questions about your thoughts as you work through this project, which are marked with '(QUESTION)' in the header. Make sure to answer all questions and to check your work against the project rubric to make sure you complete the necessary classification steps!

Your project submission will be evaluated based on the code implementations you provide, and on two main classification criteria. Your complete traffic light classifier should have:

Greater than 90% accuracy
Never classify red lights as green
1. Loading and Visualizing the Traffic Light Dataset
This traffic light dataset consists of 1484 number of color images in 3 categories - red, yellow, and green. As with most human-sourced data, the data is not evenly distributed among the types. There are:

904 red traffic light images
536 green traffic light images
44 yellow traffic light images
Note: All images come from this MIT self-driving car course and are licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
'''

import cv2 # computer vision library
import helpers # helper functions

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # for loading in images

'''
Training and Testing Data¶
All 1484 of the traffic light images are separated into training and testing datasets.

80% of these images are training images, for you to use as you create a classifier.
20% are test images, which will be used to test the accuracy of your classifier.
All images are pictures of 3-light traffic lights with one light illuminated.
Define the image directories
First, we set some variables to keep track of some where our images are stored:

IMAGE_DIR_TRAINING: the directory where our training image data is stored
IMAGE_DIR_TEST: the directory where our test image data is stored
''' 
# Image data directories
IMAGE_DIR_TRAINING = "traffic_light_images/training/"
IMAGE_DIR_TEST = "traffic_light_images/test/"

'''
Load the datasets
These first few lines of code will load the training traffic light images and store all of them in a variable, IMAGE_LIST. This list contains the images and their associated label ("red", "yellow", "green").

You are encouraged to take a look at the load_dataset function in the helpers.py file. This will give you a good idea about how lots of image files can be read in from a directory using the glob library. The load_dataset function takes in the name of an image directory and returns a list of images and their associated labels.

For example, the first image-label pair in IMAGE_LIST can be accessed by index: IMAGE_LIST[0][:].
''' 

# Using the load_dataset function in helpers.py
# Load training data
IMAGE_LIST = helpers.load_dataset(IMAGE_DIR_TRAINING)

'''
2. Pre-process the Data
After loading in each image, you have to standardize the input and output!

Input
This means that every input image should be in the same format, of the same size, and so on. We'll be creating features by performing the same analysis on every picture, and for a classification task like this, it's important that similar images create similar features!

Output
We also need the output to be a label that is easy to read and easy to compare with other labels. It is good practice to convert categorical data like "red" and "green" to numerical data.

A very common classification output is a 1D list that is the length of the number of classes - three in the case of red, yellow, and green lights - with the values 0 or 1 indicating which class a certain image is. For example, since we have three classes (red, yellow, and green), we can make a list with the order: [red value, yellow value, green value]. In general, order does not matter, we choose the order [red value, yellow value, green value] in this case to reflect the position of each light in descending vertical order.

A red light should have the label: [1, 0, 0]. Yellow should be: [0, 1, 0]. Green should be: [0, 0, 1]. These labels are called one-hot encoded labels.

(Note: one-hot encoding will be especially important when you work with machine learning algorithms).

'''

'''
(IMPLEMENTATION): Standardize the input images
Resize each image to the desired input size: 32x32px.
(Optional) You may choose to crop, shift, or rotate the images in this step as well.
It's very common to have square input sizes that can be rotated (and remain the same size), and analyzed in smaller, square patches. It's also important to make all your images the same size so that they can be sent through the same pipeline of classification steps!

''' 

# This function should take in an RGB image and return a new, standardized version
def standardize_input(image):
    
    ## TODO: Resize image and pre-process so that all "standard" images are the same size  
    standard_im = np.copy(image)
    blur = cv2.bilateralFilter(standard_im,9,100,100)
    # Define the masked area
    image_x = 32 
    image_y = 32
    standard_im = cv2.resize(blur, (image_x,image_y), interpolation = cv2.INTER_AREA)

    return standard_im

'''
Standardize the output
With each loaded image, we also specify the expected output. For this, we use one-hot encoding.

One-hot encode the labels. To do this, create an array of zeros representing each class of traffic light (red, yellow, green), and set the index of the expected class number to 1.
Since we have three classes (red, yellow, and green), we have imposed an order of: [red value, yellow value, green value]. To one-hot encode, say, a yellow light, we would first initialize an array to [0, 0, 0] and change the middle value (the yellow value) to 1: [0, 1, 0].

'''

## TODO: One hot encode an image label
## Given a label - "red", "green", or "yellow" - return a one-hot encoded label

# Examples: 
# one_hot_encode("red") should return: [1, 0, 0]
# one_hot_encode("yellow") should return: [0, 1, 0]
# one_hot_encode("green") should return: [0, 0, 1]

def one_hot_encode(label):
    
    ## TODO: Create a one-hot encoded label that works for all classes of traffic lights
    if label == 'red':
        one_hot_encoded = [1, 0, 0]
    elif label == 'yellow':
        one_hot_encoded = [0, 1, 0]
    elif label == 'green': 
        one_hot_encoded = [0, 0, 1]
    else: 
        one_hot_encoded = [1, 0, 0]
    
    return one_hot_encoded

# Importing the tests
import test_functions
tests = test_functions.Tests()

# Test for one_hot_encode function
tests.test_one_hot(one_hot_encode)

'''
Construct a STANDARDIZED_LIST of input images and output labels.
This function takes in a list of image-label pairs and outputs a standardized list of resized images and one-hot encoded labels.

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

        # One-hot encode the label
        one_hot_label = one_hot_encode(label)    

        # Append the image, and it's one hot encoded label to the full, processed list of image data 
        standard_list.append((standardized_im, one_hot_label))
        
    return standard_list

# Standardize all training images
STANDARDIZED_LIST = standardize(IMAGE_LIST)

'''
3. Feature Extraction
You'll be using what you now about color spaces, shape analysis, and feature construction to create features that help distinguish and classify the three types of traffic light images.

You'll be tasked with creating one feature at a minimum (with the option to create more). The required feature is a brightness feature using HSV color space:

A brightness feature.

Using HSV color space, create a feature that helps you identify the 3 different classes of traffic light.
You'll be asked some questions about what methods you tried to locate this traffic light, so, as you progress through this notebook, always be thinking about your approach: what works and what doesn't?
(Optional): Create more features!

Any more features that you create are up to you and should improve the accuracy of your traffic light classification algorithm! One thing to note is that, to pass this project you must never classify a red light as a green light because this creates a serious safety risk for a self-driving car. To avoid this misclassification, you might consider adding another feature that specifically distinguishes between red and green lights.

These features will be combined near the end of his notebook to form a complete classification algorithm.
'''

'''
Creating a brightness feature
There are a number of ways to create a brightness feature that will help you characterize images of traffic lights, and it will be up to you to decide on the best procedure to complete this step. You should visualize and test your code as you go.

Pictured below is a sample pipeline for creating a brightness feature (from left to right: standardized image, HSV color-masked image, cropped image, brightness feature):
'''

## TODO: Create a brightness feature that takes in an RGB image and outputs a feature vector and/or value
## This feature should use HSV colorspace values
def create_feature(rgb_image):
    
    ## TODO: Convert image to HSV color space
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    ## TODO: Create and return a feature value and/or vector
    height = 32
    width = 32 
    area = height*width
    # np.mean(rgb_image[:,:,0]) gets same value
    h = hsv[:,:,0]
    s = hsv[:,:,1]
    v = hsv[:,:,2]
    h_sum = np.sum(h)
    h_avg = h_sum / area
    s_sum = np.sum(s)
    s_avg = s_sum/area
    v_sum = np.sum(v)
    v_avg = v_sum/area
    
    
    # Feature vector along the axis = 1 over all columns
    # Sum the V component over all columns (axis = 1)
    v_sum_cols = np.sum(v[:,:], axis=1) / width  
    
    v_avg_cols = (max(v_sum_cols)+min(v_sum_cols)) / 2
    lower = np.array([0, 0, 0])
    upper = np.array([179, 255, int(v_avg_cols)])
    #############################
    # Mask the image
    #############################
    
    mask = cv2.inRange(rgb_image,lower,upper)
    masked_image = np.copy(rgb_image)
    masked_image[mask != 0] = [0, 0, 0]      
    # Isolate the masked image V component
    
    masked_hsv = cv2.cvtColor(masked_image, cv2.COLOR_RGB2HSV)    
    gray = cv2.cvtColor(masked_hsv, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(3,3),cv2.BORDER_DEFAULT)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    
    x_min = minLoc[0]
    y_min = minLoc[1]
    x_max = maxLoc[0]
    y_max = maxLoc[1]

    feature = [h_avg,s_avg,v_avg,minVal,maxVal,x_min,y_min,x_max,y_max]
    
    
    return feature

'''

This code found features to see if red/yellow/green had any easy mechanism to filter
feature = []
    
for idx in range(len((STANDARDIZED_LIST))): 
    test_im = STANDARDIZED_LIST[idx][0]
    test_vec = create_feature(test_im)
    feature.append(test_vec)
    
h_array_g = []
s_array_g = []
v_array_g = []
h_array_r = []
s_array_r = []
v_array_r = []
h_array_y = []
s_array_y = []
v_array_y = []
# "red", "green", or "yellow" 
for idx in range(len(feature)):
    selected_label = STANDARDIZED_LIST[idx][1]
    test_vec = feature[idx]
    if selected_label == [1, 0, 0]:
        h_array_r.append(test_vec[0])
        s_array_r.append(test_vec[1])
        v_array_r.append(test_vec[2])
    elif selected_label == [0, 1, 0]:
        h_array_y.append(test_vec[0])
        s_array_y.append(test_vec[1])
        v_array_y.append(test_vec[2])
    else:
        h_array_g.append(test_vec[0])
        s_array_g.append(test_vec[1])
        v_array_g.append(test_vec[2])

print('Green H Stats')
print('Mean : ' + str(np.mean(h_array_g)))
print('Std Dev: ' + str(np.std(h_array_g)))
print('Green S Stats')
print('Mean : ' + str(np.mean(s_array_g)))
print('Std Dev: ' + str(np.std(s_array_g)))
print('Green V Stats')
print('Mean : ' + str(np.mean(v_array_g)))
print('Std Dev: ' + str(np.std(v_array_g)))

print() 
print('Red H Stats')
print('Mean : ' + str(np.mean(h_array_r)))
print('Std Dev: ' + str(np.std(h_array_r)))
print('Red S Stats')
print('Mean : ' + str(np.mean(s_array_r)))
print('Std Dev: ' + str(np.std(s_array_r)))
print('Red V Stats')
print('Mean : ' + str(np.mean(v_array_r)))
print('Std Dev: ' + str(np.std(v_array_r)))

print()
print('Yellow H Stats')
print('Mean : ' + str(np.mean(h_array_y)))
print('Std Dev: ' + str(np.std(h_array_y)))
print('Yellow S Stats')
print('Mean : ' + str(np.mean(s_array_y)))
print('Std Dev: ' + str(np.std(s_array_y)))
print('Yellow V Stats')
print('Mean : ' + str(np.mean(v_array_y)))
print('Std Dev: ' + str(np.std(v_array_y)))

#Nothing from stats allows for easy filter we need to find the bright spot locaiton in image

       
'''


'''
4. Classification and Visualizing Error
Using all of your features, write a function that takes in an RGB image and, using your extracted features, outputs whether a light is red, green or yellow as a one-hot encoded label. This classification function should be able to classify any image of a traffic light!

You are encouraged to write any helper functions or visualization code that you may need, but for testing the accuracy, make sure that this estimate_label function returns a one-hot encoded label.
'''


# This function should take in RGB image input
# Analyze that image using your feature creation code and output a one-hot encoded label
def estimate_label(rgb_image):
    
    ## TODO: Extract feature(s) from the RGB image and use those features to
    ## classify the image and output a one-hot encoded label
    hsv_array = create_feature(rgb_image)
    #   feature = [h_avg,s_avg,v_avg,minVal,maxVal,x_min,y_min,x_max,y_max]
    # [red, yellow, green]: [1, 0, 0]
    '''
    
    '''
    green_y_beg = 21
    green_y_end = 32
    yellow_y_beg = 11
    yellow_y_end = 21
    red_y_beg = 0
    red_y_end = 11
    
    if hsv_array[8] >= red_y_beg and hsv_array[8] <= red_y_end:
         predicted_label = [1, 0, 0]
    elif hsv_array[8] >= green_y_beg and hsv_array[8] <= green_y_end:
        predicted_label = [0, 0, 1]
    else:
        predicted_label = [0, 1, 0]
    
    return predicted_label   
    

'''
Testing the classifier¶
Here is where we test your classification algorithm using our test set of data that we set aside at the beginning of the notebook! This project will be complete once you've pogrammed a "good" classifier.

A "good" classifier in this case should meet the following criteria (and once it does, feel free to submit your project):

Get above 90% classification accuracy.
Never classify a red light as a green light.
Test dataset
Below, we load in the test dataset, standardize it using the standardize function you defined above, and then shuffle it; this ensures that order will not play a role in testing accuracy.
'''

# Using the load_dataset function in helpers.py
# Load test data
TEST_IMAGE_LIST = helpers.load_dataset(IMAGE_DIR_TEST)

# Standardize the test data
STANDARDIZED_TEST_LIST = standardize(TEST_IMAGE_LIST)

# Shuffle the standardized test data
random.shuffle(STANDARDIZED_TEST_LIST)

'''
Determine the Accuracy
Compare the output of your classification algorithm (a.k.a. your "model") with the true labels and determine the accuracy.

This code stores all the misclassified images, their predicted labels, and their true labels, in a list called MISCLASSIFIED. This code is used for testing and should not be changed.
'''

# Constructs a list of misclassified images given a list of test images and their labels
# This will throw an AssertionError if labels are not standardized (one-hot encoded)

def get_misclassified_images(test_images):
    # Track misclassified images by placing them into a list
    misclassified_images_labels = []

    # Iterate through all the test images
    # Classify each image and compare to the true label
    for image in test_images:

        # Get true data
        im = image[0]
        true_label = image[1]
        assert(len(true_label) == 3), "The true_label is not the expected length (3)."

        # Get predicted label from your classifier
        predicted_label = estimate_label(im)
        assert(len(predicted_label) == 3), "The predicted_label is not the expected length (3)."

        # Compare true and predicted labels 
        if(predicted_label != true_label):
            # If these labels are not equal, the image has been misclassified
            misclassified_images_labels.append((im, predicted_label, true_label))
            
    # Return the list of misclassified [image, predicted_label, true_label] values
    return misclassified_images_labels


# Find all misclassified images in a given test set
MISCLASSIFIED = get_misclassified_images(STANDARDIZED_TEST_LIST)

# Accuracy calculations
total = len(STANDARDIZED_TEST_LIST)
num_correct = total - len(MISCLASSIFIED)
accuracy = num_correct/total

print('Accuracy: ' + str(accuracy))
print("Number of misclassified images = " + str(len(MISCLASSIFIED)) +' out of '+ str(total))

'''
Visualize the misclassified images
Visualize some of the images you classified wrong (in the MISCLASSIFIED list) and note any qualities that make them difficult to classify. This will help you identify any weaknesses in your classification algorithm.
''' 

'''
# Visualize misclassified example(s)
## TODO: Display an image in the `MISCLASSIFIED` list 
## TODO: Print out its predicted label - to see what the image *was* incorrectly classified as

for idx in range(len(MISCLASSIFIED)):
    #[image, predicted_label, true_label]
    misclassified = MISCLASSIFIED[idx]
    hsv_array = create_feature(misclassified[0])
    #   feature = [h_avg,s_avg,v_avg,minVal,maxVal,x_min,y_min,x_max,y_max]
    
    # [red, yellow, green]: [1, 0, 0]
    
    print('The bright spot was at : ' + str(hsv_array[8]) + ' ' + 'predicted ' + str(misclassified[1]) + ' ' + 'actual: ' + str(misclassified[2]))

'''

'''
(Question 2): After visualizing these misclassifications, what weaknesses do you think your classification algorithm has? Please note at least two.
Answer: Write your answer in this cell.

I have noticed that 9/27 cases that failed were angled. I have also noticed that 15/27 cases had arrows vs solid lights so perhaps the algorithms was biased towards looking and detecting solid lights.

The algorithm clearly had difficulty detecting these abnormalies.

'''

'''

Test if you classify any red lights as green¶
To pass this project, you must not classify any red lights as green! Classifying red lights as green would cause a car to drive through a red traffic light, so this red-as-green error is very dangerous in the real world.

The code below lets you test to see if you've misclassified any red lights as green in the test set. This test assumes that MISCLASSIFIED is a list of tuples with the order: [misclassified_image, predicted_label, true_label].

Note: this is not an all encompassing test, but its a good indicator that, if you pass, you are on the right track! This iterates through your list of misclassified examples and checks to see if any red traffic lights have been mistakenly labelled [0, 1, 0] (green).

'''

# Importing the tests

tests1 = test_functions.Tests()

if(len(MISCLASSIFIED) > 0):
    # Test code for one_hot_encode function
    tests1.test_red_as_green(MISCLASSIFIED)
else:
    print("MISCLASSIFIED may not have been populated with images.")
