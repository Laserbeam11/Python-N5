#random Game
import random
print("welcome to the statistacly impossible game of guessing the same random number as the computer")
print("the chance of this happening is 1 in",1/(2**53))
print("or in engligh, statistically impossible")
input("press enter to continue")

while True:
    guess = float(input("guess a 16 decimal place random number between 0 and 1: "))
    number = float(random.random())
    if guess == number:
        print("how")
        break
    else:
        print("point proven")
        print("it was", number)