# Q1. Print positive and negative elements of a string.

a = [2, 3, 5, 1, 7, -4, -2, -67]
pos = [] # Empty list to store positive numbers
neg = [] # Empty list to store negative numbers

for i in a:
    if i >= 0:
        pos.extend([i])
    else:
        neg.extend([i])

print(f"Positive numbers are: {pos}\n")
print(f"Negative numbers are: {neg}")


# Q2. Mean (average) of list elements.

b = [3, 4, 5, 34, 54, 23, 57, 12, 2, 4]

sum_mean = 0 # To store sum of all the numbers in the list

for i in b:
    sum_mean += i

print(f"Mean of the given list is: {sum_mean/len(b)}")


# Q3. Find the greatest element and print it's index too

c = [4, 5, 7, 2, 23, 565, -5]

greatest_element = c[0] #Assuming first element as the greatest element
index = 0

for i in range(len(c)):
    if c[i] > greatest_element:
        greatest_element = c[i]
        index = i
        
print(f"The greatest element in the given list is {greatest_element} and it's index is {index}")


# Q4. Find the second greatest element

d = [100, 45, 6, 3, 45, 34, 67]

if d[0] > d[1]:
  largest = d[0]
  sec_largest = d[1]
else:
  largest = d[1]
  sec_largest = d[0]

for i in d[2:]:
  if i > largest:
    sec_largest = largest
    largest = i
  elif i > sec_largest and i != largest:
    sec_largest = i

print(f"Second greatest element in the given list is: {sec_largest}")


# Q5. Check if the list is sorted or not

e = [45, 34, 23, 1, 54, 7]
sort = True

for i in range(len(e) - 1):
    if e[i] > e[i + 1]:
        sort = False

if sort == True:
    print("The given list is sorted.")
else:
    print("The given list is not sorted.")