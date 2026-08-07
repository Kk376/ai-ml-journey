# Q1. Seperate each digit of a new and print it on a new line.

a = int(input("Enter a number: "))

while a > 0:
    print(a % 10)   # To extract the digits, as remainder, one by one.
    a //= 10        # To stop the loop when a = 0.


# Q2. Accept a number and print it's reverse.

b = int(input("Enter a number: "))

rev = 0

while b > 0:
    rev = rev * 10 + b % 10
    b //= 10

print(rev)


# Q3. Accept a number and check if it's a palindromic number.

pal_num = int(input("Enter a number: "))
og_num = pal_num    # Basically a copy.
rev_pal_num = 0

while pal_num > 0:
    rev_pal_num = rev_pal_num * 10 + pal_num % 10
    pal_num //= 10

if og_num == rev_pal_num:
    print(f"{og_num} is a palindrome number.")
else:
    print(f"{og_num} is not a palindrome number.")


