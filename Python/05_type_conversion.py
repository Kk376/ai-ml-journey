a = 5
a = str(a)  # This will convert the integer variable 'a' to a string variable.
print(type(a))  # This will print the data type of the variable 'a', which is now 'str'.
print(a)


b = 1
b = float(b)  # This will convert the integer variable 'b' to a float variable.
print(type(b))  # This will print the data type of the variable 'b', which is now 'float'.
print(b)  # This will print the value of the variable 'b', which is now '1.0'.


c = 2.5
c = int(c)  # This will convert the float variable 'c' to an integer variable.
print(type(c))  # This will print the data type of the variable 'c', which is now 'int'.
print(c)


# Anything that is not a zero or an empty string is considered True in Python. 
d = 1
print(bool(d))
e = "Hi"
print(bool(e))
f = 0
print(bool(f))
g = ""
print(bool(g))

# Note: Until here, we have practiced explicit type conversion. In the next section, we will practice implicit type conversion.


# Implicit type conversion is when Python automatically converts one data type to another without the need for explicit instructions from the programmer. This usually happens when performing operations between different data types.

h = 12
print(12/3)  # This will print the result of the division, which is 4.0. The integer variable 'h' is implicitly converted to a float during the division operation.
# To confirm this, let's check the data type of the result of the division operation.
print(type(12/3))  # This will print the data type of the result of the division operation, which is 'float'.