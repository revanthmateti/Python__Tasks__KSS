#Number Guessing Game (5 Attempts)

import random
import math

number = random.randint(1, 50)

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 50.")
print("You have 5 attempts.")

for i in range(5):
    guess = int(input("Enter your guess: "))

    difference = math.fabs(number - guess)

    print("You are", difference, "away from the correct number.")

    if guess == number:
        print("Congratulations! You guessed correctly.")
        break
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

else:
    print("Sorry! You have used all 5 attempts.")
    print("The correct number was:", number)
