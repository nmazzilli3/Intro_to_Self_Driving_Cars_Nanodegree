'''
Position, Velocity, and Acceleration
Allow me to say the same thing about position and velocity in 5 different ways.

Velocity is the derivative of position.

Velocity is the instantaneous rate of change of position with respect to time.

An object's velocity tells us how much it's position will change when time changes.

Velocity at some time is just the slope of a line tangent to a graph of position vs. time

v(t) = \frac{dx}{dt} = \dot{x}(t)v(t)= 
dt
dx
​	 = 
x
˙
 (t)

It turns out you can say the same 5 things about velocity and acceleration.

Acceleration is the derivative of velocity.

Acceleration is the instantaneous rate of change of velocity with respect to time.

An object's acceleration tells us how much it's velocity will change when time changes.

Acceleration at some time is just the slope of a line tangent to a graph of velocity vs. time

a(t) = \frac{dv}{dt} = \dot{v}(t)a(t)= 
dt
dv
​	 = 
v
˙
 (t)

We can also make a couple interesting statements about the relationship between position and acceleration:

Acceleration is the second derivative of position.
a(t) = \frac{d^2}{dt^2}x(t) = \frac{d^2x}{dt^2} = \ddot{x}(t)a(t)= 
dt 
2
 
d 
2
 
​	 x(t)= 
dt 
2
 
d 
2
 x
​	 = 
x
¨
 (t)
We'll explore this more in the next lesson. For now, just know that differentiating position twice gives acceleration!

'''

from helpers import process_data
from helpers import get_derivative_from_data as solution_derivative
from matplotlib import pyplot as plt

# load the parallel park data
PARALLEL_PARK_DATA = process_data("parallel_park.pickle")

# get the relevant columns
timestamps    = [row[0] for row in PARALLEL_PARK_DATA]
displacements = [row[1] for row in PARALLEL_PARK_DATA]

def get_derivative_from_data(position_data, time_data):
    # TODO - try your best to implement this code yourself!
    #        if you get really stuck feel free to go back
    #        to the previous notebook for a hint.
    if(len(position_data) != len(time_data)):
        print('Error,Data has different dimensions!')
        return None
    speed = []
    for idx in range(1,len(position_data)):
        
            dx = position_data[idx]-position_data[idx-1]
            dt = time_data[idx]-time_data[idx-1]
            speed.append(dx/dt)
    
    
    return speed
	
speeds = get_derivative_from_data(displacements, timestamps)
accelerations = get_derivative_from_data(speeds, timestamps[1:])

plt.title("x(t), v(t), a(t)")
plt.xlabel("Time (seconds)")
plt.ylabel("x (blue), v (orange), a (green)")
plt.scatter(timestamps, displacements)
plt.scatter(timestamps[1:], speeds)
plt.scatter(timestamps[2:], accelerations)
plt.show()

