import random
from random import randint

prompt = input('Do you have what it takes?')
number = int(prompt)

guesses = 0

while guesses < 3:
    computer_guess = randint(1, 10)
    print("The Computer guesses", computer_guess)

    guesses = guesses + 1

    if computer_guess == number:
        break


if computer_guess == number:
    print("Amazing! That was a lucky guess")
elif computer_guess != number:
    print('HA! I beat you!')
