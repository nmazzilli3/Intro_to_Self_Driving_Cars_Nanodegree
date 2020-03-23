'''
Integrating Rate Gyro Data
The yaw rate of a vehicle can be measured by a rate gyro.

The yaw rate gives the rate of change of the vehicle's heading in radians per second and since a vehicle's heading is usually given by the greek letter  𝜃  (theta), yaw rate is given by  𝜃˙  (theta dot).

Integrating the yaw rate gives total change in heading.
'''

from helpers import process_data, get_derivative_from_data
from matplotlib import pyplot as plt

PARALLEL_PARK_DATA = process_data("parallel_park.pickle")

TIMESTAMPS    = [row[0] for row in PARALLEL_PARK_DATA]
DISPLACEMENTS = [row[1] for row in PARALLEL_PARK_DATA]
YAW_RATES     = [row[2] for row in PARALLEL_PARK_DATA]
ACCELERATIONS = [row[3] for row in PARALLEL_PARK_DATA]

def get_integral_from_data(data, times):
    # TODO - write integration code!
    integration = []
    integration_accumulation =0
    for i in range(1, len(times)):
        
        # Delta between Data
        delta_data = data[i] 
        
        # 5. Calculate delta t
        delta_t = times[i] - times[i-1]
        
        integration_accumulation += delta_data*delta_t
        
        # 8. append to speeds and update last_time
        integration.append(integration_accumulation)

    return integration
	
# Visual Testing - Compare the result of your 
# integration code to the plot above

thetas = get_integral_from_data(YAW_RATES, TIMESTAMPS)

plt.scatter(TIMESTAMPS[1:], thetas)
plt.show()