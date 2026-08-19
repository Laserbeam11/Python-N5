#On the computer: nested loops
#task 11d
validation = False
name_valid = False
age_valid = False
gender_valid = False
while validation == False:

    while name_valid == False:
        name = input('Enter your name: ')
        if name == '':
            print("Name cannot be blank")
        else:
            name_valid = True
            print()
    while age_valid == False:
        age = int(input("Enter your age: "))
        if age < 0 or age > 120:
            print("Age must be between 0 and 120")
        else:
            age_valid = True
            print()

    while gender_valid == False:
        gender = input("Enter your gender: ")
        if gender == '':
            print("Gender cannot be blank")
        elif gender != "male" and gender != "female":
            print("Gender must be either male or female")
        else:
            gender_valid = True
            print()

    print("welcome", name)
    validation = True