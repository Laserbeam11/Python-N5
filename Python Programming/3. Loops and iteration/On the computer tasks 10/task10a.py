#On the computer: nested loops
#task 10a
sub = "-" * 20
for index in range(0, 4):
    person = str(input("person: "))
    calories = 0
    for index2 in range(0, 3):
        calories = calories + int(input("calories: "))
    print(calories, "calories for", person)
    print(sub)