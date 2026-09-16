station_N = int(input("enter number of charging stations: "))
startmilage = 0
journey = []

if station_N <= 0:
    print("invalid number of charging stations")
    station_N = int(input("please enter a valid number of charging stations: "))

while station_N != 0:
    milage = float(input("enter mileage at current station: "))       

    kWr_station = float(input("enter kW rating of the current station: "))
    if kWr_station == 7:
        ppM = 0
    elif kWr_station == 22:
        ppM = 0.005
    else:
        ppM = 0.01

    milesTravelled = milage - startmilage
    startmilage = milage
    Cost = ppM * milesTravelled
    journey.append(Cost)
    print("£"+ str(round(Cost, 3)))
    station_N -= 1

print("Total cost of journey: £" + str(round(sum(journey), 3)))