# Write a program which asks the user to enter their name and the 
# school house they belong to. Acceptible data for the school house
# is either Stuart, Forbes, Douglas or Gordon and any other input
# should be rejected. Once a valid school house has been entered 
# the program should add the user’s name and school house to a 1D
# array and display this on the screen.

name = input("what's your name? ")
house = input("which school house do you go to? ")

valid_houses = ["stuart", "forbes", "douglas", "gordon"]
while house.lower() not in valid_houses:
    print("Invalid school house")
    house = input("Please enter a valid school house: ")

user_data = [name, house]
print(f"name: {user_data[0]} | school house: {user_data[1]}")