#On The Computer: pre defined functions
#task 12d
import random
repeat = False
while repeat == False:
    n1 = random.randint(1, 59)
    n2 = random.randint(1, 59)
    n3 = random.randint(1, 59)
    n4 = random.randint(1, 59)
    n5 = random.randint(1, 59)
    n6 = random.randint(1, 59)
    if n1 != n2 and n1 != n3 and n1 != n4 and n1 != n5 and n1 != n6:
        if n2 != n1 and n2 != n3 and n2 != n4 and n2 != n5 and n2 != n6:
            if n3 != n1 and n3 != n2 and n3 != n4 and n3 != n5 and n3 != n6:
                if n4 != n1 and n4 != n2 and n4 != n3 and n4 != n5 and n4 != n6:
                    if n5 != n1 and n5 != n2 and n5 != n3 and n5 != n4 and n5 != n6:
                        if n6 != n1 and n6 != n2 and n6 != n3 and n6 != n4 and n6 !=n5:
                            repeat = True 
                        else:
                            repeat = False
                    else:
                        repeat = False
                else:
                    repeat = False
            else:
                repeat = False
        else:
            repeat = False
    else:
        repeat = False
print(f"the lotter numbers are: {n1}, {n2}, {n3}, {n4}, {n5} and {n6}")
