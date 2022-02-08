"""A number-guessing game."""
import random

random_number = random.randint(1,100)

print ("Hello!")
name = input("What is your name?")
guess = 0

while guess != random_number:
    guess = int(input("What is your guess between 1 to 100?"))
    if guess > random_number:
        print("your guess is too high")
        continue
    elif guess < random_number:
        print("your guess is too low")
        continue
    else:
        print("You guessed correctly!")

