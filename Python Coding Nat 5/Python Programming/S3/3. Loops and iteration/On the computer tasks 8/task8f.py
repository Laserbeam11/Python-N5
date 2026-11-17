#On the computer: Loops and Iteration
#task 8f
bottles = 99
count = 0
for bottles in range(99, 0, -1):
    print(bottles, "bottles of beer on the wall")
    print(bottles, "bottles of beer")
    print("take one down, pass it around")
    print(bottles - 1, "bottles of beer on the wall")
    print()
