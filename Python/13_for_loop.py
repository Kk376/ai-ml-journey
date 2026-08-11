# for loop
# we use range function in for loops.
# range (s,   s,   s) and that means:
#        ↓    ↓    ↓
#      start stop steps


# Printing numbers in ascending order
a = int(input("Enter starting number: "))
b = int(input("Enter destination number: "))

print("Numbers in ascending order are: \n")

for i in range(a, b, 1):
    print(i)


# Printing numbers in descending order
c = int(input("Enter starting point: "))
d = int(input("Ennter destination point: "))

print("Numbers in descending order are: \n")

for i in range(c, d, -1):
    print(i)
    

# Printing a multiplication table
num = int(input("Enter a number: "))

print("Multiplication table of the given number is: ")
for i in range(num, num * 10 + 1, num):
    print(i)


# for loop in strings

str = input("Enter string: ")
print(f"Total characters in the given string are: {len(str)}")  # Print length of string.

for i in range(len(str)):
    print(str[i])


str1 = input("Enter string: ")

for i in str1:
    print(i)


# Break and Continue

sn = int(input("Enter starting number: ")) # Starting point of the for loop.
dn = int(input("Enter destination number: ")) # Ending point of the for loop.
con = int(input("Enter which number to skip: ")) # # The for loop will skip this number and continue to its next iteration.
brk = int(input("Enter when to stop the loop: ")) # The for loop will stop here.

for i in range(sn, dn):
    if i == con:
        continue
    if i == brk:
        print("Break statement is executed.")
        break
    print(i)

else: # Else basically works with only break statement.
    print("Break statement is not executed.") 