# Q1. Accept an integer and print Hello world num times.

num = int(input("Enter the number: "))

for i in range(num):
    print("Hello world")


# Q2. Print natural numbers up to dn (destination number).

dn = int(input("Enter destination number: "))

for i in range(1, dn + 1, 1):
    print(i)


# Q3. Reverse for loop. Print rn to 1.

rn = int(input("Enter starting number: "))

for i in range(rn, 0, -1):
    print(i)


# Q4. Take a number as input and print it's table.

t = int(input("Enter a number: "))

for i in range(t, t * 10 + 1, t):
    print(i)


# Q5. Sum up to n terms.

n = int(input("Enter a number: "))
total_sum = 0

for i in range(1, n + 1, 1):
    total_sum += i

print(f"Sum of all numbers until 'n' is: {sum}")


# Q6. Factorial of a number.

f = int(input("Enter a number: "))
fact = 1 # Can't be 0, otherwise multiplying anything with 0 will give 0.

if f < 0:
    print("Negative numbers are not defined.")
elif f == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, f + 1, 1):
        fact *= i
    print(f"Factorial of {f} is {fact}")


# Q7. Print the sum of all even and odd numbers in a range seperately.

starting_number = int(input("Enter starting number: "))
ending_number = int(input("Enter ending number: "))

sum_even = 0
sum_odd = 0

for i in range(starting_number, ending_number + 1, 1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"Sum of all even numbers in the range is: {sum_even}")
print(f"Sum of all odd numbers in the range is: {sum_odd}")


# Q8. Print all the factors of a number.

factor = int(input("Enter number: "))

for i in range(1, factor + 1):
    if factor % i == 0:
        print(i)



# Q9. Accept a number and check if it's a perfect number or not.

perfect = int(input("Enter number: "))
sum_perfect = 0

for i in range(1, perfect):
    if perfect % i == 0:
        sum_perfect += i

if sum_perfect == perfect:
    print(f"{perfect} is a perfect number.")
else:
    print(f"{perfect} is not a perfect number.")


# Q10. Check whether a number is prime or not.
# A prime number is a number greater than 1 that is divisible only by 1 and itself.
# 2 is the only even prime number.

number = int(input("Enter a number: "))

if number < 2:
    print(f"{number} is not a prime number.")
elif number == 2:
    print(f"{number} is a prime number.")
elif number % 2 == 0:
    print(f"{number} is not a prime number.")
else:
    prime = True # Assuming the number is prime.

    for i in range(3, number, 2):
        if number % i == 0:
            prime = False
            break # breaking the loop as soon as it finds a divisor.

if prime == True:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# Q11. Reverse a string without using inbuilt functions.

str = input("Enter the string you want to reverse: ")
reversed_str = ""

for i in range(len(str) - 1, -1, -1):
    reversed_str += str[i]

print(reversed_str)


# Q12. Check string is palindrome or not.

pal = input("Enter string: ")
reversed_pal = ""

for i in range(len(pal) - 1, -1, -1):
    reversed_pal += pal[i]

if pal == reversed_pal:
    print("This is a Palindrome.")
else:
    print("This is not a Palindrome.")


# Q13. Count all letters, numbers and special characters from the given string.
# Example output: Chars = x, Digits = y and Symbols = z. 'x', 'y' and 'z' are the random counts of the things.

random_string = input("Enter string: ")    # Random String

char = 0    # Initializing characters count to 0
digit = 0   # Initializing digits count to 0
sp_chr = 0  # Initializing special characters count to 0

for i in random_string:
    if i.isalpha():         # isalpha is used to count alphabets
        char += 1
    elif i.isdigit():       # isdigit is used to count numbers
        digit += 1
    else:
        sp_chr += 1         # There is nothing like the other two for special characters. So, I've used sp_chr for the last else statement.

print(f"Chars = {char}, Digits = {digit} and Symbols = {sp_chr}")