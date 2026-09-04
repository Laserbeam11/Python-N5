#Lesson 11c Project
header = "=" * 68
x = 0
price = 0.25

print()
print("touring band merchandise order form")
print(f"\n{header}\n")
print("badges: £0.25 each (+10"+"%", "discount for >150 badges)")
print(f"\n{header}\n")
while True:
    no_badges = int(input("enter number of badges you would like to order: "))

    if no_badges > 150:
        print("you have qualified for a discount of 10"+"%", "on your order")
        x = 0.1
    else:
        x = 1

    print()

    continue_order = input("would you like to continue? (y/n): ")
    if continue_order.lower() != "y":
        print()
    else:
        price = (no_badges * price) * x
        print("thank you for your order")
        print()
        print(f"you have ordered {no_badges} badges")
        print(f"your total is: £{price:.2f}")
        break