header = "=" * 68
subheader = "-" * 68
saving = []
savings = 0
deposit = 0

print(f"\n{header}\n")
print("welcome to SIMPSON ltd. banc corps.")
print(f"\n{header}\n")

print("selection terminal")
print(f"\n{subheader}\n")

print("1. deposit into account")
print("2. withdraw from account")
print("3. view account balance")
print("4. saving plan")

choice = input("select plan: ")

if choice != 4:
    print("sorry we run out of budget")
    print("we do have saving though...")
else:
    print()


print(f"\n{subheader}\n")

print("saving plan")
for i in range(12):
    deposit = float(input(f"enter savings amount for month {i + 1}: "))
    saving.append(deposit)
    if i == 0:
        savings = deposit
    elif i > 0:
        savings += deposit

    print(f"total after month {i + 1}: £{savings:.2f}")
    print()