def passed(score):
    if score >= 50:
        return True
    elif score < 0:
        return None
    else:
        return False


print("Please enter the score as an integer:")
str_score = input()
score = 0
try:
    score = int(str_score)
except ValueError:
    print("The score must be entered as an integer")
    exit(1)

did_pass = passed(score)
if did_pass:
    print("You passed!")
elif did_pass is None:
    print("You can not have a negative score!")
else:
    print("You failed!")
