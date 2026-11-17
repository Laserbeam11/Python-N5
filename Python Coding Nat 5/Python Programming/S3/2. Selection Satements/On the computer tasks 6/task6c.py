#On the computer: And / OR
#task 6c
password_1 = str("QWERTY")
password_2 = str("ASDFGH")
password_3 = str("ZXCVBN")
IN_pass_1 = input("enter password: ")
IN_pass_2 = input("enter password 2: ")
IN_pass_3 = input("enter password 3: ")
if (IN_pass_1 == password_1 and IN_pass_2 == password_2 and IN_pass_3 == password_3):
    print("access granted")
else:
    print("access denied")