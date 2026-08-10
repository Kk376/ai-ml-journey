# Write a Python script to merge two dictionaries

d1 = {10:100, 20:200, 30:200}
d2 = {30:300, 40:400, 50:500}

for i in d2:
    d1[i] = d2[i]

print(d1)


# Write a Python program to sum all the values in a dictionary

a = {10:100, 20:200, 30:300}

sum = 0

for i in a:
    sum += a[i]

print(sum) 


# Count the frequency of each element

b = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 9]

d = {}

for i in b:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print(d)


# Write a Python program to combine two dictionaries by adding two values of common keys

dt1 = {10:100, 20:200, 30:100}
dt2 = {30:200, 40:400, 50:500}

for i in dt2:
    if i in dt1.keys():
        dt1[i] += dt2[i]
    else:
        dt1[i] = dt2[i]

print(dt1)