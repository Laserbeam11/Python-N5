#On the computer: Loops and Iteration
#task 8e
#----------------------------------
#On the computer: Multiple Selection (Else IF)
#task 7a
for counter in range(0, 10):
    test_result = float(input("enter your test result %: "))

    if test_result >= 70:
        print("grade: A")
    elif test_result >= 60:
        print("grade: B")
    elif test_result >= 50:
        print("grade: C")
    elif test_result >= 40:
        print("grade: D")
    else:
        print("grade: F")