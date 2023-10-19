import random

number = random.randint(1, 25)

guess = 0

while guess != number:
    print("Guess a number between 1 and 25!")
    guess = int(input("Please enter a number:"))
    if guess < number:
        print("Increase your number")
    elif guess > number:
        print("Decrease your number")
    else:
        print("You Won!")
