#On the computer: nested loops
#task 11b
access = False
while access == False:
    print('Enter the password')
    password = input()
    if password != 'WE<3MRsimpson':
        print('Access denied')
    else:
        print("your password was correct")
        access = True