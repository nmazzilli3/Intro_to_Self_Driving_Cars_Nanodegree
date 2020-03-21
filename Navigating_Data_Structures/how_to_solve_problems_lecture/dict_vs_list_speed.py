# Run this cell first!

import time
import random
from matplotlib import pyplot as plt

def test_data_structure_speed(data_structure_type, size, N=50):
    if data_structure_type != dict:
        data_structure = data_structure_type(range(size))
    else:
        data_structure = {num: "value" for num in range(size)}
    nonexistent_element = -1
    
    start = time.clock()
    for _ in range(N):
        nonexistent_element in data_structure
    end = time.clock()
    
    millis = (end-start) * 1000
    return millis    
	
# set test
test_data_structure_speed(set, 100000, N=1000)

# list test
test_data_structure_speed(list, 100000, N=1000)

# dictionary test
test_data_structure_speed(dict, 100000, N=1000)

sizes = list(range(0, 500000, 25000))
list_speeds = [test_data_structure_speed(list, size) for size in sizes]
set_speeds  = [test_data_structure_speed(set,  size) for size in sizes]
dict_speeds = [test_data_structure_speed(dict, size) for size in sizes]

plt.scatter(sizes, list_speeds, c='g', marker="o") #green circle
plt.scatter(sizes, set_speeds,  c='r', marker="D") #red diamond
plt.scatter(sizes, dict_speeds, c='b', marker="*") #blue star

plt.xlabel("Data Structure Size")
plt.ylabel("Total Time (ms)")
plt.legend(["List", "Set", "Dictionary"])
plt.title("Comparing Membership Testing Times")
plt.show()

'''
Choosing Good Data Structures
Lists
Lists are good when:

Your data is ordered (and indexing based on position-in-list makes sense).
You need to keep track of duplicates.
Your data is mutable (dictionary keys and elements in a set must be immutable).
Sets
Sets are good for:

Fast membership testing.
Removing duplicates from a sequence.
Computing mathematical operations like intersection, union, and difference.
Dictionaries
Dictionaries are good when:

You want to associate keys with values.
You want fast key-based lookups.
'''