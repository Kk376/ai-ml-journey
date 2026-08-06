# Logical Operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# Logical AND operator
print(a > b and c == d) # Returns True if both conditions are true, otherwise returns False.
print(a > b and c != d)
print(a < b and c == d)
print(a < b and c != d)

# Logical OR operator
print(a > b or c == d) # Returns True if at least one condition is true, otherwise returns False.
print(a > b or c != d)
print(a < b or c == d)
print(a < b or c != d)

# Logical NOT operator
print(not(a > b)) # Basically reverses the result of the condition. 
# True becomes False and False becomes True.
print(not(a < b))