import time
import random
from matplotlib import pyplot as plt

''' 
Lists, Timing, and Performance¶
In this notebook we're going to explore the performance of lists. Specifically, we're going to see how the time it takes to perform a membership check on a list is affected by various properties of the list. A "membership check" is what you do when you write code like:

my_list = [1,2,3]
if 3 in my_list:
    # we just checked my_list for membership
    # of the element 3 
Let's explore the following two questions in code:

When an element IS in a list, does the location of that element (near the beginning vs near the end) impact the time it takes to perform a membership check?

When an element IS NOT in a list, does the size of the list impact the time it takes to perform a membership check?

What we find will motivate a more in depth discussion about the tradeoffs between lists and other data structures.

'''
def avg_millis_to_check_el_in_list(element, target_list, N=20):
    start = time.clock()
    for _ in range(N):
        element in target_list
    end = time.clock()
    return (end-start)*1000 / N
	
'''

Question 1
Does position in list impact the time it takes to perform a membership test?

First we're going to need to figure out how to do these timings...

'''

# now we can compare time to lookup low numbers (near the 
# beginning of the list) vs higher numbers (near the end).

# Let's use a really big list this time
list_size = 1000000
L = list(range(list_size))

# Now make three separate timings...
T_beginning = avg_millis_to_check_el_in_list(1000, L)
T_middle    = avg_millis_to_check_el_in_list(500000, L)
T_end       = avg_millis_to_check_el_in_list(999999, L)

print("T_beginning: ", T_beginning)
print("T_middle:    ", T_middle)
print("T_end:       ", T_end)

# Making a scatter plot of position in list (X-axis)
# vs. average time to find element (y-axis)

list_size = 100000
L = list(range(list_size))

# check between start and end in increments of 10000. This will
# be our X axis too!
positions = list(range(0, list_size, 10000))

# use list comprehension to generate Y-axis data!
millis = [avg_millis_to_check_el_in_list(pos, L) for pos in positions]

# first, let's look at the raw data
print("positions checked:", positions)
print("average millis:   ", millis)

# now let's make the scatter plot!
X = positions 
Y = millis
plt.scatter(X, Y)
plt.title("Membership Test Time\nvs Position in List")
plt.xlabel("Position in List")
plt.ylabel("Average # of millis / test")
plt.show()

print()

'''
Answer to Question 1
Yes! Where an element is in a list definitely impacts how long it takes to discover that the element exists in the list!

Elements near the beginning of a list are found very quickly. Elements near the end of the list take longer.
''' 

'''

Question 2
Does the size of a list impact the time it takes to test for membership of elements when they are NOT in the list?

'''

def avg_millis_to_test_for_non_existent_el(list_size, num_trials=20):
    # 1. prepare list and nonexistent element
    L = list(range(list_size))
    element = -1
    
    # 2. start the timer
    start = time.clock()
    
    # 3. repeat membership test num_trials times
    for _ in range(num_trials):
        element in L
    
    # 4. stop the timer
    end = time.clock()
    
    # 5. do the math and return the result
    millis_per_test = (end-start) * 1000 / num_trials
    return millis_per_test
	
# Let's use this function on lists of different sizes
small  = 10000
medium = 100000
large  = 1000000

T_small  = avg_millis_to_test_for_non_existent_el(small)
T_medium = avg_millis_to_test_for_non_existent_el(medium)
T_large  = avg_millis_to_test_for_non_existent_el(large)

sizes = list(range(100000, 1000000, 100000))
times = [avg_millis_to_test_for_non_existent_el(s) for s in sizes]
plt.scatter(sizes, times)
plt.xlabel("List Size")
plt.ylabel("Avg Millis")
plt.show()

'''

Answer to Question 2¶
Yes! When checking for membership of an element in a list, itt takes longer to figure out an element doesn't exist in that list when the list is big.

'''