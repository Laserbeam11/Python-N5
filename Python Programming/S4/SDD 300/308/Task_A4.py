# A smart phone app is needed to calculate the cost of electricity.

# The following
# information will be entered by the user.

# • Previous meter reading
# • Current meter reading
# • Unit cost
# • Discount eligibility

# A possible user interface for the app is shown below.

prev = float(input("Enter previous meter reading: "))
curr = float(input("Enter current meter reading: "))
cost = float(input("Enter unit cost: "))

discount_input = input("Are you eligible for a discount? (y / n): ")
if discount_input.lower() == "y":
    discount = True
else:
    discount = False


used = curr - prev 
total = used * cost


print(f"\nCalculation Breakdown:")
print(f"{curr} - {prev} = {used} units used")
print(f"{used} units at {cost} per unit")


if discount:
    total = total - 5
    print("Discount applied: -5.00")


print(f"Total Cost = {total}")