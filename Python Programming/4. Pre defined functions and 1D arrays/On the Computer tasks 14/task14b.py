#On The Computer: pre defined functions
#task 14b
name = input("name: ")
name2 = input("last name: ")
DoB = input("date of birth dd/mm/yyyy: ")

print("suggested password:  ")
passwrd = str(name[0]).upper() + str(name2) + str(DoB[8]) + str(DoB[9])
print(passwrd)
