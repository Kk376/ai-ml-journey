# This is basically hashmap. We call it dictionary in Python. 
# Dictionaries are semi mutable. We can't change Keys, but we can change values inside a key.
# Dictionaries can have duplicates, but only as values. Keys have to be unique. 
# Dictionaries follow insertion order. Basically Keys will work as index. 
# Dictionaries are also heterogenous. We can have different types of keys and values like integers, strings, lists or even another dictionary. 

d = {1:"Kushagra", 12:45}
#    ↟     ↟        ↟  ↟
#   Key  Value    Key Value -> This combo of Keys and Values is basically a Dictionary or Hashmap.

print(type(d))


a = {10:10, 20:200, 30:300}
a[10] = 100 # Updating value of Key 10 from 10 to 100
a[40] = 400 # Since Key 40 doesn't exist, Python will auto create it with the value of 400
a.update({50:500}) # Adding a new key 50 and it's value 500 using update

print(a)


# Traverse in dictionaries

# First way
for i in a:
    print(a[i])

# Second way
for i in a.values():
    print(i)
