#On the computer: nested loops
#task 10e
x = 0
y = 0
z = 1
w = int(input("How many digits of fibonacci sequence: "))
while True:

    print(x)
    print()
    print(z)
    print()

    x = x + z
    z = z + x

    if y == w:
        break
    y = y + 1