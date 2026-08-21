# If else statemnts.

a = int(input("Enter a number: "))
if a > 10:
    print("a is greater than 10") # The space before print is called indentation. If you don't use it, program won't run.
else:
    print("a is less than or equal to 10")


money = int(input("Mom, pls give me money: "))
if money > 100:
    print("Thanks mom, I am ordering pizza")
else:
    print("Thanks mom, I will eat Maggi")


age = int(input("Enter your age: "))
if age < 18: # Highest precendence to the first if statement.
    print("You are a minor. We can't issue you a driving license")
elif age >= 18 and age < 60: # Next precedence to the elif statement. There can be multiple elif statements. They all are checked in ascending order of precedence.
    print("You are an adult. You are welcome to learn driving & get a license")
else: # Last precedence to the else statement.
    print("You are a senior citizen. You can still learn driving and get a license, but please drive safely")