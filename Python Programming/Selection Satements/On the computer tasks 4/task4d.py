#On The Computer: Conditional If Statement / Using the Equals Operator
#task 4d
test_score = int(input("out of 70, how high was your test score? "))

percentage = (test_score / 70) * 100

if percentage > 70:
    print("pass")
else:
    print("fail")