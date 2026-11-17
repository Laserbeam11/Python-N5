import random

# 2d array
gameboard = [[random.randint(0,1) for col in range(64)] for row in range(64)]

for row in range(64):
    output = ''
    for column in range(64):
        output = output + str(gameboard[row][column])
    print(output)
