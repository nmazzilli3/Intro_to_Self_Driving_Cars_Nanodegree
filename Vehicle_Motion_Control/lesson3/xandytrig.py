'''
Keeping Track of Vehicle x and y¶
Now that you know how to solve trigonometry problems, you can keep track of a vehicle's	 𝑥	and	 𝑦	coordinates as it moves in any direction.

The goal of this lesson is for you to implement a few methods in a Vehicle class. Once complete, your code will be used like this:

# instantiate vehicle
v = Vehicle()

# drive forward 10 meters
v.drive_forward(10)

# turn left in 10 increments of 9 degrees each.
for _ in range(10):
	v.turn(9.0)
	v.drive_forward(1)

v.drive_forward(10)

v.show_trajectory()
and this final call to show_trajectory should produce a graph that looks like this:
'''

import numpy as np
from math import sin, cos, pi
from matplotlib import pyplot as plt

# TODO - Complete the methods in the vehicle class. If the 
#		 requirements of any method are unclear, look at 
#		 the testing code in testing.py (you'll need to
#		 click on the "Jupyter" logo in the top left and
#		 then open testing.py)
#
#		 If you really get stuck, take a look at the 
#		 solution code in the next segment.

class Vehicle:
	def __init__(self):
		self.x		 = 0.0 # meters
		self.y		 = 0.0
		self.heading = 0.0 # radians
		self.history = []
		
	def drive_forward(self, displacement):
		"""
		Updates x and y coordinates of vehicle based on 
		heading and appends previous (x,y) position to
		history.
		"""
		self.history.append((self.x, self.y))
		self.x = cos(self.heading)*displacement
		self.y = sin(self.heading)*displacement
	
	def set_heading(self, heading_in_degrees):
		"""
		Sets the current heading (in radians) to a new value
		based on heading_in_degrees. Vehicle heading is always
		between 0 and 2 * pi.
		"""
		assert(-180 <= heading_in_degrees <= 180)
		rads = heading_in_degrees*pi/180
		self.heading = rads
	
	def turn(self, angle_in_degrees):
		"""
		Changes the vehicle's heading by angle_in_degrees. Vehicle 
		heading is always between 0 and 2 * pi.
		"""
		
		rads = angle_in_degrees*pi/180
		self.heading += rads 
		
	
	def show_trajectory(self):
		"""
		Creates a scatter plot of vehicle's trajectory.
		"""
		X = [p[0] for p in self.history]
		Y = [p[1] for p in self.history]
		
		X.append(self.x)
		Y.append(self.y)
		
		plt.scatter(X,Y)
		plt.plot(X,Y)
		plt.title("Vehicle (x, y) Trajectory")
		plt.xlabel("X Position")
		plt.ylabel("Y Position")
		plt.axes().set_aspect('equal', 'datalim')
		plt.show()
		
# Use this testing code to check your code for correctness.
from testing import test_drive_forward, test_set_heading

test_set_heading(Vehicle)
test_drive_forward(Vehicle)

# You'll have to "test" your show_trajectory method 
# visually. Run the code below and see if the plot that's
# produced looks similar to the plot at the bottom of 
# this notebook.

# instantiate vehicle
v = Vehicle()

# drive forward 10 meters
v.drive_forward(10)

# turn left in 10 increments of 9 degrees each.
for _ in range(10):
	v.turn(9.0)
	v.drive_forward(1)

v.drive_forward(10)

v.show_trajectory()