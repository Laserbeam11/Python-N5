#On the computer: Loops and Iteration
#task 9a
#-------------------------------------------------
#On the computer: Multiple Selection (Else IF)
#task 7b
from asyncio import wait

marks = 0
fail = 0

print("welcome to the Aircraft quiz")

wait = input("press enter to continue")

#Question 1 - - - - - - - - - - - - - -
while True:
    Q1 = input("what delta winged plane does the RAF use (2025)?: ").strip().lower()
    if Q1 in ["typhoon", "eurofighter", "eurofighter typhoon"]:
        print("correct")
        marks += 1
        q1 = True
        break

    else:
        print("incorrect")
        q1 = False
        fail += 1
wait = input("press enter to continue")

#Question 2 - - - - - - - - - - - - - -
while True:
    Q2 = input("what's the nickname for the F-4?: ").strip().lower()
    if Q2 in ["phantom"]:
        print("correct")
        marks += 1
        q2 = True
        break
    
    else:
        print("incorrect")
        q2 = False
        fail += 1
wait = input("press enter to continue")

#Question 3 - - - - - - - - - - - - - -
while True:
    Q3 = input("what cold war american spyplane can fly at Mach 3?: ").strip().lower()
    if Q3 in ["sr-71", "sr-71 blackbird", "blackbird"]:
        print("correct")
        marks += 1
        q3 = True
        break
    
    else:
        print("incorrect")
        q3 = False
        fail += 1
wait = input("press enter to continue")

#Question 4 - - - - - - - - - - - - - -
while True:
    Q4 = input("what is the most iconic WW2 british aircraft?: ").strip().lower()
    if Q4 in ["spitfire"]:
        print("correct")
        marks += 1
        q4 = True
        break
    
    else:
        print("incorrect")
        q4 = False  
        fail += 1
wait = input("press enter to continue")

#Question 5 - - - - - - - - - - - - - -
while True:
    Q5 = input("what is the most iconic WW2 german fighter?: ").strip().lower()
    if Q5 in ["bf109", "bf-109", "messerschmitt bf109", "messerschmitt bf-109"]:
        print("correct")
        marks += 1
        q5 = True
        break
    
    else:
        print("incorrect")
        q5 = False
        fail += 1
wait = input("press enter to continue")

#Question 6 - - - - - - - - - - - - - -
while True:
    Q6 = input("what is the most iconic WW2 american fighter?: ").strip().lower()
    if Q6 in ["p-51"]:
        print("correct")
        marks += 1
        q6 = True
        break
    
    else:
        print("incorrect")
        q6 = False
        fail += 1
wait = input("press enter to continue")

#Question 7 - - - - - - - - - - - - - -
while True:
    Q7 = input("what is the most iconic WW2 japanese fighter?: ").strip().lower()
    if Q7 in ["zero"]:
        print("correct")
        marks += 1
        q7 = True
        break
    
    else:
        print("incorrect")
        q7 = False
        fail += 1
wait = input("press enter to continue")

#Question 8 - - - - - - - - - - - - - -
while True:
    Q8 = input("what jet had a 104:0 K/D ratio?: ").strip().lower()
    if Q8 in ["f-15"]:
        print("correct")
        marks += 1
        q8 = True
        break
    
    else:
        print("incorrect")
        q8 = False
        fail += 1
wait = input("press enter to continue")

#Question 9 - - - - - - - - - - - - - -
while True:
    Q9 = input("what is the bomber that dropped the atomic bomb on hiroshima?: ").strip().lower()
    if Q9 in ["enola gay", "b-29"]:
        print("correct")
        marks += 1
        q9 = True
        break
    
    else:
        print("incorrect")
        q9 = False
        fail += 1
wait = input("press enter to continue")

#Question 10 - - - - - - - - - - - - - -
while True:
    Q10 = input("what caused the development of the F-15?: ").strip().lower()
    if Q10 in ["mig-25", "foxbat", "mig-31"]:
        print("correct")
        marks += 1
        q10 = True
        break
    
    else:
        print("incorrect")
        q10 = False
        fail += 1
wait = input("press enter to end the quiz and get results")

print("you got " + str(marks - fail) + " out of 10")
if marks == 1:
    print("F-")
elif marks == 2:
    print("F-")
elif marks == 3:
    print("F-")
elif marks == 4:
    print("D-")
elif marks == 5:
    print("C-")
elif marks == 6:
    print("C+")
elif marks == 7:
    print("B-")
elif marks == 8:
    print("B+")
elif marks == 9:
    print("A")
elif marks == 10:
    print("A+")
elif marks == 0:
    print("F-")
else:
    print("error calculating results")