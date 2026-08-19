#On the computer: pre defined functions
# #task 12c

# - - - - - - - - - - - 

#On The Computer: Basic Arithmetic
#task 2b
distance_ran = int(input("distance ran in km:"))
time_taken = int(input("time taken in hours:"))
average_speed = round(distance_ran / time_taken, 2)
print("the average speed is:", average_speed, "km/h")

#On The Computer: Basic Arithmetic
#task 2c
Eng_score = int(input("english score: "))
Maths_score = int(input("maths score: "))  
computing_science_score = int(input("computing science score: "))
average_score = round((Eng_score + Maths_score + computing_science_score) / 3, 2)
print("the average score is:", average_score, "%")

#On The Computer: Basic Arithmetic
#task 2d
price_of_item = int(input("price of item: "))
discount_percentage = int(input("discount percentage: "))
discounted_price = price_of_item - round(price_of_item * discount_percentage / 100, 2)
print("the discounted price is:", discounted_price)

#On The Computer: Basic Arithmetic
#task 2e
mass = int(input("what is the mass of the object in kg (numerical no notation nor units): "))
Rs = round((2 * (6.674*10**-11) * mass) / (299792458 ** 2), 2)
print("the Schwarzschild radius of the object is:", Rs, "meters")