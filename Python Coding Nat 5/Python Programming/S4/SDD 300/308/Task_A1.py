# get test score from user
# WHILE test score is less than 0 OR greater than 100
# 	prompt user to try again
# 	get test score from user
# ENDWHILE
# add score to list

score = int(input("Enter test score: "))
while score < 0 or score > 100:
    print("invalid score")
    score = int(input("please enter a valid test score: "))
scores = [score]