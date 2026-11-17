# On The Computer: Arrays
# task 13c
x = ["" for x in range(3)]
y = ["" for y in range(3)]
z = 0

x[0] = "first pilot name in KSP"
x[1] = "first scientist name in KSP"
x[2] = "first engineer name in KSP"

for counter in range(0, 3):
    y[counter] = input(f"{x[counter]}:   ")


if y[0].lower() == "jebediah":
    print("correct")
    z = z + 1
else:
    print("incorrect")

if y[1].lower() == "bob":
        print("correct")
        z = z + 1
else:
    print("incorrect")

if y[2].lower() == "bill":
    print("correct")
    z = z + 1
else:
    print("incorrect")

for w in range(0, 3):
    print(x[w], y[w])
print(f"you got {z} out of 3 correct")
