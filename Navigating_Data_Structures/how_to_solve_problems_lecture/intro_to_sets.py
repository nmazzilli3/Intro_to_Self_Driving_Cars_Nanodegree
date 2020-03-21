'''
The Power of Sets
The set is inspired by a branch of mathematics called set theory.

The thing that makes sets so useful is that they allow us to take advantage of "Venn Diagram logic".

For example, consider two sets. primes, which contains the prime numbers less than 10. And odds which contains the odd numbers below 10. A good way to think about the relationship between these sets is with a Venn Diagram

'''

# Initializing two sets

odds   = set([1,3,5,7,9])
primes = set([2,3,5,7])

# Demonstration of the "intersection" between two sets
# The intersection corresponds to the overlapping region
# in the Venn Diagram above.

odd_AND_prime = odds.intersection(primes)
print(odd_AND_prime)

print()

# Demonstration of the "union" of two sets. The union
# of sets A and B includes ANY element that is in A OR B 
# or both.

odd_OR_prime = odds.union(primes)
print(odd_OR_prime)

print()

# Demonstration of the "set difference" between two sets.
# What do you expect odds-primes to return?

odd_not_prime = odds - primes
print(odd_not_prime)

# Another demo of "set difference"

prime_not_odd = primes - odds
print(prime_not_odd)

'''

Union vs Intersection
The union of two sets A and B contains elements that are in A or B or both. The intersection contains elements that are in both.

'''

'''
set_b - set_a
TODO - Exercise: A or B but not both
Write a function that takes two sets (set_a and set_b) as input and returns a new set which contains elements that are either in set_a OR set_b but not in both.

In the Venn Diagram above this would include everything in the diagram EXCEPT the overlapping middle area. In this case that would be the numbers 9, 1, and 2

NOTE - Try to use all of the following set operations in your answer:

intersection
union
difference

'''

def a_or_b_but_not_both(set_a, set_b):
    """Returns a set which contains any element that is 
    a member of set_a OR a member of set_b but NOT a member
    of both."""
    #What is in both groupa
    seta_AND_setb = set_a.intersection(set_b)
    # Demonstration of the "union" of two sets. The union
    # of sets A and B includes ANY element that is in A OR B 
    # or both.

    seta_OR_setb = set_a.union(set_b)  
    diff = seta_OR_setb - seta_AND_setb
    return diff

# testing code
assert a_or_b_but_not_both(odds, primes) == set([9,1,2])
print("Nice job! Your function works correctly!")
print() 

def consolidate_labels(t1_labels, t2_labels):
    """
    Combines labels from two tickets without duplication.
    
    Given t1_labels and t2_labels (both lists), return 
    a consolidated list of labels without duplicates.
    """
    
    # TODO - rewrite this function to use sets. You should
    #   be able to replace all the code below with 1 or 2
    #   lines if you use sets appropriately.
    # 
    # NOTE - to convert a set back to a list, you can
    #   use the list() function (demonstrated in the
    #   cell below).
    
    
    t1_labels_as_set = set(t1_labels)
    t2_labels_as_set = set(t2_labels)
    combined = t1_labels_as_set.union(t2_labels_as_set)
    return list(combined)


# testing code
labels_1 = ["python", "bug", "localization", "bug"]
labels_2 = ["planning", "localization"]

combined_labels = consolidate_labels(labels_1, labels_2)

assert( set(combined_labels) == set(["python", "bug", 
                                     "localization", "planning"]))
print("Nice job! Your consolidate_labels function works correctly!")

'''
https://docs.python.org/3/tutorial/datastructures.html#sets
'''
