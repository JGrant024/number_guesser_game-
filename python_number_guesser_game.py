# import random
from random import randint
from socket import ntohl

play = True

while True:
    computer = randint(1, 10)

    Guess1 = input('Guess a number between 1 and 10 ').lower()

    if int(Guess1) > computer:
        print("Try guessing lower")

    elif int(Guess1) < computer:
        print("Try guessing higher")

    elif int(Guess1) == computer:
        print('You Win!')
        break

    Guess2 = input(
        'Guess a number between 1 and 10 for the second time ').lower()

    if int(Guess2) > computer:
        print("Try guessing lower")

    elif int(Guess2) < computer:
        print("Try guessing higher")

    elif int(Guess2) == computer:
        print('You Win!')
        break
    Guess3 = input(
        'Guess a number between 1 and 10 for the last time ').lower()
    if int(Guess3) == computer:
        print('You Win!')
        break
    elif int(Guess3) != computer:
        print('You lose! The number was ' + str(computer))
        break
