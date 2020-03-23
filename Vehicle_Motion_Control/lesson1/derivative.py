'''
Understanding the Derivative
You just saw these three statements.

Velocity is the instantaneous rate of change of position
Velocity is the slope of the tangent line of position
Velocity is the derivative of position
But there's another, more formal (and mathematical) definition of the derivative that you're going to explore in this notebook as you build an intuitive understanding for what a derivative is.

BEFORE YOU CONTINUE
This notebook is a long one and it really requires focus and attention to be useful. Before you continue, make sure that:

You have at least 30 minutes of time to spend here.
You have the mental energy to read through math and some (occasionally) complex code.

'''

'''
Outline¶
In this notebook we are going to unpack this definition by walking through a series of activities that will end with us defining a python function called approximate_derivative. This function will look very similar to the math shown above.

A rough outline of how we'll get there:

Discrete vs Continuous Motion - A quick reminder of the difference between discrete and continuous motion and some practice defining continuous functions in code.

Plotting continuous functions - This is where you'll see plot_continuous_function which is a function that takes another function as an input.

Finding derivatives "by hand" - Here you'll find the velocity of an object at a particular time by zooming in on its position vs time graph and finding the slope.

Finding derivatives algorithmically - Here you'll use a function to reproduce the steps you just did "by hand".

OPTIONAL: Finding the full derivative - In steps 3 and 4 you actually found the derivative of a function at a particular time, here you'll see how you can get the derivative of a function for all times at once. Be warned - the code gets a little weird here.

'''

'''
1 - Discrete vs Continuous Motion¶
The data we deal with in a self driving car comes to us discretely. That is, it only comes to us at certain timestamps. For example, we might get a position measurement at timestamp t=352.396 and the next position measurement at timestamp t=352.411. But what happened in between those two measurements? Did the vehicle not have a position at, for example, t=352.400?

Of course not!

Even though the position data we measure comes to us discretely, we know that the actual motion of the vehicle is continuous.

Let's say I start moving forwards from x=0 at t=0 with a speed of  2𝑚/𝑠 . At t=1, x will be 2 and at t=4, x will be 8. I can plot my position at 1 second intervals as follows:
'''

from matplotlib import pyplot as plt

t = [0,1,2,3,4]
x = [0,2,4,6,8]

plt.scatter(t,x)
plt.show()

'''
This graph above is a discrete picture of motion. And this graph came from two Python lists...

But what about the underlying continuous motion? We can represent this motion with a function  𝑓  like this:

𝑓(𝑡)=2𝑡
 
How can we represent that in code?

A list won't do! We need to define (surprise, surprise) a function!
'''
def position(time):
    return 2*time
	
print("at t =", 0, "position is", position(0))
print("at t =", 1, "position is", position(1))
print("at t =", 2, "position is", position(2))
print("at t =", 3, "position is", position(3))
print("at t =", 4, "position is", position(4))

'''
2 - Plotting Continuous Functions
Now that we have a continuous function, how do we plot it??

We're going to use numpy and a function called linspace to help us out. First let me demonstrate plotting our position function for times between 0 and 4.

'''
import numpy as np

t = np.linspace(0, 4)
x = position(t)

plt.plot(t, x)
plt.show()

def position_b(time):
    return -4.9 * time ** 2 + 30 * time

def plot_continuous_function(function, t_min, t_max):
    t = np.linspace(t_min, t_max)
    x = function(t)
    plt.plot(t,x)

plot_continuous_function(position_b, 0, 6.12)
plt.show()

def approximate_derivative(f, t):
    # 1. Set delta_t. Note that I've made it REALLY small.
    delta_t = 0.00001
    
    # 2. calculate the vertical change of the function
    #    NOTE that the "window" is not centered on our 
    #    target time anymore. This shouldn't be a problem
    #    if delta_t is small enough.
    vertical_change = f(t + delta_t) - f(t)
    
    # 3. return the slope
    return vertical_change / delta_t

deriv_at_3_point_45 = approximate_derivative(position_b, 3.45)
print("The derivative at t = 3.45 is", deriv_at_3_point_45)