#On the computer: nested loops
#task 11e
valid = False
while valid == False:
    print("what year was Albyn's 100th year anniversary at queens road?")
    print("a) 2010")
    print("b) 2011")
    print("c) 2026")
    print("d) 2027")
    answer = input()
    if answer != "c":
        print("Incorrect answer, try again")
    else:
        print("Correct answer")
        valid = True