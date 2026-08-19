#On the computer: Indentation / Conditional Selection 
#task 5b
print("welcome to the advanced calculator menu")
print("pick an equation to solve: ")
print ("1. schwarzchild radius")
print ("2. kinetic energy")
print ("3. potential energy")
choice = input("enter your choice (1, 2, or 3): ")
if choice == "1":
    mass = input("enter mass (kg): ")
    G_constant = 6.674*10**-11
    speed_of_C = 299792458
    Rs = (2 * float(G_constant) * float(mass)) / (speed_of_C**2)
    print("the schwarzchild radius is: "+str(Rs)+" meters")

elif choice == "2":
    mass = input("enter mass (kg): ")
    velocity = input("enter velocity (m/s): ")    
    Ke = 0.5 * float(mass) * (float(velocity)**2)
    print("the kinetic energy is: "+str(Ke)+" joules")

elif choice == "3":
    mass = input("enter mass (kg): ")
    planet = input("enter the planet (earth, moon, mars): ").lower()
    if planet == "earth":
        g = 9.81
    elif planet == "moon":
        g = 1.62
    elif planet == "mars":
        g = 3.71
    else:
        print("invalid planet selection")
        g = None

    if g is not None:
        height = input("enter height (m): ")
        Ep = float(mass) * g * float(height)
        print("the potential energy is: "+str(Ep)+" joules")
    else:
        print("cannot compute potential energy due to invalid planet selection")