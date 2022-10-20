from random import randint


def play_user():
    player = int(input('Pick a number from 1 to 10'))

    high = 10
    low = 1
    count = 0

    while True:
        count += 1
        computer = (high + low) // 2
        if computer > player:
            high = computer - 1
            print(f'computer guessed {computer}')
        elif computer < player:
            low = computer + 1
            print(f'computer guessed {computer}')
        elif computer == player:
            print(f'computer guessed {computer}')
            print('Computer found the number', player, 'in', count, 'moves')
            break


if __name__ == "__main__":
    # execute only if run as a script
    play_user()
