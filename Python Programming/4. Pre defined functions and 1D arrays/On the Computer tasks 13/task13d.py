# On The Computer: Arrays
# task 13d
import random
x = [random.randint(0,100) for x in range(100)]
print(x)

count = 0
for index in range(0,100):
    if x[index] > 80:
        count = count + 1
print(count)