#On the computer: And / OR
#task 6a
name = input("enter your name: ")
age = int(input("enter your age: "))
if age < 11 and age > 4:
    print("you are in primary school")
elif age < 17 and age > 12:
    print("you are in High school")
else:
    print("you are in college or a baby")