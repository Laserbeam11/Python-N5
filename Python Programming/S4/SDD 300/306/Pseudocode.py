import random

def menu():
    print("selection menu")
    print("=" * 68)
    print("scenario 1: menu")
    print("scenario 2: random game")
    print("scenario 3: temperature converter")
    print("scenario 4: empty")
    choice_scenario = int(input("enter choice (1-4): "))
    if choice_scenario == 1:
        scenario1()
    elif choice_scenario == 2:
        scenario2()
    elif choice_scenario == 3:
        scenario3()
    elif choice_scenario == 4:
        scenario4()

def scenario1():
    # Scenario 1: Create a program design that calculates the total meal cost at a restaurant, including tips.
    choice = []
    num_dishes = int(input("enter total number of items ordered: "))
    for i in range(num_dishes):
        print("Dish", i + 1)
        print("1. Hong kong style sweet and sour chicken - £5.50")
        print("2. Portion of noodles - £1.50")
        print("3. Chinese Tea for 4 - £4.00")
        print("4. Glass of water - £0.50")
        user_choice = int(input("Please enter your choice (1 - 4): "))
        if user_choice == 1:
            choice.append(5.50)
        elif user_choice == 2:
            choice.append(1.50)
        elif user_choice == 3:
            choice.append(4.00)
        elif user_choice == 4:
            choice.append(0.50)
    total_cost = sum(choice)
    print("tip %: 10%")
    tip_amount = total_cost * 1.10
    print("Total cost including tip: £" + str(round(tip_amount, 2)))
    print()
    menu()

    #pseudocode
    # create array for choice
    
    # ask for and store number of dishes
    # repeat for number of dishes
    #     label which dish is being ordered
    #     display options

    #     ask for and store the user's choice
    #     if user_choice is 1
    #         add choice array with 5.50
    #     if user_choice is 2
    #         add choice array with 1.50
    #     if user_choice is 3
    #         add choice array with 4.00
    #     if user_choice is 4
    #         add choice array with 0.50
    
    # the total cost is equal to the sum of the choice array

    # store and display the tip percentage

    # calculate tip amount 
    # display tip amount rounded to 2 decimal places

def scenario2():
    # Scenario 2: Design a simple game where the user guesses a random number between 1 and 100.
    number = random.randint(1, 100)
    guess = 0
    while guess != number:
        guess = int(input("guess a number between 1 to 100: "))
        if guess == number:
            print("well done")
        else:
            print("incorrect")
    print()
    menu()

    #pseudocode
    # number equals random number between 1 - 100
    # guess equals 0
    # while guess is not equal to number

    #     ask for and store user's guess
    #     if guess equals number
    #         display well done 
    #     else
    #         display incorrect
    #         break line

def scenario3():
    # Scenario 3: Create a program that converts temperature from Celsius to Fahrenheit or vice versa based on user choice.
    print("temperature converter")
    temp = float(input("enter temperature: "))
    f_c = input("Fahrenheit or Celsius (F / C): ").strip().upper()
    if f_c == 'C':
        converted = (temp * (9 / 5)) + 32
        print("Converted temperature in Fahrenheit:", round(converted, 2))
    elif f_c == 'F':
        converted = (temp - 32) * (5 / 9)
        print("Converted temperature in Celsius:", round(converted, 2))
    else:
        print("invalid input")
    print()

    menu()

    # display temperature converter
    # ask for and store temp 
    # ask for and store if F or C
    # if f_c reads C
    #     calculated converted temperature (C -> F)
    #     display Converted temperature in Fahrenheit: converted number rounded to 2 decimal places

    # if f_c reads F
    #     calculated converted temperature (F -> C)
    #     display Converted temperature in Celsius: converted number rounded to 2 decimal places
    # else
    #     display invalid input
    # break line

def scenario4():
    numbers = []
    print("Average Number Calculator")

    n = int(input("How many numbers are there: "))

    for i in range(n):
    
        x = float(input(f"Number {i + 1}: "))
        numbers.append(x)


    if n > 0:
        average = sum(numbers) / n
        print(f"The average is: {average}")
    else:
        print("No numbers were entered.")
    print()
    menu()

    # make array for numbers
    # display Average Number Calculator

    # ask for and store number of numbers

    # repeat for number of numbers
    
    #     ask for and store number
    #     store number in numbers array


    # if n is greater than 0
    #     average equals the sum of numbers divided by number of numbers
    #     display average
    # else
    #     display No numbers were entered
    # break line


menu()