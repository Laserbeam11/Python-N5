import random

def random_n():
    return random.random()

print(random_n())
input("press enter to continue")

while True:
    # 1. Generate and store the two random numbers first
    num1 = random_n()
    num2 = random_n()
    
    # 2. Print them so you can see them
    print(f"{num1} and {num2}")
    
    # 3. Compare the actual numeric values
    if num1 == num2: 
        print("same")
        break
    else:
        print()
