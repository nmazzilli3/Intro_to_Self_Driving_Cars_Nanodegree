'''
Plotting Elevator Acceleration
I found an app for my iPhone called Sensor Kinetics that gives you direct access to the phone's IMU data, including data from the accelerometers, rate gyros, and magnetometer.

I put the phone on the floor of the Udacity elevator and pressed "Begin collecting data".

Then I pressed the elevator button for the third floor and let the app collect data as the elevator moved up to the third floor.

I want to show you a plot of that data.

'''

from matplotlib import pyplot as plt
import numpy as np
data = np.genfromtxt("elevator-lac.csv", delimiter=",")[100:570]

#unpack data 
t, a_x, a_y, a_z = data.T

# make the graph
plt.ylabel("Vertical Acceleration (m/s/s)")
plt.xlabel("Time (seconds)")
plt.plot(t,a_z+0.12) # the "+0.12" is to account for bias in the data
plt.show()