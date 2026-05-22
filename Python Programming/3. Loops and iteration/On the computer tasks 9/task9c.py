#On the computer: Loops and Iteration
#task 9c
print("enter a number between 0 and 256")
x = int(input("enter number: "))
if x == 0:
    print("00000000")
elif x == 1:
    print("00000001")
elif x == 2:
    print("00000010")
elif x == 4:
    print("00000100")
elif x == 8:
    print("00001000")
elif x == 16:
    print("00010000")
elif x == 32:
    print("00100000")
elif x == 64:
    print("01000000")
elif x == 128:
    print("10000000")
elif x > 0 and x < 256:
    digit8 = x // 128
    digit7 = (x % 128) // 64
    digit6 = (x % 64) // 32
    digit5 = (x % 32) // 16
    digit4 = (x % 16) // 8
    digit3 = (x % 8) // 4
    digit2 = (x % 4) // 2
    digit1 = x % 2
    print(f"{digit8}{digit7}{digit6}{digit5}{digit4}{digit3}{digit2}{digit1}")