snowfallTotal = 0
measurementCounter = 0
dayCounter = 0
snowfallArray = []

snowfallmeasurement = float(input("Enter the amount of snowfall in millimeters: "))

while snowfallmeasurement != 0:
    
    if snowfallmeasurement < 0:
        while snowfallmeasurement < 0:
            print("invalid input")
            snowfallmeasurement = float(input("please enter a valid measurement of snowfall in millimeters: "))

    if snowfallmeasurement >= 0.5:
        snowfallTotal += snowfallmeasurement
        measurementCounter += 1
    
    if snowfallmeasurement != 0:
        dayCounter += 1

    snowfallArray.append(snowfallmeasurement)

    averageSnowfall = sum(snowfallArray) / len(snowfallArray)

averageSnowfall = round(averageSnowfall, 2)

if snowfallTotal >= 10 and dayCounter >= 5:
    print(f"days snowfall lasted: {dayCounter}")
    #

    for measurementCounter in range(len(snowfallArray)):
        print(f"measurement {measurementCounter + 1}: {snowfallArray[measurementCounter]} mm")
    
    print(f"average snowfall: {averageSnowfall} mm")
else:
    print("not enough data for analysis")