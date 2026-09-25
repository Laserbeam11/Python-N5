def scenario1():
    # Scenario 1: Create a program design that calculates the total meal cost at a restaurant, including tips.
    choice = []
    
    num_dishes = int(input("enter total number of items ordered ordered: "))
    for i in range(num_dishes):
        print("Dish", i + 1)
        print("1. Hong kong style sweet and sour chicken - £5.50")
        print("2. Portion of noodles - £1.50")
        print("3. chinese Tea for 4 - £4.00")
        print("4. Glass of water - £0.50")

        user_choice = input("Please enter your choice (1 - 4): ")
        if user_choice == "1":
            choice.append(5.50)
        elif user_choice == "2":
            choice.append(1.50)
        elif user_choice == "3":
            choice.append(4.00)
        elif user_choice == "4":
            choice.append(0.50)
    
    total_cost = sum(choice)

    print("tip %: 10%")
    tip_percentage = 1.10
    
    tip_amount = total_cost * tip_percentage
    print("Total cost including tip: £" + str(round(tip_amount, 2)))

    #pseudocode
    # START
    # create array for choice
    
    # ask for and store number of dishes
    # repeat for number of dishes
    #     label which dish is being ordered
    #     display options
    #     (1. Hong kong style sweet and sour chicken - £5.50
    #     2. Portion of noodles - £1.50
    #     3. chinese Tea for 4 - £4.00
    #     4. Glass of water - £0.50)

    #     ask for and store the user's choice
    #     if user_choice is 1
    #         add choice array with 5.50
    #     elif user_choice is 2
    #         add choice array with 1.50
    #     elif user_choice is 3
    #         add choice array with 4.00
    #     elif user_choice is 4
    #         add choice array with 0.50
    
    # the total cost is equal to the sum of the choice array

    # store and display the tip percentage

    # calculate tip amount 
    # display tip amount rounded to 2 decimal places