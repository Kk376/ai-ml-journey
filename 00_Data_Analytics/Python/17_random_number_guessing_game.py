import random

num = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Enter your guess between 1 and 100: "))
    tries += 1
    if num == guess:
        print(f"You are right! You guessed the number in {tries} tries.")
        break
    elif num < guess:
        print("Go a little lower....")
    else:
        print("Go a little higher....")