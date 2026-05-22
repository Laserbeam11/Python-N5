#On the computer: Loops and Iteration
#task 9b
import random
random_number = random.randint(1, 100000)
guesses = 0
G = False
print("guess a number between 1 and 100000")
while G == False:
    guess = int(input("enter your guess: "))
    if guess == random_number:
        print("correct")
        G = True
    elif guess < random_number:
        print("too low")
        guesses += 1
    elif guess > random_number:
        print("too high")
        guesses += 1
    else:
        print("incorrect")
        guesses += 1

print("the number was " + str(random_number))
print("you got it in " + str(guesses) + " guesses")