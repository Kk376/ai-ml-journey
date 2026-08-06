# Q1. Accept two numbers from the user and display the largest number.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print(f"The larger number between {a} and {b} is: {a}")
elif a < b:
    print(f"The larger number between {a} and {b} is: {b}")
else:
    print("Both numbers are equal")


# Q2. Accept the gender from the user and display "Good Morning Sir" if the gender is male and "Good Morning Ma'am" if the gender is female.

gender = str(input("Enter gender (male/female): "))

if gender == "male":
    print("Good Morning Sir")
elif gender == "female":
    print("Good Morning Ma'am")
else:
    print("Invalid input. Please enter 'male' or 'female'.")


# Q3. Accept an integer from the user and check whether the number is even or odd.

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"{number} is an even integer")
else:
    print(f"{number} is an odd integer")

# Q4. Accept age and name from the user. Check if the user is a valid voter or not.

age = int(input("Enter your age: "))
name = str(input("Enter your name: "))

if age > 0 and age < 18 and gender == 'male':
    print(f"Mr. {name}, you are younger than 18, so you are not eligible to vote.")
elif age > 0 and age < 18 and gender == 'female':
    print(f"Ms. {name}, you are younger than 18, so you are not eligible to vote.")
elif age >= 18 and gender == 'male':
    print(f"Mr. {name}, you are eligible to vote.")
elif age >= 18 and gender == 'female':
    print(f"Ms. {name}, you are eligible to vote.")
else:
    print("Enter a valid age....")


# Q5. Check whether an year is a leap year or not.

# A leap year is divisible by 400.
# A leap year is also divisible by 4, but not 100. 
# So, despite 1900 being divisible by 4, it's not a leap year.
year = int(input("Enter year: "))

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# Q6. Take the input of temperature in celcius:
# Below 0 C -> Freezing Cold
# 0-10 C -> Very Cold
# 10-20 C -> Cold
# 20-30 C -> Pleasant
# 30-40 C -> Hot
# Above 40 C -> Very Hot


temp = float(input("Enter temperate in celcius: "))

if temp < 0:
    print(f"It's {temp} C - Freezing Cold")
elif temp >= 0 and temp <= 10:
    print(f"It's {temp} C - Very Cold")
elif temp > 10 and temp <= 20:
    print(f"It's {temp} C - Cold")
elif temp > 20 and temp <= 30:
    print(f"It's {temp} C - Pleasant")
elif temp > 30 and temp <= 40:
    print(f"It's {temp} C - Hot")
else:
    print(f"It's {temp} C - Very Hot")