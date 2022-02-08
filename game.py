"""A number-guessing game."""

import random

random_number = random.randint(1,100)

name = input("What is your name? ")
print(f"Hello {name}!")
guess = 0
number_of_guesses = 0

while guess != random_number:
    guess = input("What is your guess between 1 to 100? ")
    try:
        guess = int(guess)
        if guess > 100 or guess <0:
            print("Your guess is out of range. Try again.")
        elif guess > random_number:
            print("Your guess is too high. Try again.")
            number_of_guesses += 1
        elif guess < random_number:
            print("Your guess is too low. Try again.")
            number_of_guesses += 1
        else:
            print(f"You guessed correctly! It took you {number_of_guesses} guesses.")
    except ValueError:
        print("This is not a number, try again.")