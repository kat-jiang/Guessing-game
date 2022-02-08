"""A number-guessing game."""
import random

random_number = random.randint(1,100)

print ("Hello!")
name = input("What is your name?")
guess = 0
number_of_gusses = 0

while guess != random_number:
    guess = input("Hi What is your guess between 1 to 100?")
    try:
        guess = int(guess)
    except:
        print("This is not a number, try again.")
        continue
    if guess > 100:
        print("your guess is out of range")
        continue 
    elif guess > random_number:
        print("your guess is too high")
        number_of_gusses += 1
        continue
    elif guess < random_number:
        print("your guess is too low")
        number_of_gusses += 1
        continue
    else:
        print(f"You guessed correctly! It took you {number_of_gusses} guesses.")
