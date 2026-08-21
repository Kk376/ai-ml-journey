# Tuples are not mutable like lists. So we can't change values. 
# Tuples allows duplicates like lists. 
# Tuples are also ordered and can be accessed by their index values like lists. 
# Tuples also have heterogenous nature and can have multiple data types like lists. 

# Basically Tuples are lists, without being mutable. 


t = (5, 23, 5, 34, 3, 5, 65)

index = t.index(34) # Tells the index value
count = t.count(5) # Tells how many times a value has occured
print(index)
print(count)


# Tuple unpacking

a, b, c, d = (1, 2, 3, 4)

print(a)
print(b)
print(c)
print(d)


e = (1)

print(type(e)) # This will print the class as int, because there are no multiple values and variables. 
               # And after unpacking, the value is in the form of an integer. 

# To not let this happen, this is what we will do:

f = (1,) # This comma will tell python, that even after unpacking, we want this to be a tuple. 
print(type(f))