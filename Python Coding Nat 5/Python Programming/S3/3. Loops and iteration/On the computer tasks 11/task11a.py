#On the computer: Input validation
#task 11a
valid = False
while valid == False:
    age = int(input("what age are you?: "))
    if age < 0 or age > 120:
        print("age invalid")
        print("Please enter an age between 0 and 120")
    else:
        valid = True
        print("age valid")