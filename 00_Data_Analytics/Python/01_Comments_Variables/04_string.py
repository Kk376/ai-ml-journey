# String takes more memory than int and float.

a = 'A' # This is a string variable that holds the value 'A'.
print(a)    # This will print the value of the variable 'a'.
print(ord(a))  # This will print the ASCII value of the character 'A', which is 65.

b = '😊'    # This is a string variable that holds the value '😊'.
print(b)    # This will print the value of the variable 'b'.
print(ord(b)) # This will print the Unicode value of the character '😊', which is 128578.

c = 128579
print(chr(c))  # This will print the character corresponding to the Unicode value 128579, which is '😊'.


# Indexing
# Indexing is used to access individual characters in a string.

d = "Hello, Kushagra!"  # This is a string variable that holds the value "Hello, Kushagra!".
print(d[0])  # 0 denotes the first character of the string, which is 'H'.

# Slicing
# Slicing is used to access a range of characters in a string.

e = "Hello, Kushagra!"
print(e[0:5:1])  # This will print the characters from index 0 to 4, so 5 characters in total, which is 'Hello'. Basically index end + 1 is used for slicing.
# 1 is the step value. Let's understand this by an example: Stairs. We can go up the stairs one step at a time or two steps at a time. Similarly, we can access the characters in a string one character at a time or two characters at a time. If we use 1 as the step value, we will access the characters one character at a time. If we use 2 as the step value, we will access the characters two characters at a time.

print(e[7:11:1])    # So, starting number of index is not included in the output. Here, 7 is treated as 0 and 11 is treated as 8. So, the output will be 'Kush'. Total 4 characters are printed.

print(e[7::1])  # :: is used to access all the characters from the starting index to the end of the string. Here, 7 is treated as 0 and the output will be 'Kushagra!'. Total 9 characters are printed.

print(e[::])  # Everything is printed. Total 16 characters are printed.