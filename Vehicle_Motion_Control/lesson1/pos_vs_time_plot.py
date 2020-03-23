'''
Twenty minute resolution
When looking at the odometer every 20 minutes, the data looks like this:

Time	Odometer
(miles)
2:00	30
2:20	40
2:40	68
3:00	80
But a better way to think about it for plotting is like this (note the difference in how time is represented):

Time	Odometer
(miles)
2.000	30
2.333	40
2.667	68
3.000	80
EXERCISE 1 - Make a position vs time graph of the data shown above with lines connecting adjacent dots.
Reproduce the demonstration from before using the data shown above.

'''

from matplotlib import pyplot as plt

X = [2,2.333,2.667,3]
Y = [30,40,68,80]
plt.scatter(X,Y)
plt.plot(X,Y)
plt.title("Position vs. Time on a Roadtrip")
plt.xlabel("Time (in hours)")
plt.ylabel("Odometer Reading (in miles)")
plt.show()

