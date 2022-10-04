player = int(input('Pick a number from 1 to 10'))
computer = 0
high = 10
low = 1
count = 0

while computer != player:
    count += 1
    computer = (high + low) // 2
    if computer > player:
        high = computer - 1
    elif computer > player:
        low = computer + 1
    else:
        print('Computer found the number', player, 'in', count, 'moves')
