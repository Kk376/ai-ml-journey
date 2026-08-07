# This is an example of positional arguments in functions.

def total_sum(a, b):  # def will assign memory for the function: total_sum.
    print(f"Sum of two given numbers is {a + b}")

num1 = int(input("Enter your first number: "))  # Taking input of first number.
num2 = int(input("Enter your second number: ")) # Taking input of second number.

total_sum(num1, num2) 
# Calling sum function, like we call inbuilt functions, for example -> print.
# We have passed two values in sum() function -> num1 and num2. 


# This is an example of keyword arguments in functions.

def greeting(name, age):
    print(f"Hi {name}. So you're {age} years young. Nice to meet you!")

name = input("What is your name?\n")
age = int(input("And your age?\n"))

# greeting(name, age)

# Now what if I pass age first, and name after it?

greeting(age=age, name=name)    #So, instead of default arguments, I have passed keywords.
# If I don't do it, program won't run.


# This is an example of default arguments in functions.

def difference(n1, n2 = 50):    # Here I,ve pre assigned a value to n2.
    print(f"The difference between {n1} and {n2} is {n1 - n2}")

number = int(input("Enter number: "))

difference(number)


# Practice question: Create a function to check whether a string is palindrome or not.

def palindrome(str):
    reversed_str = ""
    for i in range(len(str) - 1, -1, -1):
        reversed_str += str[i]

    if reversed_str == str:
        print(f"{str} is a palindrome.")
    else:
        print(f"{str} is not a palindrome.")
    return


palindrome("NAMAN")
palindrome("KUSHAGRA")
palindrome("RUSAMA")
palindrome("NAVEEN")
palindrome("REKHA")
palindrome("NAYAN")


# Practicing Return in functions.

def pal(st):
    rev_st = ""
    for i in range(len(st) - 1, -1, -1):
        rev_st += st[i]

    if rev_st == st:
        return f"{st} is a palindrome."
    else:
        return f"{st} is not a palindrome."

pal_str = input("Enter a string: ")
print(pal(pal_str))