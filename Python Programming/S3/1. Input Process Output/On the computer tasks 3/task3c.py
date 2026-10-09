loan = float(input("Enter the loan amount: "))
monthsUntilPayback = int(input("Enter the number of months until payback: "))
interest = 1.15
interestAmount = loan * (interest ** monthsUntilPayback)
print("Total interest amount: £" + str(round(interestAmount, 2)))