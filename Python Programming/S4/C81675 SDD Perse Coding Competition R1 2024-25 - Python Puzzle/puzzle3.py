weekday = input("Enter the week day for January 1st (MO/TU/WE/TH/FR/SA/SU): ")
leapyear = input("Is it a leap year? (y/n): ")

if weekday == "SA":
    noSaturdays = 53
elif weekday == "FR" and leapyear == "y":
    noSaturdays = 52
else:
    noSaturdays = 53

#added --
print()
#--------
print("There are",noSaturdays,"Saturdays this year.")