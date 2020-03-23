from matplotlib import pyplot as plt
import numpy as np
import warnings
import math
warnings.filterwarnings('ignore')

def show_approximate_integral(f, t_min, t_max, N):
    t = np.linspace(t_min, t_max)
    plt.plot(t, f(t))
    
    delta_t = (t_max - t_min) / N
    
    print("Approximating integral for delta_t =",delta_t, "seconds")
    box_t = np.linspace(t_min, t_max, N, endpoint=False)
    box_f_of_t = f(box_t)
    plt.bar(box_t, box_f_of_t,
            width=delta_t,
            alpha=0.5,
            facecolor="orange",
            align="edge",
            edgecolor="gray")
    plt.show()
	
def f1(t):
    return -1.3 * t**3 + 5.3 * t ** 2 + 0.3 * t + 1 
	
def integral(f, t1, t2, dt=0.1):
    # area begins at 0.0 
    area = 0.0
    
    # t starts at the lower bound of integration
    t = t1
    
    # integration continues until we reach upper bound
    while t < t2:
        
        # calculate the TINY bit of area associated with
        # this particular rectangle and add to total
        dA = f(t) * dt
        area += dA
        t += dt
    return area
	
'''
Homework 1 - Example
Compute the following integral:

∫42𝑡2𝑑𝑡
 
EXPECTED ANSWER: 18.66
'''

def f2(t):
    return t**2
	

print(integral(f2,2,4, 0.0001))
print()

show_approximate_integral(f2,2,4,20)

'''
Homework 2¶
Compute the following integral

∫2−23𝑡3−4𝑡𝑑𝑡
'''

def f3(t):
	return 3*t**3 -4*t
	
print(integral(f3,-2,2, 0.0001))
print()

show_approximate_integral(f3,-2,2,40)

def f4(t):
	num = -(((t-5)**2)/0.4)
	den = np.sqrt(2*math.pi*0.2)
	return np.exp(num)/den
	
print(integral(f4,3,7, 0.0001))
print()

show_approximate_integral(f4,3,7,50)