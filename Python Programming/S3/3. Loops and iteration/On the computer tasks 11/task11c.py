#On the computer: nested loops
#task 11c
valid = False
while valid == False:
    year = input('Enter your year at school (1st 2nd...): ')
    if year == '':
        print("Year cannot be blank")
    elif year != "1st" and year != "2nd" and year != "3rd" and year != "4th" and year != "5th" and year != "6th":
        print("Invalid year. Please enter a valid year.")
    else:
        valid = True
        print("welcome to", year, "year")