# get name from user
# get age from user
# WHILE age is less than 11 OR greater than 18
# 	prompt user to try again
# 	get age from user
# ENDWHILE
# display personalised message allowing user to enter talent show

name = input("Enter your name: ")
age = int(input("Enter your age: "))
while age < 11 or age > 18:
    print("Invalid age")
    age = int(input("Please enter a valid age: "))
print(f"welcome {name}, you are eligible to enter the talent show!")