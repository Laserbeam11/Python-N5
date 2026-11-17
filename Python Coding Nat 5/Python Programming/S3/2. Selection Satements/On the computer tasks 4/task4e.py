#On The Computer: Conditional If Statement / Using the Equals Operator
#task 4e
import time
import sys

def matrix_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print() 
    #i had to... okay :D

password = input("Enter password: ")

if password == "UzaquxawvIJH<3":
    matrix_print("Access granted...")
    matrix_print("We love Mr Simpson.")
    matrix_print("He is the best teacher ever.")
    matrix_print("We are so lucky to have him!")
    matrix_print("We will never forget him.")
    matrix_print("Thank you for everything, Mr. Simpson.")
    matrix_print("We love you, Mr. Simpson.")
    matrix_print("You are the best teacher ever, Mr. Simpson.")
    matrix_print("We will always remember you, Mr. Simpson.")
    matrix_print("We will always be grateful for everything you have done for us, Mr. Simpson.")
    matrix_print("We will always be grateful for everything you have done for us, Mr. Simpson.")
    matrix_print("We will always be grateful for everything you have done for us, Mr. Simpson.")
    matrix_print("We will always be grateful for everything you have done for us, Mr. Simpson.")
                                                                                        #the ai broke lol  
else:
    matrix_print("Access denied.")