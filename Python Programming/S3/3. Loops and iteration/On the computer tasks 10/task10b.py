#On the computer: nested loops
#task 10b
for index in range(1,7):
    output = ''
    for things in range(0, index):
        output = output + str(index)
    print(output)
