# Sets are mutable. 
# You can't have duplicate values in sets.
# Sets are unordered. You can't access them using index values. And if we can't access the index values, traversing won't work here. 
# Sets are semi-heterogenous. It can store some data types like string, numbers, tuples, but not everything. This happens because of hashing. 


s = {1, 2, 3, 4, 5}


# Hash

a = hash(12)
print(a)

b = hash("Kushagra")
print(b)

c = hash((1, 2, 3, 4, 5))
print(c)


# Set Methods

d = {2, 3, 4, 6}

d.add(1) # Adds an element
d.remove(6) # Removes 6 (Error if 6 is not found)
d.discard(7) # Removes 7 (No error, if 7 is not found)
# d.clear() -> Removes all elements
# d.pop() -> Removes a random element
print(d)


# Methods involving two sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# set_union = set1.union(set2) -> Combines all the different elements in a single set
set_union = set1 | set2 # Shortcut for set union

# set_intersection = set1.intersection(set2) -> Prints the common elements between the sets
set_intersection = set1 & set2 # Shortcut for set intersection

# set_difference1 = set1.difference(set2) -> Prints every element of set1 except the elements which are similar in set2
set_difference1 = set1 - set2 # Shortcut for set difference

# set_difference2 = set2.difference(set1) -> Prints every element of set2 except the elements which are similar in set1
set_difference2 = set2 - set1

# set_symmetric_difference = set1.symmetric_difference(set2) -> Removes similar elements from all sets and gives a combined set
set_symmetric_difference = set1 ^ set2 # Shortcut for symmetric difference between sets

print(set_union)
print(set_intersection)
print(set_difference1)
print(set_difference2)
print(set_symmetric_difference)


# Compound Operations

com1 = {1, 2, 3, 4, 5}
com2 = {4, 5, 6, 7, 8}

com2 -= com1

print(com2)