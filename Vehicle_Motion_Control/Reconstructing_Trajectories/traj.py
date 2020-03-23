from helpers import process_data
import solution
from math import sin, cos, pi

'''
The Point of this Project!
Data tells a story but you have to know how to find it!

Contained in the data above is all the information you need to reconstruct a fairly complex vehicle trajectory. After processing this exact data, it's possible to generate this plot of the vehicle's X and Y position:

Data Explained
timestamp - Timestamps are all measured in seconds. The time between successive timestamps ( Δ𝑡 ) will always be the same within a trajectory's data set (but not between data sets).

displacement - Displacement data from the odometer is in meters and gives the total distance traveled up to this point.

yaw_rate - Yaw rate is measured in radians per second with the convention that positive yaw corresponds to counter-clockwise rotation.

acceleration - Acceleration is measured in  𝑚/𝑠𝑠  and is always in the direction of motion of the vehicle (forward).

NOTE - you may not need to use all of this data when reconstructing vehicle trajectories.

Your Job
Your job is to complete the following functions, all of which take a processed data_list (with 𝑁 entries, each Δ𝑡 apart) as input:

get_speeds - returns a length 𝑁 list where entry 𝑖 contains the speed (𝑚/𝑠) of the vehicle at 𝑡=𝑖×Δ𝑡

get_headings - returns a length 𝑁 list where entry 𝑖 contains the heading (radians, 0≤𝜃<2𝜋) of the vehicle at 𝑡=𝑖×Δ𝑡
get_x_y - returns a length 𝑁 list where entry 𝑖 contains an (x, y) tuple corresponding to the 𝑥 and 𝑦 coordinates (meters) of the vehicle at 𝑡=𝑖×Δ𝑡

show_x_y - generates an x vs. y scatter plot of vehicle positions.

'''

def get_speeds(data_list):
    TIMESTAMPS    = [row[0] for row in data_list]
    DISPLACEMENTS = [row[1] for row in data_list]
    if len(TIMESTAMPS) != len(DISPLACEMENTS):
        raise(ValueError, "Data sets must have same length")    
    speed = []
    speed.append(0.0)
    for idx in range(1,len(TIMESTAMPS)):   
        dx = DISPLACEMENTS[idx]-DISPLACEMENTS[idx-1]
        dt = TIMESTAMPS[idx]-TIMESTAMPS[idx-1]
        speed.append(dx/dt)
    return speed

def get_headings(data_list):
    #get_headings - returns a length  𝑁  list where entry  𝑖  
    #contains the heading (radians,  0≤𝜃<2𝜋 ) of the vehicle at  𝑡=𝑖×Δ𝑡
    TIMESTAMPS    = [row[0] for row in data_list]
    YAWRATE = [row[2] for row in data_list]
    heading = []
    heading.append(0) 
    theta =0
    if len(TIMESTAMPS) != len(YAWRATE):
        raise(ValueError, "Data sets must have same length")     

    for idx in range(1,len(TIMESTAMPS)):   
        
        dt = TIMESTAMPS[idx]-TIMESTAMPS[idx-1]
        dtheta = YAWRATE[idx]*dt 
        theta += dtheta 
        theta %= 2*pi
        heading.append(theta)
    
    return heading

def get_x_y(data_list):
    #get_x_y - returns a length  𝑁  list where entry  𝑖  contains an (x, y) 
    #tuple corresponding to the  𝑥  and  𝑦 
    #coordinates (meters) of the vehicle at  𝑡=𝑖×Δ𝑡
    TIMESTAMPS    = [row[0] for row in data_list]
    DISPLACEMENTS = [row[1] for row in data_list]
    YAW_RATES     = [row[2] for row in data_list]
    ACCELERATIONS = [row[3] for row in data_list]
    
    headings = get_headings(data_list)
    speed = get_speeds(data_list)
    coords = tuple([0.0,0.0])
    x_y_coords = []
    x_y_coords.append(coords)
    x = 0.0
    y =0.0
    hypot = 0
    for idx in range(1,len(TIMESTAMPS)):
        dt = TIMESTAMPS[idx] - TIMESTAMPS[idx-1]
        hypot = speed[idx]*dt
        dx = cos(headings[idx])*hypot
        dy = sin(headings[idx])*hypot
        x += dx
        y += dy
        coords = tuple([x,y])
        x_y_coords.append(coords)

    
    return x_y_coords
    

def show_x_y(data_list, increment=1):
    XY = get_x_y(data_list)
    headings = get_headings(data_list)
    X  = [d[0] for d in XY]
    Y  = [d[1] for d in XY]
    h_x = np.cos(headings)
    h_y = np.sin(headings)
    Q = plt.quiver(X[::increment],
                   Y[::increment],
                   h_x[::increment],
                   h_y[::increment],
                   units='x',
                   pivot='tip')
    qk = plt.quiverkey(Q, 0.9, 0.9, 2, r'$1 \frac{m}{s}',
                       labelpos='E', coordinates='figure')
    plt.show()
	
from testing import test_get_speeds, test_get_x_y, test_get_headings

test_get_speeds(get_speeds)

print()

test_get_headings(get_headings)

print()

test_get_x_y(get_x_y)