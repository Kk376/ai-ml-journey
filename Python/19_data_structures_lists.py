# Data Structures are used to store, organize and manipulate data efficiently.
# There are 4 inbuilt data structures in Python -> List, Tuple, Dictionary & Set.
# There are custom data structures as well like Stack, Queue, Linked List, Graph, etc.
# And around these custom data structures
# There are some algorithms like searching algorithm, sorting algorithm. 
# This study is called Data Structures and Algorithms.
# We are only gonna cover inbuilt data structures for now.

# Let's look at Lists first:
# These are some keywords that are frequently used in Lists:-
# Mutable -> Object's value can be changed.
# Duplicates -> Same value can occur multiple times.
# Ordered -> Accessing elements using their positions.
# Heterogenous -> We can have multiple data types inside a list.

# Example:
a = [12, 34, 34, 3.5, True, False, "Hi Kushagra. Good luck learning Data Structures."]
print(a[6])


# List traversing and methods:

# First method, using index:
b = [12, 34, 45, 56, 34.3, 45]
for i in range(len(b)):
    print(b[i])


# Second method, using values:
c = [34, 42, 64, 234, 13, 13, 34.6]
for i in c:
    print(i)


print(dir(list))


# Append

l = [2, 3, 4, 5]
l.append(6) # Adds another value at the last of the list.
l.insert(1, 2) # Adds the value '2' at index '1'.
l.extend([7, 8, 9]) # Adds multiple values.
l.remove(9) # Remove the first occurence of a value.
l[0] = 1 # Thanks to mutability, I can change the value of any index in a list.

print(l)