# Keywords and their puropose:

# Try -> Wrap the block of code that might cause an exception
# Except -> Handles the exception if it occurs
# Else -> Run code only if no exception errors
# Finally -> Run code no matter what, whether there's an exception or not
# Raise -> Manually throws an exception

# Division by Zero error:
a = int(input("Enter your number: "))   # Taking input from the user

try:
    print(10 / a)   # Dividing 10 by the user's number
except ZeroDivisionError:   # Dividing by 0 causes error in Python. That is why, we are using try and expect to have no errors.
    print("Sorry, you can't divide by 0")   # This print function will only run, if user inputs 0 as a divisor. 

print("The code is executed.")


# Random Error:
b = int(input("Enter a number: "))

try:
    print(10 / b)
except Exception as err:    # Here we have made a variable named 'err' where the error information will be stored. 
    print(f"Sorry, there is an error -> {err}")

print("The code is executed.")


# Another example:
c = input("Enter your number: ")    # Here we are taking a string as input, instead of a number

try:
    print(10 / c)   # We know, that a number can't be divided by a string or vice versa. 
except Exception as err:
    print(f"Sorry, there is an error -> {err}")

print("The code is executed. ")


# Example of else:
d = int(input("Enter your number: "))

try:
    print(10 / d)
except Exception as err:
    print(f"Sorry, there is an error -> {err}")
else:
    print("Good, there is no exception")    # This else block will run, if there is no error

print("The code is executed.")


# Example of finally:
e = int(input("Enter your number: "))

try:
    print(10 / e)
except Exception as err:
    print(f"Sorry, there is an error -> {err}")
else:
    print("Good, there is no exception")
finally:
    print("I'll run no matter what. I don't care if there's an error or not. I am a sigma, a chad!")

print("The code is executed.")


# Example of raise:
age = int(input("Enter your age: "))

try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be between 10 to 18")
    else:
        print("Welcome to the club!")
        print("The club will start soon....")

except Exception as err:
    print(f"An error occured -> {err}")
    print("Sorry, you can't join the club")