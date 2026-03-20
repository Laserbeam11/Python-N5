#On The Computer: Basic Arithmetic
#task 2e
mass = int(input("what is the mass of the object in kg (numerical no notation nor units): "))
Rs = (2 * (6.674*10 ** -11) * mass) / (299792458 ** 2)
print("the Schwarzschild radius of the object is:", Rs, "meters")