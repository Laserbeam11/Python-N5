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

discount = input("Are you eligible for a discount? (y / n): ")
if discount.lower() == "y":
    discount = True
else:
    discount = False
