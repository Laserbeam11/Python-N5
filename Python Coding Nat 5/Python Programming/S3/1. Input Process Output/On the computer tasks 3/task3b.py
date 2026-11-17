no_people = int(input("Enter the number of people: "))
bill = float(input("Enter the total bill amount: "))
tip = 1.10
totalTip = bill * tip
print("Total tip amount: £" + str(round(totalTip, 2)))
tipPerPerson = totalTip / no_people
print("Tip per person: £" + str(round(tipPerPerson, 2)))