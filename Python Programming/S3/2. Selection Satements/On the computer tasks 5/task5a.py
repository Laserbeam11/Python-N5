#On the computer: Indentation / Conditional Selection
#task 5a
from asyncio import wait

marks = 0

print("welcome to the Aircraft quiz")

wait = input("press enter to continue")

Q1 = input("what delta winged plane does the RAF use (2025)?: ")

#Question 1 - - - - - - - - - - - - - -
if Q1 == "Typhoon" .casefold():
    print("correct")
    marks += 1
elif Q1 == "eurofighter" .casefold():
    print("correct")
    marks += 1
elif Q1 == "eurofighter typhoon" .casefold():
    print("correct")
    marks += 1
else:
    print("incorrect the answer is the eurofighter typhoon")

wait = input("press enter to continue")

#Question 2 - - - - - - - - - - - - - -
Q2 = input("what is the nickname for the F-4?: ")
if Q2 == "phantom" .casefold():
    print("correct")
    marks += 1
else:
    print("incorrect the answer is the phantom")

wait = input("press enter to continue")

#Question 3 - - - - - - - - - - - - - -
Q3 = input("what spyplane can fly at Mach 3? (hint: black): ")
if Q3 == "SR-71" .casefold():
    print("correct")    
    marks += 1
elif Q3 == "SR-71 blackbird" .casefold():
    print("correct")
    marks += 1
elif Q3 == "blackbird" .casefold():
    print("correct")
    marks += 1
else:
    print("incorrect the answer is the SR-71 blackbird")

wait = input("press enter to continue")

#Question 4 - - - - - - - - - - - - - -
Q4 = input("what is the most iconic WW2 british aircraft?: ")
if Q4 == "spitfire" .casefold():
    print("correct")
    marks += 1
else:
    print("incorrect the answer is the spitfire")

wait = input("press enter to continue")

#Question 5 - - - - - - - - - - - - - -
Q5 = input("what is the most iconic WW2 german figher?: ")
if Q5 == "bf-109" .casefold():
    print("correct")
    marks += 1
else:
    print("incorrect the answer is the bf-109")

wait = input("press enter to continue")

#Question 6 - - - - - - - - - - - - - -
Q6 = input("what is the most iconic WW2 american fighter?: ")
if Q6 == "P-51" .casefold():
    print("correct")
    marks += 1
else:
    print("incorrect the answer is the P-51")

wait = input("press enter to continue")

#Question 7 - - - - - - - - - - - - - -
Q7 = input("what is the most iconic WW2 japanese fighter?: ")
if Q7 == "zero" .casefold():
    print("correct")
    marks += 1
else:
    print("incorrect the answer is the zero")

wait = input("press enter to continue")

#Question 8 - - - - - - - - - - - - - -
Q8 = input("what jet had* a 104:0 K/D ratio?: ")
if Q8 == "f-15" .casefold():
    print("correct")    
    marks += 1
else:
    print("incorrect the answer is the f-15")

wait = input("press enter to continue")

#Question 9 - - - - - - - - - - - - - -
Q9 = input("what is the bomber that dropped the atomic bomb on hiroshima?: ")
if Q9 == "enola gay" .casefold():
    print("correct")
    marks += 1
elif Q9 == "B-29" .casefold():
    print("correct")
    marks += 1
else:
    print("incorrect the answer is the enola gay B-29")

wait = input("press enter to continue")

#Question 10 - - - - - - - - - - - - - -
Q10 = input("what caused the development of the F-15?: ")
if Q10 == "the Mig-25" .casefold():
    print("correct")
    marks += 1
elif Q10 == "Mig-25" .casefold():
    print("correct")
    marks += 1
elif Q10 == "the Mig-25 Foxbat" .casefold():
    print("correct")
    marks += 1
elif Q10 == "Mig-31" .casefold():
    print("correct... but the Mig-25 is more correct")
    marks += 1
else:
    print("incorrect the answer is the Mig-25")

wait = input("press enter to end the quiz and get results")

print("you got " + str(marks) + " out of 10")
if marks == 1:
    print("10%... you need to do some research")
elif marks == 2:
    print("20%... you need to do some research")
elif marks == 3:
    print("30%... you need to do some research")
elif marks == 4:
    print("40%... you need to do some research")
elif marks == 5:
    print("50%... you need to do some research")
elif marks == 6:
    print("60%... nice try but you can do better")
elif marks == 7:
    print("70%... not bad but you can do better")
elif marks == 8:
    print("80%... good job but you can do better")
elif marks == 9:
    print("90%... great job but you can do better")
elif marks == 10:
    print("100%... perfect score! well done")
elif marks == 0:
    if input("0%... wow, you stupid, what's 10+9?") == "21":
        print("correct... but you still got 0%")
    else:
        print("so you know math but not planes? bravo...")
else:
    print("error calculating results")