#On The Computer: Arrays
#task 13a
y = 0
x = ["" for x in range(5)]
for counter in range(0, 5):
    
    x[counter] = int(input(f"Enter number for list {counter + 1}:"))
while y < 5:
    print(x[y])
    y = y + 1