# w -> Write --- Creates file or overwrite
w = open("file_handling.txt", "w")  # This 'w' will create a new file, if it doesn't exist, or overwrite the current contents of the file. 
w.write("Hello, I am Kushagra Kumar. I am learning File Handling in Python.")
w.close()

# a -> Append --- Creates or adds to the end of the file
a = open("file_handling.txt", "a")  # I am using the same file, but this time with 'a'. This will add new contents to the end of the file.
a.write(" I have already used 'w' and now I am using 'a'.")
a.close()

# r -> Read (default) --- The file must exist
r = open("file_handling.txt", "r")  # Just a variable. I've chosen 'r' because I am reading the file.
print(r.read())
r.close()

# x -> Create --- Create a new file and fails if it exists
x = open("dummy.txt", "x")  # Since this only works to make a new file, I am choosing a new name for a new file
x.write("This dummy file is created to test 'x' method in file handling")
x.close()

# Reading the file created by 'w'
x_dummy = open("dummy.txt", "r")
print(x_dummy.read())
x_dummy.close()