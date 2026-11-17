#On the computer: And / OR
#task 6d
number = 0
print("out of the list, what subjects do you take?")
print("english")
print("drama")
print("music")
subjects = input("enter your subjects: ").lower()
if "english" in subjects:
    number += 1
if "drama" in subjects:
    number += 1
if "music" in subjects:
    number += 1

if number >= 2:
    print("you are eligible to attend the London trip")
else:
    print("you are not eligible to attend the London trip")