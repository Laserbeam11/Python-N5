# On The Computer: Arrays
# task 13b
x = ["" for x in range(5)]
y = ["" for y in range(5)]
z = 0

for counter in range(0, 5):
    x[counter] = input(f"Enter name:   ")
    y[counter] = int(input(f"Enter marks out of 150:   "))
    if y[counter] >= (150/100)*70:
        y[counter] = "Pass"
    else:
        y[counter] = "Fail"

while z < 5:
    print(x[z], y[z])
    print()
    z = z + 1