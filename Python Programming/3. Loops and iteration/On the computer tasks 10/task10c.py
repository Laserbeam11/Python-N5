#On the computer: nested loops
#task 10c
for index in range(1,6):
    output = ''
    for things in range(5, 0,-1):
            if things == index:
                output = output + str(index)
            else:
                 output = output + '.'
    print(output)