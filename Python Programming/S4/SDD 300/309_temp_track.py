temps = []
for i in range (5):
    temp = float(input(f"enter tempreture for day {i+1} (°C): "))
    temps.append(temp)

for x in range (5):
    print(f"day {x+1}: {temps[x]}")

avg = sum(temps) / 5
print(f"average temperature: {avg} °C")